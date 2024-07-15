
from tkinter import *
from tkinter import messagebox
import os
import pyttsx3
from PIL import ImageTk,Image
import ast 
import webbrowser
import pyttsx3
import requests
import calendar
import time

def say():
    pyttsx3.speak("which Applications you want me to open")
    
def welcome():
    
   
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[1].id)
    engine.runAndWait()
    zed=user1.get()
    pyttsx3.speak("HEllo")
    pyttsx3.speak(zed)
    pyttsx3.speak("I'm Eren,your virtual desktop assistant")
    pyttsx3.speak("Following are the tasks i can help you with")

    

root=Tk()
root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)

root.geometry("900x500+300+200")

root.resizable(False,False)



page1=Frame(root)
page2=Frame(root)
page3=Frame(root)
page4=Frame(root)
page5=Frame(root)
page6=Frame(root)
page7=Frame(root)
page8=Frame(root)
page9=Frame(root)
page10=Frame(root)
page11=Frame(root)

happy_label=Label(root)
sad_label=Label(root)
confused_label=Label(root)
angry_label=Label(root)
demotivated_label=Label(root)

for frame_01 in (page1,page2,page3,page4,page5,page6,page7,page8,page9,page10,page11):
    frame_01.grid(row=0,column=0,sticky="nsew")
    
    
def show_frame(frame_01):
    frame_01.tkraise()

show_frame(page1)


#  CODE FOR FIRST PAGE STARTS HERE HIHI 
page1.config(bg="violet")
























def  signup1():
    
    username=user1.get()
    password=code1.get()
    conform_password=c_password1.get()
    
    if password==conform_password:
            comparison();
            
            
    else:
        messagebox.showerror('Invalid',"Both Password should match")
def comparison():
    with open(r'C:\Users\hp\Desktop\datasheet.txt','r') as file:
        for line in file:
            line=line.split(",")
            if (user1.get()==line[0] and code1.get()==line[1]):
               
                show_frame(page5)
                welcome()
                
                break
            else:
                messagebox.showerror("Invalid",'User not found')
                
            

            
            


frame=Frame(page1,width=550,height=390,bg="#fff")
frame.place(x=175,y=50)

heading=Label(frame,text="Login",fg="#59a1f8",bg="white",font=("forte",23)).place(x=220,y=2)


#FUNCTION FOR USERNAME 
def on_enter1(e):
    user1.delete(0,"end")
    
def on_leave1(e):
    if user1.get()=="":
        user1.insert(0,'Username')
        
user1=Entry(frame,width=25,fg="black",border=0,bg="white",font=('forte',14))

user1.place(x=100,y=80)
user1.insert(0,"Username")
user1.bind("<FocusIn>",on_enter1)
user1.bind("<FocusOut>",on_leave1)
Frame(frame,width=295,height=2,bg="black").place(x=100,y=210)


#FUNCTION FOR PASSWORD 
def on_enter1(e):
    code1.delete(0,"end")
    
def on_leave1(e):
    if code1.get()=="":
        code1.insert(0,'Password')
        
code1=Entry(frame,width=25,fg="black",border=0,bg="white",font=('forte',15))

code1.place(x=100,y=130)
code1.insert(0,"Password")
code1.bind("<FocusIn>",on_enter1)
code1.bind("<FocusOut>",on_leave1)
Frame(frame,width=295,height=2,bg="black").place(x=100,y=110)

            
#FUNCTION FOR CONFIRM PASSWORD
def on_enter1(e):
    c_password1.delete(0,"end")
    
def on_leave1(e):
    if c_password1.get()=="":
        c_password1.insert(0,'Confirm Password')
        
c_password1=Entry(frame,width=25,fg="black",border=0,bg="white",font=('forte',15))

c_password1.place(x=100,y=177)
c_password1.insert(0,"Confirm Password")
c_password1.bind("<FocusIn>",on_enter1)
c_password1.bind("<FocusOut>",on_leave1)
Frame(frame,width=295,height=2,bg="black").place(x=100,y=158)

Button(frame,height=2,width=24,pady=1,padx=1,text="Login",font="forte",bg="#57a168",fg="white",border=0,command= signup1).place(x=126,y=230)

label=Label(frame,text="New User",fg='black',bg="white",font=("forte",13)).place(x=150,y=290)

SignIn=Button(frame,width=7,height=-2,text="signup?",font=("forte",12),border=0,bg="white",cursor="hand2",fg="purple",command=lambda:show_frame(page2)).place(x=240,y=289)

    
    
    
    
    
    
    #=====================================PAGE 2==================================================================================#



bg1=PhotoImage(file=r"C:\Users\hp\Desktop\Project_VA\pat.png")
my_label=Label(page2,image=bg1).pack()






 




def  signup():
    username =user.get()
    password=code.get()
    conform_password=c_password.get()
    P_Number=Number_1.get()
    
    if len(P_Number)==10:
        
    
    
        if password==conform_password:
            try:
                file=open(r"C:\Users\hp\Desktop\datasheet.txt",'a')
                
                file.write(username)
                file.write(',')
                file.write(password)
                file.write(',')
                file.write('\n')
                
                file.close()
                
                messagebox.showinfo("Signup","Succesfully signed up")
        
            except:
                file=open(r'C:\Users\hp\Desktop\datasheet.txt',"w")
                pp=str({"username":'password'})
                file.write(pp)
                file.close()
        else:
            messagebox.showerror('Invalid',"Both Password should match")

    else:
        messagebox.showinfo("Error","Enter a 10 Digit Phone Number")

