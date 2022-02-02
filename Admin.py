from tkinter import*
import mysql.connector
from PIL import ImageTk
import tkinter as tk
from tkinter import messagebox
def show_function():
    my_w = tk.Tk()
    my_w.geometry("400x250")
    my_connect = mysql.connector.connect(host="localhost", user="root", password="", database="employee")
    my_conn = my_connect.cursor()
    my_conn.execute("SELECT * FROM employee1")
    i = 0
    for student in my_conn:
        for j in range(len(student)):
            e = Entry(my_w, width=25, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, student[j])
            f = Label(my_w, width=10, text=student[j], borderwidth=2, relief='ridge', anchor="w")
        i = i + 1
    my_w.mainloop()
class Login:
    def __init__(self,root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1600x900+0+0")
        self.bg = ImageTk.PhotoImage(file="images/admin.jpg")
        self.bg_image = Label(self.root,image = self.bg).place(x=0,y=0,relwidth=1, relheight=1)
        Frame_login = Frame(self.root,bg="white")
        Frame_login.place(x=150,y=150,height=500,width=500)
        title = Label(Frame_login,text="Login Here",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=90,y=30)
        desc = Label(Frame_login, text="Administrator Login Here",font=("Goudy old style", 15, "bold"),fg="#d25d17",bg="white").place(x=90,y=100)
        lbl_user = Label(Frame_login, text="Username", font=("Goudy old style", 15, "bold"), fg="gray", bg="white").place(x=90,y=140)
        self.txt_user = Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        self.txt_user.place(x=90,y=170,width=350,height=35)

        lbl_pass = Label(Frame_login, text="Password", font=("Goudy old style", 15, "bold"), fg="gray",
                         bg="white").place(x=90, y=210)
        self.txt_pass = Entry(Frame_login, font=("times new roman", 15),show='*', bg="lightgray")
        self.txt_pass.place(x=90, y=240, width=350, height=35)

        forget_btn= Button(Frame_login,text="Forget Password?",cursor="hand2",bg="white",bd=0,fg="#d77337",font=("times new roman",12)).place(x=90,y=280)
        Login_btn = Button(Frame_login,command=self.login_function,cursor="hand2" ,text="Login", fg="white", bg="#d77337",
                        font=("times new roman", 20)).place(x=90, y=320,width=180,height=40)
    def login_function(self):
        if self.txt_pass.get() == "" or self.txt_user.get() == "":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        elif self.txt_pass.get() != "souvik03" or self.txt_user.get() != "souvik":
            messagebox.showerror("Error","Invalid Username/Password",parent=self.root)
        else:
            show_function()
root = Tk()
obj = Login(root)
root.mainloop()
