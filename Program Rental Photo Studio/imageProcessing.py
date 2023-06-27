from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

#jadiin satu fungsi
#def display(nameFile):
    #img = Image.open('CozyRoomStudio.png')
    #draw = ImageDraw.Draw(img)
    #font = ImageFont.truetype("arial.ttf",100)
    #font1 = ImageFont.truetype("arial.ttf",25)
    #draw.text((0,0),"Cozy\nRoom\nStudio\n",font=font,fill=(255, 0, 0))
    #draw.text((800,800),"Photo by Spacejoy on Unsplash",font=font1,fill=(255, 0, 0))
    #img.show()
    #img.save("sampleStudio1.png")
#display('CozyRoomStudio.png')

#revise for letak gambar agak ke kanan
#def display(nameFile):
    #img = Image.open('WhiteScreenStudio.png')
    #draw = ImageDraw.Draw(img)
    #font = ImageFont.truetype("arial.ttf",100)
    #font1 = ImageFont.truetype("arial.ttf",25)
    #draw.text((0,0),"White\nScreen\nStudio\n",font=font,fill=(255, 0, 0))
    #draw.text((700,700),"Image by Pexels from Pixabay",font=font1,fill=(255, 0, 0))
    #img.show()
#display('WhiteScreenStudio.png')

""""
def display(nameFile):
    photoby1 = "Photo by John Matychuk on Unsplash"
    img = Image.open(nameFile)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf",100)
    font1 = ImageFont.truetype("arial.ttf",25)
    draw.text((0,0),"Music\nRoom\nStudio\n",font=font,fill=(255,0,0))
    draw.text((700,700),photoby1,font=font1,fill=(255,0,0))
    img.show()
#display('MusicRoomStudio.png')
"""
studio1 = "Music\nRoom\nStudio\n"
studio2 = "Cozy\nRoom\nStudio\n"
studio3 = "White\nScreen\nStudio\n"
studio_dict = {studio1:"Photo by John Matychuk on Unsplash",
studio2:"Photo by Spacejoy on Unsplash",
studio3:"Image by Pexels from Pixabay"}
def display(nameFile,nameStudio,photoby):
    img = Image.open(nameFile)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf",100)
    font1 = ImageFont.truetype("arial.ttf",25)
    draw.text((0,0),nameStudio,font=font,fill=(255, 0, 0))
    draw.text((700,780),photoby,font=font1,fill=(255, 0, 0))
    img.show()

#display('MusicRoomStudio.png',studio1,studio_dict[studio1])
#display('CozyRoomStudio.png',studio2,studio_dict[studio2])
#display('WhiteScreenStudio.png',studio3,studio_dict[studio3])

"""""
while True:
    inp = input("Do you want to see our studio?  ")
    if inp == 'yes':
        display('MusicRoomStudio.png')
        inp1 = input("Are you OK with the visual? ")
        if inp1 == 'yes':
            print("Thank You Make Sure You Rent This One:)")
            break
    else:
        print("OK Come Back Here Again Immediately Dear:)")
        break
"""
