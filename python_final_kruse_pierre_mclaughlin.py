from PIL import Image, ImageDraw, ImageFont
import math
#importing the stuff

imageFileName = input("enter path of image: ") 
image = Image.open(imageFileName)
print("Image is loading...")

def deepfry(img):
    #get the height and width of the image
    w, h = img.size
    for row in range(h):
        for col in range(w):
            coordinates = col, row
            p = img.getpixel(coordinates)
            #What are the red, blue and green values for p?
            rgb_img = img.convert('RGB')
            r, g, b = rgb_img.getpixel(coordinates)
            red_value = r
            green_value = g
            blue_value = b
            max_color = max(red_value, blue_value, green_value)
            #makes white
            if red_value + green_value + blue_value >= 550:
                newred = red_value + 100
                newgreen = green_value + 50
                newblue = blue_value + 25
            #makes black
            elif red_value + green_value + blue_value <= 150:
                newred = red_value + 200
                newgreen = green_value + 100
                newblue = blue_value - 200
            #makes red
            elif max_color == red_value:
                newred = red_value + 50
                newgreen = 0
                newblue = 0
            #makes green
            elif max_color == green_value:
                newred = 255
                newgreen = 255
                newblue = 0
            #makes blue
            else:
                newred = red_value - 25
                newgreen = green_value - 75
                newblue = blue_value - 75

            #set new pixel to new color values.
            newpixel = (newred, newgreen, newblue)
            img.putpixel((col, row), newpixel)
            
    # then draw the new images
    draw = ImageDraw.Draw(img)
    return draw


def top_text():
    W, H = image.size
    top_choice = input("Do you wish to add top text? Yes or no")
    top_choice = top_choice.lower()
    if top_choice == "yes":
        #Text input and preparing image
        txt = input("<insert top text here>")
        font_size = input("How large do you want the text? Big, Small")
        font_size = font_size.lower()
        if font_size == "big":
            f = 72
        else:
            f = 24
        font_type = ImageFont.truetype('Impact.ttf', f)
        draw = ImageDraw.Draw(image)
        w, h = draw.textsize(txt)
        #Adding outline
        draw.text(((W-w)/2-1, 0-1), txt, font=font_type, fill=(0,0,0))
        draw.text(((W-w)/2+1, 0-1), txt, font=font_type, fill=(0,0,0))
        draw.text(((W-w)/2-1, 0+1), txt, font=font_type, fill=(0,0,0))
        draw.text(((W-w)/2+1, 0+1), txt, font=font_type, fill=(0,0,0))
        #Printing centered text
        draw.text(((W-w)/2, 0), text=txt, fill=(255, 255 ,255), font=font_type)
    else:
        return

def bottom_text():
    W, H = image.size
    bottom_choice = input("Do you wish to add bottom text? Yes or no")
    bottom_choice = bottom_choice.lower()
    if bottom_choice == "yes":
        txt = input("<insert bottom text here>")
        font_size = input("How large do you want the text? Big, Small")
        font_size = font_size.lower()
        if font_size == "big":
            f = 72
        else:
            f = 24
        font_type = ImageFont.truetype('Impact.ttf', f)
        draw = ImageDraw.Draw(image)
        w, h = draw.textsize(txt)
        draw.text(((W-w)/2-1, H-100-1), txt, font=font_type, fill=(0,0,0))
        draw.text(((W-w)/2+1, H-100-1), txt, font=font_type, fill=(0,0,0))
        draw.text(((W-w)/2-1, H-100+1), txt, font=font_type, fill=(0,0,0))
        draw.text(((W-w)/2+1, H-100+1), txt, font=font_type, fill=(0,0,0))
        draw.text(((W-w)/2, H-100), text=txt, fill=(255, 255 ,255), font=font_type)
    else:
        return

#Save the file to desktop
def save():
    x = input("Would you like to save your image?")
    if x == "yes":
        y = input("Enter filename and filetype. Example: image.png")
        image.save(y)
    else:
        return

final = deepfry(image)
top_text()
bottom_text()
image.show()
save()



                   
