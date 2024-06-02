import customtkinter as ctk
import customtkinter
from tkinter import filedialog
from playsound import playsound
import cv2
from PIL import ImageTk, Image  
import os
from customtkinter import filedialog
from pygame import mixer
import time
from cryptography.fernet import Fernet
# Create the Tkinter window

window = ctk.CTk()
mainaudio=None
maintextfile=None   
# Set window attributes
window.geometry("900x600")
window.title("Data Encrypter")
customtkinter.set_appearance_mode("dark")

current_dir = os.path.dirname(__file__)
icon_path1 = os.path.join(current_dir, "assets", "protection_shield_security_secured_padlock_icon_225158 (1).ico")

window.iconbitmap(icon_path1)



for widget in window.winfo_children():
        widget.configure(text_color='red')

image_path = os.path.join(current_dir, "assets","ic_photo_128_28568.png")
if os.path.exists(image_path):
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
image_path1= os.path.join(current_dir, "assets","video_284_34299 (2).png")
if os.path.exists(image_path1):
    image1 = Image.open(image_path1)
    photo1 = ImageTk.PhotoImage(image1)
image_path2= os.path.join(current_dir, "assets","music_audio_7173.png")
if os.path.exists(image_path2):
    image2 = Image.open(image_path2)
    photo2 = ImageTk.PhotoImage(image2)

image_path3= os.path.join(current_dir, "assets","documentediting_editdocuments_text_documentedi_2820.png" )
if os.path.exists(image_path3):
    image3 = Image.open(image_path3)
    photo3 = ImageTk.PhotoImage(image3)
    
encryptimg1=os.path.join(current_dir, "assets","encryption.png")
if os.path.exists(encryptimg1):
    encimage = Image.open(encryptimg1)
    encimage1 = ImageTk.PhotoImage(encimage)
    
decrypt=os.path.join(current_dir, "assets","decryption.png")
if os.path.exists(decrypt):
    decimage = Image.open(decrypt)
    decimage1 = ImageTk.PhotoImage(decimage)

musicpng=os.path.join(current_dir, "assets","music_audio_7173 (1).png")
if os.path.exists(musicpng):
    musicpng = Image.open(musicpng)
    musicpng = ImageTk.PhotoImage(musicpng)

startpng=os.path.join(current_dir, "assets","pngegg.png")


if os.path.exists(startpng):
    
    startpng= Image.open(startpng)
    startpng=startpng.resize((25,25))
    
    startpng= ImageTk.PhotoImage(startpng)
   
        
pausepng=os.path.join(current_dir, "assets","pngwing.com (3).png")
if os.path.exists(pausepng):
    pausepng = Image.open(pausepng)
    pausepng = pausepng.resize((25, 25))
    pausepng = ImageTk.PhotoImage(pausepng)


stoppng=os.path.join(current_dir, "assets","pngwing.com (2).png")
if os.path.exists(stoppng):
    stoppng = Image.open(stoppng)
    stoppng=stoppng.resize((25,25))
    stoppng = ImageTk.PhotoImage(stoppng)
    
def textframe():
    # Hide other frames if visibl
    photosframe1.place_forget()
    Videoframe1.place_forget()
    Audioframe1.place_forget()
    textframe1.place(x=400, y=60)

    # Show text frame
def photosframe():
    textframe1.place_forget()
    Videoframe1.place_forget()
    Audioframe1.place_forget()
    photosframe1.place(x=400, y=60)  # Show photos frame

def videoframe():
    textframe1.place_forget()
    photosframe1.place_forget()
    Audioframe1.place_forget()
    Videoframe1.place(x=400,y=60)
    
def Audioframe():
    textframe1.place_forget()
    Videoframe1.place_forget()
    Audioframe1.place_forget()
    photosframe1.place_forget()
    Audioframe1.place(x=400,y=60)
    
    
 
def selectfile():
    global maintextfile
    filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if filename.endswith('.txt'):
            with open(filename,"r")as data:
                data=data.read()
                maintextfile=filename
                textbox1.delete('1.0',"end")
                textbox1.insert('1.0', data)
    else:
            print("invalid")
    
