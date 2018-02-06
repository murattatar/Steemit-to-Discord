''' ######################## '''
''' Steemit to Discord v.1.0 '''
''' by Murat Tatar, 2018	 '''
''' Send your last Steemit post to public Discord promo channels '''
''' ######################## '''


''' You Must have logged on Discord via WEB '''
''' Browser should remember you '''

''' Cliq function running according to 1360x168 resolution, you should set to your own resolution '''

''' Don't use ClipBoard for anything while running (may can send a your image/txt that has been copied ) '''



''' We are using TkInter window UserBox. If you want, you can set USERNAME in here '''
# suser = 'USERNAME'


''' # Keyboard - Mouse '''
import win32api, win32con

''' # time '''
import time

''' # OS '''
import os

''' get pages '''
import requests


''' clipboard '''
import pyperclip

''' #windows ''' 
from Tkinter import *

''' # bg image ''' 
from PIL import Image, ImageTk, ImageGrab

''' # bring to front '''
import win32gui


''' # Quick exit '''
def e():
  exit()






''' Public and free "post-promotion" channel for Steemit on Discord.
as dictionary '''

channel_list = {
"Steemians" : "https://discord.gg/d74sVjM",
"channel PAL" : "https://discord.gg/zwQ2FQ7",
"Steemit Turkey" : "https://discord.gg/r8a5xcH",
"Steemit Kulucka" : "https://discord.gg/yAhddFK",
"dLive" : "https://discord.gg/sRPbX38",
"Steem Gigs" : "https://discord.gg/ty8uMuA",
"Steemit Talk" : "https://discord.gg/s4JrpNR",
"MinnowBooster" : "https://discord.gg/eqEpZjg",
"BuildAWhale" : "https://discord.gg/2ARrZBW",
"SteemTrail" : "https://discord.gg/gHt2aGN",
"Whaleshares" : "https://discord.gg/7EnUvT",
"Votovzla" : "https://discord.gg/kvyUQUq",
"dMania" : "https://discord.gg/R3cqGpa",
"Steemit Lover" : "https://discord.gg/tkHq5WJ",
"Money Match Gaming" : "https://discord.gg/Xb9CgHR",
"Na" : "https://discord.gg/Z8A5PSj",
"Be Awesome" : "https://discord.gg/RNUuhaK",
"Utopian-io" : "https://discord.gg/kk3SVXZ",
"Steem Life" : "https://discord.gg/YQJhfK2",
"Jerry & Friends" : "https://discord.gg/tDY7qye",
"GuideSteemit" : "https://discord.gg/UbmhYCS",
"Looking for Niche" : "https://discord.gg/3RFmV9m",
"Minnows Unite" : "https://discord.gg/McSTVGf",
"SteemSpeak" : "https://discord.gg/3Z63Z3h",
"SteemPi" : "https://discord.gg/tNwHKqf",
"Tech Studio18" : "https://discord.gg/xwD67FF",
"Steemit Archievers" : "https://discord.gg/j7T7G3d",
"SteemDeepThink" : "https://discord.gg/DnSWSwx",
"SteemBNB" : "https://discord.gg/XzyGES4",
"SteemVenue" : "https://discord.gg/7QGj5Wb",
"SteemMagick" : "https://discord.gg/faaDATC",
"Promotion" : "https://discord.gg/vEKZ3Ay",
"Postpromo" : "https://discord.gg/sUx9taD",
"NinjaWhale" : "https://discord.gg/A7NUk8Z",
"From The Ground Up" : "https://discord.gg/eF3Qr8a",
"Cryto India" : "https://discord.gg/CjBH9eS",
"EOS Talk" : "https://discord.gg/QSat99M"
 }
 


''' ######################## '''
''' Keyboard '''