img=ImageTk.PhotoImage(Image.open(r"C:\Users\hp\Desktop\Project_VA\login.png"))
Label(page2,image=img,border=0,bg="white").place( x=50 ,y=90)


frame=Frame(page2,width=350,height=390,bg="#fff")
frame.place(x=480,y=50)

heading=Label(frame,text="SignUp",fg="#59a1f8",bg="white",font=("forte",23)).place(x=110,y=2)


#FUNCTION FOR USERNAME 
def on_enter(e):
    user.delete(0,"end")
    
def on_leave(e):
    if user.get()=="":
        user.insert(0,'Username')
        
user=Entry(frame,width=25,fg="black",border=0,bg="white",font=('forte',14))

user.place(x=30,y=60)
user.insert(0,"Username")
user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>",on_leave)
Frame(frame,width=295,height=2,bg="black").place(x=30,y=220)


#FUNCTION FOR PASSWORD 
def on_enter(e):
    code.delete(0,"end")
    
def on_leave(e):
    if code.get()=="":
        code.insert(0,'Password')
        
code=Entry(frame,width=25,fg="black",border=0,bg="white",font=('forte',15))

code.place(x=30,y=195)
code.insert(0,"Password")
code.bind("<FocusIn>",on_enter)
code.bind("<FocusOut>",on_leave)
Frame(frame,width=295,height=2,bg="black").place(x=30,y=90)

#FUNCTIION FOR EMAIL ID 


def on_enter(e):
    mail_1.delete(0,"end")
    
def on_leave(e):
    if mail_1.get()=="":
        mail_1.insert(0,'Email')
        
        
mail_1=Entry(frame,width=25,fg="black",border=0,bg="white",font=('forte',14))

mail_1.place(x=30,y=105)
mail_1.insert(0,"Email")
mail_1.bind("<FocusIn>",on_enter)
mail_1.bind("<FocusOut>",on_leave)
Frame(frame,width=295,height=2,bg="black").place(x=30,y=135)




#FUNCTIION FOR  PHONE NUMBER


def on_enter(e):
    Number_1.delete(0,"end")
    
def on_leave(e):
    if Number_1.get()=="":
        Number_1.insert(0,'Phone Number')
        
        
Number_1=Entry(frame,width=25,fg="black",border=0,bg="white",font=('forte',14))

Number_1.place(x=30,y=150)
Number_1.insert(0,"Phone Number")
Number_1.bind("<FocusIn>",on_enter)
Number_1.bind("<FocusOut>",on_leave)
Frame(frame,width=295,height=2,bg="black").place(x=30,y=180)










































            
#FUNCTION FOR CONFIRM PASSWORD
def on_enter(e):
    c_password.delete(0,"end")
    
def on_leave(e):
    if c_password.get()=="":
        c_password.insert(0,'Confirm Password')
        
c_password=Entry(frame,width=25,fg="black",border=0,bg="white",font=('forte',15))

c_password.place(x=25,y=237)
c_password.insert(0,"Confirm Password")
c_password.bind("<FocusIn>",on_enter)
c_password.bind("<FocusOut>",on_leave)
Frame(frame,width=295,height=2,bg="black").place(x=30,y=270)

Button(frame,height=2,width=24,pady=1,padx=1,text="SignUp",font="forte",bg="#57a168",fg="white",border=0,command= signup ).place(x=66,y=290)

label=Label(frame,text="I have an account",fg='black',bg="white",font=("forte",13)).place(x=80,y=340)

SignIn=Button(frame,width=7,height=-2,text="Login?",font=("forte",12),border=0,bg="white",cursor="hand2",fg="purple",command=lambda:show_frame(page1)).place(x=220,y=340)



#==========================================================CODE FOR THIRD PAGE==========================================================================#


label_02=Label(page3,text="Welcome",bg="red",font=("Forte",24,"bold")).pack()












#widthxheight

page3.configure(bg="lavender")