def switch_event():
    response = switch_var.get()
    if response == "on":
        customtkinter.set_appearance_mode("light")
        buttons = [
            framebutton1, framebutton2, framebutton3, framebutton4, 
            filedialog1, clearbutton, encbutton, decbutton, 
            filedialog2, clearbutton2, encbutton2, decbutton2, 
            filedialog3, vidplaybtn44, clearbutton3, encbutton3, decbutton3, 
            filedialog4, clearbutton4, encbutton4, decbutton4, 
            stopbtn, unstopbtn, audioplay1,filedialog1,framebutton1,framebutton2,
            framebutton3,framebutton4
        ]
        for button in buttons:
            button.configure(text_color="black")
        customtkinter.set_appearance_mode("light")
        switch.configure(text="Dark Mode")
    elif response == "off":
        
        buttons = [
            framebutton1, framebutton2, framebutton3, framebutton4, 
            filedialog1, clearbutton, encbutton, decbutton, 
            filedialog2, clearbutton2, encbutton2, decbutton2, 
            filedialog3, vidplaybtn44, clearbutton3, encbutton3, decbutton3, 
            filedialog4, clearbutton4, encbutton4, decbutton4, 
            stopbtn, unstopbtn, audioplay1,filedialog1,framebutton1,framebutton2,
            framebutton3,framebutton4
        ]
        for button in buttons:
            button.configure(text_color="white")
        customtkinter.set_appearance_mode("dark")
        switch.configure(text="Light Mode")

def clearselection():
        textbox1.delete('1.0',"end")
mainimgfile1=None        
def selectimage():
    global mainimgfile1
    filename1 = filedialog.askopenfilename(filetypes=[("Images", "*.png")])
    mainimgfile1=filename1
    if os.path.exists(filename1):
        my_image = ctk.CTkImage(light_image=Image.open(filename1),size=(500, 300))
        label.place(x=30,y=150)
        label2.place(x=50,y=460)
        label.configure(image=my_image)
        label2.configure(text=filename1)

    
def clearimamge():
    
    label.configure(image=None)
    label2.configure(text="")
    



def clearaudio():
    
    musicimg1.place_forget()
    label3.place_forget()
    audioplay1.place_forget()
    stopbtn.place_forget()
    unstopbtn.place_forget()
    
    label.place_forget()
    label2.place_forget()
       
def audiopause():
    
    mixer.music.pause()

def audiounpause():
    mixer.music.unpause()
    
    
def audioplay():
    mixer.init()
    mixer.music.load(mainaudio) 
    mixer.music.play()
   

       
def selectaudio1():
    global mainaudio
    audiofile = filedialog.askopenfilename(filetypes=[("Audio", "*.mp3")])
    if audiofile and os.path.exists(audiofile):
        mainaudio=audiofile
        musicimg1.place(x=80,y=200)
        stopbtn.place(x=200,y=400)
        unstopbtn.place(x=350,y=400)
        audioplay1.place(x=20,y=400)
        label3.configure(text=audiofile)
        label3.place(x=70,y=300)



mainvideofile1=None          

def selectvideo():
    global mainvideofile1
    global cap
    videofile= filedialog.askopenfilename(filetypes=[("Video", "*.mp4")])
    mainvideofile1=videofile
    label4.configure(text=mainvideofile1)
    if videofile:
        cap = cv2.VideoCapture(videofile)
   
    
   

    # if os.path.exists(videofile):
        
    #     label4.configure(text=videofile)
    #     label4.place(x=50,y=460)
    
                                                      
                                                      
                                                
#----------------------------------------------------------------------------------------------------------------------------    
    

    
        
def encrypt_audio():
    
    key=Fernet.generate_key()
    print(key)
    
    fernet=Fernet(key)
    with open("enckeytoday.key","wb")as filenew:
        filenew.write(key)
    
    with open("enckeytoday.key","rb")as filenew1:
        data=filenew1.read()
    print(mainaudio) 
    
    with open(mainaudio,"rb") as sound:
        
        original_wav=sound.read()

        encryptedsound=fernet.encrypt(original_wav)    

    with open("encryptedsoundnew.mp3","wb") as sound1:
          sound1.write(encryptedsound)
   
