import re
import os
import shutil


def move_images(dirSrc, dirDest):
    """
    Move all JPEG images from dirSrc to dirDest. Do not keep the
    directory structure. Change the extension to "jpg".
    """
    usedFnames = set()
    for path, dirs, files in os.walk(dirSrc):
        for fname in files:
            if re.search('\\.jpe?g', fname.lower()) is None:
                continue
            fnameNormalized = re.sub('\\.[^.]*$', '.jpg', fname)
            if fnameNormalized in usedFnames:
                print('Warning: duplicate image with the name "' + fnameNormalized + '".')
            fnameSrc = os.path.join(path, fname)
            fnameDest = os.path.join(dirDest, fnameNormalized)
            shutil.copy2(fnameSrc, fnameDest)


if __name__ == '__main__':
    imgDir = input('Please enter the full path of the image directory: ')
    if len(imgDir) > 0:
        move_images(imgDir, '/var/www/html/wc_corpus/img/')

