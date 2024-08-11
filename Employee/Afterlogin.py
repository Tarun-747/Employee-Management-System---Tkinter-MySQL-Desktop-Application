from tkinter import *
import time
import ttkthemes
from tkinter import ttk,messagebox,filedialog
import pymysql
import pandas


def iexit():
    result=messagebox.askyesno('Confirm','Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass


def export():
    url=filedialog.asksaveasfilename(defaultextension='.csv')
    indexing=employeetable.get_children()
    newlist=[]
    for index in indexing:
        content=employeetable.item(index)
        datalist=content['values']
        newlist.append(datalist)

    table=pandas.DataFrame(newlist,columns=['Name','ID','Mobile','Email','Gender','DOB','Added Time','Added Date'])
    print(table)
    table.to_csv(url,index=False)
    messagebox.showinfo('Success','Data is saved successfully')



def function(title,buttontext,command):

    global nameentry,IDentry,Mobileentry,Emailentry,DOBentry,Genderentry,common

    common=Toplevel()
    common.title('Dataset values')
    common.resizable(False,False)
    common.grab_set()
    namelable=Label(common,text='Name',font=('times new roman',20,'bold'))
    namelable.grid(row=0,column=0,padx=30,pady=20)
    nameentry=Entry(common,font=('roman',15,'bold'),width=25)
    nameentry.grid(row=0,column=1,padx=10,pady=15)

    IDlable=Label(common,text='ID',font=('times new roman',20,'bold'))
    IDlable.grid(row=1,column=0,padx=30,pady=20)
    IDentry=Entry(common,font=('roman',15,'bold'),width=25)
    IDentry.grid(row=1,column=1,padx=10,pady=15)

    Mobilelable=Label(common,text='Mobile',font=('times new roman',20,'bold'))
    Mobilelable.grid(row=3,column=0,padx=30,pady=20)
    Mobileentry=Entry(common,font=('roman',15,'bold'),width=25)
    Mobileentry.grid(row=3,column=1,padx=10,pady=15)

    Emaillable=Label(common,text='E-mail',font=('times new roman',20,'bold'))
    Emaillable.grid(row=2,column=0,padx=30,pady=20)
    Emailentry=Entry(common,font=('roman',15,'bold'),width=25)
    Emailentry.grid(row=2,column=1,padx=10,pady=15)
    
    # Adresslable=Label(common,text='Adress',font=('times new roman',20,'bold'))
    # Adresslable.grid(row=4,column=0,padx=30,pady=20)
    # Adressentry=Entry(common,font=('roman',15,'bold'),width=25)
    # Adressentry.grid(row=4,column=1,padx=10,pady=15)

    Genderlable=Label(common,text='Gender',font=('times new roman',20,'bold'))
    Genderlable.grid(row=4,column=0,padx=30,pady=20)
    Genderentry=Entry(common,font=('roman',15,'bold'),width=25)
    Genderentry.grid(row=4,column=1,padx=10,pady=15)

    DOBlable=Label(common,text='D.O.B',font=('times new roman',20,'bold'))
    DOBlable.grid(row=5,column=0,padx=30,pady=20)
    DOBentry=Entry(common,font=('roman',15,'bold'),width=25)
    DOBentry.grid(row=5,column=1,padx=10,pady=15)

    button=ttk.Button(common,text=buttontext,cursor='hand2',command=command )
    button.grid(row=6,columnspan=2)
    if title=='Update employee':
        indexing=employeetable.focus()
        print(indexing)
        content=employeetable.item(indexing)
        listdata = content['values']
        nameentry.insert(0,listdata[0])
        IDentry.insert(0,listdata[1])
        Mobileentry.insert(0,listdata[3])
        Emailentry.insert(0,listdata[2])
        #Adressentry.insert(0,listdata[])
        Genderentry.insert(0,listdata[4]) 
        DOBentry.insert(0,listdata[5])



    
    
def updatedata():
    

    query = 'UPDATE employee SET Name=%s, Email=%s, Mobile=%s, Gender=%s, `D.O.B`=%s, `Added Date`=%s, `Added Time`=%s WHERE ID=%s'
    
    try:
        # Execute the query
        mycursor.execute(query, (nameentry.get(), Emailentry.get(), Mobileentry.get(), Genderentry.get(), DOBentry.get(), date, currenttime, IDentry.get()))
        # Commit the transaction
        con.commit()
        
        # Notify the user of success
        messagebox.showinfo('Success', 'Updated successfully',parent=common)
    except Exception as e:
        # Handle any errors that occur during the update
        messagebox.showerror('Error', f'Update failed: {str(e)}')

    common.destroy()
    showdata()





def deleteemployee():
    indexing = employeetable.focus()
    
    # Check if any row is selected
    if not indexing:
        messagebox.showwarning("Warning", "No employee selected to delete")
        return

    content = employeetable.item(indexing)
    contentid = content['values'][1]  # Assuming the ID is in the second column

    query = 'DELETE FROM employee WHERE ID=%s'
    mycursor.execute(query, (contentid,))
    con.commit()

    messagebox.showinfo('Deleted', 'Deleted successfully')

    # Refresh the table after deletion
    query = 'SELECT * FROM employee'
    mycursor.execute(query)
    fetcheddata = mycursor.fetchall()
    employeetable.delete(*employeetable.get_children())
    
    for data in fetcheddata:
        employeetable.insert('', END, values=data)


# def deleteemployee():
#     indexing=employeetable.focus()
#     print(indexing)
#     content=employeetable.item(indexing)
#     contentid=content['values'][1]
#     print(contentid)
#     query='delete *from employee where ID=%s'
#     mycursor.execute(query,contentid)
#     con.commit()
#     messagebox.showinfo('Deleted','Deleted successfully')
#     query='select *from employee'
#     mycursor.execute(query)
#     fetcheddata=mycursor.fetchall()
#     employeetable.delete(*employeetable.get_children())
#     for data in fetcheddata:
#         employeetable.insert('',END,values=data)


def showdata():
    query='select *from employee'
    mycursor.execute(query)
    fetcheddata=mycursor.fetchall()
    employeetable.delete(*employeetable.get_children())
    for data in fetcheddata:
        employeetable.insert('',END,values=data)





def search_data():
    query='select * from employee where name=%s or ID=%s or Mobile=%s or Email=%s or Gender=%s or DOB=%s'
    mycursor.execute(query,(nameentry.get(),IDentry.get(),Mobileentry.get(),Emailentry.get(),
                                    Genderentry.get(),DOBentry.get()))
    employeetable.delete(*employeetable.get_children())
    Fetcheddata=mycursor.fetchall()
    for data in Fetcheddata:
        employeetable.insert('',END,values=data)

    

def add_data():
    # Check if any required field is empty
    if (IDentry.get() == '' or nameentry.get() == '' or Emailentry.get() == '' or
        Mobileentry.get() == '' or DOBentry.get() == '' or Genderentry.get() == ''):
        messagebox.showerror('Error', 'All fields are required', parent=common)
    else:
        currentdate = time.strftime('%d/%m/%Y')
        currenttime = time.strftime('%H:%M:%S')
        try:
            query = 'INSERT INTO employee (Name, ID, Mobile, Email, Gender, `D.O.B`, `Added Date`, `Added Time`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
            
            mycursor.execute(query, (
                nameentry.get(),
                IDentry.get(),
                Mobileentry.get(),
                Emailentry.get(),
                Genderentry.get(),
                DOBentry.get(),
                currentdate,
                currenttime
            ))
            con.commit()

            result = messagebox.askyesno('Confirm', 'Data added successfully. Do you want to clean the form?', parent=common)
            if result:
                nameentry.delete(0, END)
                IDentry.delete(0, END)
                Mobileentry.delete(0, END)
                Emailentry.delete(0, END)
                Genderentry.delete(0, END)
                DOBentry.delete(0, END)
            else:
                pass

            # Refresh the employee table
            query = 'SELECT * FROM employee'
            mycursor.execute(query)
            fetcheddata = mycursor.fetchall()
            employeetable.delete(*employeetable.get_children())
            for data in fetcheddata:
                employeetable.insert('', END, values=data)

        except pymysql.err.IntegrityError as e:
            messagebox.showerror('Error', f'Integrity Error: {e}', parent=common)
        except Exception as e:
            messagebox.showerror('Error', f'Error: {e}', parent=common)

    


def connect_database():

    def connect():
        global mycursor, con
        try:
            con = pymysql.connect(host=hostentry.get(), user=userentry.get(), password=passwordentry.get())
            mycursor = con.cursor()
            messagebox.showinfo('Success', 'Database Connection Successful', parent=connectwindow)
            connectwindow.destroy()
        except Exception as e:
            messagebox.showerror('Error', f'Error: {e}', parent=connectwindow)
            return

        try:
            # Create database if it doesn't exist
            mycursor.execute('CREATE DATABASE IF NOT EXISTS employeemanagementsystem')
            mycursor.execute('USE employeemanagementsystem')

            # Create table if it doesn't exist
            mycursor.execute('''
            CREATE TABLE IF NOT EXISTS employee (
                `Name` VARCHAR(30),
                `ID` INT NOT NULL PRIMARY KEY,
                `Mobile` VARCHAR(30),
                `Email` VARCHAR(30),
                `Gender` VARCHAR(30),
                `D.O.B` VARCHAR(30),
                `Added Date` VARCHAR(50),
                `Added Time` VARCHAR(50)
            )
        ''')

        except Exception as e:
            messagebox.showerror('Error', f'Error: {e}', parent=connectwindow)
            return

        addemployeebutton.config(state=NORMAL)
        searchemployeebutton.config(state=NORMAL)
        showemployeebutton.config(state=NORMAL)
        deleteemployeebutton.config(state=NORMAL)
        updateemployeebutton.config(state=NORMAL)
        exportdatabutton.config(state=NORMAL)
        exitbutton.config(state=NORMAL)




        

    connectwindow=Toplevel()
    connectwindow.grab_set()
    connectwindow.geometry('470x250+700+230')
    connectwindow.title('Database connection')
    hostnamelable=Label(connectwindow,text='Hostname',font=('roman',20,'bold'),fg='grey')
    hostnamelable.grid(row=0,column=0,padx=20)
    hostentry=Entry(connectwindow,font=('roman',15,),bd=2)
    hostentry.grid(row=0,column=1,padx=40,pady=20)

    usernamelable=Label(connectwindow,text='Username',font=('roman',20,'bold'),fg='grey')
    usernamelable.grid(row=1,column=0,padx=20)
    userentry=Entry(connectwindow,font=('roman',15,),bd=2)
    userentry.grid(row=1,column=1,padx=40,pady=20)

    passwordlable=Label(connectwindow,text='Password',font=('roman',20,'bold'),fg='Grey')
    passwordlable.grid(row=2,column=0,padx=20)
    passwordentry=Entry(connectwindow,font=('roman',15,),bd=2)
    passwordentry.grid(row=2,column=1,padx=40,pady=20)

    Loginbutton=ttk.Button(connectwindow,text='Login',cursor='hand2',command=connect)
    Loginbutton.grid(row=3,columnspan=2)
    
    




def clock():
    global date,currenttime
    date=time.strftime('%d/%m/%Y')
    currenttime=time.strftime('%H:%M:%S')
    datetimeLable.config(text=f'    Date: {date}\nTime: {currenttime}')
    datetimeLable.after(1000,clock)





root=ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')

root.geometry('1920x1080+0+0')
root.title('employee Management')

datetimeLable=Label(root,font=('times new roman',10,'bold'))
datetimeLable.place(x=5,y=5)
clock()

titleLable=Label(root,text='Employee Management System',font=('times new roman',25,'bold'))
titleLable.place(x=550,y=10)

connectbutton=ttk.Button(root,text='Connect Database',cursor='hand2',command=connect_database)
connectbutton.place(x=1350,y=0)


LeftFrame=Frame(root)
LeftFrame.place(x=60,y=80,width=400,height=700)
logoimage=PhotoImage(file=r'C:\Coding_fun\Student managment\Employee\employeelogo.png')
logolable=Label(LeftFrame,image=logoimage)
logolable.grid(row=0,column=0)

addemployeebutton=ttk.Button(LeftFrame,text='Add employee',cursor='hand2',width=25,command=lambda :function('Add employee','add',add_data))
addemployeebutton.grid(row=1,column=0,pady=30)

searchemployeebutton=ttk.Button(LeftFrame,text='Search employee',cursor='hand2',width=25,command=lambda :function('Search employee','search',search_data))
searchemployeebutton.grid(row=2,column=0,pady=25)

deleteemployeebutton=ttk.Button(LeftFrame,text='Delete employee',cursor='hand2',width=25,command=deleteemployee)
deleteemployeebutton.grid(row=3,column=0,pady=30)

updateemployeebutton=ttk.Button(LeftFrame,text='Update employee',cursor='hand2',width=25,command=lambda :function('Update employee','update',updatedata))
updateemployeebutton.grid(row=4,column=0,pady=30)

showemployeebutton=ttk.Button(LeftFrame,text='Show employee',cursor='hand2',width=25,command=showdata)
showemployeebutton.grid(row=5,column=0,pady=30)

exportdatabutton=ttk.Button(LeftFrame,text='Export Data',cursor='hand2',width=25,command=export)
exportdatabutton.grid(row=6,column=0,pady=30)

exitbutton=ttk.Button(LeftFrame,text='Exit',cursor='hand2',width=25,command=iexit)
exitbutton.grid(row=7,column=0,pady=25)


"""right frame"""

rightFrame=Frame(root)
rightFrame.place(x=400,y=80,width=1050,height=700)

Xscrollbar=Scrollbar(rightFrame,orient=HORIZONTAL)
Yscrollbar=Scrollbar(rightFrame,orient=VERTICAL)


employeetable=ttk.Treeview(rightFrame,columns=('Name','ID','Email','Mobile','Gender','D.O.B','Added Date','Added Time'),
                          xscrollcommand=Xscrollbar.set,yscrollcommand=Yscrollbar.set,show='headings')
employeetable.pack(fill=BOTH,expand=1)

Xscrollbar.config(command=employeetable.xview)
Yscrollbar.config(command=employeetable.yview)

Xscrollbar.pack(side=BOTTOM,fill=X)
Yscrollbar.pack(side=RIGHT,fill=Y)

employeetable.heading('Name',text='Name')
employeetable.heading('ID',text='ID')
employeetable.heading('Email',text='Email')
employeetable.heading('Mobile',text='Mobile')
employeetable.heading('Gender',text='Gender')
employeetable.heading('D.O.B',text='D.O.B')
employeetable.heading('Added Date',text='Added Date')
employeetable.heading('Added Time',text='Added Time')

employeetable.column('ID',anchor=CENTER)
employeetable.column('Name',anchor=CENTER)
employeetable.column('Email',anchor=CENTER)
employeetable.column('Mobile',anchor=CENTER)
employeetable.column('Gender',anchor=CENTER)
employeetable.column('D.O.B',anchor=CENTER)
employeetable.column('Added Date',anchor=CENTER)
employeetable.column('Added Time',anchor=CENTER)

style=ttk.Style()
style.configure('Treeview',rowheight=40,font=('arial',13),foreground='black')
style.configure('Treeview.Heading',font=('arial',15,'bold'),foreground='black')

employeetable.config(show='headings')


root.mainloop()