#command
def command1():
    if(useEntry.get()=="google"):
        pyttsx3.speak("opening google")
    
        webbrowser.open("https://www.google.co.in")
    elif(useEntry.get()=="youtube"):
        pyttsx3.speak("opening youtube")
        webbrowser.open("https://www.youtube.com")
        
    elif(useEntry.get()=="netflix"):
        pyttsx3.speak("opening netflix")
        webbrowser.open("https://www.netflix.com/in")
    elif (useEntry.get() == "amazon prime video"):
        pyttsx3.speak("opening Amazon Prime Video")
        webbrowser.open("https://www.primevideo.com/?ref_=dvm_pds_amz_in_as_s_g_146")
    elif (useEntry.get() == "hotstar"):
        pyttsx3.speak("opening Disney Hotstar")
        pyttsx3.speak("Grab your Popcorn")
        webbrowser.open("https://www.hotstar.com/in")
    elif (useEntry.get() == "amazon"):
        pyttsx3.speak("opening Amazon Enjoy Shopping")
        webbrowser.open("https://www.amazon.in")
    elif (useEntry.get() == "flipkart"):
        pyttsx3.speak("opening Flipkart")
        webbrowser.open("https://www.flipkart.com")
    elif (useEntry.get() == "myntra"):
        pyttsx3.speak("opening Myntra")
        webbrowser.open("https://www.myntra.com")
    elif (useEntry.get() == "whatsapp web"):
        pyttsx3.speak("opening whatsapp web")
        webbrowser.open("https://web.whatsapp.com")
    elif (useEntry.get() == "instagram"):
        pyttsx3.speak("opening Instagram")
        webbrowser.open("https://www.instagram.com")
    elif (useEntry.get() == "twitter"):
        pyttsx3.speak("opening twitter")
        webbrowser.open("https://twitter.com")
    elif (useEntry.get() == "facebook"):
        pyttsx3.speak("opening facebook")
        webbrowser.open("https://www.facebook.com")
    elif (useEntry.get() == "linkedin"):
        pyttsx3.speak("opening linkedin")
        webbrowser.open("https://www.linkedin.com")


#title of web browser




title_label=Label(page3,text="Search from Web Browser:",font=("Forte",29,"bold"),fg="green").place(x=240,y=120)



useEntry=Entry(page3,bg="grey")
useEntry.lower()
useEntry.place(x=300,y=190)


b1=Button(page3,text="Search",width=11,bg="cyan",font=("Forte",20,"bold"),command=command1).place(x=350,y=260)



b0=Button(page3,text="next",width=11,bg="cyan",font=("Forte",15,"bold"),command=lambda:show_frame(page4)).place(x=590,y=450)


menu_1=Button(page3,text="Menu",bg="cyan",font=("Forte",15,"bold"),command=lambda:show_frame(page5)).place(x=740,y=450)








#==========================================CODE FOR FOURTH PAGE ==============================================================================================


def sendmail():
   pyttsx3.speak('Connecting to G-Mail...')
   webbrowser.open("http://www.gmail.com")
   
def sendmail1():
   pyttsx3.speak("Connecting to hangouts...")
   webbrowser.open("http://hangouts.goggle.com")
   
def sendmail2():
   pyttsx3.speak("Connecting to Yahoo!")
   webbrowser.open("http://mail.yahoo.com")
   
def sendmail3():
   pyttsx3.speak("Connecting to Outlook")
   webbrowser.open("http://www.outlook.office.com")


page4.configure(bg="light green")


hell1="Send Email through Gmail"
hell2="Send Email through Hotmail"
hell3="Send Email through Yahoo! mail"
hell4="Send Email through Outlook"


b1=Button(page4,text=hell1,font=("forte",14,"bold"),command=sendmail).place(x=210,y=60,width=425)
b2=Button(page4,text=hell2,font=("forte",14,"bold"),command=sendmail1).place(x=210,y=130,width=425)
b3=Button(page4,text=hell3,font=("forte",14,"bold"),command=sendmail2).place(x=210,y=200,width=425)
b4=Button(page4,text=hell4,font=("forte",14,"bold"),command=sendmail3).place(x=210,y=270,width=425)



b01=Button(page4,text="Previous",width=11,bg="cyan",font=("Forte",15,"bold"),command=lambda:show_frame(page3)).place(x=560,y=420)


menu_2=Button(page4,text="Menu",bg="cyan",font=("Forte",15,"bold"),command=lambda:show_frame(page5)).place(x=695,y=420)
#CODE FOR PAGE FIVE
#===========================================================================================================================================================

page5.configure(bg="lavender")

label_02=Label(page5,text="Welcome!! \nI'm EREN ! Your very own desktop assistant\n\n Following are the tasks I can help  you with::",bg="light blue",font=("Kristen ITC",24,"bold")).place(x=0,y=0,width=900)
web_button=Button(page5,text="Search the Web",bg="light blue",font=("forte",20,"bold"),command=lambda:show_frame(page3)).place(x=197,y=220,width=250)

web_button=Button(page5,text="ChatBot",bg="red",font=("forte",20,"bold"),command=lambda:show_frame(page10)).place(x=447,y=220,width=250)

web_button=Button(page5,text="Calender",bg="light blue",font=("forte",20,"bold"),command=lambda:show_frame(page6)).place(x=447,y=290,width=250)
web_button=Button(page5,text="Thoughts",bg="red",font=("forte",20,"bold"),command=lambda:show_frame(page7)).place(x=447,y=360,width=250)
web_button=Button(page5,text="AppOpener",bg="light blue",font=("forte",20,"bold"),command=lambda:{show_frame(page11),say()}).place(x=197,y=360,width=250)
web_button=Button(page5,text="Weather",bg="light blue",font=("forte",20,"bold"),command=lambda:show_frame(page8)).place(x=447,y=430,width=250)
web_button=Button(page5,text="E-Mail",bg="red",font=("forte",20,"bold"),command=lambda:show_frame(page4)).place(x=197,y=430,width=250)

web_button=Button(page5,text="scheduler",bg="red",font=("forte",20,"bold"),command=lambda:show_frame(page9)).place(x=197,y=290,width=250)





#======================================================CODE FOR SIXTH PAGE=======================================================
page6.configure(bg="yellow")



