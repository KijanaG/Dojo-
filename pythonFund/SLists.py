class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class SList:
    def __init__(self):
        self.head = None
    def addnode(self, val):
        node = Node(val)
        if self.head == None:
            self.head = node
        else:
            runner = self.head
            while runner.next != None:
                runner = runner.next
            runner.next = node
    def removenode(self, value):
        runner = self.head
        if runner.val == value:
            self.head = runner.next
            return
        while runner.next.val != value:
            runner = runner.next
        runner.next = runner.next.next
    def printAllValues(self, msg=""):
        runner = self.head
        # val = Node(runner)
        print("\n\nhead points to ", self.head)
        print("Printing the values in the list ---", msg,"---")
        while(runner.next != None):
            print(runner, runner.val)
            runner = runner.next        
        print(runner, runner.val)

List = SList()
List.addnode(4)
List.addnode(3)
List.addnode(8)
List.addnode(95)
List.addnode(100)
List.addnode(18)
List.addnode(1)
List.removenode(1)
List.removenode(3)
List.removenode(4)
List.printAllValues("The Matrix")


