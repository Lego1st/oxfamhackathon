import numpy as np
from PIL import Image
import requests
import PIL
import pickle
import base64

def main():
    # inputs = input("Image:") 
    inputs = "demo/hnll11.jpg"
    location = raw_input("Location: ")
    
    with open(inputs, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    data = {
        'location': location,
        'image': encoded_string,
        'name' : inputs
    }
    # oim =  Image.open(data['image'])
    r = requests.post("http://10.182.17.48:8000/floody/campost/",data=data)

if __name__ =="__main__":
    main()
