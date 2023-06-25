class node:
    def __init__(self,value):
        self.value = value
        self.next = None
class Linkedlist:
    def push(self,head,value):
        newnode = node(value)
        temp=head
        while temp.next != None:
            temp=temp.next
        temp.next = newnode
    def pushatposition(self,head,value,pos):
        newnode = node(value)
        prev = None
        curr = head
        while pos!=0:
            prev = curr
            curr = curr.next
            pos = pos - 1
        prev.next = newnode
        newnode.next = curr
    def pushathead(self,head,value):
        newnode = node(value)
        temp=head
        newnode.next = temp
        head = newnode
        return head
    def prints(self,head):
        temp=head
        while temp!= None:
            print(temp.value,end = '->')
            temp=temp.next
obj = Linkedlist()
head = node(10)
obj.push(head,20)
obj.push(head,30)
obj.pushatposition(head,23,1)
obj.push(head,45)
obj.prints(head)
print()
head = obj.pushathead(head,6000)
obj.prints(head)