def month_cal():
    month = int(monthspinBox.get())
    year = int(yearspinBox.get())
    
    data=calendar.month(year,month)
    textfield.delete(0.0,END)
    textfield.insert(INSERT,data)
    


Label(page6,text='Calender',font=("forte",32,),fg="black",bg='yellow').place(x=328,y=7)
monthLabel= Label(page6, text ="Month", bg = "yellow").place(x=177,y=67)
yearLabel= Label(page6, text = "Year", bg = "yellow").place(x=477,y=67)
monthspinBox=Spinbox(page6,from_=1, to=12,width=8).place(x=290,y=67)
yearspinBox=Spinbox(page6,from_=1996, to=2500,width=8).place(x=548,y=67)
#monthspinBox.bind('<Return>',month_cal)
#yearspinBox.bind('<Return>',month_cal)
go_button=Button(page6,text='Go',font=("forte",18),width=24,bg="yellow",command=month_cal).place(x=274,y=112)

textfield=Text(page6,width=32,height=10,fg='red').place(x=172,y=160)



menu_3=Button(page6,text="Menu",bg="lavender",font=("Forte",15,"bold"),command=lambda:show_frame(page5)).place(x=730,y=440)


 #===================================================== CODE FOR PAGE7 ==============================================================================[===]


page7.configure(bg="pink")

#photo for thoughts

#command for different moods
def on_click_1():
    for a in (happy_label,sad_label,demotivated_label,angry_label,confused_label):
        a.after(1000,a.destroy())



def happy_mood():
    global happy_label
    happy_label=Label(page7,text='''NO MEDICINES CURES 
    WHAT HAPPINESS CANNOT.''',font=("forte",14,"bold"))
    happy_label.pack()
def sad_mood():
    
    global sad_label
    sad_label=Label(page7,text='''NOBODY CAN MAKE YOU HAPPY UNTIL 
    YOU'RE HAPPY WITH YOURSELF FIRST.''',font=("forte",14,"bold"))
    sad_label.pack()
def angry_mood():
    global angry_label
    angry_label=Label(page7,text='''ANGER DOES'NT SOLVE ANYTHING.
    IT BUILDS NOTHING, BUT 
    IT CAN DESTROY EVERYTHING''',font=("forte",14,"bold"))
    angry_label.pack()
def demotivated_mood():
    global demotivated_label
    demotivated_label=Label(page7,text='''SOMETIMES GOD DOES'NT GIVE YOU WHAT YOU THINK YOU WANT,
    NOT BECAUSE YOU DON'T DESERVE IT , 
    BUT BECAUSE YOU DESERVE BETTER''',font=("forte",14,"bold"))
    demotivated_label.pack()
def confused_mood():
    global confused_label
    confused_label=Label(page7,text='''IT IS OKAY TO BE CONFUSED,
     CONFUSION IS THE ROUTE TO ALL CLARITY IN THIS WORLD''',font=("forte",14,"bold"))
    confused_label.pack()
#title for mood
thoughts_title=Label(page7,text="What is your mood?",font=("forte",14,"bold"))
thoughts_title.pack()
def thoughts_frame():
    f1=Frame(page7,bg="pink")
    f1.pack()
    l=Label(f1)
    l.pack()
    b1=Button(f1,text="Happy",font=("forte",14,"bold"),bg="yellow",command=lambda:[on_click_1(),happy_mood()])
    b1.pack(side=LEFT)
    b2=Button(f1,text="Sad",font=("forte",14,"bold"),bg="grey",command=lambda:[on_click_1(),sad_mood()])
    b2.pack(side=LEFT)
    b3 = Button(f1, text="Angry", font=("forte", 14, "bold"),bg="red",command=lambda:[on_click_1(),angry_mood()])
    b3.pack(side=LEFT)
    b4 = Button(f1, text="Demotivated", font=("forte", 14, "bold"),bg="green",command=lambda:[on_click_1(),demotivated_mood()])
    b4.pack(side=LEFT)
    b5 = Button(f1, text="Confused", font=("forte", 14, "bold"),bg="purple",command=lambda:[on_click_1(),confused_mood()])
    b5.pack(side=LEFT)
    
thoughts_frame()


menu_4=Button(page7,text="Menu",bg="lavender",font=("Forte",15,"bold"),command=lambda:show_frame(page5)).place(x=300,y=450)

#============================================================CODE FOR EIGHTH PAGE================================================================

page8.configure(bg="lavender")
def getWeather(canvas):
    city=textField.get()
    api = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=06c921750b9a82d8f5d1294e1586276f"
    json_data=requests.get(api).json()
    condition=json_data['weather'][0]['main']
    temp=int(json_data['main']['temp']-273.15)
    min_temp=int(json_data['main']['temp_min']-273.15)
    max_temp=int(json_data['main']['temp_max']-273.15)
    pressure=json_data['main']['pressure']
    humidity=json_data['main']['humidity']
    wind=json_data['wind']['speed']
    sunrise=time.strftime('%I:%M:%S',time.gmtime(json_data['sys']['sunrise']-21600))
    sunset=time.strftime('%I:%M:%S',time.gmtime(json_data['sys']['sunset']-21600))
    final_info=condition+"\n"+str(temp)+"degree celsius"
    final_data="\n"+"Min Temp:"+str(min_temp)+"degree celsius"+"\n"+"Max Temp:"+str(max_temp)+"degree celsius"+"\n"+"Pressure:"+str(pressure)+"\n"+"Humidity:"+str(humidity)+"\n"+"Wind Speed:"+str(wind)+"\n"+"Sunrise:"+sunrise+"\n"+"Sunset:"+sunset
    label1.config(text=final_info)
    label2.config(text=final_data)
