import sys
import time
import random
import turtle
from p1 import *
from p2 import *
from cirq import *
from vector import *
from tkinter import *
limit=0
flag=True
class time_travel():
        
        def __init__(self):
                
                self.imageq=Queue()
                self.imageq.createQueue(20)
                self.ansq=Queue()
                self.ansq.createQueue(20)
                self.string_vector=vector()
                self.string_vector.createvector(5)

        def vec(self):
        
                self.string_vector.insertatrank(0,"Awesome!!")
                self.string_vector.insertatrank(1,"Great!!")
                self.string_vector.insertatrank(2,"That's right!!")
                self.string_vector.insertatrank(3,"Wonderful!!")
                self.string_vector.insertatrank(4,"Cool!!")

        def insert(self):
                
                self.ansq=answers
                self.imageq=images

        def welcome(self):
                wn=turtle.Screen()
                wn.listen(xdummy=None, ydummy=None)
                wn.bgcolor("#E6E651")
                wn.bgpic("wel.gif")
                inst=turtle.Turtle()
                inst.pencolor("#445110")
                inst.penup()
                inst.ht()
                inst.sety(200)
                inst.write("WELCOME !!!",move=False, align="center", font=("Garamond", 24, "bold"))
                inst.sety(-240)
                inst.pencolor("#445110")
                inst.write("PRESS ' SPACEBAR ' TO START THE GAME ",move=False, align="center", font=("Garamond", 24, "bold"))
                wn.onkey(self.ans_input, "space")
                inst.setx(200)
                inst.sety(-275)
                inst.write("Image Source : LiteracyPlanet® and Nickelodeon™ ",move=False, align="center", font=("Garamond", 10, "normal"))
                
        def initialize(self):

                time.sleep(2)
                clearscreen()
                
                #alex=turtle.Turtle()
                #level=turtle.Turtle()
        def end(self):
                alex=turtle.Turtle()
                hideturtle()
                wn=turtle.Screen()
                #turtle.setx(-100)
                bgpic("endpade.gif")
                alex.penup()
                alex.ht()
                alex.sety(-260)
                alex.pencolor("#445110")
                alex.write("DESIGNED BY ANUROOP SRIRAM AND KEERTHIMANU ",move=False, align="center", font=("Garamond", 16, "bold"))
                alex.setx(0)
                alex.sety(-280)
                alex.pencolor("#445110")
                alex.write("THANKS TO GOOGLE IMAGES... ",move=False, align="center", font=("Garamond", 12, "bold"))
                turtle.delay(2)
                time.sleep(5)
                exit()
                
        def ans_input(self):
                alex=turtle.Turtle()
                hideturtle()
                global limit
                global flag
                if limit==5 or flag ==False:
                        
                        #wn=turtle.Screen()
                        bgcolor("#BFE0D6")
                        resetscreen()
                        #alex.write(limit+1, move=False, align="center", font=("Arial", 20, "normal"))
                        bgpic("end.gif")
                        
                        #turtle.mainloop()
                        alex.penup()
                        alex.ht()
                        turtle.delay(2)
                        time.sleep(2)
                        turtle.bye()
                        c=int(input("Press 1 to continue and 2 to exit the game : "))
                        #c=raw_input("Press 1 to continue and 2 to exit the game")
                        if c==1:
                                flag=True
                                limit=0
                                self.initialize()
                                self.ans_input()
                        elif c==2:
                                self.end()
                        else:
                                #limit=5
                                flag=False
                                self.ans_input()
                                                        
                else:
                        #flag=True
                        alex.ht()
                        clearscreen()
                        wn=turtle.Screen()
                        bgcolor("#BFE0D6")
                        turtle.title("PHASE 1 PROJECT ")
                        alex.penup()
                        alex.setx(0)
                        alex.sety(160)
                        alex.pendown()
                        alex.write("LEVEL ",move=False, align="center", font=("Arial", 20, "normal"))
                        alex.penup()
                        alex.forward(56)
                        alex.pendown()
                        alex.write(limit+1, move=False, align="center", font=("Arial", 20, "normal"))
                        alex.pendown()
                        bgpic(self.imageq.return_front())           
                        a=wn.textinput("TIME TRAVEL","Dude!Answer:")
                        if a==self.ansq.return_front():
                                limit+=1
                                b=random.randint(0,4)
                                alex.penup()
                                alex.setx(120)
                                alex.pensize(6)
                                alex.ht()
                                alex.pencolor("#0d97fb")
                                alex.sety(-180)
                                alex.pendown()
                                alex.write(self.string_vector.elementatrank(b), move=False, align="center", font=("Arial", 20, "normal"))
                                #alex.write(self.string_vector.elementatrank(b))
                                self.imageq.enqueue(self.imageq.dequeue())
                                self.ansq.enqueue(self.ansq.dequeue())
                                self.initialize()
                                self.ans_input()
                        else:
                                hideturtle()
                                alex.hideturtle()
                                alex.penup()
                                alex.setx(120)
                                alex.pensize(6)
                                
                                alex.pencolor("#ff0000")
                                alex.sety(-180)
                                alex.pendown()
                                alex.write("Sorry Dude !!!  Keep Trying :) ", move=False, align="center", font=("Arial", 20, "normal"))
                                time.sleep(2)
                                alex.clear()
                                self.ans_input()

        
        
        
t=time_travel()
t.vec()
t.insert()
t.welcome()
#t.end()
#t.ans_input()