VK_CODE = {'backspace':0x08,
           'tab':0x09,
           'clear':0x0C,
           'enter':0x0D,
           'shift':0x10,
           'ctrl':0x11,
           'alt':0x12,
           'pause':0x13,
           'caps_lock':0x14,
           'esc':0x1B,
           'spacebar':0x20,
           'page_up':0x21,
           'page_down':0x22,
           'end':0x23,
           'home':0x24,
           'left_arrow':0x25,
           'up_arrow':0x26,
           'right_arrow':0x27,
           'down_arrow':0x28,
           'select':0x29,
           'print':0x2A,
           'execute':0x2B,
           'print_screen':0x2C,
           'ins':0x2D,
           'del':0x2E,
           'help':0x2F,
           '0':0x30,
           '1':0x31,
           '2':0x32,
           '3':0x33,
           '4':0x34,
           '5':0x35,
           '6':0x36,
           '7':0x37,
           '8':0x38,
           '9':0x39,
           'a':0x41,
           'b':0x42,
           'c':0x43,
           'd':0x44,
           'e':0x45,
           'f':0x46,
           'g':0x47,
           'h':0x48,
           'i':0x49,
           'j':0x4A,
           'k':0x4B,
           'l':0x4C,
           'm':0x4D,
           'n':0x4E,
           'o':0x4F,
           'p':0x50,
           'q':0x51,
           'r':0x52,
           's':0x53,
           't':0x54,
           'u':0x55,
           'v':0x56,
           'w':0x57,
           'x':0x58,
           'y':0x59,
           'z':0x5A,
           'numpad_0':0x60,
           'numpad_1':0x61,
           'numpad_2':0x62,
           'numpad_3':0x63,
           'numpad_4':0x64,
           'numpad_5':0x65,
           'numpad_6':0x66,
           'numpad_7':0x67,
           'numpad_8':0x68,
           'numpad_9':0x69,
           'multiply_key':0x6A,
           'add_key':0x6B,
           'separator_key':0x6C,
           'subtract_key':0x6D,
           'decimal_key':0x6E,
           'divide_key':0x6F,
           'F1':0x70,
           'F2':0x71,
           'F3':0x72,
           'F4':0x73,
           'F5':0x74,
           'F6':0x75,
           'F7':0x76,
           'F8':0x77,
           'F9':0x78,
           'F10':0x79,
           'F11':0x7A,
           'F12':0x7B,
           'F13':0x7C,
           'F14':0x7D,
           'F15':0x7E,
           'F16':0x7F,
           'F17':0x80,
           'F18':0x81,
           'F19':0x82,
           'F20':0x83,
           'F21':0x84,
           'F22':0x85,
           'F23':0x86,
           'F24':0x87,
           'num_lock':0x90,
           'scroll_lock':0x91,
           'left_shift':0xA0,
           'right_shift ':0xA1,
           'left_control':0xA2,
           'right_control':0xA3,
           'left_menu':0xA4,
           'right_menu':0xA5,
           'browser_back':0xA6,
           'browser_forward':0xA7,
           'browser_refresh':0xA8,
           'browser_stop':0xA9,
           'browser_search':0xAA,
           'browser_favorites':0xAB,
           'browser_start_and_home':0xAC,
           'volume_mute':0xAD,
           'volume_Down':0xAE,
           'volume_up':0xAF,
           'next_track':0xB0,
           'previous_track':0xB1,
           'stop_media':0xB2,
           'play/pause_media':0xB3,
           'start_mail':0xB4,
           'select_media':0xB5,
           'start_application_1':0xB6,
           'start_application_2':0xB7,
           'attn_key':0xF6,
           'crsel_key':0xF7,
           'exsel_key':0xF8,
           'play_key':0xFA,
           'zoom_key':0xFB,
           'clear_key':0xFE,
           '+':0xBB,
           ',':0xBC,
           '-':0xBD,
           '.':0xBE,
           '/':0xBF,
           '`':0xC0,
           ';':0xBA,
           '[':0xDB,
           '\\':0xDC,
           ']':0xDD,
           "'":0xDE,
           '`':0xC0}







''' # Codes begins after dictionaries ########################'''





''' Control Functions ######################## '''


def Cliq(x, y):
    #ctypes.windll.user32.SetCursorPos(x, y)
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)



def Press(*args):
    #one Press, one release.
    #accepts as many arguments as you want. e.g. Press('left_arrow', 'a','b').

    for i in args:
        win32api.keybd_event(VK_CODE[i], 0, 0, 0)
        time.sleep(.02)
        win32api.keybd_event(VK_CODE[i], 0, win32con.KEYEVENTF_KEYUP, 0)



