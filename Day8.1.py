
class Node:
    def __init__(self,data):
        self.__data=data
        self.__next=None
    
    def get_data(self):
        return self.__data
    
    def set_data(self,data):
        self.__data=data
        
    def get_next(self):
        return self.__next
    
    def set_next(self,next_node):
        self.__next=next_node
    
        
class LinkedList:    
    def __init__(self):
        self.__head=None
        self.__tail=None
        
    def get_head(self):
        return self.__head
    
    def get_tail(self):
        return self.__tail
    
           
    def add(self,data):
        new_node=Node(data)
        if(self.__head is None):
            self.__head=self.__tail=new_node
        else:
            self.__tail.set_next(new_node) 
            self.__tail=new_node
    
    def insert(self,data,data_before):
        new_node=Node(data)
        if(data_before==None):
            new_node.set_next(self.__head)
            self.__head=new_node
            if(new_node.get_next()==None):
                self.__tail=new_node
            
        else:
            node_before=self.find_node(data_before)
            if(node_before is not None):
                new_node.set_next(node_before.get_next()) 
                node_before.set_next(new_node)   
                if(new_node.get_next() is None):       
                    self.__tail=new_node
            else:
                print(data_before,"is not present in the Linked list")
    
    def display(self):
        temp=self.__head
        while(temp is not None):
            print(temp.get_data())
            temp=temp.get_next()     
    
    
    def find_node(self,data):
        temp=self.__head
        while(temp is not None):
            if(temp.get_data()==data):
                return temp
            temp=temp.get_next()    
        return None
    
    def delete(self,data):
        node=self.find_node(data)
        if(node is not None):
            if(node==self.__head):
                if(self.__head==self.__tail):
                    self.__tail=None
                self.__head=node.get_next()
            else:
                temp=self.__head
                while(temp is not None):
                    if(temp.get_next()==node): 
                        temp.set_next(node.get_next())    
                        if(node==self.__tail):
                            self.__tail=temp
                        node.set_next(None)
                        break
                    temp=temp.get_next()    
        else:
            print(data,"is not present in Linked list")
			
    #You can use the below _str_() to print the elements of the DS object while debugging        
    def _str_(self):
        temp=self.__head
        msg=[]
        while(temp is not None):
            msg.append(str(temp.get_data()))
            temp=temp.get_next()
        msg=" ".join(msg)
        msg="Linkedlist data(Head to Tail): "+ msg
        return msg


def find_nth_element(list1,n):
    temp = list1.get_head()
    count = 1
    while temp is not None:
        if count == n:
            return temp.get_data()
        temp = temp.get_next()
        count += 1
    return None

    

list1=LinkedList()
list1.add("Mysore")
list1.add("Chennai")
list1.add("Pune")
list1.add("Chandigarh")
list1.add("Hyderabad")
list1.add("Trivandrum")
list1.add("Jaipur")
list1.add("Bhubaneswar")
result=find_nth_element(list1,2)
print("The nth element is:",result)