#----------------------------------------------------------------------------------------------------------------------    


def decrypt_audio():
    with open("enckeytoday.key", "rb") as filenew12:
        key1 = filenew12.read()
    
    fernet1 = Fernet(key1)
    
    with open(mainaudio, "rb") as sound1:
        original_wav1 = sound1.read()
        decrypted = fernet1.decrypt(original_wav1)
        
    with open("decryptedaudionew.mp3", "wb") as dec:
        dec.write(decrypted)
    
#-------------------------------------------------------------------------------------------------------------------------------    
def encrypt_txt():
    key3=Fernet.generate_key()
    fernet3=Fernet(key3)
    with open("enckeytext.key","wb")as filenew:
        filenew.write(key3)
    
    with open("enckeytext.key","rb")as filenew1:
        data=filenew1.read()
    
    with open(maintextfile,"rb") as textenc:
        
        textread=textenc.read()
        print(textread)
        encryptedtext1=fernet3.encrypt(textread)    

    with open("111111111111111.txt","wb") as enctxt:
          enctxt.write(encryptedtext1)
    
#----------------------------------------------------------------------------------------------------------------------------    
def decrypt_txt():
    with open("enckeytext.key", "rb") as filenew5:
            key5 = filenew5.read()
            fernet5 = Fernet(key5)
            
    with open(maintextfile, "rb") as dectxtfile:
        
        newdectext = dectxtfile.read()
        decryptedtxt5 = fernet5.decrypt(newdectext)
        
    with open("2222222222.txt", "wb") as dec5:
        
        dec5.write(decryptedtxt5)
    
     
#----------------------------------------------------------------------------------------------------------------------------        

def encrypt_img():
    key6=Fernet.generate_key()
    fernet6=Fernet(key6)
    with open("enckeyphotos.key","wb")as filenew:
        filenew.write(key6)
    
    with open("enckeyphotos.key","rb")as filenew6:
        data=filenew6.read()
    
    with open(mainimgfile1,"rb") as imgp:
        
        
        photsread=imgp.read()
        encryptedphoto6=fernet6.encrypt(photsread)    

    with open("encphotos.png","wb") as enctxt:
          enctxt.write(encryptedphoto6)
    
#---------------------------------------------------------------------------------------------------------------------------
def decrypt_img():
    with open("enckeyphotos.key", "rb") as filenew7:
            key7 = filenew7.read()
            fernet7 = Fernet(key7)
            
    with open(mainimgfile1, "rb") as dectxtfile7:
        
        newdecpng = dectxtfile7.read()
        decryptedimg7 = fernet7.decrypt(newdecpng)
        
    with open("dec_img1.png", "wb") as dec7:
        
        dec7.write(decryptedimg7)
    
    
        
def encrypt_video():
    global cap

    key8=Fernet.generate_key()
    fernet8=Fernet(key8)
    with open("enckeyvideos.key","wb")as filenew8:
        filenew8.write(key8)
    
    with open("enckeyvideos.key","rb")as filenew8:
        data12=filenew8.read()
    
    with open(mainvideofile1,"rb") as videof:
        
        
        videoread1=videof.read()
        encryptdvideo=fernet8.encrypt(videoread1)    

    with open("encvideo1.mp4","wb") as encvid:
          encvid.write(encryptdvideo)
    
    
def decrypt_video():
    with open("enckeyvideos.key", "rb") as filenew9:
            
            key9 = filenew9.read()
            fernet9 = Fernet(key9)
    
     
            
    with open(mainvideofile1, "rb") as file99:
        
        
        newdecvid1= file99.read()
        decryptedvid9 = fernet9.decrypt(newdecvid1)
        
    with open("decvideo.mp4", "wb") as dec9:
        
        
        dec9.write(decryptedvid9)
    
    
    
#-----------------------------------------------------------------------------------------------------------------------

playing = False
cap = None
label = None



