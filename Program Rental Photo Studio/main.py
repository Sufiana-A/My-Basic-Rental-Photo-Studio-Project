from PIL import Image, ImageDraw, ImageFont
import string
import random
import vlc
import time

revenueBS = []
revenueMS = []
revenueCS = []
def addFile(revenue,name):
    with open(revenue, 'w') as j:
        for i in name:
            j.write("%s\n" %str(i))
        #j.write("\n".join(str(i) for i in name))
    j.close()


#for specifying every studio 
class Studio:

    def __str__(self):
        return("""Hello....Greeting From Rainbow Here \U0001F603.
        \nWe provide you photo studio rental services.
        \nRegister for yourself & for your group.
        \nREGISTER NOW and LET RAINBOW COLOR YOUR PICT.
        """)

    def __init__(self,name,theme,fee,large,capacity,wifi=True):
        self.name = name
        self.theme = theme
        self.fee = fee
        self.large = large
        self.capacity = capacity
        self.wifi = wifi

    def info(self):
        if self.wifi == True:
            wifi_availability = "Available 100 mbps"
        else:
            wifi_availability = "Unavailable"
        return ("Name\t\t\t: {}".format(self.name) +
                "\nStudio Theme\t\t: {}".format(self.theme) +
                "\nFare Per 5 Minutes\t: {} $".format(self.fee) +
                "\nLarge Studio\t\t: {} m^2".format(self.large) +
                "\nCozy Capacity\t\t: {}".format(self.capacity) +
                "\nWifi Availability\t: {}".format(wifi_availability) +
                "\n=============================================================================" +
                """\nNOTE: for rental times that are not multiples of 5 (minutes) 
                        \nwill be rounded so that it affects the total fare.
                        \n1. If your rental times 24 minutes, it will be counted as 20 minutes
                        \n2. If your rental times is 27 minutes, it will be counted as 30 minutes
                \n================================================================================""")

#instantiate object
CozyRS = Studio('Cozy Room Studio','Small Living Room',13,'29 x 50',9,wifi=False)
MusicRS = Studio('Music Room Studio','Clasic Music Room',20,'50 x 40',14,wifi=True)
WhiteSC = Studio('White Screen Studio','White Background',19,'45 x 30',10,wifi=True)
    
#fungsi show image of studio foto
studio1 = "Music\nRoom\nStudio\n"
studio2 = "Cozy\nRoom\nStudio\n"
studio3 = "White\nScreen\nStudio\n"
studio_dict = {studio1:"Photo by John Matychuk on Unsplash",
studio2:"Photo by Spacejoy on Unsplash",
studio3:"Image by Pexels from Pixabay"}
def display(nameFile,nameStudio,photoby,anotherFile):
    img = Image.open(nameFile)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf",100)
    font1 = ImageFont.truetype("arial.ttf",25)
    draw.text((0,0),nameStudio,font=font,fill=(255, 0, 0))
    draw.text((700,780),photoby,font=font1,fill=(255, 0, 0))
    img.save(anotherFile)
    img.show()
    

#fungsi play audio & tampilkan pesan rental berakhir
def delay(howlong):
    print("Sound and message will imediately appear")
    time.sleep(howlong*60) #in seconds
    print("Your Rental time is over.\nPlease empty this room imediately!")

#function to generate user ID
def userID():
    S = 5  #number of characters in the string.  
    #call random.choices() string module to find the string in Uppercase + numeric data.  
    userID = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))    
    #print(f"Your ID: {userID}")
    return userID

