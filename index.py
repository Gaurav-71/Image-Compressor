import os
import sys
from PIL import Image


def compressMe(file, verbose=False):
    # Get the path of the file
    root = os.getcwd()
    raw = os.path.join(os.getcwd(), "Raw Files")
    compressed = os.path.join(os.getcwd(), "Compressed")
    filepath = os.path.join(raw, file)
    # open the image
    picture = Image.open(filepath)
    picture = picture.convert('RGB')
    os.chdir(compressed)
    picture.save(file.split(".")[0]+".webp", "webp", optimize=True, quality=30)
    os.chdir(root)
    return


def main():

    verbose = False
    # checks for verbose flag
    if (len(sys.argv) > 1):
        if (sys.argv[1].lower() == "-v"):
            verbose = True
    # finds current working dir
    cwd = os.getcwd()
    raw = os.path.join(cwd, "Raw Files")
    formats = ('.jpg', '.jpeg', '.png')
    # looping through all the files
    # in a current directory
    for file in os.listdir(raw):
        # If the file format is JPG or JPEG
        if os.path.splitext(file)[1].lower() in formats:
            print('compressing', file)
            compressMe(file, verbose)
    print("Done")


# Driver code
if __name__ == "__main__":
    main()