Label(page8,text="Enter the city",font=("forte",28),bg="lavender",fg="brown").place(x=185,y=10)
textField=Entry(page8,width=15,font=("forte",20,"bold"),bg="violet")
textField.place(x=429,y=15)
textField.focus()
textField.bind('<Return>',getWeather)
label1=Label(page8,font=("forte",35,"bold"),bg='lavender')
label1.place(x=245,y=59)
label2=Label(page8,font=("forte",25,"bold"),bg="lavender")
label2.place(x=220,y=160)


menu_5=Button(page8,text="Menu",bg="light blue",font=("Forte",15,"bold"),command=lambda:show_frame(page5)).place(x=640,y=450)
  
#======================================================CODE FOR NINTH PAGE===========================================================================


def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")

def deleteTask():
    lb.delete(ANCHOR)
    

page9.configure(bg='black')







frame = Frame(page9)
frame.pack(pady=10)

lb = Listbox(
    frame,
    width=40,
    height=8,
    font=('forte', 10),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
    
)
lb.pack(side=LEFT, fill=BOTH)

task_list = [
    'Drink Water',
    'Take Medicines'
    ]

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    page9,
    font=('forte', 18)
    )

my_entry.pack(pady=20)

button_frame = Frame(page9)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('forte 14'),
    bg='sky blue',
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('forte 14'),
    bg='pink',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

menu_6=Button(page9,text="Menu",bg="lavender",font=("Forte",15,"bold"),command=lambda:show_frame(page5)).place(x=620,y=450)
#=======================================================CODE FOR 10TH PAGE==============================================================================


BG_COLOR = "lavender"
TEXT_COLOR = "Black"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"



