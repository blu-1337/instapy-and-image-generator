from PIL import Image, ImageDraw, ImageFont
import textwrap
import os
from os.path import join, dirname, abspath
from dotenv import load_dotenv
from pyunsplash import PyUnsplash
import requests



def get_image_from_unsplash():
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

    def apply_filters(message):
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

    (lineWidth, fontSize, margin, blue_heart_divider) = apply_filters(message)

    width = 1080
    height = 1080  # this is recommended insta post size
    font = ImageFont.truetype("./jetbrains.ttf", size=fontSize)
    # img = Image.new('RGB', (width, height), color='blue')
    # img = Image.open(r'./sample-imgs/portrait_food_4.jpg')
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
        imgDraw.text(((width - w)/2, offset), line, font=font, fill="#ffffff")
        offset += textHeight

    blue_heart = Image.open('./blue-heart.png')
    blue_heart = blue_heart.resize((100,100))
    img.paste(blue_heart, (int((width-100)/2), int((height-100)/blue_heart_divider)), blue_heart)
    img.save('result.png')


message = \
    "Alwaysaa try to end the day with a positiveday with a positiveday with a positive thought. No matter how hard as df  asdfas dfas asdf a things are, tomorrow is a fresh opportunity to make everything better."

message2 = "When you say you suffer from a physical illness, you get sympathy. When you say you suffer from depression, you sometimes get blamed. We know it sucks, but at the very least, please take solace in the fact that you are not alone – as evidenced by the fact that 350 million people in the world struggle with depression."

message3 = 'asdf asdf asdf asdf asdf asdf asdf asdf asdf asdf asdf asdf asdf asdf asdf asdf asdf asdf asdf qwe qwer qwer qwer qwer qwer asdf asdf asdf qwer qwef qwef qwef asdf asdf qwef qwefq wef qwef asdf asdf qwef asdf awef awefa wef awef awef asdf asdf asd fasd fasdf asdf asdf '
message4 = 'Alwaysaa try to end the day with a positiveday with a positiveday with a positive thought. No matter how hard as df'
message5 = 'giochero per vincere niggas be niggas all the time no cap we strong brosefinos leggo my birtth light'
message25 = "Lorem ipsum dolor sit ame"
message50 = "Lorem ipsum dolor sit amet, consectetuer adipiscin"
message120 = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis nat"  # average quote size
message220 = 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies.'
message260 = 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem.'
message325 = 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel'
message500 = 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibu'
print('message has the following number of characters:', len(message325))

# up to 260 incl. fontsize: 72, width 20
# up to 120 incl. fontsize: 72, width 16

# run program:

get_image_from_unsplash()
create_image_with_message(message50, 'post')
# create_image_with_message(message50, 'story')