while True:
    print(CozyRS)
    print("==THIS IS OUR MENU==")
    print("""
    1. Lihat Tema Studio Foto Kami
    2. Daftar untuk Sewa
    3. Exit
    """)
    try:
        inp1 = int(input("Kamu Mau Pilih Menu Yang Mana Nih (1-3)? "))
    except ValueError:
        print("Whoops...Tolong Inputkan Angka Saja Ya (1-3)")
        #inp1 = int(input("Kamu Mau Pilih Menu Yang Mana Nih (1-3)? "))
    else:
        if inp1 == 1:
            print("Yuk Lihat Contoh Gambar dan Spesifikasi Studio Foto Kami:)")
            print("""TEMA STUDIO FOTO RAINBOW:
1. Music Room Studio
2. Cozy Room Studio
3. White Screen Studio
""")
            try:
                inp3 = int(input("Silakan Input Nomor Sesuai Nama Tema Yang Mau Kamu Lihat (1-3): "))
            except ValueError:
                print("Sorry, Input Integer Only (1-3)")
                #inp3 = int(input("Silakan Input Nomor Sesuai Nama Tema Yang Mau Kamu Lihat (1-3): "))
            else:
                if inp3 == 1:
                    print(MusicRS.info())
                    display('MusicRoomStudio.png',studio1,studio_dict[studio1],'SampleStudio1.png')
                elif inp3 == 2:
                    print(CozyRS.info())
                    display('CozyRoomStudio.png',studio2,studio_dict[studio2],'SampleStudio2.png')
                elif inp3 == 3:
                    print(WhiteSC.info())
                    display('WhiteScreenStudio.png',studio3,studio_dict[studio3],'SampleStudio3.png')
                else:
                    print("OOPS...Inputkan Nomor Antara 1-3 Ya Sesuai Tema Yang Mau Kamu Lihat")
                    #inp3 = int(input("Silakan Input Nomor Sesuai Nama Tema Yang Mau Kamu Lihat (1-3): "))
        elif inp1 == 2:
            print("""TEMA STUDIO FOTO RAINBOW:
1. Music Room Studio
2. Cozy Room Studio
3. White Screen Studio
""")                
            try:
                inp4 = int(input("Tema Studio Foto Mana, Nih Yang Mau Kamu Pesan? "))
            except ValueError:
                print("Sorry, Tolong Input Dalam Bentuk Angka Ya (1-3)")
                #inp4 = int(input("Tema Studio Foto Mana, Nih Yang Mau Kamu Pesan? "))
            else:
                if inp4 in range(1,4):
                    try:
                        print("Inputkan Berapa Lama Waktu Sewa dalam Menit")
                        a = int(input("Enter time in minutes (integer only): "))
                        if a < 5:
                            print("Whoops...Time Minimum For Rent Is 5 Minutes!")
                            a = int(input("Enter time in minutes (integer only): "))
                        elif a % 10 in range(6,10):
                            time1 = a + (10-(a % 10))
                            print(f"From {a} become {time1}")
                        elif a % 10 in range(1,5):
                            time1 = a - (a % 10)
                            print(f"From {a} become {time1}")
                        elif a % 5 == 0:
                            print(f"Time {a} in minutes is not changed at all")
                    except ValueError:
                        print("Sorry, Enter time in minutes but 'integer only'!")
                    print("----==========----==========----==========----==========----==========")
                    print("INI SPESIFIKASI STUDIO FOTO YANG KAMU SEWA")
                    if inp4 == 1:
                        print(MusicRS.info())
                        iduser = userID()
                        print(f"User Room ID Kamu: {iduser}")
                        print("Silakan Masukkan User Room ID Kamu di Monitor di Depan Ruangan Studio Foto Yang Kamu Sewa")
                        total_fare = round((MusicRS.fee * (a/5)),2)
                        revenueMS.append(total_fare)
                        print(f"Total Biaya Sewa Kamu = {total_fare} $")
                        addFile('RevenueMusicRoomStudio.txt',revenueMS)
                        sound = vlc.MediaPlayer("Register's voice.mp3")
                        sound.play()
                    elif inp4 == 2:
                        print(CozyRS.info())
                        iduser = userID()
                        print(f"User Room ID Kamu: {iduser}")
                        print("Silakan Masukkan User Room ID Kamu di Monitor di Depan Ruangan Studio Foto Yang Kamu Sewa")
                        total_fare = round((CozyRS.fee * (a/5)),2)
                        revenueCS.append(total_fare)
                        print(f"Total Biaya Sewa Kamu = {total_fare} $")
                        addFile('RevenueCozyRoomStudio.txt',revenueCS)
                        sound = vlc.MediaPlayer("Register's voice.mp3")
                        sound.play()
                    elif inp4 == 3:
                        print(WhiteSC.info())
                        iduser = userID()
                        print(f"User Room ID Kamu: {iduser}")
                        print("Silakan Masukkan User Room ID Kamu di Monitor di Depan Ruangan Studio Foto Yang Kamu Sewa")
                        total_fare = round((WhiteSC.fee * (a/5)),2)
                        revenueBS.append(total_fare)
                        print(f"Total Biaya Sewa Kamu = {total_fare} $")
                        addFile('RevenueWhiteScreenStudio.txt',revenueBS)
                        sound = vlc.MediaPlayer("Register's voice.mp3")
                        sound.play()
                    try:
                        print("=====================================================================")
                        reminder = input("Remind For Rental Time Limit? (yes/no) ")
                    except:
                        print("Tolong Inputkan Lagi Ya (yes/no)")
                    else:
                        if reminder == 'yes' or reminder == 'Yes':
                            delay(a)
                            rem = 1
                            while rem == 1:
                                sound2 = vlc.MediaPlayer("Time limit.mp3")
                                sound2.play()
                                print("==============================================================")
                                break
                        else:
                            print("Ok..No Problem, Please Be On Time!")
                            print("==================================================================")
                else:
                    print("OOPS..Tolong Input Angka (1-3) Sesuai Studio Foto Yang Kamu Pilih Ya")
                    inp4 = int(input("Tema Studio Foto Mana, Nih Yang Mau Kamu Pesan? "))
        elif inp1 == 3:
            print("Yah...Kamu Keluar Program")
            print("Masuk Lagi Untuk Lihat Layanan dan Pesan Sewa")
            break
        else:
            print("Whoops...Tolong Inputkan Angka 1 sampai 3 Saja Ya")
            