# Send function
def send(page10):
    send = "You -> " + e.get()
    txt.insert(END, "\n" + send)

    user = e.get().lower()
    
    

    if (user == "hello"):
        txt.insert(END, "\n" + "Bot -> Hi there, how can I help?")

    elif (user == "hi" or user == "hii" or user == "hiii"):
        txt.insert(END, "\n" + "Bot -> Hi there, what can I do for you?")

    elif (user == "how are you"):
        txt.insert(END, "\n" + "Bot -> fine! and you")

    elif (user == "fine" or user == "i am good" or user == "i am doing good"):
        txt.insert(END, "\n" + "Bot -> Great! how can I help you.")

    elif (user == "thanks" or user == "thank you" or user == "now its my time"):
        txt.insert(END, "\n" + "Bot -> My pleasure !")

    elif (user == "tell me a joke" or user == "tell me something funny" or user == "crack a funny line"):
        txt.insert(END, "\n" + "Bot -> What did the buffalo say when his son left for college? Bison.! ")

    elif (user == "goodbye" or user == "see you later" or user == "see yaa"):
        txt.insert(END, "\n" + "Bot -> Have a nice day!")

    #Python related qurries

    elif (user == "what is python" or user == "what do you understand by python" or user == "python"):
        txt.insert(END, "\n" + "Bot -> Python is a programming language on which I was programmed to talk with you :) ")

    elif (user == "data types in python"):
        txt.insert(END, "\n" + "Bot -> Some of the data types in python are List , Tuple , Dictionary , String , Integer")

    elif (user == "who developed python" or user == "developer of python" or user == "Who designed python"):
        txt.insert(END, "\n" + "Bot ->Python was designed by Guido van Rossum in 1991")

    elif (user == "what is the extension of the python file" or user == "extension of file in python" or user == "file extension in python"):
        txt.insert(END, "\n" + "Bot ->.py is the extension of python file")

    elif (user == "indentation in python" or user == "how to define a block of code in python" or user == "what is indentation"):
        txt.insert(END ,"\n" + "Bot ->In python, to define a block of code we use indentation.Indentation refers to whitespaces at the beginning of the line")

    elif (user == "in which language is python written"):
        txt.insert(END , "\n" + "Bot ->Python is written in C programming language and it is also known as CPython")

    elif (user == "python comments" or user == "comments in python" or user == "how to make comments in python"):
        txt.insert(END , "\n" + "Bot ->There are three types of comments in python:single-line,multi-line and docstring comments.Comments begin with a hash(#) and extend to the end of line")

    elif (user == "python operators" or user == "types of operators in python" or user == "what are operators in python"):
        txt.insert(END , "\n" + "Bot ->Operators are used to perform operations on values and variables.There are 7 types of operators in python")

    elif (user == "python modules" or user == "what is module in python"):
        txt.insert(END, "\n" + "Bot -> A module is a bunch of related code saved in a file with the extension .py")

    elif (user == "python packages" or user == "packages in python" or user == "what is package in python"):
        txt.insert(END, "\n" + "Bot -> Python")

    elif ( user == "python libraries" or user == "libraries in python" or user == "what is library in python"):
        txt.insert(END, "\n" + "Bot ->Library in python is a collection of packages")

    elif (user == "python objects and classes" or user == "python object" or user == "python classes"):
        txt.insert(END, "/n" + "Bot ->An object is an instance of a class.A class is like a blueprint for that object")

    elif (user == "python frameworks"):
        txt.insert(END, "\n" + "Bot ->A framework is a collection of modules or packages which helps in writing web applications")

    elif (user == "method and function in python" or user == "python methods" or user == "methods in python"):
        txt.insert(END, "\n" + "Bot ->Python method is like a function,except it is attached to an object")

    elif (user == "python functions" or user == "functions in python"):
        txt.insert(END,"\n" + "Bot ->A function is a block of code which only runs when it is called.In python, function is defined using def keyword")

    elif (user == "python keywords"):
        txt.insert(END,"\n" + "Bot -> Python has a set of keywords that are reserved words with defined meanings and cannot be used as variable names.")

    elif (user == "type casting in python"):
        txt.insert(END, "\n" + "Bot ->Type casting is the process of converting data from one type to another")

    elif (user == "python loops"):
        txt.insert(END, "\n" + "Bot -> Python provides:while loop,for loop and nested loops")

    # HTML related querries

    elif (user == "what is html" or user == "what do you understand by html" or user == "full form of html"):
        txt.insert(END, "\n" + "Bot ->HTML or HyperText Markup Language is the standard markup language for documents designed to be displayed in a web browser.")

    elif (user == "html inventor" or user == "who is the father of html"):
        txt.insert(END, "\n" + "Bot ->The first version of HTML was written by Tim Berners-Lee in 1993 ")

    elif (user == "subset of html" or user == "html is extended from"):
        txt.insert(END, "\n" + "Bot ->HTML is a subset of SGML.")

    elif (user == "doctype" or user == "html document type declaration"):
        txt.insert(END,"\n" + "Bot ->It is an instruction that associates a webpage with a document type definition(DTD).")

    elif (user == "html elements" or user == "elements in html"):
        txt.insert(END, "\n" + "Bot ->An HTML element is defined by a start tag,some content and an end tag.")

    elif (user == "html tags" or user == "tags in html"):
        txt.insert(END, "\n" + "Bot ->HTML tags are simple instructions that tell a web browser how to format text.")

    elif (user == "html attributes" or user == "attributes in html"):
        txt.insert(END,"\n" + "Bot ->HTML attributes are special words used inside the opening tag to control the element's behaviour")

    elif (user == "comments in html" or user == "html comments"):
        txt.insert(END,"\n" + "Bot ->Comments in HTML start with <!-- and end with -->.Comments are not displayed in the browser")

    elif (user == "what is the extension of html file" or user == "html file extension "):
        txt.insert(END, "\n" + "Bot ->The extension of HTML file is .htm or .html")

    elif (user == "what is href"):
        txt.insert(END,"\n" + "Bot ->Hypertext reference or href is an HTML attribute used to create a link to another web page.")

    elif (user == "header and footer in html"):
        txt.insert(END,"\n" + "Bot ->A header is text that is placed at the top of a page,while a footer is placed at the bottom.")

    elif (user == "html list"):
        txt.insert(END, "\n" + "Bot ->There are 3 types of list in HTML:Unordered,ordered and description lists")

    elif (user == "html heading" or user == "heading in html"):
        txt.insert(END,"\n" + "Bot ->HTML defines 6 levels of headings:h1,h2,h3,h4,h5 and h6 in which h1 is the largest one")

    elif (user == "what do you need for html"):
        txt.insert(END, "\n" + "Bot ->Text editor and web browser.")

    elif (user == "what type of language is html"):
        txt.insert(END, "\n" + "Bot -> HTML is not a case sensitive language")

    elif (user == "what is c" or user == "what do you understand by c"):
        txt.insert(END,"\n" + "Bot ->c is a structured, procedural programming  that has been widely used both for operating systems and applications.")

    elif (user == "Who developed c" or user == "Who developed c"):
        txt.insert(END, "\n" + "Bot ->c was developed by Dennis Ritchie in 1970s.")

    elif (user == "what is extension of c" or user == "what is extension of c"):
        txt.insert(END, "\n" + "Bot ->The extension of c  is .c.")

    elif (user == "what type of  is c" or user == "what type of  is c"):
        txt.insert(END, "\n" + "Bot ->c is a structured, procedural programming .")

    elif (user == "what is procedural programming" or user == "what do you mean by procedural programming"):
        txt.insert(END,"\n" + "Bot ->Procedural programming is a programming paradigm, derived from imperative programming.\n based on the concept of the procedure call.")

    elif (user == "what is array in c" or user == "what is array in c"):
        txt.insert(END,"\n" + "Bot ->Array in c can be defined as a method of clubbing multiple entities of similar type into a larger group.")

    elif (user == "what are the various types of array in c" or user == "what are the various types of array in c"):
        txt.insert(END, "\n" + "Bot ->Single dimensional arrays and Multidimensional arrays.")

    elif (user == "what is pointer in c" or user == "what is pointer in c"):
        txt.insert(END, "\n" + "Bot ->The pointer in c  is a variable which stores the address of another variable.")

    elif (user == "what are datatypes used in c" or user == "what are datatypes used in c"):
        txt.insert(END, "\n" + "Bot ->The fundamental datatypes in c are int, char, float, and double.others include array, structure, union, and pointer.")

    elif (user == "what is union in c" or user == "what is union in c"):
        txt.insert(END, "\n" + "Bot -A union is a special data type available in c that allows to store different data types in the same memory location.>.")

    elif (user == "what is structure in c" or user == "what is structure in c"):
        txt.insert(END,"\n" + "Bot ->Structures (also called structs) are a way to group several related variables into one place..")

    elif (user == "what is preprocessor c" or user == "what is preprocessor in c"):
        txt.insert(END,"\n" + "Bot ->The C preprocessor is a macro processor that is used automatically by the c compiler to transform your program before actual compilation.")

    elif (user == "what are the various types of preprocessor used in c" or user == "what are the various types of preprocessor used in c"):
        txt.insert(END,"\n" + "Bot ->.There are 4 Main Types of Preprocessor Directives:Macros,File Inclusion,conditional compilation,Other directives.")

    elif (user == "what is macro in c" or user == "what is macro in c"):
        txt.insert(END,"\n" + "Bot ->The macro in C  is known as the piece of code which can be replaced by the macro value.")

    elif (user == "what is file inclusion in c" or user == "what is file inclusion in c"):
        txt.insert(END,"\n" + "Bot ->This type of preprocessor directive tells the compiler to include a file in the source code program.")

    elif (user == "what is conditional compilation in c" or user == "what is conditional compilation in c"):
        txt.insert(END,"\n" + "Bot ->conditional compilation is the process of selecting which code to compile and which code to not compile.")

    # Sql qurreies

    elif (user == "what is sql" or user == "what do you understand by sql"):
        txt.insert(END,"\n" + "Bot ->SQL refers to Structured Query Language and is a 4th generation non-procedural language.")

    elif (user == "what is non procedural language" or user == "what do you understand by non procedural language" or user == "what do you mean by non-procedural language"):
        txt.insert(END,"\n" + "Bot ->Non-procedural languages just need to be specified with what of the problem rather than HOW it is to be done.")

    elif ( user == "when was sql developed" or user == "in which year was sql developed"):
        txt.insert(END, "\n" + "Bot ->SQL was developed in 1970s in an IBM Laboratory.")

    elif (user == "who developed sql" ):
        txt.insert(END, "\n" + "Bot ->SQL was developed by Raymond Boyce and Donald Chamberlin.")

    elif ( user == "why was sql developed" or  user == "what was reason for development of sql"):
        txt.insert(END, "\n" + "Bot ->SQL was developed for getting access and modifying data held in databases.")

    elif ( user == "what are sql datatypes" or  user == "what are different datatypes available in sql"):
        txt.insert(END,"\n" + "Bot ->SQL datatypes are divided into 3 categories namely numeric,date and time and string datatypes.")

    elif (user == "what are various sql elements" ):
        txt.insert(END, "\n" + "Bot ->Literals,Datatypes,NULLS,Comments are various elements of SQL.")

    elif (user == "what are Literals in sql" ):
        txt.insert(END, "\n" + "Bot ->Literals refer to fixed data value be of character or numeric type.")

    elif (user == "what is null in sql" ):
        txt.insert(END, "\n" + "Bot ->NULL in SQL refers to having no value.")

    elif ( user == "what is comment in sql"):
        txt.insert(END,"\n" + "Bot ->Comments in SQL refers to text that is not executed i.e only for purpose of documentation.")

    elif (user == " " or user == "what is primary key in sql" ):
        txt.insert(END, "\n" + "Bot ->The PRIMARY KEY constraint uniquely identifies each record in a table.")

    elif (user == " what is foreign key in sql" ):
        txt.insert(END,"\n" + "Bot ->A foreign key is a field (or collection of fields) in one table, that refers to the PRIMARY KEY in another table.")

    elif (user == "when are constraints in sql" ):
        txt.insert(END,"\n" + "Bot ->Constraints in SQL refers to a condition that is applied to a column(field) or set of columns in a table.")

    elif (user == "what are integrity constraints" ):
        txt.insert(END, "\n" + "Bot ->Constraints applied to maintain data integrity are referred to as Integrity Constraints.")

    elif ( user == "what is unique constraint in sql"):
        txt.insert(END, "\n" + "Bot ->Unique constraint in SQL are used to uniquely identify each record in a column.")

    elif ( user == "how is a table created in sql"):
        txt.insert(END, "\n" + "Bot ->Tables can be created in SQL using CREATE TABLE command.")

    elif ( user == "how is data inserted in sql"):
        txt.insert(END, "\n" + "Bot ->INSERT INTO command is used to insert data in a table.")

    elif (user == "how to update data in a table in sql" ):
        txt.insert(END, "\n" + "Bot ->UPDATE command is used to update data in a table.")

    elif (user == "how can table be deleted in sql" ):
        txt.insert(END, "\n" + "Bot ->DELETE commmand is used to delete tables in SQL.")

    elif ( user == "what is alter command in sql" or user == "what is alter command in sql" ):
        txt.insert(END, "\n" + "Bot ->ALTER command is used to alter definition of already existing tables.")
        
    
    elif ( user == "what is love" or user == "love" ):
        txt.insert(END, "\n" + "Bot -> Concentrate on coding,dont you wish to marryy her.")


    else:
        txt.insert(END, "\n" + "Bot -> Sorry! I dind't got you")

    e.delete(0, END)