def Video_play():
    global cap
    global playing
    if playing:
        ret, frame = cap.read()
        if ret:
            frame = cv2.resize(frame, (700, 400))  # Resize the frame
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            videolabelmain.imgtk = imgtk
            videolabelmain.configure(image=imgtk)
            videolabelmain.after(15, Video_play)
        else:
            # cap.release()
         cap.release() 
  

def play():
        global startpngfvideo 
        startpngfvideo=startpng
        global playing
        if playing:
             playing = False
             
             vidplaybtn44.configure(text='Play',image=startpng)
             
        
        else:
            playing = True
            vidplaybtn44.configure(text='Pause',image=pausepng)
            Video_play()


        
   
def clear_video():
    playing= False
    videolabelmain.configure(image="")
   
        
        
mainframe = ctk.CTkFrame(master=window, width=250, height=750, corner_radius=20)
mainframe.place(x=10, y=20)

framebutton1 = ctk.CTkButton(master=mainframe, text="TEXT",fg_color="transparent",image=photo3,text_color="white",border_width=2,width=200,command=textframe)
framebutton1.place(x=5, y=20)
framebutton2 = ctk.CTkButton(master=mainframe, text="PHOTOS",fg_color="transparent",border_width=2,text_color="white",image=photo, width=200, command=photosframe)
framebutton2.place(x=5, y=80)
framebutton3 = ctk.CTkButton(master=mainframe, text="VIDEOS",fg_color="transparent",text_color="white",border_width=2,image=photo1,width=200,command=videoframe)
framebutton3.place(x=5, y=140)
framebutton4 = ctk.CTkButton(master=mainframe, text="AUDIO",fg_color="transparent",border_width=2,text_color="white",image=photo2, width=200,command=Audioframe)
framebutton4.place(x=5, y=200)
check_var = customtkinter.StringVar(value="on")

switch_var = customtkinter.StringVar(value="off")
switch = customtkinter.CTkSwitch(master=mainframe, text="Light Mode", command=switch_event,
                                 variable=switch_var, onvalue="on", offvalue="off")

switch.place(x=15,y=600)
textframe1 = ctk.CTkFrame(master=window, width=1000, height=700)
filedialog1=ctk.CTkButton(master=textframe1,fg_color="transparent",text="Select File",border_width=2,command=selectfile)
filedialog1.place(x=50,y=50)
clearbutton=ctk.CTkButton(master=textframe1,fg_color="transparent",text="Clear",border_width=2,command=clearselection)
clearbutton.place(x=210,y=50)

combobox = ctk.CTkComboBox(master=textframe1, values=["AES", "RSA","BASE-64"])
combobox.place(x=850,y=40)
combobox.set(" Select Encryption")
textbox1=ctk.CTkTextbox(master=textframe1,width=755,height=500)
textbox1.place(x=50,y=100)
encbutton = ctk.CTkButton(master=textframe1, text="Encrypt",fg_color="transparent",border_width=2,text_color="white",height=30,image=encimage1, width=130,command=encrypt_txt)
encbutton.place(x=850, y=130)
decbutton = ctk.CTkButton(master=textframe1, text="Decrypt",fg_color="transparent",border_width=2,text_color="white",height=30,image=decimage1, width=130,command=decrypt_txt)
decbutton.place(x=850, y=230)

photosframe1 = ctk.CTkFrame(master=window, width=1000, height=700)
filedialog2=ctk.CTkButton(master=photosframe1,text="Select Image",fg_color="transparent",border_width=2,command=selectimage)
filedialog2.place(x=50,y=50)
clearbutton2=ctk.CTkButton(master=photosframe1,text="Clear",border_width=2,fg_color="transparent",command=clearimamge)
clearbutton2.place(x=210,y=50)

