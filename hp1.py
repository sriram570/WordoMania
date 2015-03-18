class Heap():
  def __init__(self):
    self.list = []

  def Insert(self, val):
    l = int(len(self.list))
    self.list.append(val)
    self.upHeap(l)

  def upHeap(self, pos):
    if pos == 0:
      return
    parent = self.getParent(pos)
    if self.list[pos] > self.list[parent]:
      self.swap(pos, parent)
      self.upHeap(parent)

  def getParent(self, pos):
    if pos == 1 or pos == 2:
      return 0
    if pos % 2 == 0:
      return int((pos-2)/2)
    else:
      return int((pos-1)/2)

  def RemoveLargest(self):
    if len(self.list)==1:
      return self.list.pop()
    else:
      result = self.list[0]
      self.list[0] = self.list.pop()
      self.downHeap(0)
      return result

  def downHeap(self, pos):
    
    children = self.getChildren(pos)
    if children == []:
      return
    elif len(children) == 1:
      if self.list[children[0]] > self.list[pos]:
        self.swap(children[0], pos)
        self.downHeap(children[0])
    else: 
      left = self.list[children[0]]
      right = self.list[children[1]]
      root = self.list[pos]
      if left > root or right > root:
        if left > right:
          self.swap(children[0], pos)
          self.downHeap(children[0])
        else:
          self.swap(children[1], pos)
          self.downHeap(children[1])

  def swap(self, p1, p2):
    tmp = self.list[p1]
    self.list[p1] = self.list[p2]
    self.list[p2] = tmp

  def getChildren(self, pos):
    l = len(self.list)
    if l <= (2*pos+1):
      return []
    elif l == (2*pos+2):
      return [2*pos+1]
    else:
      return [2*pos+1, 2*pos+2]

   
  def preorder(self,pos):
     children = self.getChildren(pos)
     print (self.list[pos])
     for c in children:
         self.preorder(c)
 

h=Heap()
'''

A = [2,50,16]
for i in range(len(A)):
    h.Insert(A[i])
h.preorder(0)
print(h.RemoveLargest())
print(h.RemoveLargest())
print(h.RemoveLargest())'''










