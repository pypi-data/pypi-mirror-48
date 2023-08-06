from __future__ import division

import glob
import os
import subprocess
import re

import click
import numpy as np

from bw_plex import LOG
from bw_plex.video import video_frame_by_frame
from bw_plex.misc import sec_to_hh_mm_ss

try:
    import cv2
except ImportError:
    cv2 = None
    LOG.warning('Scanning for credits is not supported. '
                'Install the package with pip install bw_plex[all] or bw_plex[video]')

try:
    import pytesseract
except ImportError:
    pytesseract = None
    LOG.warning('Extracting text from images is not supported. '
                'Install the package with pip install bw_plex[all] or bw_plex[video]')

try:
    import Image
except ImportError:
    from PIL import Image


color = {'yellow': (255, 255, 0),
         'red': (255, 0, 0),
         'blue': (0, 0, 255),
         'lime': (0, 255, 0),
         'white': (255, 255, 255),
         'fuchsia': (255, 0, 255),
         'black': (0, 0, 0)
         }


def make_imgz(afile, start=600, dest=None, fps=1):
    """Helper to generate images."""

    dest_path = dest + '\out%d.jpg'
    fps = 'fps=%s' % fps
    t = sec_to_hh_mm_ss(start)

    cmd = [
        'ffmpeg', '-ss', t, '-i',
        afile, '-vf', fps, dest_path
    ]

    # fix me
    subprocess.call(cmd)
    print(dest)
    return dest


def extract_text(img, lang='eng', encoding='utf-8'):
    if pytesseract is None:
        return

    if isinstance(img, str):
        img = Image.open(img)

    return pytesseract.image_to_string(img, lang=lang).encode(encoding, 'ignore')


def calc_success(rectangles, img_height, img_width, success=0.9):  # pragma: no cover
    """Helper to check the n percentage of the image is covered in text."""
    t = sum([i[2] * i[3] for i in rectangles if i])
    p = 100 * float(t) / float(img_height * img_width)
    return p > success


def locate_text(image, debug=False):
    """Locate where and if there are text in the images.

       Args:
            image(numpy.ndarray, str): str would be path to image
            debug(bool): Show each of the images using open cv.

       Returns:
            list of rectangles


    """
    # Mostly ripped from https://github.com/hurdlea/Movie-Credits-Detect
    # Thanks!
    import cv2

    # Compat so we can use a frame and img file..
    if isinstance(image, str) and os.path.isfile(image):
        image = cv2.imread(image)

    if debug:
        cv2.imshow('original image', image)

    height, width, _ = image.shape
    mser = cv2.MSER_create(4, 10, 8000, 0.8, 0.2, 200, 1.01, 0.003, 5)
    # Convert to gray.
    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    if debug:
        cv2.imshow('grey', grey)

    # Pull out grahically overlayed text from a video image
    blur = cv2.GaussianBlur(grey, (3, 3), 0)
    # test media blur
    # blur = cv2.medianBlur(grey, 1)

    if debug:
        cv2.imshow('blur', blur)

    adapt_threshold = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                            cv2.THRESH_BINARY, 5, -25)

    contours, _ = mser.detectRegions(adapt_threshold)

    # for each contour get a bounding box and remove
    rects = []
    for contour in contours:
        # get rectangle bounding contour
        [x, y, w, h] = cv2.boundingRect(contour)

        # Remove small rects
        if w < 5 or h < 5:  # 2
            continue

        # Throw away rectangles which don't match a character aspect ratio
        if (float(w * h) / (width * height)) > 0.005 or float(w) / h > 1:
            continue

        rects.append(cv2.boundingRect(contour))

    # Mask of original image
    mask = np.zeros((height, width, 1), np.uint8)
    # To expand rectangles, i.e. increase sensitivity to nearby rectangles
    # Add knobs?
    # lets scale this alot so we get mostly one big square
    # todo when/if detect motion.
    xscaleFactor = 14  # 14
    yscaleFactor = 4  # 4
    for box in rects:
        [x, y, w, h] = box
        # Draw filled bounding boxes on mask
        cv2.rectangle(mask, (x - xscaleFactor, y - yscaleFactor),
                      (x + w + xscaleFactor, y + h + yscaleFactor),
                      color['white'], cv2.FILLED)

    if debug:
        cv2.imshow("Mask", mask)

    # Find contours in mask if bounding boxes overlap,
    # they will be joined by this function call
    rectangles = []
    contours = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    if cv2.__version__.startswith('4'):
        contours = contours[0]
    else:
        contours = contours[1]

    for contour in contours:
        # This is disabled since we are not after the text but the text area.
        # Only preserve "squarish" features
        # peri = cv2.arcLength(contour, True)
        # approx = cv2.approxPolyDP(contour, 0.01 * peri, True)

        # the contour is 'bad' if it is not a rectangluarish
        # This doesnt have to be bad, since we match more then one char.
        # if len(approx) > 8:
        #    cv2.drawContours(image, [contour], -1, color['lime'])
        #    if debug:
        #        cv2.imshow("bad Rectangles check lime", image)
        #    continue

        rect = cv2.boundingRect(contour)

        x, y, w, h = rect
        cv2.rectangle(image, (x, y), (x + w, y + h), color['blue'], 2)

        # Remove small areas and areas that don't have text like features
        # such as a long width.
        if ((float(w * h) / (width * height)) < 0.006):
            # remove small areas
            if float(w * h) / (width * height) < 0.0018:
                continue

            # remove areas that aren't long
            if (float(w) / h < 2.5):
                continue

        else:
            pass
            # This is disabled as we want to cache the large area of text
            # to backup this shit for movement detection
            # General catch for larger identified areas that they have
            # a text width profile
            # and it does not fit for jap letters.

            # if float(w) / h < 1.8:
            #    continue

        rectangles.append(rect)

        cv2.rectangle(image, (x, y), (x + w, y + h), color['fuchsia'], 2)

    if debug:
        cv2.imshow("Final image", image)
        cv2.waitKey(0)

    return rectangles