combobox2 = ctk.CTkComboBox(master=photosframe1, values=["AES", "RSA","BASE-64"])
combobox2.place(x=850,y=40)
combobox.set(" Select Encryption")
encbutton2 = ctk.CTkButton(master=photosframe1, text="Encrypt",fg_color="transparent",border_width=2,text_color="white",height=30,image=encimage1, width=130,command=encrypt_img)
encbutton2.place(x=850, y=130)
decbutton2 = ctk.CTkButton(master=photosframe1, text="Decrypt",fg_color="transparent",border_width=2,text_color="white",height=30,image=decimage1, width=130,command=decrypt_img)
decbutton2.place(x=850, y=230)
label = customtkinter.CTkLabel(master=photosframe1, text="", fg_color="transparent",image=None)
label2=customtkinter.CTkLabel(master=photosframe1,text=None)



Videoframe1=ctk.CTkFrame(master=window,width=1000,height=700)
filedialog3=ctk.CTkButton(master=Videoframe1,text="Select Video",border_width=2,fg_color="transparent",height=30,command=selectvideo)
filedialog3.place(x=50,y=50)
clearbutton3=ctk.CTkButton(master=Videoframe1,text="Clear",fg_color="transparent",border_width=2,height=30,command=clear_video)
clearbutton3.place(x=210,y=50)

vidplaybtn44=ctk.CTkButton(master=Videoframe1,text="Play",image=startpng,fg_color="transparent",border_width=2,command=play)
vidplaybtn44.place(x=360,y=50)


videolabelmain=ctk.CTkLabel(master=Videoframe1,width=200, height=300,text=None)
videolabelmain.place(x=60,y=250)

combobox3 = ctk.CTkComboBox(master=Videoframe1, values=["AES", "RSA","BASE-64"])
combobox3.place(x=850,y=40)
combobox.set(" Select Encryption")
encbutton3 = ctk.CTkButton(master=Videoframe1, text="Encrypt",fg_color="transparent",border_width=2,text_color="white",height=30,image=encimage1, width=130,command=encrypt_video)
encbutton3.place(x=850, y=130)
decbutton3 = ctk.CTkButton(master=Videoframe1, text="Decrypt",fg_color="transparent",border_width=2,text_color="white",height=30,image=decimage1, width=130,command=decrypt_video)
decbutton3.place(x=850, y=230)
label4=customtkinter.CTkLabel(master=Videoframe1, text="", fg_color="transparent")
label4.place(x=50,y=600)

Audioframe1=ctk.CTkFrame(master=window,width=1000,height=700)
filedialog4=ctk.CTkButton(master=Audioframe1,fg_color="transparent",text="Select Audio",border_width=2,command=selectaudio1)
filedialog4.place(x=50,y=50)
clearbutton4=ctk.CTkButton(master=Audioframe1,fg_color="transparent",text="Clear",border_width=2,command=clearaudio)
clearbutton4.place(x=210,y=50)

combobox4 = ctk.CTkComboBox(master=Audioframe1, values=["AES", "RSA","BASE-64"])
combobox4.place(x=850,y=40)
combobox.set(" Select Encryption")
encbutton4 = ctk.CTkButton(master=Audioframe1, text="Encrypt",fg_color="transparent",border_width=2,text_color="white",height=30,image=encimage1, width=130,command=encrypt_audio)
encbutton4.place(x=850, y=130)
decbutton4 = ctk.CTkButton(master=Audioframe1, text="Decrypt",fg_color="transparent",border_width=2,text_color="white",height=30,image=decimage1, width=130,command=decrypt_audio)
decbutton4.place(x=850, y=230)
stopbtn=ctk.CTkButton(master=Audioframe1,text="Pause",image=stoppng,border_width=0,fg_color="transparent",command=audiopause,width=100)

unstopbtn=ctk.CTkButton(master=Audioframe1,text="Resume",border_width=0,fg_color="transparent",image=pausepng,width=100,command=audiounpause)

audioplay1=ctk.CTkButton(master=Audioframe1,text="Play",border_width=0,image=startpng,fg_color="transparent",command=audioplay,width=100)

label3 = customtkinter.CTkLabel(master=Audioframe1, text="", fg_color="transparent")

musicimg1=customtkinter.CTkLabel(master=Audioframe1, text=" ", fg_color="transparent",image=musicpng)



window.mainloop()
