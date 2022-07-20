# Time and Space - For all functions

# O(1) in best case and O(n) in worst case Time Complexity
# O(1) in best case and O(n) in worst case Space Complexity

class Node(object):
    def __init__(self,key):
        self.k = key
        self.next = None
        
class MyHashSet:

    def __init__(self):
        self.array = [None for i in range(1000)]

    def getIndex(self,key):
        return key % 1000
    
    def getElement(self,key):
        index = self.getIndex(key)
        
        if self.array[index] == None:
            dummyNode = Node(-1)
            self.array[index] = dummyNode
            return dummyNode 
        currentNode = self.array[index]
        while currentNode.next != None:
            if(currentNode.next.k == key):
                return currentNode
            currentNode = currentNode.next
        return currentNode
    
    def add(self, key: int) -> None:
        currentNode = self.getElement(key)
        
        if currentNode.next == None:
            currentNode.next = Node(key)
        else:
            currentNode.next.k = key
        return
        

    def remove(self, key: int) -> None:
        currentNode = self.getElement(key)
        
        if(currentNode.next != None):
            currentNode.next = currentNode.next.next
        return 
    
    def contains(self, key: int) -> bool:
        currentNode = self.getElement(key)
        if (currentNode.next) == None:
            return False
        else:
            return True
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