def find_credits(path, offset=0, fps=None, duration=None, check=7, step=1, frame_range=True):
    """Find the start/end of the credits and end in a videofile.
       This only check frames so if there is any silence in the video this is simply skipped as
       opencv only handles videofiles.

       use frame_range to so we only check frames every 1 sec.

       # TODO just ffmepg to check for silence so we calculate the correct time? :(

       Args:
            path (str): path to the videofile
            offset(int): If given we should start from this one.
            fps(float?): fps of the video file
            duration(None, int): Duration of the vfile in seconds.
            check(int): Stop after n frames with text, set a insane high number to check all.
                        end is not correct without this!
            step(int): only use every n frame
            frame_range(bool). default true, precalc the frames and only check thous frames.

       Returns:
            1, 2


    """
    # LOG.debug('%r %r %r %r %r %r %r', path, offset, fps, duration, check, step, frame_range)
    if cv2 is None:
        return
    frames = []
    start = -1
    end = -1
    LOG.debug('Trying to find the credits for %s', path)

    try:
        if fps is None:
            # we can just grab the fps from plex.
            cap = cv2.VideoCapture(path)
            fps = cap.get(cv2.CAP_PROP_FPS)
            cap.release()

        for _, (frame, millisec) in enumerate(video_frame_by_frame(path, offset=offset,
                                                                   step=step, frame_range=frame_range)):
            # LOG.debug('progress %s', millisec / 1000)
            if frame is not None:
                recs = locate_text(frame, debug=False)

                if recs:
                    frames.append(millisec)

                if check != -1 and len(frames) >= check:
                    break

        if frames:
            LOG.debug(frames)
            start = min(frames) / 1000
            end = max(frames) / 1000

        LOG.debug('credits_start %s, credits_end %s', start, end)

    except:  # pragma: no cover
        # We just want to log the exception not halt the entire process to db.
        LOG.exception('There was a error in find_credits')

    return start, end


def fill_rects(image, rects):
    """This is used to fill the rects (location of credits)

       The idea if to mask the credits so we can check if there is any background
       movement while the credits are running. Like the movie cars etc.
       See if we can grab something usefull from
       https://gist.github.com/luipillmann/d76eb4f4eea0320bb35dcd1b2a4575ee
    """
    for rect in rects:
        x, y, w, h = rect
        cv2.rectangle(image, (x, y), (x + w, y + h), color['black'], cv2.FILLED)

    return image


@click.command()
@click.argument('path')
@click.option('-c', type=float, default=0.0)
@click.option('-d', '--debug', is_flag=True, default=False)
@click.option('-p', '--profile', is_flag=True, default=False)
@click.option('-o', '--offset', default=0, type=int)
def cmd(path, c, debug, profile, offset):  # pragma: no cover

    if os.path.isfile(path):
        files = [path]
    else:
        files = glob.glob(path)

    d = {}

    for f in files:
        if f.endswith(('.png', '.jpeg', '.jpg')):
            filename = os.path.basename(f)
            hit = re.search(r'(\d+)', filename)

            t = locate_text(f, debug=debug)

            if hit:
                d[int(hit.group()) + offset] = (bool(t), filename)
        else:
            t = find_credits(f, offset=offset)

        if c:
            img = cv2.read_img(f, cv2.IMREAD_UNCHANGED)
            height, width, _ = img.shape
            t = calc_success(t, height, width)

    if d:
        click.echo('Image report')
        for k, v in sorted(d.items()):
            if v[0] is True:
                color = 'green'
            else:
                color = 'red'
            click.secho('%s %s %s %s' % (k, sec_to_hh_mm_ss(k), v[0], v[1]), fg=color)


if __name__ == '__main__':
    # cmd()
    def test():
        import cv2
        i = r"C:\Users\alexa\OneDrive\Dokumenter\GitHub\bw_plex\tests\test_data\blacktext_whitebg_2.png"
        i = r'C:\Users\alexa\.config\bw_plex\third_images\out165.jpg'

        img = cv2.imread(i)
        ffs = img.copy()
        rects = locate_text(ffs, debug=True)

        f = fill_rects(img, rects)
        cv2.imshow('ass', f)
        cv2.waitKey(0)

    # test()
