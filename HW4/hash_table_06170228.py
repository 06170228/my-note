class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
        
class MyHashSet:
    def MD5(self,key):
        from Crypto.Hash import MD5
        h = MD5.new()
        h.update(key.encode("utf-8")) #告訴電腦我們要使用utf-8，而不是big5或其他方式
        h = int(h.hexdigest(),16)  #16進位轉10
        return h
        
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity  #[None,None,None,None,None]
       
    
    def add(self, key):
        key = self.MD5(key)
        index = key % self.capacity #key除以5的餘數有[0,1,2,3,4]
        node = ListNode(key)
        if self.data[index] == None:
            self.data[index] = node
        else:
            curr = self.data[index]
            
            if curr.next == None:
                if curr.val != key:
                    curr.next = node
            else:
                while curr.val != key and curr.next != None:
                    curr == curr.next
                if curr.val != key:
                    curr.next = node
        
            
    def remove(self, key):
        key = self.MD5(key)
        index = key % self.capacity
        if self.data[index] == None:
            return
        if self.data[index].val == key:
            self.data[index] = self.data[index].next
        else:
            curr = self.data[index]
            while curr.next:
                if curr.next.val == key:
                    curr.next = curr.next.next
                else:
                    curr = curr.next

        
    def contains(self, key):
        key = self.MD5(key)
        index = key % self.capacity
        curr = self.data[index]
        while curr:
            if curr.val == key:
                return True
            else:
                curr = curr.next
        return False #查詢不到這個值 回傳False
    
