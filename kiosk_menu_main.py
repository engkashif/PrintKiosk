import tkinter as tk
import subprocess
import webbrowser
import linecache
#import time

class Data_class():
    scan_roll=""
    name=""
    department=""
    phone=""
    password=""

    no_account_warn=0
    wrong_pass=0
    
    dep_name=""
    depart_clicked=0
    dpart_warn=0
    name_warn=0
    cell_warn=1
    pass_warn1=0
    pass_warn2=0


class Application(tk.Frame):
    global vals
    vals=Data_class()
    def __init__(self, master=None):
        super().__init__(master)
        #root.overrideredirect(1)
        #root.focus_force()
        #root.wm_attributes('-type', 'splash')
        self.pack()
        self.signmenu()



    def frontmenu(self):
        self.frontpic=tk.PhotoImage(file='pictures/photo6.png')

        self.frontback=tk.Label(self,image=self.frontpic)
        #self.frontback['height']=800
        #self.frontback['width']=800
        self.frontback.place(x=0, y=0, relwidth=1, relheight=1)
        #self.frontback.grid()

        

        self.headinglabel= tk.Label(self, text="KIOSK PRINTER")
        self.headinglabel['fg']='blue'
        self.headinglabel['bg']='white'
        #self.headinglabel['height']='3'
        #self.headinglabel['width']='10'
        self.headinglabel['font'] = 'Courier 20 bold'
        self.headinglabel.grid(row=0,columnspan=2,column=0,padx=(321,321),pady=(16,425))
        #self.headinglabel.place(x=347,y=20)


        self.welcomelabel= tk.Label(self, text="WELCOME, PLEASE SWIPE YOUR UNIVERSITY CARD TO PRINT")
        self.welcomelabel['fg']='blue'
        self.welcomelabel['bg']='white'
        #self.welcomelabel['height']='3'
        #self.welcomelabel['width']='10'
        self.welcomelabel['font'] = 'Courier 18 bold'
        #self.welcomelabel.grid(row=0,columnspan=2,column=0,padx=(321,321),pady=(16,425))
        self.welcomelabel.place(x=60,y=100)



        self.complabel= tk.Label(self, text="For complaints:\nphone: 03017882885\nemail:160504@students.au.edu.pk")
        self.complabel['fg']='blue'
        self.complabel['bg']='white'
        #self.complabel['height']='3'
        #self.complabel['width']='10'
        self.complabel['font'] = 'Helvetica 14 bold'
        #self.complabel.grid(row=0,columnspan=2,column=0,padx=(321,321),pady=(16,425))
        self.complabel.place(x=500,y=380)
        


        self.front_admin_btn_1 =tk.Button(self,image=self.frontpic, command=self.sign_clicked)
        #self.front_admin_btn_1['font'] = 'Helvetica 12 bold'
        self.front_admin_btn_1['height'] = '50'
        self.front_admin_btn_1['width'] = '80'
        self.front_admin_btn_1['anchor'] = 'nw'
        self.front_admin_btn_1['borderwidth']='0'
        self.front_admin_btn_1['relief'] = 'flat'
        #self.front_admin_btn_1['fg'] = 'white'
        #self.front_admin_btn_1['bg'] = 'red'
        #self.front_admin_btn_1['activebackground'] = 'white'
        #self.front_admin_btn_1['activeforeground'] = 'red'
        self.front_admin_btn_1["cursor"] = "hand2"
        self.front_admin_btn_1.place(x=-0.5,y=-0.5)


        self.front_admin_btn_2 =tk.Button(self,image=self.frontpic, command=self.sign_clicked)
        #self.front_admin_btn_2['font'] = 'Helvetica 12 bold'
        self.front_admin_btn_2['height'] = '50'
        self.front_admin_btn_2['width'] = '80'
        #self.front_admin_btn_2['anchor'] = 'nw'
        self.front_admin_btn_2['borderwidth']='0'
        self.front_admin_btn_2['relief'] = 'flat'
        #self.front_admin_btn_2['fg'] = 'white'
        #self.front_admin_btn_2['bg'] = 'red'
        #self.front_admin_btn_2['activebackground'] = 'white'
        #self.front_admin_btn_2['activeforeground'] = 'red'
        self.front_admin_btn_2["cursor"] = "hand2"
        self.front_admin_btn_2.place(x=380,y=211)


        self.front_admin_btn_3 =tk.Button(self,image=self.frontpic, command=self.sign_clicked)
        #self.front_admin_btn_3['font'] = 'Helvetica 12 bold'
        self.front_admin_btn_3['height'] = '50'
        self.front_admin_btn_3['width'] = '80'
        self.front_admin_btn_3['anchor'] = 'ne'
        self.front_admin_btn_3['borderwidth']='0'
        self.front_admin_btn_3['relief'] = 'flat'
        #self.front_admin_btn_3['fg'] = 'white'
        #self.front_admin_btn_3['bg'] = 'red'
        #self.front_admin_btn_3['activebackground'] = 'white'
        #self.front_admin_btn_3['activeforeground'] = 'red'
        self.front_admin_btn_3["cursor"] = "hand2"
        self.front_admin_btn_3.place(x=761.5,y=-0.5)


        self.front_admin_btn_4 =tk.Button(self,image=self.frontpic, command=self.sign_clicked)
        #self.front_admin_btn_4['font'] = 'Helvetica 12 bold'
        self.front_admin_btn_4['height'] = '50'
        self.front_admin_btn_4['width'] = '80'
        self.front_admin_btn_4['anchor'] = 'sw'
        self.front_admin_btn_4['borderwidth']='0'
        self.front_admin_btn_4['relief'] = 'flat'
        #self.front_admin_btn_4['fg'] = 'white'
        #self.front_admin_btn_4['bg'] = 'red'
        #self.front_admin_btn_4['activebackground'] = 'white'
        #self.front_admin_btn_4['activeforeground'] = 'red'
        self.front_admin_btn_4["cursor"] = "hand2"
        self.front_admin_btn_4.place(x=-0.5,y=422.5)





    def signmenu(self):
        
        self.signpic=tk.PhotoImage(file='pictures/photo6.png')

        self.signback=tk.Label(self,image=self.signpic)
        #self.signback['height']=800
        #self.signback['width']=800
        self.signback.place(x=0, y=0, relwidth=1, relheight=1)
        #self.signback.grid()


        self.headingOne= tk.Label(self, text="KIOSK PRINTER")
        self.headingOne['fg']='blue'
        self.headingOne['bg']='white'
        #self.headingOne['height']='3'
        #self.headingOne['width']='10'
        self.headingOne['font'] = 'Courier 20 bold'
        self.headingOne.grid(row=0,columnspan=2,column=0,padx=(321,321),pady=(16,425))
        #self.headingOne.place(x=347,y=20)




        self.headingTwo= tk.Label(self, text="Sign in to print your documents")
        self.headingTwo['fg']='blue'
        self.headingTwo['bg']='white'
        #self.headingTwo['height']='3'
        #self.headingTwo['width']='10'
        self.headingTwo['font'] = 'Courier 16 bold'
        #self.headingTwo.grid(row=1,columnspan=2,column=0,padx=(10,10),pady=(14,10))
        self.headingTwo.place(x=218,y=65)





        self.label_username = tk.Label(self, text="ROLL NO")
        self.label_password = tk.Label(self, text="PASSWORD")
        self.label_username['font'] = 'Helvetica 16 bold'
        self.label_password['font'] = 'Helvetica 16 bold'
        self.label_password['fg']='white'
        self.label_password['bg']='blue'
        self.label_username['fg']='white'
        self.label_username['bg']='blue'
        self.label_username['height']='2'
        self.label_username['width']='15'
        self.label_password['height']='2'
        self.label_password['width']='15'
        self.label_username.place(x=120,y=120)
        self.label_password.place(x=120,y=185)

        vals.scan_roll="160007"

        self.entry_username = tk.Label(self,text=vals.scan_roll)
        self.entry_password = tk.Entry(self, show="*")
        self.entry_username['font'] = 'Helvetica 18 bold'
        self.entry_password['font'] = 'Helvetica 18 bold'
        
        self.entry_username['relief']='groove'
        
        self.entry_username['fg']='blue'
        self.entry_password['fg']='blue'
        self.entry_username['bg']='white'
        self.entry_password['bg']='white'
        #self.entry_username['height']='20'
        #self.entry_password['height']='20'
        self.entry_username['width']='26'
        self.entry_password['width']='30'
        self.entry_username.place(x=330,y=129)
        self.entry_password.place(x=330,y=194)


        #self.msg=tk.Label(self,text='')
        #self.msg.grid(row=4,column=1)



        self.signbtn =tk.Button(self, text="SIGN IN", command=self.sign_clicked)
        self.signbtn['font'] = 'Helvetica 18 bold'
        self.signbtn['height'] = '2'
        self.signbtn['width'] = '7'
        self.signbtn['fg'] = 'white'
        self.signbtn['bg'] = 'blue'
        self.signbtn['activebackground'] = 'white'
        self.signbtn['activeforeground'] = 'blue'
        self.signbtn["cursor"] = "hand2"
        self.signbtn.place(x=570,y=260)


        self.sign_up_msg= tk.Label(self, text="Don't have an account, sign up now!")
        self.sign_up_msg['fg']='blue'
        self.sign_up_msg['bg']='white'
        #self.sign_up_msg['height']='3'
        #self.sign_up_msg['width']='10'
        self.sign_up_msg['font'] = 'Courier 14 bold'
        #self.sign_up_msg.grid(row=5,columnspan=1,column=0,padx=(10,10),pady=(14,10))
        self.sign_up_msg.place(x=140,y=360)



        self.sign_up_btn =tk.Button(self, text="SIGN UP", command=self.sign_up_menu)
        self.sign_up_btn['font'] = 'Helvetica 18 bold'
        self.sign_up_btn['height'] = '2'
        self.sign_up_btn['width'] = '7'
        self.sign_up_btn['fg'] = 'white'
        self.sign_up_btn['bg'] = 'blue'
        self.sign_up_btn['activebackground'] = 'white'
        self.sign_up_btn['activeforeground'] = 'blue'
        self.sign_up_btn["cursor"] = "hand2"
        self.sign_up_btn.place(x=570,y=350)



        #self.admin_trans_pic=tk.PhotoImage(file='pictures/nophoto6.png')


        '''self.admin_btn =tk.Button(self, text="ADMIN", command=self.in_to_admin)
        self.admin_btn['font'] = 'Helvetica 12 bold'
        self.admin_btn['height'] = '2'
        #self.admin_btn['image'] = self.admin_trans_pic
        self.admin_btn['width'] = '5'
        self.admin_btn['fg'] = 'white'
        self.admin_btn['bg'] = 'red'
        self.admin_btn['activebackground'] = 'white'
        self.admin_btn['activeforeground'] = 'red'
        self.admin_btn["cursor"] = "hand2"
        self.admin_btn.grid(row=5,columnspan=1,column=0,padx=(28,250),pady=(44,30))'''




    def sign_clicked(self):
        #username = self.entry_username.get()
        get_pass= self.entry_password.get()

        scan_roll_line=vals.scan_roll[2:]
        get_line=int(scan_roll_line)
        get_line=get_line+1
        #print(get_line)

        student_line=linecache.getline('user_data/batch16.txt', get_line)
        linecache.clearcache()
        #print(student_line)

        vals.name=""
        vals.department=""
        vals.phone=""
        vals.password=""
        vals.no_account_warn=0
        vals.wrong_pass=0
        startn=0
        endn=0

        while endn<len(student_line):
            if student_line[endn]=="@":
                startn=endn+1
                endn=endn+1
                break
            endn=endn+1

        while endn<len(student_line):
            if student_line[endn]=="@":
                vals.name=student_line[startn:endn]
                startn=endn+1
                endn=endn+1
                break
            endn=endn+1

        while endn<len(student_line):
            if student_line[endn]=="@":
                vals.department=student_line[startn:endn]
                startn=endn+1
                endn=endn+1
                break
            endn=endn+1

        while endn<len(student_line):
            if student_line[endn]=="@":
                vals.phone=student_line[startn:endn]
                startn=endn+1
                endn=endn+1
                break
            endn=endn+1

        while endn<len(student_line):
            vals.password=student_line[startn:endn]
            endn=endn+1

        #print(vals.name)
        #print(vals.department)
        #print(vals.phone)
        #print(vals.password)
        if vals.name!="":
            if get_pass==vals.password:
                self.signback.destroy()
                self.headingOne.destroy()
                self.headingTwo.destroy()
                self.label_username.destroy()
                self.label_password.destroy()
                self.entry_username.destroy()
                self.entry_password.destroy()
                self.signbtn.destroy()
                self.sign_up_msg.destroy()
                self.sign_up_btn.destroy()
                #self.admin_btn.destroy()
                if vals.no_account_warn==1:
                    self.no_account_issue.destroy()
                if vals.wrong_pass==1:
                    self.wrong_pass_issue.destroy()
                self.mainmenu()
            else:
                vals.wrong_pass=1
                if vals.no_account_warn==1:
                    self.no_account_issue.destroy()
                self.wrong_pass_issue = tk.Label(self, text="Wrong password")
                self.wrong_pass_issue['font'] = 'Helvetica 15 bold'
                self.wrong_pass_issue['fg']='white'
                self.wrong_pass_issue['bg']='red'
                self.wrong_pass_issue.place(x=340,y=270)
        else:
            vals.no_account_warn=1
            if vals.wrong_pass==1:
                self.wrong_pass_issue.destroy()
            self.no_account_issue = tk.Label(self, text="You do not have an account. Please sign up")
            self.no_account_issue['font'] = 'Helvetica 15 bold'
            self.no_account_issue['fg']='white'
            self.no_account_issue['bg']='red'
            self.no_account_issue.place(x=130,y=270)


    def in_to_admin(self):
        self.signback.destroy()
        self.headingOne.destroy()
        self.headingTwo.destroy()
        self.label_username.destroy()
        self.label_password.destroy()
        self.entry_username.destroy()
        self.entry_password.destroy()
        self.signbtn.destroy()
        self.sign_up_msg.destroy()
        self.sign_up_btn.destroy()
        self.admin_btn.destroy()
        self.adminmenu()

        

    def front_to_admin(self):
        self.frontback.destroy()
        self.headinglabel.destroy()
        self.welcomelabel.destroy()
        self.complabel.destroy()
        self.front_admin_btn.destroy()
        self.adminmenu()



    def adminmenu(self):
        self.adminpic=tk.PhotoImage(file='pictures/photo6.png')

        self.adminback=tk.Label(self,image=self.adminpic)
        #self.adminback['height']=800
        #self.adminback['width']=800
        self.adminback.place(x=0, y=0, relwidth=1, relheight=1)
        #self.adminback.grid()


        self.adminheadingOne= tk.Label(self, text="ADMIN LOGIN")
        self.adminheadingOne['fg']='blue'
        self.adminheadingOne['bg']='white'
        #self.adminheadingOne['height']='3'
        #self.adminheadingOne['width']='10'
        self.adminheadingOne['font'] = 'Courier 20 bold'
        self.adminheadingOne.grid(row=0,columnspan=2,column=0,padx=(350,350),pady=(16,450))
        #self.adminheadingOne.place(x=347,y=20)




        self.adminheadingTwo= tk.Label(self, text="Sign in to gain admin access")
        self.adminheadingTwo['fg']='blue'
        self.adminheadingTwo['bg']='white'
        #self.adminheadingTwo['height']='3'
        #self.adminheadingTwo['width']='10'
        self.adminheadingTwo['font'] = 'Courier 16 bold'
        #self.adminheadingTwo.grid(row=1,columnspan=2,column=0,padx=(10,10),pady=(14,10))
        self.adminheadingTwo.place(x=262,y=90)



        self.admin_label_username = tk.Label(self, text="USERNAME")
        self.admin_label_username['font'] = 'Helvetica 16 bold'
        self.admin_label_username['fg']='white'
        self.admin_label_username['bg']='blue'
        self.admin_label_username['height']='2'
        self.admin_label_username['width']='15'
        self.admin_label_username.place(x=120,y=150)




        self.admin_label_password = tk.Label(self, text="PASSWORD")
        self.admin_label_password['font'] = 'Helvetica 16 bold'
        self.admin_label_password['fg']='white'
        self.admin_label_password['bg']='blue'
        self.admin_label_password['height']='2'
        self.admin_label_password['width']='15'
        self.admin_label_password.place(x=120,y=220)


        self.admin_entry_username = tk.Entry(self)
        self.admin_entry_username['font'] = 'Helvetica 18 bold'
        self.admin_entry_username['fg']='blue'
        self.admin_entry_username['bg']='white'
        #self.admin_entry_username['height']='20'
        self.admin_entry_username['width']='30'
        self.admin_entry_username.place(x=350,y=159)




        self.admin_entry_password = tk.Entry(self, show="*")
        self.admin_entry_password['font'] = 'Helvetica 18 bold'
        self.admin_entry_password['fg']='blue'
        self.admin_entry_password['bg']='white'
        #self.admin_entry_password['height']='20'
        self.admin_entry_password['width']='30'
        self.admin_entry_password.place(x=350,y=229)




        #self.msg=tk.Label(self,text='')
        #self.msg.grid(row=4,column=1)



        self.admin_signbtn =tk.Button(self, text="SIGN IN", command=self.admin_sign_clicked)
        self.admin_signbtn['font'] = 'Helvetica 18 bold'
        self.admin_signbtn['height'] = '2'
        self.admin_signbtn['width'] = '7'
        self.admin_signbtn['fg'] = 'white'
        self.admin_signbtn['bg'] = 'blue'
        self.admin_signbtn['activebackground'] = 'white'
        self.admin_signbtn['activeforeground'] = 'blue'
        self.admin_signbtn["cursor"] = "hand2"
        self.admin_signbtn.place(x=630,y=300)


        self.admin_go_back_btn =tk.Button(self, text="GO BACK", command=self.admin_to_in)
        self.admin_go_back_btn['font'] = 'Helvetica 12 bold'
        self.admin_go_back_btn['height'] = '2'
        self.admin_go_back_btn['width'] = '8'
        self.admin_go_back_btn['fg'] = 'white'
        self.admin_go_back_btn['bg'] = 'red'
        self.admin_go_back_btn['activebackground'] = 'white'
        self.admin_go_back_btn['activeforeground'] = 'red'
        self.admin_go_back_btn["cursor"] = "hand2"
        #self.admin_go_back_btn.grid(row=5,columnspan=1,column=0,padx=(28,250),pady=(44,30))
        self.admin_go_back_btn.place(x=70,y=360)

        
    def admin_sign_clicked(self):
        root.destroy()


    def admin_to_in(self):
        self.adminback.destroy()
        self.adminheadingOne.destroy()
        self.adminheadingTwo.destroy()
        self.admin_label_username.destroy()
        self.admin_label_password.destroy()
        self.admin_entry_username.destroy()
        self.admin_entry_password.destroy()
        self.admin_signbtn.destroy()
        self.admin_go_back_btn.destroy()
        self.signmenu()
        




    def sign_up_menu(self):
        self.signback.destroy()
        self.headingOne.destroy()
        self.headingTwo.destroy()
        self.label_username.destroy()
        self.label_password.destroy()
        self.entry_username.destroy()
        self.entry_password.destroy()
        self.signbtn.destroy()
        self.sign_up_msg.destroy()
        self.sign_up_btn.destroy()
        #self.admin_btn.destroy()

        self.signuppic=tk.PhotoImage(file='pictures/photo6.png')
        self.sign_up_back=tk.Label(self,image=self.signuppic)
        #self.sign_up_back['height']=800
        #self.sign_up_back['width']=800
        self.sign_up_back.place(x=0, y=0, relwidth=1, relheight=1)
        #self.sign_up_back.grid(row=0,column=0)

        self.heading_new= tk.Label(self, text="NEW ACCOUNT")
        self.heading_new['fg']='blue'
        self.heading_new['bg']='white'
        #self.heading_new['height']='3'
        #self.heading_new['width']='10'
        self.heading_new['font'] = 'Courier 20 bold'
        self.heading_new.grid(row=0,columnspan=2,column=0,padx=(335,335),pady=(16,425))
        #self.heading_new.place(x=347,y=20)

        self.fill_name = tk.Label(self, text="NAME")
        self.fill_name['font'] = 'Helvetica 16 bold'
        self.fill_name['fg']='white'
        self.fill_name['bg']='blue'
        #self.fill_name['height']='2'
        self.fill_name['width']='18'
        #self.fill_name.grid(row=1,column=0,padx=(0,0),pady=(0,0))
        self.fill_name.place(x=100,y=70)

        self.fill_id = tk.Label(self, text="ROLL NO")
        self.fill_id['font'] = 'Helvetica 16 bold'
        self.fill_id['fg']='white'
        self.fill_id['bg']='blue'
        #self.fill_id['height']='2'
        self.fill_id['width']='18'
        #self.fill_id.grid(row=2,column=0,padx=(0,0),pady=(0,0))
        self.fill_id.place(x=100,y=110)

        self.fill_department = tk.Label(self, text="DEPARTMENT")
        self.fill_department['font'] = 'Helvetica 16 bold'
        self.fill_department['fg']='white'
        self.fill_department['bg']='blue'
        #self.fill_department['height']='2'
        self.fill_department['width']='18'
        #self.fill_department.grid(row=3,column=0,padx=(0,0),pady=(0,0))
        self.fill_department.place(x=100,y=150)

        self.fill_cellno = tk.Label(self, text="PHONE NO")
        self.fill_cellno['font'] = 'Helvetica 16 bold'
        self.fill_cellno['fg']='white'
        self.fill_cellno['bg']='blue'
        #self.fill_cellno['height']='2'
        self.fill_cellno['width']='18'
        #self.fill_cellno.grid(row=4,column=0,padx=(0,0),pady=(0,0))
        self.fill_cellno.place(x=100,y=190)

        self.fill_pass = tk.Label(self, text="PASSWORD")
        self.fill_pass['font'] = 'Helvetica 16 bold'
        self.fill_pass['fg']='white'
        self.fill_pass['bg']='blue'
        #self.fill_pass['height']='2'
        self.fill_pass['width']='18'
        #self.fill_pass.grid(row=4,column=0,padx=(0,0),pady=(0,0))
        self.fill_pass.place(x=100,y=230)

        self.fill_con_pass = tk.Label(self, text="CONFIRM PASSWORD")
        self.fill_con_pass['font'] = 'Helvetica 16 bold'
        self.fill_con_pass['fg']='white'
        self.fill_con_pass['bg']='blue'
        #self.fill_con_pass['height']='2'
        self.fill_con_pass['width']='18'
        #self.fill_con_pass.grid(row=4,column=0,padx=(0,0),pady=(0,0))
        self.fill_con_pass.place(x=100,y=270)

        self.entry_name = tk.Entry(self)
        self.entry_name['font'] = 'Helvetica 18 bold'
        self.entry_name['fg']='blue'
        self.entry_name['bg']='white'
        #self.entry_name['height']='20'
        self.entry_name['width']='29'
        #self.entry_name.grid(row=1, column=1,padx=(0,100),pady=(0,0),ipadx=5,ipady=5)
        self.entry_name.place(x=350,y=68)

        self.entry_roll_no = tk.Label(self,text=vals.scan_roll)
        self.entry_roll_no['font'] = 'Helvetica 18 bold'
        self.entry_roll_no['fg']='blue'
        self.entry_roll_no['bg']='white'
        self.entry_roll_no['relief']='groove'
        #self.entry_roll_no['height']='20'
        self.entry_roll_no['width']='25'
        #self.entry_roll_no.grid(row=2, column=1,padx=(0,100),pady=(0,0),ipadx=5,ipady=5)
        self.entry_roll_no.place(x=350,y=108)

        #global depart_clicked
        #depart_clicked=0
        vals.depart_clicked=0
        vals.depart_warn=0
        vals.name_warn=0
        vals.cell_warn=0
        vals.pass_warn1=0
        vals.pass_warn2=0
        
        vals.dep_name="Select department"

        self.entry_department = tk.Button(self,command=self.department_list)
        self.entry_department['font'] = 'Helvetica 13 bold'
        self.entry_department['text'] = vals.dep_name
        self.entry_department['fg']='blue'
        self.entry_department['justify']='left'
        self.entry_department['bg']='white'
        self.entry_department['relief']='groove'
        #self.entry_department['height']='0.8'
        self.entry_department['width']='37'
        #self.entry_department.grid(row=3, column=1,padx=(0,100),pady=(0,0),ipadx=5,ipady=5)
        self.entry_department.place(x=351,y=149)

        self.entry_cellno = tk.Entry(self)
        self.entry_cellno['font'] = 'Helvetica 18 bold'
        self.entry_cellno['fg']='blue'
        self.entry_cellno['bg']='white'
        #self.entry_cellno['height']='20'
        self.entry_cellno['width']='29'
        #self.entry_cellno.grid(row=4, column=1,padx=(0,100),pady=(0,0),ipadx=5,ipady=5)
        self.entry_cellno.place(x=350,y=188)

        self.entry_pass = tk.Entry(self,show='*')
        self.entry_pass['font'] = 'Helvetica 18 bold'
        self.entry_pass['fg']='blue'
        self.entry_pass['bg']='white'
        #self.entry_pass['height']='20'
        self.entry_pass['width']='29'
        #self.entry_pass.grid(row=4, column=1,padx=(0,100),pady=(0,0),ipadx=5,ipady=5)
        self.entry_pass.place(x=350,y=228)

        self.entry_con_pass = tk.Entry(self,show='*')
        self.entry_con_pass['font'] = 'Helvetica 18 bold'
        self.entry_con_pass['fg']='blue'
        self.entry_con_pass['bg']='white'
        #self.entry_con_pass['height']='20'
        self.entry_con_pass['width']='29'
        #self.entry_con_pass.grid(row=4, column=1,padx=(0,100),pady=(0,0),ipadx=5,ipady=5)
        self.entry_con_pass.place(x=350,y=268)

        self.sign_up_reg =tk.Button(self, text="SIGN UP", command=self.signed_up_new)
        self.sign_up_reg['font'] = 'Helvetica 18 bold'
        self.sign_up_reg['height'] = '2'
        self.sign_up_reg['width'] = '7'
        self.sign_up_reg['fg'] = 'white'
        self.sign_up_reg['bg'] = 'blue'
        self.sign_up_reg['activebackground'] = 'white'
        self.sign_up_reg['activeforeground'] = 'blue'
        self.sign_up_reg["cursor"] = "hand2"
        #self.sign_up_reg.grid(row=5,columnspan=1,column=1,padx=(250,80),pady=(5,5))
        self.sign_up_reg.place(x=615,y=320)

        self.go_back_btn =tk.Button(self, text="GO BACK", command=self.up_to_in)
        self.go_back_btn['font'] = 'Helvetica 12 bold'
        self.go_back_btn['height'] = '2'
        self.go_back_btn['width'] = '8'
        self.go_back_btn['fg'] = 'white'
        self.go_back_btn['bg'] = 'red'
        self.go_back_btn['activebackground'] = 'white'
        self.go_back_btn['activeforeground'] = 'red'
        self.go_back_btn["cursor"] = "hand2"
        #self.go_back_btn.grid(row=5,columnspan=1,column=0,padx=(28,250),pady=(44,30))
        self.go_back_btn.place(x=70,y=360)


    def department_list(self):
        self.entry_department.destroy()
        self.sign_up_reg.place_forget()
        self.go_back_btn.place_forget()

        #global depart_clicked
        #depart_clicked=1
        vals.depart_clicked=1

        self.depart_list_widget=tk.Label(self)
        self.depart_list_widget['bg']='white'
        self.depart_list_widget['height']='16'
        self.depart_list_widget['width']='54'
        self.depart_list_widget.place(x=350, y=67)

        self.department1 = tk.Button(self,command=self.depart1)
        self.department1['font'] = 'Helvetica 17 bold'
        self.department1['text'] = 'Mechatronics'
        self.department1['fg']='white'
        self.department1['bg']='blue'
        self.department1['activeforeground']='blue'
        self.department1['height']='1'
        self.department1['width']='12'
        self.department1.place(x=359,y=80)


        self.department2 = tk.Button(self,command=self.depart2)
        self.department2['font'] = 'Helvetica 17 bold'
        self.department2['text'] = 'Mechanical'
        self.department2['fg']='white'
        self.department2['bg']='blue'
        self.department2['activeforeground']='blue'
        self.department2['height']='1'
        self.department2['width']='12'
        self.department2.place(x=545,y=80)


        self.department3 = tk.Button(self,command=self.depart3)
        self.department3['font'] = 'Helvetica 17 bold'
        self.department3['text'] = 'Electrical'
        self.department3['fg']='white'
        self.department3['bg']='blue'
        self.department3['activeforeground']='blue'
        self.department3['height']='1'
        self.department3['width']='12'
        self.department3.place(x=359,y=130)


        self.department4 = tk.Button(self,command=self.depart4)
        self.department4['font'] = 'Helvetica 17 bold'
        self.department4['text'] = 'Computer Sc.'
        self.department4['fg']='white'
        self.department4['bg']='blue'
        self.department4['activeforeground']='blue'
        self.department4['height']='1'
        self.department4['width']='12'
        self.department4.place(x=545,y=130)
        

        self.department5 = tk.Button(self,command=self.depart5)
        self.department5['font'] = 'Helvetica 17 bold'
        self.department5['text'] = 'FMC'
        self.department5['fg']='white'
        self.department5['bg']='blue'
        self.department5['activeforeground']='blue'
        self.department5['height']='1'
        self.department5['width']='12'
        self.department5.place(x=359,y=180)
        

        self.department6 = tk.Button(self,command=self.depart6)
        self.department6['font'] = 'Helvetica 17 bold'
        self.department6['text'] = 'App. Sciences'
        self.department6['fg']='white'
        self.department6['bg']='blue'
        self.department6['activeforeground']='blue'
        self.department6['height']='1'
        self.department6['width']='12'
        self.department6.place(x=545,y=180)


        self.department7 = tk.Button(self,command=self.depart7)
        self.department7['font'] = 'Helvetica 17 bold'
        self.department7['text'] = 'Humanities'
        self.department7['fg']='white'
        self.department7['bg']='blue'
        self.department7['activeforeground']='blue'
        self.department7['height']='1'
        self.department7['width']='12'
        self.department7.place(x=451,y=230)



    def depart1(self):
        self.depart_list_widget.destroy()
        self.department1.destroy()
        self.department2.destroy()
        self.department3.destroy()
        self.department4.destroy()
        self.department5.destroy()
        self.department6.destroy()
        self.department7.destroy()

        self.sign_up_reg.place(x=600,y=320)
        self.go_back_btn.place(x=70,y=360)

        vals.dep_name="Mechatronics"

        self.entry_department = tk.Button(self,command=self.department_list)
        self.entry_department['font'] = 'Helvetica 13 bold'
        self.entry_department['text'] = vals.dep_name
        self.entry_department['fg']='blue'
        self.entry_department['justify']='left'
        self.entry_department['bg']='white'
        self.entry_department['relief']='groove'
        #self.entry_department['height']='0.8'
        self.entry_department['width']='37'
        #self.entry_department.grid(row=3, column=1,padx=(0,100),pady=(0,0),ipadx=5,ipady=5)
        self.entry_department.place(x=351,y=149)
        

    def depart2(self):
        self.depart_list_widget.destroy()
        self.department1.destroy()
        self.department2.destroy()
        self.department3.destroy()
        self.department4.destroy()
        self.department5.destroy()
        self.department6.destroy()
        self.department7.destroy()

        self.sign_up_reg.place(x=600,y=320)
        self.go_back_btn.place(x=70,y=360)

        vals.dep_name="Mechanical"

        self.entry_department = tk.Button(self,command=self.department_list)
        self.entry_department['font'] = 'Helvetica 13 bold'
        self.entry_department['text'] = vals.dep_name
        self.entry_department['fg']='blue'
        self.entry_department['justify']='left'
        self.entry_department['bg']='white'
        self.entry_department['relief']='groove'
        #self.entry_department['height']='0.8'
        self.entry_department['width']='37'
        #self.entry_department.grid(row=3, column=1,padx=(0,100),pady=(0,0),ipadx=5,ipady=5)
        self.entry_department.place(x=351,y=149)

    def depart3(self):
        self.depart_list_widget.destroy()
        self.department1.destroy()
        self.department2.destroy()
        self.department3.destroy()
        self.department4.destroy()
        self.department5.destroy()
        self.department6.destroy()
        self.department7.destroy()

        self.sign_up_reg.place(x=600,y=320)
        self.go_back_btn.place(x=70,y=360)
        
        vals.dep_name="Electrical"

        self.entry_department = tk.Button(self,command=self.department_list)
        self.entry_department['font'] = 'Helvetica 13 bold'
        self.entry_department['text'] = vals.dep_name
        self.entry_department['fg']='blue'
        self.entry_department['justify']='left'
        self.entry_department['bg']='white'
        self.entry_department['relief']='groove'
        #self.entry_department['height']='0.8'
        self.entry_department['width']='37'
        #self.entry_department.grid(row=3, column=1,padx=(0,100),pady=(0,0),ipadx=5,ipady=5)
        self.entry_department.place(x=351,y=149)


    def depart4(self):
        self.depart_list_widget.destroy()
        self.department1.destroy()
        self.department2.destroy()
        self.department3.destroy()
        self.department4.destroy()
        self.department5.destroy()
        self.department6.destroy()
        self.department7.destroy()

        self.sign_up_reg.place(x=600,y=320)
        self.go_back_btn.place(x=70,y=360)

        vals.dep_name="Computer Science"

        self.entry_department = tk.Button(self,command=self.department_list)
        self.entry_department['font'] = 'Helvetica 13 bold'
        self.entry_department['text'] = vals.dep_name
        self.entry_department['fg']='blue'
        self.entry_department['justify']='left'
        self.entry_department['bg']='white'
        self.entry_department['relief']='groove'
        #self.entry_department['height']='0.8'
        self.entry_department['width']='37'
        #self.entry_department.grid(row=3, column=1,padx=(0,100),pady=(0,0),ipadx=5,ipady=5)
        self.entry_department.place(x=351,y=149)

    def depart5(self):
        self.depart_list_widget.destroy()
        self.department1.destroy()
        self.department2.destroy()
        self.department3.destroy()
        self.department4.destroy()
        self.department5.destroy()
        self.department6.destroy()
        self.department7.destroy()

        self.sign_up_reg.place(x=600,y=320)
        self.go_back_btn.place(x=70,y=360)

        vals.dep_name="Fazaia Medical College"

        self.entry_department = tk.Button(self,command=self.department_list)
        self.entry_department['font'] = 'Helvetica 13 bold'
        self.entry_department['text'] = vals.dep_name
        self.entry_department['fg']='blue'
        self.entry_department['justify']='left'
        self.entry_department['bg']='white'
        self.entry_department['relief']='groove'
        #self.entry_department['height']='0.8'
        self.entry_department['width']='37'
        #self.entry_department.grid(row=3, column=1,padx=(0,100),pady=(0,0),ipadx=5,ipady=5)
        self.entry_department.place(x=351,y=149)


    def depart6(self):
        self.depart_list_widget.destroy()
        self.department1.destroy()
        self.department2.destroy()
        self.department3.destroy()
        self.department4.destroy()
        self.department5.destroy()
        self.department6.destroy()
        self.department7.destroy()

        self.sign_up_reg.place(x=600,y=320)
        self.go_back_btn.place(x=70,y=360)

        vals.dep_name="Applied Sciences"

        self.entry_department = tk.Button(self,command=self.department_list)
        self.entry_department['font'] = 'Helvetica 13 bold'
        self.entry_department['text'] = vals.dep_name
        self.entry_department['fg']='blue'
        self.entry_department['justify']='left'
        self.entry_department['bg']='white'
        self.entry_department['relief']='groove'
        #self.entry_department['height']='0.8'
        self.entry_department['width']='37'
        #self.entry_department.grid(row=3, column=1,padx=(0,100),pady=(0,0),ipadx=5,ipady=5)
        self.entry_department.place(x=351,y=149)


    def depart7(self):
        self.depart_list_widget.destroy()
        self.department1.destroy()
        self.department2.destroy()
        self.department3.destroy()
        self.department4.destroy()
        self.department5.destroy()
        self.department6.destroy()
        self.department7.destroy()

        self.sign_up_reg.place(x=600,y=320)
        self.go_back_btn.place(x=70,y=360)

        vals.dep_name="Humanities"

        self.entry_department = tk.Button(self,command=self.department_list)
        self.entry_department['font'] = 'Helvetica 13 bold'
        self.entry_department['text'] = vals.dep_name
        self.entry_department['fg']='blue'
        self.entry_department['justify']='left'
        self.entry_department['bg']='white'
        self.entry_department['relief']='groove'
        #self.entry_department['height']='0.8'
        self.entry_department['width']='37'
        #self.entry_department.grid(row=3, column=1,padx=(0,100),pady=(0,0),ipadx=5,ipady=5)
        self.entry_department.place(x=351,y=149)





    def signed_up_new(self):
        get_name= self.entry_name.get()

        up_scan_roll_line=vals.scan_roll[2:]
        up_get_line=int(up_scan_roll_line)

        #dep_name

        get_cellno=self.entry_cellno.get()
        get_passw=self.entry_pass.get()
        get_passwcon=self.entry_con_pass.get()

        abcd="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "

        size_name=len(get_name)
        name_let_check=0

        for letter in get_name:
            for ch_letter in abcd:
                if letter==ch_letter:
                    name_let_check=name_let_check+1

        size_cell=len(get_cellno)
        size_pass=len(get_passw)

        digits_p="0123456789"
        total_cell=0
        for digit in get_cellno:
            for d2 in digits_p:
                if digit==d2:
                    total_cell=total_cell+1


        get_line=int(up_scan_roll_line)
        get_line=get_line+1

        student_line=linecache.getline('user_data/batch16.txt', get_line)
        linecache.clearcache()


        

        
            

        if True:
            if vals.depart_clicked==1:
                if size_name<=20 and size_name>=4 and name_let_check==size_name:
                    if size_cell==11 and total_cell==size_cell:
                        if size_pass>=6 and size_pass<=25:
                            if get_passw==get_passwcon:
                                self.sign_up_back.destroy()
                                self.heading_new.destroy()
                                self.fill_name.destroy()
                                self.fill_id.destroy()
                                self.fill_department.destroy()
                                self.fill_cellno.destroy()
                                self.fill_pass.destroy()
                                self.fill_con_pass.destroy()
                                self.entry_name.destroy()
                                self.entry_roll_no.destroy()
                                self.entry_department.destroy()
                                self.entry_cellno.destroy()
                                self.entry_pass.destroy()
                                self.entry_con_pass.destroy()
                                self.sign_up_reg.destroy()
                                self.go_back_btn.destroy()
                                self.mainmenu()
                            else:
                                vals.pass_warn2=1
                                if vals.dpart_warn==1:
                                    self.depart_issue.destroy()
                                if vals.name_warn==1:
                                    self.name_issue.destroy()
                                if vals.cell_warn==1:
                                    self.cell_issue.destroy()
                                if vals.pass_warn1==1:
                                    self.pass_issue1.destroy()
                                self.pass_issue2 = tk.Label(self, text="Passwords do not match")
                                self.pass_issue2['font'] = 'Helvetica 15 bold'
                                self.pass_issue2['fg']='white'
                                self.pass_issue2['bg']='red'
                                self.pass_issue2.place(x=200,y=315)
                                
                        else:
                            vals.pass_warn1=1
                            if vals.dpart_warn==1:
                                self.depart_issue.destroy()
                            if vals.name_warn==1:
                                self.name_issue.destroy()
                            if vals.cell_warn==1:
                                self.cell_issue.destroy()
                            self.pass_issue1 = tk.Label(self, text="Password should be b/w 6 and 25 characters")
                            self.pass_issue1['font'] = 'Helvetica 15 bold'
                            self.pass_issue1['fg']='white'
                            self.pass_issue1['bg']='red'
                            self.pass_issue1.place(x=160,y=315)
                            
                    else:
                        vals.cell_warn=1
                        if vals.dpart_warn==1:
                            self.depart_issue.destroy()
                        if vals.name_warn==1:
                            self.name_issue.destroy()
                        self.cell_issue = tk.Label(self, text="Please use a correct phone number")
                        self.cell_issue['font'] = 'Helvetica 15 bold'
                        self.cell_issue['fg']='white'
                        self.cell_issue['bg']='red'
                        self.cell_issue.place(x=200,y=315)
                        
                else:
                    vals.name_warn=1
                    if vals.dpart_warn==1:
                        self.depart_issue.destroy()
                    self.name_issue = tk.Label(self, text="Please use a correct name")
                    self.name_issue['font'] = 'Helvetica 15 bold'
                    self.name_issue['fg']='white'
                    self.name_issue['bg']='red'
                    self.name_issue.place(x=200,y=315)
            else:
                vals.dpart_warn=1
                self.depart_issue = tk.Label(self, text="Please select a department")
                self.depart_issue['font'] = 'Helvetica 15 bold'
                self.depart_issue['fg']='white'
                self.depart_issue['bg']='red'
                self.depart_issue.place(x=200,y=315)
        else:
            afdaf






    def up_to_in(self):
        self.sign_up_back.destroy()
        self.heading_new.destroy()
        self.fill_name.destroy()
        self.fill_id.destroy()
        self.fill_department.destroy()
        self.fill_cellno.destroy()
        self.fill_pass.destroy()
        self.fill_con_pass.destroy()
        self.entry_name.destroy()
        self.entry_roll_no.destroy()
        self.entry_department.destroy()
        self.entry_cellno.destroy()
        self.entry_pass.destroy()
        self.entry_con_pass.destroy()
        self.sign_up_reg.destroy()
        self.go_back_btn.destroy()
        self.signmenu()
        
        
        
        
   

    def mainmenu(self):
        
        self.mainpic=tk.PhotoImage(file='pictures/photo6.png')

        self.mainback=tk.Label(self,image=self.mainpic)
        #self.mainback['height']=800
        #self.mainback['width']=800
        self.mainback.place(x=0, y=0, relwidth=1, relheight=1)
        #self.mainback.grid()



        self.heading1= tk.Label(self, text="KIOSK PRINTER")
        self.heading1['fg']='blue'
        self.heading1['bg']='white'
        #self.heading1['height']='3'
        #self.heading1['width']='10'
        self.heading1['font'] = 'Courier 20 bold'
        self.heading1.grid(row=0,columnspan=2,column=0,padx=(321,321),pady=(16,425))
        #self.heading1.place(x=347,y=20)
        



        self.headinguser= tk.Label(self)
        self.headinguser['text']="""Roll NO : \nName : \nPrints this month : 
Credits : \nPages left : """
        
        self.headinguser['justify']='left'
        self.headinguser['fg']='blue'
        self.headinguser['bg']='white'
        #self.headinguser['height']='3'
        self.headinguser['width']='25'
        self.headinguser['font'] = 'Courier 15 bold'
        #self.headinguser.grid(row=1,columnspan=2,column=0,padx=(0,80),pady=(10,10))
        self.headinguser.place(x=267,y=70)






        self.changeinfo_btn = tk.Button(self)
        self.changeinfo_btn["text"] = "Change account info"
        self.changeinfo_btn["height"] = '2'
        self.changeinfo_btn["width"] = '17'
        self.changeinfo_btn["fg"] = "white"
        self.changeinfo_btn["bg"] = "blue"
        self.changeinfo_btn["activebackground"] = "white"
        self.changeinfo_btn["activeforeground"] = "blue"
        self.changeinfo_btn["cursor"] = "hand2"
        self.changeinfo_btn['font'] = 'Helvetica 12 bold'
        self.changeinfo_btn["command"] = self.change_account_info
        #self.changeinfo_btn.grid(row=2,column=0,padx=(205, 60),pady=30)
        self.changeinfo_btn.place(x=580,y=70)






        
        
        self.b1 = tk.Button(self)
        self.b1["text"] = "Print from email\n   or cloud"
        self.b1["height"] = '5'
        self.b1["width"] = '15'
        self.b1["fg"] = "white"
        self.b1["bg"] = "blue"
        self.b1["activebackground"] = "white"
        self.b1["activeforeground"] = "blue"
        self.b1["cursor"] = "hand2"
        self.b1['font'] = 'Helvetica 12 bold'
        self.b1["command"] = self.openchrome
        #self.b1.grid(row=2,column=0,padx=(205, 60),pady=30)
        self.b1.place(x=193,y=250)
        




        self.b2 = tk.Button(self, text='Print from USB',
                                  fg='white', command=self.openusb,
                                  height=5, width=15)
        self.b2['font'] = 'Helvetica 12 bold'
        self.b2['bg'] = "blue"
        self.b2['activebackground'] = "white"
        self.b2['activeforeground'] = "blue"
        self.b2['cursor'] = "hand2"
        #self.b2.grid(row=2,column=1,padx=(60,205),pady=30)
        self.b2.place(x=493,y=250)






        self.signout = tk.Button(self, text="SIGN OUT", fg="white",bg="red",
                              command=self.main_to_in, height=3, width=10)
        self.signout['font'] = 'Helvetica 12 bold'
        self.signout['cursor'] = "hand2"
        #self.signout.grid(row=3,column=0,padx=(0,200),pady=(2,30))
        self.signout.place(x=30,y=380)


    def main_to_in(self):
        self.mainback.destroy()
        self.heading1.destroy()
        self.headinguser.destroy()
        self.changeinfo_btn.destroy()
        self.b1.destroy()
        self.b2.destroy()
        self.signout.destroy()
        self.signmenu()
        
        

    def openchrome(self):
        subprocess.Popen(['C:\Program Files (x86)\Google\Chrome\Application\\chrome.exe'])
        #webbrowser.open('www.google.com', new=2, autoraise=True)
        #webbrowser.open_new_tab('www.google.com')
        '''#browser = Popen(["chromium", "http://www.google.com"])'''
        #webbrowser.open('http://www.google.com')
        #webbrowser.get('chromium-browser').open_new_tab(a_website)


    def openusb(self):
        subprocess.Popen('explorer')
        #webbrowser.open("D:\to print\")
        '''#webbrowser.open("//home//pi//Desktop//Images//")'''
        #open("//home//pi//Desktop//Images//")   also import os
        #os.system('xdg-open "%s"' % foldername)
        #xdg-open



    def change_account_info(self):
        self.mainback.destroy()
        self.heading1.destroy()
        self.headinguser.destroy()
        self.changeinfo_btn.destroy()
        self.b1.destroy()
        self.b2.destroy()
        self.signout.destroy()
        
        self.accountpic=tk.PhotoImage(file='pictures/photo6.png')

        self.account_back=tk.Label(self,image=self.accountpic)
        #self.account_back['height']=800
        #self.account_back['width']=800
        self.account_back.place(x=0, y=0, relwidth=1, relheight=1)
        #self.account_back.grid(row=0,column=0)



        self.account_heading_new= tk.Label(self, text="MY ACCOUNT")
        self.account_heading_new['fg']='blue'
        self.account_heading_new['bg']='white'
        #self.account_heading_new['height']='3'
        #self.account_heading_new['width']='10'
        self.account_heading_new['font'] = 'Courier 20 bold'
        self.account_heading_new.grid(row=0,columnspan=2,column=0,padx=(345,345),pady=(16,425))
        #self.account_heading_new.place(x=347,y=20)


        self.account_fill_name = tk.Label(self, text="NAME")
        self.account_fill_name['font'] = 'Helvetica 16 bold'
        self.account_fill_name['fg']='white'
        self.account_fill_name['bg']='blue'
        #self.account_fill_name['height']='2'
        self.account_fill_name['width']='18'
        #self.account_fill_name.grid(row=1,column=0,padx=(0,0),pady=(0,0))
        self.account_fill_name.place(x=100,y=70)



        self.account_fill_id = tk.Label(self, text="PHONE NO")
        self.account_fill_id['font'] = 'Helvetica 16 bold'
        self.account_fill_id['fg']='white'
        self.account_fill_id['bg']='blue'
        #self.account_fill_id['height']='2'
        self.account_fill_id['width']='18'
        #self.account_fill_id.grid(row=2,column=0,padx=(0,0),pady=(0,0))
        self.account_fill_id.place(x=100,y=110)



        self.account_fill_department = tk.Label(self, text="PASSWORD")
        self.account_fill_department['font'] = 'Helvetica 16 bold'
        self.account_fill_department['fg']='white'
        self.account_fill_department['bg']='blue'
        #self.account_fill_department['height']='2'
        self.account_fill_department['width']='18'
        #self.account_fill_department.grid(row=3,column=0,padx=(0,0),pady=(0,0))
        self.account_fill_department.place(x=100,y=150)



        self.account_fill_pass = tk.Button(self, text="CHANGE PASSWORD",command=self.change_pass)
        self.account_fill_pass['font'] = 'Helvetica 16 bold'
        self.account_fill_pass['fg']='white'
        self.account_fill_pass['bg']='blue'
        self.account_fill_pass['height']='2'
        self.account_fill_pass['width']='18'
        #self.account_fill_pass.grid(row=4,column=0,padx=(0,0),pady=(0,0))
        self.account_fill_pass.place(x=300,y=230)



        self.account_entry_name = tk.Entry(self)
        self.account_entry_name.insert (0, 'kashif' )
        self.account_entry_name['font'] = 'Helvetica 18 bold'
        self.account_entry_name['fg']='blue'
        self.account_entry_name['bg']='white'
        #self.account_entry_name['height']='20'
        self.account_entry_name['width']='30'
        #self.account_entry_name.grid(row=1, column=1,padx=(0,100),pady=(0,0),ipadx=5,ipady=5)
        self.account_entry_name.place(x=350,y=68)



        self.account_entry_roll_no = tk.Entry(self)
        self.account_entry_roll_no.insert(0,'03001234567')
        self.account_entry_roll_no['font'] = 'Helvetica 18 bold'
        self.account_entry_roll_no['fg']='blue'
        self.account_entry_roll_no['bg']='white'
        #self.account_entry_roll_no['height']='20'
        self.account_entry_roll_no['width']='30'
        #self.account_entry_roll_no.grid(row=2, column=1,padx=(0,100),pady=(0,0),ipadx=5,ipady=5)
        self.account_entry_roll_no.place(x=350,y=108)


        self.account_entry_cellno = tk.Entry(self,show='*')
        self.account_entry_cellno['font'] = 'Helvetica 18 bold'
        self.account_entry_cellno['fg']='blue'
        self.account_entry_cellno['bg']='white'
        #self.account_entry_cellno['height']='20'
        self.account_entry_cellno['width']='30'
        #self.account_entry_cellno.grid(row=3, column=1,padx=(0,100),pady=(0,0),ipadx=5,ipady=5)
        self.account_entry_cellno.place(x=350,y=148)








        self.account_save =tk.Button(self, text="SAVE", command=self.info_changed)
        self.account_save['font'] = 'Helvetica 18 bold'
        self.account_save['height'] = '2'
        self.account_save['width'] = '7'
        self.account_save['fg'] = 'white'
        self.account_save['bg'] = 'blue'
        self.account_save['activebackground'] = 'white'
        self.account_save['activeforeground'] = 'blue'
        self.account_save["cursor"] = "hand2"
        #self.account_save.grid(row=5,columnspan=1,column=1,padx=(250,80),pady=(5,5))
        self.account_save.place(x=600,y=320)


        self.account_go_back_btn =tk.Button(self, text="GO BACK", command=self.change_to_main)
        self.account_go_back_btn['font'] = 'Helvetica 12 bold'
        self.account_go_back_btn['height'] = '2'
        self.account_go_back_btn['width'] = '8'
        self.account_go_back_btn['fg'] = 'white'
        self.account_go_back_btn['bg'] = 'red'
        self.account_go_back_btn['activebackground'] = 'white'
        self.account_go_back_btn['activeforeground'] = 'red'
        self.account_go_back_btn["cursor"] = "hand2"
        #self.account_go_back_btn.grid(row=5,columnspan=1,column=0,padx=(28,250),pady=(44,30))
        self.account_go_back_btn.place(x=70,y=360)


    def info_changed(self):
        self.account_back.destroy()
        self.account_heading_new.destroy()
        self.account_fill_name.destroy()
        self.account_fill_id.destroy()
        self.account_fill_department.destroy()
        self.account_fill_pass.destroy()
        self.account_entry_name.destroy()
        self.account_entry_roll_no.destroy()
        self.account_entry_cellno.destroy()
        self.account_save.destroy()
        self.account_go_back_btn.destroy()
        self.mainmenu()
        

    def change_to_main(self):
        self.account_back.destroy()
        self.account_heading_new.destroy()
        self.account_fill_name.destroy()
        self.account_fill_id.destroy()
        self.account_fill_department.destroy()
        self.account_fill_pass.destroy()
        self.account_entry_name.destroy()
        self.account_entry_roll_no.destroy()
        self.account_entry_cellno.destroy()
        self.account_save.destroy()
        self.account_go_back_btn.destroy()
        self.mainmenu()
        

    def change_pass(self):
        self.pass_back=tk.Label(self)
        self.pass_back['bg']='silver'
        self.pass_back['height']=25
        self.pass_back['width']=95
        self.pass_back.place(x=70, y=60)

        self.current_pass_label = tk.Label(self, text="CURRENT PASSWORD")
        self.current_pass_label['font'] = 'Helvetica 14 bold'
        self.current_pass_label['fg']='white'
        self.current_pass_label['bg']='blue'
        #self.current_pass_label['height']='2'
        self.current_pass_label['width']='18'
        #self.current_pass_label.grid(row=3,column=0,padx=(0,0),pady=(0,0))
        self.current_pass_label.place(x=160,y=100)

        
        self.new_pass_label = tk.Label(self, text="NEW PASSWORD")
        self.new_pass_label['font'] = 'Helvetica 14 bold'
        self.new_pass_label['fg']='white'
        self.new_pass_label['bg']='blue'
        #self.new_pass_label['height']='2'
        self.new_pass_label['width']='18'
        #self.new_pass_label.grid(row=3,column=0,padx=(0,0),pady=(0,0))
        self.new_pass_label.place(x=160,y=150)


        self.con_new_pass_label = tk.Label(self, text="CONFIRM PASSWORD")
        self.con_new_pass_label['font'] = 'Helvetica 14 bold'
        self.con_new_pass_label['fg']='white'
        self.con_new_pass_label['bg']='blue'
        #self.con_new_pass_label['height']='2'
        self.con_new_pass_label['width']='18'
        #self.con_new_pass_label.grid(row=3,column=0,padx=(0,0),pady=(0,0))
        self.con_new_pass_label.place(x=160,y=200)


        self.current_pass_enter = tk.Entry(self,show='*')
        self.current_pass_enter['font'] = 'Helvetica 16 bold'
        self.current_pass_enter['fg']='blue'
        self.current_pass_enter['bg']='white'
        #self.current_pass_enter['height']='20'
        self.current_pass_enter['width']='20'
        #self.current_pass_enter.grid(row=3, column=1,padx=(0,100),pady=(0,0),ipadx=5,ipady=5)
        self.current_pass_enter.place(x=410,y=98)




        self.new_pass_enter = tk.Entry(self,show='*')
        self.new_pass_enter['font'] = 'Helvetica 16 bold'
        self.new_pass_enter['fg']='blue'
        self.new_pass_enter['bg']='white'
        #self.new_pass_enter['height']='20'
        self.new_pass_enter['width']='20'
        #self.new_pass_enter.grid(row=3, column=1,padx=(0,100),pady=(0,0),ipadx=5,ipady=5)
        self.new_pass_enter.place(x=410,y=148)


        self.con_new_pass_enter = tk.Entry(self,show='*')
        self.con_new_pass_enter['font'] = 'Helvetica 16 bold'
        self.con_new_pass_enter['fg']='blue'
        self.con_new_pass_enter['bg']='white'
        #self.con_new_pass_enter['height']='20'
        self.con_new_pass_enter['width']='20'
        #self.con_new_pass_enter.grid(row=3, column=1,padx=(0,100),pady=(0,0),ipadx=5,ipady=5)
        self.con_new_pass_enter.place(x=410,y=198)


        self.pass_save =tk.Button(self, text="SAVE", command=self.pass_saved)
        self.pass_save['font'] = 'Helvetica 18 bold'
        self.pass_save['height'] = '2'
        self.pass_save['width'] = '7'
        self.pass_save['fg'] = 'white'
        self.pass_save['bg'] = 'blue'
        self.pass_save['activebackground'] = 'white'
        self.pass_save['activeforeground'] = 'blue'
        self.pass_save["cursor"] = "hand2"
        #self.pass_save.grid(row=5,columnspan=1,column=1,padx=(250,80),pady=(5,5))
        self.pass_save.place(x=530,y=250)


        self.pass_cancel =tk.Button(self, text="GO BACK", command=self.pass_cancelled)
        self.pass_cancel['font'] = 'Helvetica 12 bold'
        self.pass_cancel['height'] = '2'
        self.pass_cancel['width'] = '8'
        self.pass_cancel['fg'] = 'white'
        self.pass_cancel['bg'] = 'red'
        self.pass_cancel['activebackground'] = 'white'
        self.pass_cancel['activeforeground'] = 'red'
        self.pass_cancel["cursor"] = "hand2"
        self.pass_cancel.place(x=140,y=330)




    def pass_saved(self):
        self.pass_back.destroy()
        self.current_pass_label.destroy()
        self.new_pass_label.destroy()
        self.con_new_pass_label.destroy()
        self.current_pass_enter.destroy()
        self.new_pass_enter.destroy()
        self.con_new_pass_enter.destroy()
        self.pass_save.destroy()
        self.pass_cancel.destroy()

    def pass_cancelled(self):
        self.pass_back.destroy()
        self.current_pass_label.destroy()
        self.new_pass_label.destroy()
        self.con_new_pass_label.destroy()
        self.current_pass_enter.destroy()
        self.new_pass_enter.destroy()
        self.con_new_pass_enter.destroy()
        self.pass_save.destroy()
        self.pass_cancel.destroy()




        

root = tk.Tk()
app = Application(master=root)
#root.overrideredirect(1)
#root.focus_force()
#root.wm_attributes('-type', 'splash')
app.master.title("KIOSK Printer GUI")
app.master.maxsize(843,474)
app.master.minsize(843,474)
app.mainloop()
