from tkinter import CENTER, PhotoImage
from  PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import PIL


# (650, 1039)

# receiving input from user

myphoto = str(input("Enter the location of your's photo in this computer :"))
college_logo = str(input("Enter the location your's college logo image in this computer:"))
college_name1 = str(input("Enter your college name (enter main tittle only ) :"))
college_name2 = str(input("Enter your college name (enter remaining name only ) :"))
your_name = str(input("Enter your name :"))
roll_no = str(input("Enter your roll no :"))
year = str(input("Enter which year you are studying :"))
degree = str(input("Enter your degree :"))
course = str(input("Enter your branch :"))

# open the image

front = Image.open("C:\\Users\\USER\\Downloads\\4958577397a4539.png").convert("RGBA")
P1 = Image.open(myphoto).convert("RGBA")
l1 = Image.open(college_logo).convert("RGBA")

# giving size for image

size_front = (650, 900)
size_photo = (270,300)
size_logo = (110,110)

# resize the image

photo = P1.resize(size_photo)
logo = l1.resize(size_logo)
front = front.resize(size_front)

Image.Image.paste(front,photo,(180,270))

title_font = ImageFont.truetype("C:\\Users\\USER\\Downloads\\poppins\\Poppins-Black.otf",55)

d1 = ImageDraw.Draw(front)

d1.text((170,10),college_name1,font = title_font,fill= (255,255,0))


title_sub = ImageFont.truetype("C:\\Users\\USER\\Downloads\\poppins\\Poppins-Regular.otf",30)

d1.text((200,70),college_name2,font = title_sub ,fill= (0,0,0))

sub_font = ImageFont.truetype("C:\\Users\\USER\\Downloads\\poppins\\Poppins-Black.otf",35)
myname_font = ImageFont.truetype("C:\\Users\\USER\\Downloads\\poppins\\Poppins-Medium.otf",35)

d1.text((10,600),"NAME        :",font = sub_font,fill= (77,25,201),align=CENTER)
d1.text((200,600),your_name,font = myname_font,fill= (0,0,0),align=CENTER)

d1.text((10,660),"ROLL NO :",font = sub_font,fill= (77,25,201),align=CENTER)
d1.text((200,660),roll_no,font = myname_font,fill= (0,0,0),align=CENTER)

d1.text((10,720),"YEAR          :",font = sub_font,fill= (77,25,201),align=CENTER)
d1.text((200,720),year,font = myname_font,fill= (0,0,0),align=CENTER)

d1.text((10,780),"DEGREE/BRANCH :",font = sub_font,fill= (77,25,201),align=CENTER)


course_font = ImageFont.truetype("C:\\Users\\USER\\Downloads\\poppins\\Poppins-Medium.otf",28)
d1.text((10,840),degree,font = course_font,fill= (0,0,0),align=CENTER)
d1.text((93,840),"/",font = course_font,fill= (0,0,0),align=CENTER)
d1.text((103,840),course,font = course_font ,fill= (0,0,0),align=CENTER)

Image.Image.paste(front,logo,(20,20))

front.show()
