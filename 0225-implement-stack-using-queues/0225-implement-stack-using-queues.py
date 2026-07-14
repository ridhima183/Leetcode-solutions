from collections import deque
class MyStack(object):

    def __init__(self, size=100):
        self.q1=deque()
        self.q2=deque()
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q2.append(x) #append the element into q2
        while self.q1: #iterate through every element in q1
            self.q2.append(self.q1.popleft()) #move elements from q1 to q2 
        self.q1, self.q2 = self.q2, self.q1 #swap q1 and q2

    def pop(self):
        """
        :rtype: int
        """
        return self.q1.popleft()
    def top(self):
        """
        :rtype: int
        """
        return self.q1[0]
        
    def empty(self):
        """
        :rtype: bool
        """
        return len(self.q1) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()