lable1 = Label(page10, bg="lavender", fg="dark green", text=" Hii I'm a python bot , wanna chat let's go ", font=FONT_BOLD, pady=10, width=60, height=1).place()

txt = Text(page10, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=175)
txt.pack()

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

e = Entry(page10, bg="navy blue", fg="white", font=FONT, width=55)
e.place(x=0,y=460,width=900,height=35)


e.bind('<Return>',send)


menu_3=Button(page10,text="Menu",bg="lavender",font=("Forte",15,"bold"),command=lambda:show_frame(page5)).place(x=720,y=460)

#=================================CODE FOR PAGE 11=======================================================================================

def execute(a):
    global p
    p=user.get()
    Call_it()
def Call_it():

   
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[1].id)
    engine.runAndWait()
    print("")
    print("")

    global p
    
    p = p.upper()
    
    if ("DONT" in p) or ("DON'T" in p) or ("NOT" in p):
        pyttsx3.speak("Type Again")
        print(".")
        print(".")
        
    elif ("GOOGLE" in p) or ("SEARCH" in p) or ("WEB BROWSER" in p) or ("CHROME" in p) or ("BROWSER" in p) or ("4" in p):
        pyttsx3.speak("Opening")
        pyttsx3.speak("GOOGLE CHROME")
        print(".")
        print(".")
        os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")

    elif ("AR" in p) or ("reader" in p) or ("adobe" in p) or ("8" in p):
        pyttsx3.speak("Opening")
        pyttsx3.speak("Adobe reader")
        os.startfile(r"C:\Program Files (x86)\Adobe\Reader 9.0\Reader\AcroRd32.exe")

    elif ("Note" in p) or ("Notes" in p) or ("Notepad" in p) or ("EDITOR" in p) or ("9" in p):
        pyttsx3.speak("Opening")
        pyttsx3.speak("NOTEPAD")
        os.startfile(r"%windir%\system32\notepad.exe")

    elif ("paint" in p) or ("Paint" in p) or ("Draw" in p) or ("5" in p):
        pyttsx3.speak("Opening")
        pyttsx3.speak("Paint")
        os.startfile(r"%windir%\system32\mspaint.exe")

    elif ("Python" in p) or ("IDLE" "idle" in p) or ("python" in p):
        pyttsx3.speak("Opening")
        pyttsx3.speak("Python")
        print(".")
        print(".")
        os.startfile(r"C:\Users\hp\AppData\Local\Programs\Python\Python310\Lib\idlelib\idle.pyw")

    elif ("VISUAL STUDIO" in p) or ("VS CODE" in p) or ("VS" in p) or ("7" in p):
        pyttsx3.speak("Opening")
        pyttsx3.speak("VISUAL STUDIO")
        os.startfile(r"C:\Users\hp\AppData\Local\Programs\Microsoft VS Code\Code.exe")

    elif ("TELEGRAM" in p) or ("TG" in p) or ("10" in p):
        pyttsx3.speak("Opening")
        pyttsx3.speak("TELEGRAM")
        print(".")
        print(".")
        os.startfile(r"C:\Users\hp\AppData\Roaming\Telegram Desktop\Telegram.exe")

    elif ("COMMAND PROMPT" in p) or ("cmd" in p) or ("Terminal" in p) or ("terminal" in p) or ("3" in p):
        pyttsx3.speak("Opening")
        pyttsx3.speak("command prompt")
        
        os.startfile(r"%windir%\system32\cmd.exe")

    elif ("zoom" in p) or ("ZOOM" in p) or ("videocall" in p) or ("zooom" in p) or ("2" in p):
        pyttsx3.speak("Opening")
        pyttsx3.speak("zoom")
        print(".")
        print(".")
        os.startfile(r"C:\Users\hp\AppData\Roaming\Zoom\bin\Zoom.exe")

    elif ("WORD" in p) or ("MSWORD" in p) or ("1" in p):
        pyttsx3.speak("Opening")
        pyttsx3.speak("MICROSOFT WORD")
        print(".")
        print(".")
        os.system("winword")

    # close the program
    elif ("EXIT" in p) or ("QUIT" in p) or ("CLOSE" in p) or ("0" in p):
        pyttsx3.speak("Exiting")
        

    # for invalid input
    else:
        pyttsx3.speak(p)
        print("Is Invalid,Please Try Again")
        pyttsx3.speak("is Invalid,Please try again")
        print(".")
        print(".")














page11.configure(bg="#B0E0E6")

Label(page11,text="What should i open??",bg="#B0E0E6",fg="#191970",font=("forte",32,"bold")).place(x=237,y=92)
user=Entry(page11,width=30,fg="black",bg="white",font=('forte',24))

user.place(x=200,y=158)
user.bind('<Return>',execute)

menu_3=Button(page11,text="Menu",bg="lavender",font=("Forte",15,"bold"),command=lambda:show_frame(page5)).place(x=720,y=460)


root.mainloop()