def PressHoldRelease(*args):    
    #useful for shortcut command or shift commands.
    #e.g. PressHoldRelease('ctrl', 'alt', 'del'), PressHoldRelease('shift','a')
        
    for i in args:
        win32api.keybd_event(VK_CODE[i], 0, 0, 0)
        time.sleep(.02)

    for i in args:
        win32api.keybd_event(VK_CODE[i], 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(.02)



def Write(f):
    ''' # First, clear field '''
    Press('home'); PressHoldRelease('shift','end'); Press('backspace')
    contnt = str(f)

    for c in contnt:
      if c == ':':
        PressHoldRelease('shift','.')
      elif c == '/':
        PressHoldRelease('shift','7')
      elif c == '@':
        PressHoldRelease('ctrl','alt','q')
      else:
        Press(c); 
        ''' Press('right_arrow'); Press('right_arrow') '''



# Right Click
def RightCliq(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, x, y, 0, 0)
    time.sleep(0.015)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, x, y, 0, 0)






''' # catch the requested word(s) '''
def Between(begin,end,sentence):
    b1 = sentence.split(begin)
    b2 = b1[1].split(end)
    ar = b2[0]
    return ar





''' +++++++++++  Run Forest  +++++++++++  '''


def SteemitToDicord(username):



	''' Get your lastest post '''
	st_url = 'https://steemit.com/@'+username

	comepage = requests.get(st_url)
	cont = comepage.content

	''' # html code has "timestamp__link" class for fist link on user blog page '''
	search_first_post = Between('timestamp__link','</a>',cont)

	first_post =  Between('href="','"',search_first_post)

	first_post_url = 'https://steemit.com'+first_post 

	''' # If international keyboards cause trouble you can use pyperclip.copy(post) '''
	pyperclip.copy(first_post_url)




	count = 0
	for k in channel_list:
		''' get chanel links '''
		link = channel_list[k]

		''' and open link '''
		os.startfile(link)
		print link

		''' wait for opening '''
		time.sleep(12)

		''' Clik on Accpept Button of Invite '''
		Cliq(660,520); time.sleep(6)

		''' # Paste post url '''
		''' # Write(first_post_url) ;  '''
		''' # We use pyperclip instead of Write() function because international keys'''
		PressHoldRelease('ctrl','v')
		Press('enter')

		time.sleep(6)

		''' # Close current tab (at Chrome) '''
		PressHoldRelease('ctrl','w')

		count = count + 1
		add_wait = count * 3
		time.sleep(60 + add_wait)

	e()













''' ## Window functions ########## '''

def wquit():
    global sbox
    print "exited"    
    sbox.destroy()
    e()



def SendtoStrBox(sunu):    
    var.set(sunu)



def Startd():
	username = ReadUser()
	print "started"
	SteemitToDicord(username)



def Stopd():
    wquit()

    


def BoxPlace(event):
       
    if userBox.get() == ' UserName?':
       userBox.delete(0, "end") 
       userBox.insert(0, '  ',)
       
  
def ReadUser():
    buser = userBox.get()
    buser = buser.strip()
    return buser





''' ## Windows Creating ###################  '''

sbox = Tk()
sbox.iconbitmap(default='std.ico')
sboxTitle = sbox.title("Steemit to Discord v1.0 -alfa")

en = 530; by = 345
#ekran boyutu ogren
sw = sbox.winfo_screenwidth()
sh = sbox.winfo_screenheight()
x = (sw-en)/2+7
y = (sh-by)/2-102

go = str(en) + "x" + str(by) + "+" + str(x) + "+" + str(y)

sbox.geometry(go) 
sbox["bg"] = "#15151A"
sbox.resizable(width=FALSE, height=FALSE)


photo = PhotoImage(file="back.gif")
label = Label(image=photo)
label.place(x=0, y=0)



userBox = Entry(sbox, font=("Tahoma",12), fg="#ddaed0", bg="#15151A")
userBox.place(x=130,y=80,height=38, width=145)

userBox.insert(0, ' UserName?')
userBox.bind('<FocusIn>', BoxPlace)



symimage1 = ImageTk.PhotoImage(file="start.gif")


startBtn  = Button(image=symimage1,command= Startd); startBtn.place(x=290, y=80)



var = StringVar()
var.set('Enter your Steemit User Name and click to Start.\nWait for finish or stop python with Ctrl-Alt-Del')
strBox = Label(sbox, textvariable = var,
               font=("Tahoma",11), fg="#ddaed0", bg="#15151A")

strBox.place(x=0, y=305,height=37, width=530)



##  bring to front
def bringFront():
    sbox.lift()
    sbox.attributes('-topmost', 1)
    #sbox.attributes('-topmost', 0)

bringFront()	






while True:
  sbox.mainloop()




