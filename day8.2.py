#lex_auth_0127667363049881603477

"""Queue"""
class Queue:
    def __init__(self,max_size):

        self.__max_size=max_size
        self._elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0

    def is_full(self):
        if(self.__rear==self.__max_size-1):
                return True
        return False

    def is_empty(self):
        if(self._front>self._rear):
            return True
        return False

    def enqueue(self,data):
        if(self.is_full()):
            print("Queue is full!!!")
        else:
            self.__rear+=1
            self._elements[self.__rear]=data

    def dequeue(self):
        if(self.is_empty()):
            print("Queue is empty!!!")
        else:
            data=self._elements[self._front]
            self.__front+=1
            return data

    def display(self):
        for index in range(self.__front, self.__rear+1):
            print(self._elements[index])


    def get_max_size(self):
        return self.__max_size

    #You can use the below _str_() to print the elements of the DS object while debugging
    def _str_(self):
        msg=[]
        index=self.__front
        while(index<=self.__rear):
            msg.append((str)(self.__elements[index]))
            index+=1
        msg=" ".join(msg)
        msg="Queue data(Front to Rear): "+msg
        return msg

"""Stack"""
class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self._elements=[None]*self._max_size
        self.__top=-1

    def is_full(self):
        if(self._top==self._max_size-1):
            return True
        return False

    def is_empty(self):
        if(self.__top==-1):
            return True
        return False

    def push(self,data):
        if(self.is_full()):
            print("The stack is full!!")
        else:
            self.__top+=1
            self._elements[self._top]=data

    def pop(self):
        if(self.is_empty()):
            print("The stack is empty!!")
        else:
            data= self._elements[self._top]
            self.__top-=1
            return data

    def display(self):
        if(self.is_empty()):
            print("The stack is empty")
        else:
            index=self.__top
            while(index>=0):
                print(self.__elements[index])
                index-=1

    def get_max_size(self):
        return self.__max_size

    #You can use the below _str_() to print the elements of the DS object while debugging
    def _str_(self):
        msg=[]
        index=self.__top
        while(index>=0):
            msg.append((str)(self.__elements[index]))
            index-=1
        msg=" ".join(msg)
        msg="Stack data(Top to Bottom): "+msg
        return msg


def separate_boxes(box_stack):
    # Create a queue to store "Red" boxes
    red_queue = Queue(box_stack.get_max_size())
    temp_stack = Stack(box_stack.get_max_size())
    # Move all boxes from box_stack to temp_stack, enqueue "Red" boxes
    while not box_stack.is_empty():
        box = box_stack.pop()
        if box == "Red":
            red_queue.enqueue(box)
        else:
            temp_stack.push(box)
    # Restore non-red boxes back to box_stack
    while not temp_stack.is_empty():
        box_stack.push(temp_stack.pop())
    return red_queue

#Use different values for stack and test your program
box_stack=Stack(8)
box_stack.push("Red")
box_stack.push("Magenta")
box_stack.push("Yellow")
box_stack.push("Red")
box_stack.push("Orange")
box_stack.push("Green")
box_stack.push("White")
box_stack.push("Purple")
print("Boxes in the stack:")
box_stack.display()
result=separate_boxes(box_stack)
print()
print("Boxes in the stack after modification:")
box_stack.display()
print("Boxes in the queue:")
result.display()