from tkinter import*
arrr=[]
cnt4=1
class Node:
 
      def __init__(self,value,uname): 
          self.username=uname
          self.value = value  
          self.left = None  
          self.right = None 
          self.level = None 
 
      def __str__(self):
 
          return str(self.value)
 
 
class searchtree:
 
      def __init__(self):
 
          self.root = None
          self.arr=[]

      def size(self,node): 
        if node==None: 
            return 0
        else :    
            return self.size(node.left) + 1 + self.size(node.right)
 
      def isInternal(self,node):
        
        if node.left!=None or node.right!=None:
            return True
        else:
            return False

      def isLeaf(self,node):
        
        if node.left==None and node.right==None:
            return True
        else:
            return False


      def disp_table(self):
            global arrr
            for r in range(3):
                  for c in range(3):
                    Label(root, text='%s'%(arrr.pop(0)),
                        borderwidth=75,bg="yellow",justify="center" ).grid(row=r,column=c)
                  

      def create(self,val,uname):
                if self.root == None:
                   self.root = Node(val,uname)
                else:
                   current = self.root
                   while 1:
                        if val < current.value:
                         if current.left:
                            current = current.left
                         else:
                            current.left = Node(val,uname)
                            break      
                        elif val > current.value:
                          if current.right:
                             current = current.right
                          else:
                             current.right = Node(val,uname)
                             break

                        else:
                          break

      def printLevelOrder(self,root):
        i=0
        queue=[]
        temp_node = root
        while temp_node and i<self.size(root):
            print( temp_node.value)
        
            if temp_node.left:
                queue.append(temp_node.left)

            if temp_node.right:
                queue.append(temp_node.right)

            if i<self.size(root)-1:    
                temp_node = queue.pop(0)
                
            i+=1

 
      def inorder(self,node):
          global cnt4
          global arrr
          if node is not None:
              self.inorder(node.right)
              #disp_table(node.username,node.value)
              arrr.append(str(cnt4))
              cnt4+=1
              arrr.append(node.username)
              arrr.append(node.value)
              self.inorder(node.left)
          return (arrr)
          
          



'''tree = searchtree()     
arr = [4,10]
a=['w','s']
for i in range(len(arr)):
      tree.create(arr[i],a[i])
print ('Inorder Traversal')
print(tree.inorder(tree.root))
a=['w', 's']
in sample
b=['10', '4']
after forming tree in sample
['1', 's', '4', '2', 'w', '10']'''
'''a=['w', 's']
b=[10, 4]
for i in range(len(a)):
      tree.create(b[i],a[i])
print(tree.inorder(tree.root))'''
