class MyLinkedList:
    class ListNode:
        def __init__(self, val, next=None):
            self.val = val
            self.next = next

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def _findNodeAtIndex(self, index, flag=None): 
        """ 
        flag=None, return i-th index
        flag=True return (i-1)th  index 
        
        if invalid index return False
        else: return node
        """
        if index < 0 or index > self.length-1:
            return False

        if flag: index -= 1 

        node = self.head
        for _ in range(index):
            node = node.next
        return node

    def get(self, index: int) -> int:
        node = self._findNodeAtIndex(index)
        if node:
            return node.val
        return -1

    def addAtHead(self, val: int) -> None:
        if self.head == None:
            self.head = self.ListNode(val)
            self.tail = self.head
        else:
            node = self.ListNode(val, next = self.head)
            self.head = node   
        self.length += 1

    def addAtTail(self, val: int) -> None:
        if self.head == None:
            self.head = self.ListNode(val)
            self.tail = self.head
        else:
            node = self.ListNode(val, next=None)
            self.tail.next = node
            self.tail = node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val) 
        elif index == self.length:
            self.addAtTail(val)
        else:
            node = self._findNodeAtIndex(index, True) 
            if node:
                new_node = self.ListNode(val, node.next)
                node.next = new_node
                self.length += 1

    def _RemoveAtHead(self):
        temp = self.head.next
        self.head.next = None
        self.head = temp
    
        self._isEmpty()

    def _RemoveAtTail(self):
        node = self._findNodeAtIndex(self.length-1, True)
        node.next = None
        self.tail = node
        
        self._isEmpty()


    def deleteAtIndex(self, index: int) -> None:
        node = self._findNodeAtIndex(index, True)
        if node:
            if self.length-1 == index:
                self._RemoveAtTail()
                return None
            elif index == 0:
                self._RemoveAtHead()
                return None
            
            temp = node.next
            node.next = node.next.next
            temp.next = None
            
            self._isEmpty()
    


    def _isEmpty(self):
        self.length -= 1
        if self.length <= 0:
            self.head = None
            self.tail = None





def test(op, input):
    obj = eval(f"{op[0]}()")
    for i in range(1, len(input)):
        if not input[i]:
            print(eval(f"obj.{op[i]}()"))
        elif len(input[i]) == 2:
            print(eval(f"obj.{op[i]}({input[i][0]},{input[i][1]})"))
        else:
            print(eval(f"obj.{op[i]}({input[i][0]})"))

# op = ["MyLinkedList", "addAtTail", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
op =["MyLinkedList","addAtHead","deleteAtIndex","addAtHead","addAtHead","addAtHead","addAtHead","addAtHead","addAtTail","get","deleteAtIndex","deleteAtIndex"]
input = [[],[2],[1],[2],[7],[3],[2],[5],[5],[5],[6],[4]]

# input = [[], [1], [3], [-1, 50], [1], [1], [1]]

test(op, input)

# addAtHead
# addAtTail
# addAtIndex
# deleteAtIndex
# get