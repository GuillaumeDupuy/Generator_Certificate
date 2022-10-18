# import

import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import os

# process

if os.path.exists('certificates'):
    print("Creating....Wait")
else:
    os.mkdir('certificates')

data = pd.read_csv(r'setup/Git and Git-Hub.csv')
name_list = data["Name"].tolist()

for i in name_list:

    im = Image.open(r'img/Template.jpg')
    width, height = im.size
    w = width+height/width-height
    h = width+height/width-height
    d = ImageDraw.Draw(im)

    # Attendee name
    fon = ImageFont.truetype("Fonts/GothamBold.ttf", 52)
    location = (w+175, h+150)
    text_color = (64, 86, 125)

    # location for Attendee name
    d.text(location, i, fill=text_color,
           font=fon, stroke_width=1, align='left')

    # my name signature
    fox = ImageFont.truetype("Fonts/PWSignaturetwo.ttf", 55)
    locat = (85, 1000)
    txt_color = (127, 82, 23)
    l = "Muhammad Saad Fareed"

    # location for my signature
    d.text(locat, l, fill=txt_color, font=fox, stroke_width=1, align='left')
    # Saving my certificate
    cwd = os.getcwd()
    cert_dir = cwd+'/certificates/'
    filee = cert_dir+"certificate_" + i + ".jpeg"
    im.save(filee)
    filee = cert_dir+"certificate_" + i + ".pdf"
    im.save(filee)
