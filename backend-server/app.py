#meme API / meme generator
#a simple API with GUI for creating simple memes
#it can be called with memegen.pythonanywhere.com/memegen/{textsize}/{number ot meme image}/{text at top}/{text at bottom}/
#this returns an html file with the image embedded
#I would really apprechiate it if you could check it out at meme-gen.github.io
#made by Laurin Seeholzer in august 2021

import time
from PIL import Image, ImageDraw, ImageFont
from flask import Flask, render_template
import os
from os import listdir


#function needed to convert a list to string
def list_to_string(s):
    new = ""
    for x in s:
        new += x
    return new

#initializing the app
app = Flask(__name__)

#route for meme-API
#uses parameters textsize, image (for the number ot the image), txt1 (String for the top), txt2 (String for the bottom)
@app.route('/memegen/<int:textsize>/<int:image>/<string:txt1>/<string:txt2>/')
def memegen(textsize, image, txt1, txt2):

    #deleding previously created memes 
    #because I dont have enough server-space
    for file_name in listdir("/home/memegen/mysite/static/"):
        if file_name.endswith('.jpg'):
            os.remove("/home/memegen/mysite/static/" + file_name)

    #assigning ID
    id = str(int(round(time.time() * 1000000, 0)))

    #getting image to work on
    image = "/home/memegen/mysite/static/" + str(image) + ".png"
    img = Image.open(image).convert('RGB')
    Draw = ImageDraw.Draw(img)

    #replace %20 with acctual spaces
    txt1 = txt1.replace("%20", " ")
    txt2 = txt2.replace("%20", " ")

    #defining the font
    font = ImageFont.truetype('/home/memegen/mysite/impact.ttf', textsize)

    #calculating text size (used later)
    txt1_width, txt1_height = Draw.textsize(txt1, font=font)
    txt2_width, txt2_height = Draw.textsize(txt2, font=font)




    #if text width of txt1 is bigger than image width
    #if yes, split txt1 up to txt1_1 and txt1_2
    if txt1_width >=  1024:
        
        #dividing word-count in two, so we can create two strings (txt1_1 and txt1_2)
        fisthalf = round(len(txt1.split())/2)
        secondhalf = len(txt1.split()) - fisthalf

        #initializing new strings (txt1_1 and txt1_2)
        txt1_1 = ""
        txt1_2 = ""

        #adding first half of the words to txt1_1
        for i in range(fisthalf):
            txt1_1 = txt1_1 + txt1.split()[i] + " "

        #adding second half of the words to txt1_2
        for i in range(fisthalf, fisthalf + secondhalf):
            txt1_2 = txt1_2 + txt1.split()[i] + " "

        #calculating text size of the new strings
        txt1_1_width, txt1_1_height = Draw.textsize(txt1_1, font=font)
        txt1_2_width, txt1_2_height = Draw.textsize(txt1_2, font=font)

        #calculating x coordinates of text position
        top1_1 = txt1_height / 2
        top1_2 = txt1_height + txt1_height

        #calculating y coordinates of text position
        left1_1 = (1024 / 2) - (txt1_1_width / 2)
        left1_2 = (1024 / 2) - (txt1_2_width / 2)

        #drawing outline/shadow of txt1_1
        Draw.text((left1_1 -1, top1_1 -1), txt1_1, font=font, fill=(0,0,0))
        Draw.text((left1_1 +1, top1_1 -1), txt1_1, font=font, fill=(0,0,0))
        Draw.text((left1_1 -1, top1_1 +1), txt1_1, font=font, fill=(0,0,0))
        Draw.text((left1_1 +1, top1_1 +1), txt1_1, font=font, fill=(0,0,0))

        #drawing outline/shadow of txt1_2
        Draw.text((left1_2 -1, top1_2 -1), txt1_2, font=font, fill=(0,0,0))
        Draw.text((left1_2 +1, top1_2 -1), txt1_2, font=font, fill=(0,0,0))
        Draw.text((left1_2 -1, top1_2 +1), txt1_2, font=font, fill=(0,0,0))
        Draw.text((left1_2 +1, top1_2 +1), txt1_2, font=font, fill=(0,0,0))

        #drawing txt1_1 and txt1_2
        Draw.text((left1_1, top1_1), txt1_1, font=font, fill=(255, 255, 255))
        Draw.text((left1_2, top1_2), txt1_2, font=font, fill=(255, 255, 255))

    #if text width of txt1 is smaller than image width
    #just drawing txt1 on the image
    else:

        #calculating coordinates for position
        top1 = txt1_height / 2
        left1 = (1024 / 2) - (txt1_width / 2)

        #drawing outline/shadow of txt1
        Draw.text((left1 -1, top1 -1), txt1, font=font, fill=(0,0,0))
        Draw.text((left1 +1, top1 -1), txt1, font=font, fill=(0,0,0))
        Draw.text((left1 -1, top1 +1), txt1, font=font, fill=(0,0,0))
        Draw.text((left1 +1, top1 +1), txt1, font=font, fill=(0,0,0))

        #drawing txt1
        Draw.text((left1, top1), txt1, font=font, fill=(255, 255, 255))




    #if text width of txt2 is bigger than image width
    #if yes, split txt2 up to txt2_1 and txt2_2
    if txt2_width >  1024:

        #dividing word-count in two, so we can create two strings (txt2_1 and txt2_2)
        fisthalf = round(len(txt2.split())/2)
        secondhalf = len(txt2.split()) - fisthalf

        #initializing new strings (txt2_1 and txt2_2)
        txt2_1 = ""
        txt2_2 = ""

        #adding first half of the words to txt1_1
        for i in range(fisthalf):
            txt2_1 = txt2_1 + txt2.split()[i] + " "

        #adding second half of the words to txt1_2
        for i in range(fisthalf, fisthalf + secondhalf):
            txt2_2 = txt2_2 + txt2.split()[i]+ " "
        
        #calculating text size of the new strings
        txt2_1_width, txt2_1_height = Draw.textsize(txt2_1, font=font)
        txt2_2_width, txt2_2_height = Draw.textsize(txt2_2, font=font)

        #calculating x coordinates of text position
        top2_1 = 1024 - txt2_height - txt2_height - txt2_height
        top2_2 = 1024 - txt2_height - (txt2_height / 2)

        #calculating y coordinates of text position
        left2_1 = (1024 / 2) - (txt2_1_width / 2)
        left2_2 = (1024 / 2) - (txt2_2_width / 2)

        #drawing outline/shadow of txt2_1
        Draw.text((left2_1 -1, top2_1 -1), txt2_1, font=font, fill=(0,0,0))
        Draw.text((left2_1 +1, top2_1 -1), txt2_1, font=font, fill=(0,0,0))
        Draw.text((left2_1 -1, top2_1 +1), txt2_1, font=font, fill=(0,0,0))
        Draw.text((left2_1 +1, top2_1 +1), txt2_1, font=font, fill=(0,0,0))

        #drawing outline/shadow of txt2_2
        Draw.text((left2_2 -1, top2_2 -1), txt2_2, font=font, fill=(0,0,0))
        Draw.text((left2_2 +1, top2_2 -1), txt2_2, font=font, fill=(0,0,0))
        Draw.text((left2_2 -1, top2_2 +1), txt2_2, font=font, fill=(0,0,0))
        Draw.text((left2_2 +1, top2_2 +1), txt2_2, font=font, fill=(0,0,0))

        #drawing txt2_1 and txt2_2
        Draw.text((left2_1, top2_1), txt2_1, font=font, fill=(255, 255, 255))
        Draw.text((left2_2, top2_2), txt2_2, font=font, fill=(255, 255, 255))

    #if text width of txt2 is smaller than image width
    #just drawing txt1 on the image
    else:

        #calculating coordinates for position
        top2 = 1024 - txt2_height - (txt2_height / 2)
        left2 = (1024 / 2) - (txt2_width / 2)

        #drawing outline/shadow of txt2
        Draw.text((left2 -1, top2 -1), txt2, font=font, fill=(0,0,0))
        Draw.text((left2 +1, top2 -1), txt2, font=font, fill=(0,0,0))
        Draw.text((left2 -1, top2 +1), txt2, font=font, fill=(0,0,0))
        Draw.text((left2 +1, top2 +1), txt2, font=font, fill=(0,0,0))

        #writing txt2
        Draw.text((left2, top2), txt2, font=font, fill=(255, 255, 255))

    #save image
    img.save("/home/memegen/mysite/static/" + id + ".jpg")

    #return image.html with the variable id = id (which was assigned at the beginning)
    #by knowing the id of the image, you can get it from the static directory (id.jpg)
    return render_template("image.html", id=id)



#made by Laurin Seeholzer in august 2021
