import PySimpleGUI as sg 
import io
import base64
import PIL.Image
import os

def resize_image(image_path, resize=None): #image_path: "C:User/Image/img.jpg"

    img = PIL.Image.open(image_path)

    cur_width, cur_height = img.size
    if resize:
        new_width, new_height = resize
        scale = min(new_height/cur_height, new_width/cur_width)
        img = img.resize((int(cur_width*scale), int(cur_height*scale)), PIL.Image.LANCZOS)
    bio = io.BytesIO()
    img.save(image_path, format="PNG")
    del img
    return bio.getvalue()


resize_image('poker_chip3.png',(40,40))


#directory = os.fsencode()

#for file in os.listdir(os.getcwd()):
#    filename = os.fsdecode(file)
#    
#    
#    resize_image(filename, (90,120))
    
