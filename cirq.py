from turtle import *
from tkinter import *
class Queue :
 def createQueue( self, n ) :
     self.count = 0
     self.front = 0
     self.rear = n - 1
     self.a = ['Null' for i in range(n)]
 
 def isEmpty( self ) :
     return self.count == 0
 
 def isFull( self ) :
     return self.count == len(self.a)
 
 def length( self ) :
     return self.count

 def enqueue( self, item ):
     if self.isFull():
         print ("Cannot enqueue to a full queue")
     else:
         n = len(self.a)
         self.rear = (self.rear + 1) % n
         self.a[self.rear] = item
#         print item,' Queued. '
         self.count += 1

 def dequeue( self ):
     if self.isEmpty():
         print ("Cannot dequeue from an empty queue.")
     else:    
         item = self.a[ self.front ]
         self.a[ self.front ]='Null'
         n = len(self.a)
         self.front = (self.front + 1) % n
         self.count -= 1
#         print item, ' Dequeued. '
         return item

 def disp(self):
     print (' Circular Queue : ',self.a)

 def return_front(self):
     return self.a[self.front]


