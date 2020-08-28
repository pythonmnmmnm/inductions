#this file is used to process data and extract text on the deployed image
#sudo pip3 install pillow pytesseract
from PIL import Image
import pytesseract
im = Image.open("<image>file goes here")
text = pytesseract.image_to_string(im,lang='eng')
print(text)
#this will be used to test on images which are being deployed.