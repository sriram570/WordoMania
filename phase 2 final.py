import sys
import time
import turtle
import random
from p1 import*
from p2 import*
from hp1 import*
from bst import*
from cirq import*
from vector import*
from tkinter import*
import tkinter.messagebox
global p,l,us_name
l_flag=False
flag=True
root=Tk()

canvas=Canvas(root)
E1 = Entry(root)
E2 = Entry(root)
E3 = Entry(root)
E4 = Entry(root)
E5 = Entry(root)
E6 = Entry(root)
sub_b=Button(root)

class time_travel():
    def __init__(self):
                
                self.imageq=Queue()                 #Queue to store images
                self.imageq.createQueue(20)
                self.ansq=Queue()                   #Queue to store the answers
                self.ansq.createQueue(20)
                self.string_vector=vector()         #Vector to randomly give the comment for answer
                self.string_vector.createvector(5) 
                self.score=0                        #Score intitialized to zero
                self.limit=1                        #Level of the user initialized to 1
 
    def vec(self):                                  #Vector to give random message 
    
            self.string_vector.insertatrank(0,"AWESOME !!!")
            self.string_vector.insertatrank(1,"GREAT !!!")
            self.string_vector.insertatrank(2,"THAT'S RIGHT !!!")
            self.string_vector.insertatrank(3,"WONDERFUL !!!")
            self.string_vector.insertatrank(4,"COOL !!!")

    def insert(self):
            
            self.ansq=answers
            self.imageq=images    
    
    def writetofile(self,Name,uname='',pw=''):      #Adding each new user to the file
            try:
                    f=open(r'leaderboardfile.txt','a')
                    f.write(uname+'\n')
                    f.write(pw+'\n')
                    f.write('0')
                    f.write('\n')
                    f.write('1')
                    f.write('\n\n')
                    tkinter.messagebox.showinfo(" REGISTRATION ","Successfully Registered !!!")
                    self.check_user()
                 
            except Exception:'Print error in writing to file...'
            finally:
                    
                    f.flush()
                    f.close()     
    
    def add(self,Name,UName,PW):                       
                if UName=="":
                    tkinter.messagebox.showinfo("  ERROR ","  Please provide valid Username  ")
                    self.register()
                elif PW=="":
                    tkinter.messagebox.showinfo("  ERROR ","  Please provide valid Password  ")
                    self.register()
                elif UName==PW:
                    tkinter.messagebox.showinfo("  ERROR ","  Username and password cannot be same  ")
                    self.register()
                else:
                    self.writetofile(Name,UName,PW)
                            
    def search(self,name,pwd):
        global us_name
        global p
        if name=="" and pwd=="":
            tkinter.messagebox.showinfo("  ERROR ","  Required fields cannot be empty  ")
            self.check_user()
        else:
            with open("leaderboardfile.txt", "r") as f:
                found = False    
                for line in f:
                    if line.strip() == name:
                        con=f.readline()
                        us_name=name
                        if con.strip()==pwd:
                            tkinter.messagebox.showinfo("  Login Status  ","      LOGIN SUCCESSFUL ")
                            p=pwd
                            con=f.readline()
                            self.score=int(con.strip())
                            con1=f.readline()
                            self.limit=int(con1.strip())
                            found = True
                            self.welcome()
                if not found:
                    tkinter.messagebox.showinfo(" Warning !!! ", " Credentials Mismatch"+'\n\n'+"          Try Again")
                    self.clear()
                    self.check_user()
   
    def clear(self):
                global root
                global canvas
                root.destroy()
                root=Tk()

    def chec(self):
        global E3,E2
        
        un=E3.get()
        pw=E2.get()
        
        self.search(un,pw)

    def addUser(self):
            global E4,E5,E6
            
            name=E4.get()
            un=E5.get()
            pw=E6.get()
            
            self.add(name,un,pw)

    def rank(self):
        cnt2=1
        count=1
        score_arr=[]
        self.score_write()
        with open("leaderboardfile.txt", "r") as f:
            for line in f:
                if count==1:
                    f.readline()
                    con=f.readline()
                    count+=1
                else:
                    f.readline()
                    f.readline()
                    f.readline()
                    con=f.readline()
                score_arr.append(con.strip())        
        h.list=[]
        for i in range(len(score_arr)-1):
            h.Insert(int(score_arr[i]))
        for j in range(len(h.list)) :
            if h.RemoveLargest() ==self.score:
                st="Your Current Rank :  "
                st+=str(cnt2)
                tkinter.messagebox.showinfo(" RANK ", st)
                break
            else:
                cnt2+=1
        
        
        
    def register(self):
            global root
            global canvas
            global E4,E5,E6
            
            self.clear()
            RWidth=root.winfo_screenwidth()
            RHeight=root.winfo_screenheight()
            root.geometry(("%dx%d")%(RWidth,RHeight))
            canvas = Canvas(width = 500, height = 500, bg = '#E6E651')
            canvas.pack(expand = YES, fill = BOTH) 
            canvas.pack(side="top", fill="both", expand=True)
            canvas_id = canvas.create_text(640,120, anchor="center")

            font1 = font.Font()
            font1.config(family='Helvetica', size=32, weight='bold')
            canvas.itemconfig(canvas_id, text=" REGISTER HERE",font=font1,fill='#CC9900')
            
            L1 = Label(root,bd="2.5", text=" NAME ",bg="#00CED1")
            L1.pack()
            L1.place(x=520, y=200)

            L2 = Label(root,bd="6", text=" USERNAME ",bg="#00CED1")
            L2.pack()
            L2.place(x=520, y=300)

            L3 = Label(root,bd="6", text=" PASSWORD ",bg="#00CED1")
            L3.pack()
            L3.place(x=520, y=400)

            E4 = Entry(root,bd="5",bg="#F5F5F5")
            E4.pack()
            E4.focus_set()
            E4.place(x=620, y=200)

            E5 = Entry(root,bd="5",bg="#F5F5F5")
            E5.pack()
            E5.focus_set()
            E5.place(x=620, y=300)

            E6 = Entry(root,bd="5",show="*",bg="#F5F5F5")
            E6.pack()
            E6.focus_set()
            E6.place(x=620, y=400)

            b2 = Button(root, text = " REGISTER ",bd="4",width=9, command = self.addUser,bg="#9966FF")
            b2.pack()
            b2.place(x=900, y=520)
            
    def check_user(self):
            global root
            global canvas
            global E2,E3
            self.clear()
            RWidth=root.winfo_screenwidth()
            RHeight=root.winfo_screenheight()
            root.geometry(("%dx%d")%(RWidth,RHeight))
            canvas = Canvas(width = 500, height = 500, bg = '#E6E651')
            canvas.pack(expand = YES, fill = BOTH) 
            canvas.pack(side="top", fill="both", expand=True)
            canvas_id = canvas.create_text(650,120, anchor="center")
            font1 = font.Font()
            font1.config(family='Helvetica', size=40, weight='bold')
            canvas.itemconfig(canvas_id, text=" LOGIN / REGISTER ",font=font1,fill='#CC9900')
            L = Label(root,bd="6", text=" USERNAME ",bg="#00CED1")
            L.pack()
            L.place(x=520, y=300)

            E3 = Entry(root,bd="5",bg="#F5F5F5")
            E3.pack()
            E3.focus_set()
            E3.place(x=620, y=300)

            M = Label(root,bd="6", text=" PASSWORD ",bg="#00CED1")
            M.pack()
            M.place(x=520, y=400)

            E2 = Entry(root,bd="5",show="*",bg="#F5F5F5")
            E2.pack()
            E2.focus_set()
            E2.place(x=620, y=400)

            font1 = font.Font()
            font1.config(family='Helvetica', size=16, weight='bold')
            canvas_id0 = canvas.create_text(650,600, anchor='center')
            canvas.itemconfig(canvas_id0, text=" Not Yet Registered? CLICK               to REGISTER  ",font=font1,fill='#CC0033')

            b10 = Button(root, text = " LOGIN ",bd="4",width=10, command = self.chec ,bg="#9966FF")
            b10.pack()
            b10.place(x=820, y=500)
            
            b22 = Button(root, text = " HERE ",bd="4",width=9, command = self.register,bg="#9966FF")
            b22.pack()
            b22.place(x=680, y=585)

    def welcome(self):                
            global root
            global canvas
            self.clear()
            RWidth=root.winfo_screenwidth()
            RHeight=root.winfo_screenheight()
            root.geometry(("%dx%d")%(RWidth,RHeight))
            canvas = Canvas(width = 500, height = 500, bg = '#E6E651')
            canvas.pack(expand = YES, fill = BOTH)

            canvas.pack(side="top", fill="both", expand=True)
            canvas_id = canvas.create_text(700,90, anchor="center")
            font1 = font.Font()
            font1.config(family='Helvetica', size=30, weight='bold')
            canvas.itemconfig(canvas_id, text="WELCOME !!! ",font=font1,fill='#CC9900')
            
            self.gif1 = PhotoImage(file = 'wel2.gif')
            canvas.create_image(375, 150, image = self.gif1, anchor = NW)

            b11 = Button(root, text = " PLAY ",bd="4",width=10, command = self.ans_input,bg="#9966FF")
            b11.pack()
            b11.place(x=750, y=600)

            b23 = Button(root, text = " READ INSTRUCTIONS ",bd="4",width=20, command = self.instructions ,bg="#9966FF")
            b23.pack()
            b23.place(x=525, y=600)
                                    
    def instructions(self):
            global root
            global canvas
            self.clear()
            RWidth=root.winfo_screenwidth()
            RHeight=root.winfo_screenheight()
            root.geometry(("%dx%d")%(RWidth,RHeight))
            canvas = Canvas(root, width=800, height=500, bg = '#E6E651')
            canvas.pack(side="top", fill="both", expand=True)
            
            font1 = font.Font()
            font1.config(family='Helvetica', size=16, weight='bold')

            canvas_id = canvas.create_text(650,80, anchor='center')
            canvas.itemconfig(canvas_id, text="WORDOMANIA",font=font1,fill='#CC0033')
            
            canvas_id0 = canvas.create_text(250,180, anchor='center')
            canvas.itemconfig(canvas_id0, text="INSTRUCTIONS :",font=font1,fill='#CC0033')
            
            canvas_id1 = canvas.create_text(399,250, anchor="center")
            canvas.itemconfig(canvas_id1, text="> +5 FOR EVERY RIGHT ANSWER...",font=font1,fill='#003333')
            
            canvas_id2 = canvas.create_text(396,300, anchor="center")
            canvas.itemconfig(canvas_id2, text="> -1 FOR EVERY WRONG GUESS...",font=font1,fill='#003333')

            canvas_id3 = canvas.create_text(400,350, anchor="center")
            canvas.itemconfig(canvas_id3, text="> KEEP AN EYE ON YOUR SCORE...",font=font1,fill='#003333')

            canvas_id4 = canvas.create_text(460,400, anchor="center")
            canvas.itemconfig(canvas_id4, text="> PRESS QUIT TO SAVE AND END THE GAME...",font=font1,fill='#003333')

            canvas_id4 = canvas.create_text(347,450, anchor="center")
            canvas.itemconfig(canvas_id4, text="> GO BACK TO START...",font=font1,fill='#003333')

            b = Button(root, text = "BACK",bd="4",width=10,command=self.welcome ,bg="#9966FF")
            b.pack()
            b.place(x=720, y=500)

    def check(self):

                global l_flag
                global E1
                global canvas
                global root
                global l
                global sub_b
                
                ans=E1.get()
                l_flag=True

                if ans==self.ansq.return_front():
                        self.imageq.dequeue()
                        self.ansq.dequeue()
                        self.score+=5
                        self.limit+=1
                        if self.limit==16:
                            self.score_write()
                            tkinter.messagebox.showinfo(" GAME OVER ", "CONGRATS !!!\n\nALL LEVELS CRACKED :)\n\nYOUR FINAL SCORE : "+str(self.score))
                            sub_b.config(state="disabled")
                        else:    
                            l=self.limit
                            b=random.randint(0,4)
                            
                            font1 = font.Font()
                            font1.config(family='Helvetica', size=22, weight='bold')
                            canvas_id10 = canvas.create_text(1100,500, anchor='center')
                            
                            canvas.itemconfig(canvas_id10, text=self.string_vector.elementatrank(b),font=font1,fill='#003333')
                            E1.after(1000,lambda:self.ans_input() )
                else:
                        self.score-=1
                        font1 = font.Font()
                        font1.config(family='Helvetica', size=20, weight='bold')
                        canvas_id10 = canvas.create_text(1100,500, anchor='center')
                        canvas.itemconfig(canvas_id10, text="Sorry Dude !!!  Keep Trying :) ",font=font1,fill='#003333')
                        E1.after(1000,lambda:self.ans_input() )

    def score_write(self):
                global p
                cnt=0
                sc=str(self.score)
                lim=str(self.limit)
                with open("leaderboardfile.txt", "r") as f:
                    for line in f:
                        if line.strip() == p: 
                            self.replace_line('leaderboardfile.txt',cnt+1,sc)
                            self.replace_line('leaderboardfile.txt',cnt+2,lim)
                        else:
                            cnt+=1

    def replace_line(self,file_name, line_num, text):
        text=text+"\n"
        lines = open(file_name, 'r').readlines()
        lines[line_num] = text
        out = open(file_name, 'w')
        out.writelines(lines)
        out.close()
                        
    def end(self):
                choice=tkinter.messagebox.askyesno(' LOGOUT ',  'Are you sure you want to LogOut? ')
                if choice:
                    self.score_write()
                    global root
                    global canvas
                    self.clear()
                    RWidth=root.winfo_screenwidth()
                    RHeight=root.winfo_screenheight()
                    root.geometry(("%dx%d")%(RWidth,RHeight))
                    canvas = Canvas(width = 500, height = 500, bg = '#E6E651')
                    canvas.pack(expand = YES, fill = BOTH)
                    self.gif1 = PhotoImage(file = 'quit.gif')
                    canvas.create_image(RWidth/2-25,RHeight/2+75, image = self.gif1, anchor = CENTER)

                    font1 = font.Font()
                    font1.config(family='Helvetica', size=16, weight='bold')
                    canvas_id0 = canvas.create_text(675,80, anchor='center')
                    canvas.itemconfig(canvas_id0, text=" DESIGNED BY KEERTHIMANU, SRIRAM AND ANUROOP  ",font=font1,fill='#CC0033')
                    canvas_id1 = canvas.create_text(675,180, anchor='center')
                    canvas.itemconfig(canvas_id1, text=" THANKS TO GOOGLE IMAGES...  ",font=font1,fill='#CC0033')

                    b = Button(root, text = "EXIT ",bd="2.5", command = quit,bg="#00CED1")
                    b.pack()
                    b.place(x=1200, y=650)

                    b = Button(root, text = "LEADER BOARD ",bd="2.5", command = self.lb,bg="#00CED1")
                    b.pack()
                    b.place(x=1050, y=650)

    def lb(self):
            x=200
            y=220
            global root
            global canvas
            global arrr
            a=[]
            b=[]         
            with open("leaderboardfile.txt", "r") as f:
                for line in f:
                    a.append(line.strip())
                    f.readline()
                    c=f.readline()
                    b.append(c.strip())
                    f.readline()
                    f.readline()
                    
            tree=searchtree()
            for i in range(len(a)):
                tree.create(int(b[i]),a[i])
            tree.inorder(tree.root)
            
            self.clear()
            RWidth=root.winfo_screenwidth()
            RHeight=root.winfo_screenheight()
            root.geometry(("%dx%d")%(RWidth,RHeight))

            canvas = Canvas(width = 400, height = 300, bg = '#E6E651')
            canvas.pack(expand = YES, fill = BOTH)
            font1 = font.Font()
            font1.config(family='Helvetica', size=20, weight='bold')

            canvas_id0 = canvas.create_text(650,120, anchor='center')
            canvas.itemconfig(canvas_id0, text=" LEADER BOARD  ",font=font1,fill='#CC0033')
            j=0       
            while j <int(len(arrr)):
                    s=""
                    canvas_id0 = canvas.create_text(435,y, anchor="nw")
                    s+=str(arrr[j]+"               "+arrr[j+1])
                    canvas.itemconfig(canvas_id0, text=s,font=font1,fill='#CC0033')
                    canvas_id0 = canvas.create_text(800,y, anchor='nw')
                    canvas.itemconfig(canvas_id0, text=arrr[j+2],font=font1,fill='#CC0033')
                    y+=75
                    j+=3

            but = Button(root,bd="4",text=" QUIT ",bg="#F5597E",activebackground="yellow",activeforeground="pink",command=quit)
            but.pack()
            but.place(x=1250, y=646)                   

    def ans_input(self):
            global sub_b
            global l_flag
            global root
            global limit
            global E1
            global canvas
            global us_name
            
            self.clear()
            RWidth=root.winfo_screenwidth()
            RHeight=root.winfo_screenheight()
            root.geometry(("%dx%d")%(RWidth,RHeight))
            
            canvas = Canvas(width = 400, height = 300, bg = '#E6E651')
            canvas.pack(expand = YES, fill = BOTH)

            if not l_flag and self.limit <16:
                for i in range(self.limit-1):
                    self.imageq.dequeue()
                    self.ansq.dequeue()
                self.gif1 = PhotoImage(file = self.imageq.return_front())
                canvas.create_image(RWidth/2-15,RHeight/2-50, image = self.gif1, anchor = CENTER)

                font1 = font.Font()
                font1.config(family='Helvetica', size=20, weight='bold')
    
                font2 = font.Font()
                font2.config(family='Helvetica', size=30, weight='bold')
    
                canvas_id = canvas.create_text(200,615, anchor='center')
                canvas.itemconfig(canvas_id, text="SCORE :       ",font=font1,fill='#CC0033')
                canvas_id = canvas.create_text(250,615, anchor='center')
                canvas.itemconfig(canvas_id, text=self.score,font=font1,fill='#CC0033')

                canvas_id1 = canvas.create_text(710,125, anchor='center')
                canvas.itemconfig(canvas_id1, text="LEVEL :          ",font=font2,fill='#CC0033')
                canvas_id1 = canvas.create_text(760,125, anchor='center')
                canvas.itemconfig(canvas_id1, text=self.limit,font=font2,fill='#CC0033')

                canvas_id1 = canvas.create_text(125,125, anchor='nw')
                canvas.itemconfig(canvas_id1, text="hi",font=font1,fill='#CC0033')
                canvas_id1 = canvas.create_text(165,125, anchor='nw')
                canvas.itemconfig(canvas_id1, text=us_name+" !!!",font=font1,fill='#CC0033')

                but = Button(root,bd="6",text=" LOGOUT ",bg="#F5597E",activebackground="yellow",activeforeground="pink",command=self.end)
                but.pack()
                but.place(x=1250, y=646)

                L1 = Label(root,bd="8", text="Answer",bg="#00CED1")
                L1.pack()
                L1.place(x=538, y=600)
                E1 = Entry(root,bd="8",bg="#F5F5F5")
                E1.pack()
                E1.focus_set()
                E1.place(x=595, y=602)
             
                sub_b = Button(root, text = "SUBMIT",bd="5.6", command = self.check,bg="#00CED1")
                sub_b.pack()
                sub_b.place(x=733.9, y=600)

                b2 = Button(root, text = "MY RANK",bd="5.6", command = self.rank,bg="#F5597E")
                b2.pack()
                b2.place(x=1135, y=646)

            elif self.limit <16:
                self.gif1 = PhotoImage(file = self.imageq.return_front())
                canvas.create_image(RWidth/2-15,RHeight/2-50, image = self.gif1, anchor = CENTER)

                font1 = font.Font()
                font1.config(family='Helvetica', size=20, weight='bold')
    
                font2 = font.Font()
                font2.config(family='Helvetica', size=30, weight='bold')
    
                canvas_id = canvas.create_text(200,615, anchor='center')
                canvas.itemconfig(canvas_id, text="SCORE :       ",font=font1,fill='#CC0033')
                canvas_id = canvas.create_text(250,615, anchor='center')
                canvas.itemconfig(canvas_id, text=self.score,font=font1,fill='#CC0033')

                canvas_id1 = canvas.create_text(710,125, anchor='center')
                canvas.itemconfig(canvas_id1, text="LEVEL :          ",font=font2,fill='#CC0033')
                canvas_id1 = canvas.create_text(760,125, anchor='center')
                canvas.itemconfig(canvas_id1, text=self.limit,font=font2,fill='#CC0033')

                canvas_id1 = canvas.create_text(125,125, anchor='nw')
                canvas.itemconfig(canvas_id1, text="hi",font=font1,fill='#CC0033')
                canvas_id1 = canvas.create_text(165,125, anchor='nw')
                canvas.itemconfig(canvas_id1, text=us_name+" !!!",font=font1,fill='#CC0033')        

                but = Button(root,bd="6",text="LOGOUT",bg="#F5597E",activebackground="yellow",activeforeground="pink",command=self.end)
                but.pack()
                but.place(x=1250, y=646)

                L1 = Label(root,bd="8", text="Answer",bg="#00CED1")
                L1.pack()
                L1.place(x=538, y=600)
                E1 = Entry(root,bd="8",bg="#F5F5F5")
                E1.pack()
                E1.focus_set()
                E1.place(x=595, y=602)
             
                sub_b = Button(root, text = "SUBMIT",bd="5.6", command = self.check,bg="#00CED1")
                sub_b.pack()
                sub_b.place(x=733.9, y=600)

                b2 = Button(root, text = "MY RANK",bd="5.6", command = self.rank,bg="#F5597E")
                b2.pack()
                b2.place(x=1135, y=646)
            else:
                tkinter.messagebox.showinfo(" GAME OVER ", " YOUR GAME HAS FINISHED ")
                quit()
                
t=time_travel()
t.vec()
t.insert()
t.check_user()


        
