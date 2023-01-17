class Pagination:
    index=0
    def __init__(self,items=[],pageSize=10):
        self.items=items
        self.pageSize=int(pageSize)
        
            
    def firstPage(self):
        self.index=0
        
        
        
        
    def nextPage(self):
        if self.index+self.pageSize>len(self.items):
             self.index=0
        else:
            self.index=self.index+self.pageSize
        
       
            
    
    def getVisibleItems(self):
        
        if self.index<self.pageSize:
            print(self.items[self.index:self.pageSize])
        elif self.index+self.pageSize>len(self.items):
            print(self.items[self.index:self.pageSize])
        else:
            print(self.items[self.index:self.index+self.pageSize])
        print("Total page:",(len(self.items)//self.pageSize)+1,"\nnumero page:",(self.index//self.pageSize)+1)
        
        
    def prevPage(self):
        if self.index-self.pageSize<0:
            self.index=0
        else:
            self.index=self.index-self.pageSize
        
            
            
    def lastPage(self):
        n=(len(self.items)//self.pageSize)
        p=(self.pageSize*n)
        self.index=p
        
       
    def goToPage(self,n):
        if (self.index+n+self.pageSize)<=len(self.items):
            self.index=self.index+int(n)+self.pageSize
        elif n<=0:
            self.index=0
        elif  (self.index+n+self.pageSize)>=len(self.items):
            self.index=(int(n)//self.index)+self.index
        
        
       
           
        

alphabetlist="a b c d e f g h i j k l m n o p q r s t u v w x y z".split(' ')
p=Pagination(alphabetlist,4)
#print(p.items,p.pageSize)
p.getVisibleItems()
p.nextPage()
p.getVisibleItems()
p.nextPage()
p.getVisibleItems()
#p.prevPage()
#p.getVisibleItems()

p.goToPage(2)
p.getVisibleItems()
#p.lastPage()
#p.getVisibleItems()