class MyQueue(object):

    def __init__(self):
        self.s1=[]
        self.s2=[]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        while self.s1: #until elements are there in s1 stack
            self.s2.append(self.s1.pop()) #first pop element from s1 and then append the same in s2 

        self.s1.append(x) #add the element to s1

        while self.s2: #move the elements from s2 to s1
            self.s1.append(self.s2.pop())
   
    def pop(self):
        """
        :rtype: int
        """
        return self.s1.pop()

    def peek(self):
        """
        :rtype: int
        """
        return self.s1[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.s1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()