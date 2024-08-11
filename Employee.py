from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','Fileds cannot be empty')
    elif usernameEntry.get()=='Tarun' and passwordEntry.get()=='1234':
        window.destroy()
        import Afterlogin
        
    else:
        messagebox.showerror('Error','The username or the password is incorrect')


window=Tk()

window.geometry('1280x700+0+0')
window.title('LogIn Page Of Employee System')
window.resizable(False,False)

backgroundImage = ImageTk.PhotoImage(file='C:/Coding_fun/Student managment/Employee/bg.jpg')

bgLabel=Label(window,image=backgroundImage)
bgLabel.place(x=0,y=0)

LoginFrame=Frame(window,bg='white')
LoginFrame.place(x=400,y=150)

LogoImage=PhotoImage(file='C:\Coding_fun\Student managment\Employee\employee.png')
logoLable=Label(LoginFrame,image=LogoImage,bg='white')
logoLable.grid(row=0,column=0,pady=10,padx=10,columnspan=2) 

userimage=PhotoImage(file=r'C:\Coding_fun\Student managment\Employee\user.png')
passwordImage=PhotoImage(file=r'C:\Coding_fun\Student managment\Employee\password.png')

usernameLable= Label(LoginFrame,image=userimage,text='Username',compound=LEFT,font=('times new roman',20,'bold'),bg='white')
usernameLable.grid(row=1,column=0,pady=10,padx=10)

usernameEntry=Entry(LoginFrame,font=('times new roman',20))
usernameEntry.grid(row=1,column=1,pady=10,padx=10)

passwordLable= Label(LoginFrame,image=passwordImage,text='Password',compound=LEFT,font=('times new roman',20,'bold'),bg='white')
passwordLable.grid(row=2,column=0,pady=10,padx=10)

passwordEntry=Entry(LoginFrame,font=('times new roman',20))
passwordEntry.grid(row=2,column=1,pady=10,padx=10)

LoginButton= Button(LoginFrame,text='LogIn',font=('times new roman',15,'bold'),width=12,bg='cornflowerblue',fg='white',
                    activebackground='cornflowerblue',activeforeground='white',cursor='hand2',command=login)
LoginButton.grid(row=3,column=1,pady=10)

window.mainloop()