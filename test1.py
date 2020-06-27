import tkinter
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
root=Tk()

root.title('Codebuzz Registeration 2k20')


bimage=PhotoImage(file="bgimg.gif")
wid=bimage.width()
hei=bimage.height()

x=200
y=50
root.geometry("%dx%d+%d+%d" % (wid,hei,x,y))

l2=Label(root,image=bimage)
l2.pack(side='top',fill='both',expand='yes')

l1=Label(l2,text="Codebuzz2k20",background="black",foreground="red")
l1.place(x=300,y=30)
l1.config(font=("Hokjesgeest",24))

l4=Label(l2,text='an intersection of coding and entertainment',background='Black',foreground='white')
l4.place(x=350,y=70)
l4.config(font=("Slope Opera",8))

l3=Label(l2,text="Registeration form ",background='black',foreground='red')
l3.place(x=380,y=90)
l3.config(font=("Bowlby One SC",15,'underline'))
def input1():
    fullname_get=vfullname.get()
    email_get=vemail.get()
    password_get=vpassword.get()
    age_get=str(vage.get())
    gender_get=vgender.get()
    course_get=vcourse.get()
    college_get=vcollege.get()
    phone_get=str(vphoneno.get())

    file=open("Details.txt","a")
    file.write('\n')
    file.write("Fullname=")
    file.write(fullname_get)
    file.write('\n')
    file.write("Email=")
    file.write(email_get)
    file.write('\n')
    file.write("Password=")
    file.write(password_get)
    file.write('\n')
    file.write("Age=")
    file.write(age_get)
    file.write('\n')
    file.write("Gender=")
    file.write(gender_get)
    file.write('\n')
    file.write("Course=")
    file.write(course_get)
    file.write('\n')
    file.write("Phone=")
    file.write(phone_get)
    file.write('\n')
    file.write("College Name=")
    file.write(college_get)
    file.write('\n')
    file.close()
    

style=Style()

style.configure('W.TButton',font=('Calibri',12,'bold'),foreground='red',background="white")
style.configure('TRadiobutton',font=('Slope Opera',10,'bold'),foreground='red',background='black')

def create_window():
    window =Toplevel(l2)
    window.geometry("400x200")
    sample=Label(window,text="        Thank you for registering in our event!\n               Stay tuned for further updates",foreground="#ffffff",background='black')
    sample.place(x=50,y=20)
    sample.config(font=('Ebrima',10))
    sample1=Label(window,text="Keep Coding!!",foreground='#ffffff',background='#000000')
    sample1.place(x=110,y=100)
    sample1.config(font=('Slope Opera',18,'bold','underline'))
    window.config(background="#000000")
    window.mainloop()



def proquit():
    window1=Toplevel(l2)
    window1.geometry("400x130")
    sample2=Label(window1,text="  Do you want to quit the registeration process?",foreground="#ffffff",background='black')
    sample2.place(x=40,y=20)
    sample2.config(font=('Ebrima',12))
    window1.config(background="#000000")
    qubtn=Button(window1,text='Yes',style='W.TButton',command=root.destroy)
    qubtn.place(x=75,y=65)
    ctbtn=Button(window1,text='No',style='W.TButton',command=window1.destroy)
    ctbtn.place(x=225,y=65)
    window1.mainloop()

btn1=Button(l2,text="QUIT",style='W.TButton',command=proquit)
btn1.place(x=525,y=600)

vfullname=StringVar()
vemail=StringVar()
vpassword=StringVar()
vage=IntVar()
vgender=StringVar()
vphoneno=IntVar()
vcollege=StringVar()
vcourse=StringVar()



fullname=Label(l2,text="Fullname",background="black",foreground="white")
fullname.place(x=100,y=150)
fullname.config(font=("Slope Opera",12))

p1=Entry(l2,width=30,textvariable=vfullname).place(x=290,y=150)

email=Label(l2,text="Email",background="black",foreground="white")
email.place(x=100,y=190)
email.config(font=("Slope Opera",12))

p2=Entry(l2,width=30,textvariable=vemail).place(x=290,y=190)


password=Label(l2,text="Password",background="black",foreground="white")
password.place(x=100,y=230)
password.config(font=("Slope Opera",12))

p3=Entry(l2,width=30,textvariable=vpassword).place(x=290,y=230)

age=Label(l2,text="Age",background="black",foreground="white")
age.place(x=100,y=270)
age.config(font=("Slope Opera",12))

p4=Spinbox(l2,from_=18,to=24,width=8,textvariable=vage).place(x=290,y=270)

gender=Label(l2,text="Gender",background="black",foreground="white")
gender.place(x=100,y=310)
gender.config(font=("Slope Opera",12))

var=IntVar()
R1=Radiobutton(l2,text="Male",variable=vgender,value='Male',style='TRadiobutton').place(x=290,y=310)
R2=Radiobutton(l2,text="Female",variable=vgender,value='Female',style='TRadiobutton').place(x=370,y=310)
R3=Radiobutton(l2,text="Others",variable=vgender,value='Other',style='TRadiobutton').place(x=460,y=310)

phoneno=Label(l2,text="Phoneno",background="black",foreground="white")
phoneno.place(x=100,y=350)
phoneno.config(font=("Slope Opera",12))

p5=Entry(l2,width=30,textvariable=vphoneno).place(x=290,y=350)

college=Label(l2,text="College",background="black",foreground="white")
college.place(x=100,y=390)
college.config(font=("Slope Opera",12))

p6=Entry(l2,width=50,textvariable=vcollege).place(x=290,y=390)

course=Label(l2,text="course of study",background="black",foreground="white")
course.place(x=100,y=430)
course.config(font=("Slope Opera",12))

p7=Entry(l2,width=30,textvariable=vcourse).place(x=290,y=430)

def enabling():
    if temp.get()==1:
        btn.config(state=NORMAL)
    elif temp.get()==0:
        btn.config(state=DISABLED)

btn=Button(l2,text="SUBMIT",style='W.TButton',command=lambda:[input1(),create_window()])
btn.place(x=375,y=600)
temp=IntVar()
check=tk.Checkbutton(l2,text=" I agree to all rules and regulations of the event",variable=temp,command=enabling, font=('Slope Opera', 12), bg='black',fg='red').place(x=100,y=470)
btn.config(state=DISABLED)




l2.image=bimage


root.mainloop()
