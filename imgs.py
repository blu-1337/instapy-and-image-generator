from PIL import Image, ImageDraw, ImageFont
import textwrap


def crop_center(pil_img, crop_width, crop_height):  # make image square
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))


def create_image_with_message(message):
    width = 1080
    height = 1080
    font = ImageFont.truetype("./jetbrains.ttf", size=72)
        # img = Image.new('RGB', (width, height), color='blue')
    img = Image.open(r'./sample-imgs/Heart-Rose1.jpg')

    img = crop_center(img, 1080, 1080)  # make a square
    img.putalpha(127)  # make half transparent

    imgDraw = ImageDraw.Draw(img)

    # textWidth, textHeight = imgDraw.textsize(message, font=font)
    textWidth = imgDraw.textlength('cristiancristian1234', font=font)
    textHeight = imgDraw.textsize('cristiancristian1234', font=font)[1]  # it's deprecated but it's more precise
    xText = (width - textWidth) / 2
    yText = (height - textHeight) / 2

    print('text width:', textWidth)
    print('text height:', textHeight)
    print('textbox:', imgDraw.textlength('cristiancristian1234', font=font))  # 20 characters
    print('textbox height:', imgDraw.textlength('C', font=font, direction="ttb"))  # 20 characters


    # imgDraw.text((xText, yText), message, font=font, fill=(255, 255, 0))


    totalHeight = 0
    for line in textwrap.wrap(message, width=20):  # first get total height
        totalHeight += textHeight

    margin = 100
    offset = (height - totalHeight) / 2

    for line in textwrap.wrap(message, width=20):
        imgDraw.text((margin, offset), line, font=font, fill="#ffffff")
        offset += textHeight



    img.save('result.png')


message = \
        "Alwaysaa try to end the day with a positiveday with a positiveday with a positive thought. No matter how hard as df  asdfas dfas asdf a things are, tomorrow is a fresh opportunity to make everything better."


create_image_with_message(message)



