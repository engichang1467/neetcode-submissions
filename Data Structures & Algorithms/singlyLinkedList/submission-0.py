class LLNode:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = LLNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr_node = self.head
        counter = 0
        while curr_node:

            if counter == index:
                return curr_node.data

            counter += 1
            curr_node = curr_node.next
            
        return -1

    def insertHead(self, val: int) -> None:
        new_node = LLNode(val)
        new_node.next = self.head.next
        self.head.next = new_node

        if not new_node.next:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        new_node = LLNode(val)
        curr_node = self.tail

        curr_node.next = new_node
        self.tail = curr_node.next
        
    def remove(self, index: int) -> bool:
        curr_node = self.head
        counter = 0
        while counter < index and curr_node:
            counter += 1
            curr_node = curr_node.next

        if curr_node and curr_node.next:
            # if it's tail
            if curr_node.next == self.tail:
                self.tail = curr_node
            curr_node.next = curr_node.next.next
            return True
        
        return False
        

    def getValues(self) -> List[int]:
        res_arr = []
        curr_node = self.head.next

        while curr_node:
            res_arr.append(curr_node.data)
            curr_node = curr_node.next

        return res_arr
        
