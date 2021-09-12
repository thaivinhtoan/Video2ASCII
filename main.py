import cv2
import os
import PIL.Image
from cv2 import cv2

ASSSII_CHAR = ['$', '&', '#', '@', '%', '?',
               '=', '/', '+', '^', '*', ',', '`', '-', '.', ' ']
NEW_WIDTH = 25


def ExtractImage(video):
    folder = 'test'
    os.mkdir(folder)
    # use opencv to do the job
    vidcap = cv2.VideoCapture(video)
    count = 0
    while True:
        success, image = vidcap.read()
        if not success:
            break
        # save frame as JPEG file
        cv2.imwrite(os.path.join(folder, "frame{:d}.jpg".format(count)), image)
        count += 1
    return count


def resize_image(image):
    width, height = image.size
    ratio = height / width
    new_height = int(NEW_WIDTH * ratio)
    resized_image = image.resize((NEW_WIDTH, new_height), PIL.Image.ANTIALIAS)
    return(resized_image)


def grayify(image):
    grayscale_image = image.convert("L")
    return (grayscale_image)


def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASSSII_CHAR[pixel//15] for pixel in pixels])
    return(characters)


def main():
    # path = input("Enter name: ")
    path = 'hi.mp4'
    countFrame = ExtractImage(path)

    vidcap = cv2.VideoCapture(path)

    for i in range(countFrame):
        iImage = "test/frame" + str(i) + ".jpg"
        image = PIL.Image.open(iImage)

        new_image_data = pixels_to_ascii(grayify(resize_image(image)))
        pixel_count = len(new_image_data)
        ascii_image = "\n".join(
            new_image_data[i:(i+NEW_WIDTH)] for i in range(0, pixel_count, NEW_WIDTH))
        print(ascii_image)
        os.system('cls')

    os.system('rm -rf test')
    # with open("ascii_image.txt", "w") as f:
    #     f.write(ascii_image)


main()
