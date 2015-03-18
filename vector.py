class vector():
      def createvector(self,size):
           self.s=[" " for i in range(size)]
           self.ctr=0
           self.size=size
           #print ("Vector created:",self.s)

      def insertatrank(self,r,val):
           if(self.ctr==len(self.s)):
              print ("Vector Full")
              b=[" " for i in range(self.size)]
              for i in range(self.ctr):
                b[i]=self.s[i]
                ctr=self.ctr
              a.createvector(2*(self.size))
              for i in range(ctr):
                self.s[i]=b[i]
              a.insertatrank(ctr,val)
              self.ctr=ctr+1
           else:
              if(self.s[r]==" "):
                 self.s[r]=val
                 self.ctr+=1
              else:
                 ptr=self.ctr-1
                 for i in range(self.ctr-r):
                    self.s[ptr+1]=self.s[ptr]
                    ptr-=1
                 self.s[ptr+1]=val
                 self.ctr+=1

      def replaceatrank(self,r,val):
           self.s[r]=val
           print (val,"replaced at rank ",r)

      def removeatrank(self,r):
           if(self.s[r]==" "):
                   print ("No element at specified rank")
           else:
                   ptr=r
                   ret=self.s[r]
                   self.s[r]=" "
                   return ret
                   for i in range(self.ctr-r-1):
                     self.s[ptr]=self.s[ptr+1]
                     ptr+=1
                   self.s[ptr]=" "
                   self.ctr-=1

      def show(self):
           print (self.s)

      def isfull(self):
           if(self.ctr==len(self.s)):
                   return True
           else:
                   return False

      def isempty(self):
           if(self.ctr==0):
                   return True
           else:
                   return False

      def length(self):
           print ("No.of elements in the Vector=",self.ctr)

      def elementatrank(self,r):
           #print "The element at rank ",r,"is ",self.s[r]
           return self.s[r]
'''a=vector()
a.createvector(5)
a.show()'''
