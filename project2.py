from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import pymysql
gender1 = "null"
class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Window")
        self.root.geometry("1600x900+0+0")
        self.root.config(bg="white")
        self.bg = ImageTk.PhotoImage(file="images/3.jpg")
        bg = Label(self.root, image=self.bg).place(x=0, y=0, width=1600, height=900)
        self.left = ImageTk.PhotoImage(file="images/5.jpeg")
        left = Label(self.root, image=self.left,bg = "black").place(x=50, y=100, width=600, height=600)
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=650, y=100, width=700, height=600)
        title = Label(frame1, text="REGISTER HERE", font=("times new roman", 20, "bold"), bg="white", fg="green").place \
            (x=45, y=10)
        f_name = Label(frame1, text="First Name", font=("times new roman", 15, "bold"), bg="white", fg="gray").place \
            (x=50, y=60)
        self.txt_fname = Entry(frame1, font=("times new roman", 15), bg="lightgrey")
        self.txt_fname.place(x=50, y=90, width=250)
        l_name = Label(frame1, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="gray").place \
            (x=370, y=60)
        self.txt_lname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_lname.place(x=370, y=90, width=250)
        contact = Label(frame1, text="Contact No.", font=("times new roman", 15, "bold"), bg="white", fg="gray").place \
            (x=50, y=130)
        self.txt_contact = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_contact.place(x=50, y=160, width=250)
        email = Label(frame1, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="gray").place \
            (x=370, y=130)
        self.txt_email = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_email.place(x=370, y=160, width=250)
        branch = Label(frame1, text="Select Branch", font=("times new roman", 15, "bold"), bg="white", fg="gray").place \
            (x=50, y=200)
        self.cmb_quest = ttk.Combobox(frame1, font=("times new roman", 13),state = "readonly",justify = CENTER)
        self.cmb_quest["values"] = ("Science","Humanities","Commerce")
        self.cmb_quest.place(x=50, y=230, width=250)
        self.cmb_quest.current(0)
        marks = Label(frame1, text="Class 10 Marks", font=("times new roman", 15, "bold"), bg="white", fg="gray").place \
        (x=370, y=200)
        self.txt_marks = ttk.Combobox(frame1, font=("times new roman", 13),state = "readonly",justify = CENTER)
        self.txt_marks["values"] = ("91-100","81-90","71-80","61-70","51-60","41-50","31-40","21-30","11-20","1-10")
        self.txt_marks.place(x=370, y=230, width=250)
        self.txt_marks.current(0)
        password= Label(frame1, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place \
            (x=50, y=270)
        self.txt_password = Entry(frame1, font=("times new roman", 15),show='*', bg="lightgray")
        self.txt_password.place(x=50, y=300, width=250)
        cpassword = Label(frame1, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place \
            (x=370, y=270)
        self.txt_cpassword = Entry(frame1, font=("times new roman", 15),show='*', bg="lightgray")
        self.txt_cpassword.place(x=370, y=300, width=250)
        self.btn_img = ImageTk.PhotoImage(file ="images/9.png")
        btn_register = Button(frame1,image = self.btn_img,bd = 0,cursor ="hand2",command = self.register_data).place(x = 250,y = 545,width = 200,height = 50)
        dob = Label(frame1, text="Date Of Birth", font=("times new roman", 15, "bold"), bg="white", fg="gray").place \
            (x=-15, y=340, width=250)
        self.dob1 = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.dob1.place(x=50, y=375, width=250)
        self.dob1.insert(0,"DD/MM/YYYY")
        def click(event):
            self.dob1.configure(state=NORMAL)
            self.dob1.delete(0, END)
            self.dob1.unbind('<Button-1>', clicked)
        clicked = self.dob1.bind('<Button-1>', click)
        Age= Label(frame1, text="Age", font=("times new roman", 15, "bold"), bg="white", fg="gray")
        Age.place(x=270, y=340, width=250)
        self.age = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.age.place(x=370, y=370, width=250)
        def viewSelected():
            global gender1
            choice = var.get()
            gender1 = choice
            return gender1
        gender = Label(frame1, text="Gender", font=("times new roman", 15, "bold"), bg="white",
                          fg="gray").place(x=50, y=410)
        var = StringVar()
        self.male = Radiobutton(frame1, text='Male', variable=var, value='male',command=viewSelected)
        self.male.place(x=50, y=450)
        self.female = Radiobutton(frame1, text='Female', variable=var, value='female',command=viewSelected)
        self.female.place(x=130, y=450)
    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpassword.delete(0, END)
        self.dob1.delete(0,END)
        self.age.delete(0,END)
        self.cmb_quest.current(0)
        self.txt_marks.current(0)
    def register_data(self):
        global gender1
        if self.txt_fname.get() == "" or self.txt_contact.get() == "" or self.txt_email.get() == "" or \
                self.txt_password.get() == "" or self.txt_cpassword.get() == "" or  self.dob1.get() == "" \
                or  self.age.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
        elif self.txt_password.get() != self.txt_cpassword.get():
            messagebox.showerror("Error","Password and Confirm Password should be same",parent = self.root)
        elif "@" not in self.txt_email.get():
            messagebox.showerror("Error", "Invalid Email", parent=self.root)
        elif len(self.txt_contact.get()) != 10:
            messagebox.showerror("Error", "Contacts Should be at least 10 characters long", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost",user="root",password="",database="employee")
                cur = con.cursor()
                cur.execute("insert into employee1 (f_name,l_name,contact,email,branch,marks,password,date_of_birth,age,gender) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                               (self.txt_fname.get(),
                                self.txt_lname.get(),
                                self.txt_contact.get(),
                                self.txt_email.get(),
                                self.cmb_quest.get(),
                                self.txt_marks.get(),
                                self.txt_password.get(),
                                self.dob1.get(),
                                self.age.get(),
                                gender1
                            ))
                con.commit()
                con.close()
                messagebox.showinfo("Success","Registration Successful",parent = self.root)
                self.clear()
            except Exception as es:
                messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self.root)
root = Tk()
obj = Register(root)
root.mainloop()
