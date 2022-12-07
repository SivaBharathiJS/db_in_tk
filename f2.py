import pymongo
from tkinter import messagebox
from tkinter import *
win1=Tk()
l=Label(win1,text='username')
l2=Label(win1,text="password")
l.place(x=10,y=10)
l2.place(x=10,y=30)
E1=StringVar()
E2=StringVar()
e1=Entry(textvariable=E1)
e1.place(x=80,y=10)
e2=Entry(textvariable=E2)
e2.place(x=80,y=30)
def d():
    a=E1.get()
    b=E2.get()
    try:
        con=pymongo.MongoClient("mongodb://localhost:27017/")
        db1=con['tksiva']
        col1=db1['tkcol1']
        q={'username':a,'password':b}
        x=col1.insert_one(q)
        xx="data stored in the object id:"+str(x.inserted_id)
        messagebox.showinfo("app-chat",xx)
    except:
        messagebox.showerror("app-chat","error in login...")
def d1():
        t=Tk()
        con=pymongo.MongoClient("mongodb://localhost:27017/")
        db1=con['tksiva']
        col1=db1['tkcol1']
        r=col1.find()
        y1=10
        for i in r:
            l3=Label(t,text=i['username'])
            l3.place(x=10,y=y1)
            l4=Label(t,text=i['password'])
            l4.place(x=80,y=y1)
            y1+=30
def d2():
    aaa=E1.get()
    con=pymongo.MongoClient("mongodb://localhost:27017/")
    db1=con['tksiva']
    col1=db1['tkcol1']
    a={'username':aaa}
    col1.delete_one(a)
    xx=a['username']+"deleted"
    messagebox.showinfo("app-chat",xx)
    
def d3():
    aaa=E1.get()
    bbb=E2.get()
    con=pymongo.MongoClient("mongodb://localhost:27017/")
    db1=con['tksiva']
    col1=db1['tkcol1']
    old={"username":aaa}
    new={'$set':{"password":bbb}}
    col1.update_one(old,new)
    messagebox.showinfo("app-chat","edited..")
b1=Button(win1,text="save",command=d)
b1.place(x=50,y=60)
b2=Button(win1,text="view",command=d1)
b2.place(x=50,y=90)
b3=Button(win1,text='delete',command=d2)
b3.place(x=50,y=120)
b4=Button(win1,text='update',command=d3)
b4.place(x=50,y=140)
win1.mainloop()
