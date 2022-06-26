from tkinter import CENTER, PhotoImage
from  PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from barcode import EAN13
from barcode.writer import ImageWriter
import random
import PIL
from numpy import number

# 523x280
number_barcode = random.randint(100000000000,999999999999)
barcode = EAN13(str(number_barcode),writer=ImageWriter())
barcode.save("barcode_image")

DOB = str(input("Enter your DOB :"))
blood_group = str(input("Enter your blood group :"))
student = str(input("Enter dayscalar or hostelar :"))
door_no = str(input("Enter the door number :"))
street = str(input("Enter your street :"))
near_location = str(input("Enter your nearby location :"))
city = str(input("Enter your city :"))
district = str(input("Enter your district :"))
state = str(input("Enter your state :"))
pincode = str(input("Enter your pincode :"))
parent_number = str(input("Enter your parent's number :"))
your_number =  str(input("Enter your number :"))


image = Image.open("C:\\Users\\USER\\Downloads\\id2.png").convert("RGBA")
bar = Image.open("barcode_image.png").convert("RGBA")

size_front = (650, 900)
size_bar = (450, 130)
main_image = image.resize(size_front)
main_bar = bar.resize(size_bar)

Image.Image.paste(main_image,main_bar,(60,680))

sub_font = ImageFont.truetype("C:\\Users\\USER\\Downloads\\poppins\\Poppins-Black.otf",35)
myname_font = ImageFont.truetype("C:\\Users\\USER\\Downloads\\poppins\\Poppins-Medium.otf",35)
d1 = ImageDraw.Draw(main_image)
d1.text((10,50),"DOB                                 :",font = sub_font,fill= (77,25,201),align=CENTER)
d1.text((330,50),DOB,font = myname_font,fill= (0,0,0),align=CENTER)

d1.text((10,110),"BLOOD  GROUP   :",font = sub_font,fill= (77,25,201),align=CENTER)
d1.text((330,110),blood_group,font = myname_font,fill= (0,0,0),align=CENTER)

d1.text((10,170),"STUDENT                   : ",font = sub_font,fill= (77,25,201),align=CENTER)
d1.text((330,170),student,font = myname_font,fill= (0,0,0),align=CENTER)

d1.text((10,230),"ADDRESS                   :",font = sub_font,fill= (77,25,201),align=CENTER)
d1.text((10,290)," ".join([door_no,street]),font = myname_font,fill= (0,0,0),align=CENTER)
d1.text((10,350)," ".join([near_location,city]),font = myname_font,fill= (0,0,0),align=CENTER)
d1.text((10,410)," ".join([district,state]),font = myname_font,fill= (0,0,0),align=CENTER)
d1.text((10,470),pincode,font = myname_font,fill= (0,0,0),align=CENTER)

d1.text((10,530),"PARENT'S NUMBER      : ",font = sub_font,fill= (77,25,201),align=CENTER)
d1.text((410,530),parent_number,font = myname_font,fill= (0,0,0),align=CENTER)

d1.text((10,590),"STUDENT'S NUMBER   :",font = sub_font,fill= (77,25,201),align=CENTER)
d1.text((410,590),your_number,font = myname_font,fill= (0,0,0),align=CENTER)


# print(bar.show)
main_image.show()