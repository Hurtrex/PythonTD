# Stack Last In First Out
# really simple a stack of plate new ones goes on top of the old one
# and you take them first cuz it would be dumb to take the old one
# at the bottom
from src.TD7.TempSLL import TempSLL

#IStack: has push(item), pull(), top/peek

class Stack:
    def __init__(self):
        self.items = TempSLL()
        
    def push(self,item):
        self.items.add_back(item) #0(n)
        
    def push(self):
        return self.items.add_front() #0(1)
        
    def pull(self):
        return self.items.remove_back() #0(n)
        
    def pull(self):
        return self.items.remove_front() #0(1)
    #These big 0 notation are only for a SLL
    
# class stack that herite from SLL    
class Stack(TempSLL):
    
    def push(self,item):
        self.add_front(item)
     
# class stack with a list intead of a ssl     
class stack:
    def __init__(self):
        data = []
    
    def push(self,item):
        self.data.append(item)
    
    def pull(self):
        return self.data.pop(self.data.len-1)

        
       