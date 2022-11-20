from PIL import Image, ImageDraw, ImageFont
import textwrap
import os
from os.path import join, dirname, abspath
from dotenv import load_dotenv
from pyunsplash import PyUnsplash
import requests


def get_image_from_unsplash():  # it downloads an image in the main folder
    dotenv_path = join(dirname(abspath("__file__")), './.env')
    load_dotenv(dotenv_path)

    UNSPLASH_ACCESS_KEY = os.environ.get("UNSPLASH_ACCESS_KEY")

    # instantiate PyUnsplash object
    pu = PyUnsplash(api_key=UNSPLASH_ACCESS_KEY)

    photos = pu.photos(type_='random', count=1, featured=True, query="splash")
    [photo] = photos.entries
    print(photo.id, photo.link_download)

    response = requests.get(photo.link_download, allow_redirects=True)
    open('./unsplash_temp.png', 'wb').write(response.content)


def crop_center(pil_img, crop_width, crop_height):  # make image square
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))


def create_image_with_message(message, type_of_image):
    def apply_filters_post(message):
        if len(message) < 51:
            return (14, 120, 70, 8)  # return lineWidth, fontSize,  margin and blue_heart_position
        if len(message) < 121:
            return (16, 78, 70, 10)  # return lineWidth, fontSize,  margin and blue_heart_position
        if len(message) < 221:
            return (23, 64, 100, 12)  # return lineWidth, fontSize,  margin and blue_heart_position
        if len(message) < 261:
            return (24, 60, 100, 14)  # return lineWidth, fontSize,  margin and blue_heart_position
        if len(message) < 351:
            return (27, 56, 100, 16)
        if len(message) < 501:
            return (30, 48, 100, 32)
        else:
            raise ValueError('Value too big for text, put in a smaller quote')

    def apply_filters_story(message):
        if len(message) < 51:
            return (14, 120, 70, 8)  # return lineWidth, fontSize,  margin and blue_heart_position
        if len(message) < 121:
            return (16, 94, 70, 10)  # return lineWidth, fontSize,  margin and blue_heart_position
        if len(message) < 221:
            return (20, 76, 100, 8)  # return lineWidth, fontSize,  margin and blue_heart_position
        if len(message) < 261:
            return (20, 76, 100, 10)  # return lineWidth, fontSize,  margin and blue_heart_position
        if len(message) < 351:
            return (22, 72, 100, 10)
        if len(message) < 501:
            return (22, 58, 100, 18)
        else:
            raise ValueError('Value too big for text, put in a smaller quote')

    if type_of_image == 'post':
        width = 1080
        height = 1080  # this is recommended insta post size
        (lineWidth, fontSize, margin, blue_heart_divider) = apply_filters_post(message)
    elif type_of_image == 'story':
        width = 1080
        height = 1920  # this is recommended insta story size 9:16
        (lineWidth, fontSize, margin, blue_heart_divider) = apply_filters_story(message)
    else:
        print(type_of_image, type(type_of_image), "shit!!!!!")
        print(type_of_image == 'post')
        raise ValueError('This type of image is not recognized and covered. Please use post or story')

    font = ImageFont.truetype("./jetbrains.ttf", size=fontSize)
    # img = Image.new('RGB', (width, height), color='blue')
    # img = Image.open(r'./sample-imgs/bird.jpg')
    img = Image.open(r'./unsplash_temp.png')

    img = crop_center(img, width, height)  # make a square
    img.putalpha(69)  # make half transparent

    imgDraw = ImageDraw.Draw(img)

    # textWidth, textHeight = imgDraw.textsize(message, font=font)
    textWidth = imgDraw.textlength('cristiancristian1234', font=font)
    textHeight = imgDraw.textsize('cristiancristian1234', font=font)[1]  # it's deprecated but it's more precise

    # imgDraw.text((xText, yText), message, font=font, fill=(255, 255, 0))

    totalHeight = 0
    for line in textwrap.wrap(message, width=lineWidth):  # first get total height
        totalHeight += textHeight

    offset = (height - totalHeight) / 2 + 50

    for line in textwrap.wrap(message, width=lineWidth):
        w = imgDraw.textlength(line, font=font)
        imgDraw.text(((width - w) / 2, offset), line, font=font, fill="#ffffff")
        offset += textHeight

    blue_heart = Image.open('./blue-heart.png')
    blue_heart = blue_heart.resize((100, 100))
    img.paste(blue_heart, (int((width - 100) / 2), int((height - 100) / blue_heart_divider)), blue_heart)
    img.save('result.png')



