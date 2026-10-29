class MinStack:

    def __init__(self):
        self.arr = []
        self.m = float('inf')
    def push(self, val: int) -> None:
        if self.arr:
            self.m = min(self.arr[-1][1], val)
            self.arr.append([val, self.m])
        else:    
            self.arr.append([val, val])
            self.m = val
        print(self.arr, self.m)
    def pop(self) -> None:
        self.arr.pop()
        print(f'after pop: {self.arr}')

    def top(self) -> int:
        return self.arr[-1][0]

    def getMin(self) -> int:
        return self.arr[-1][1]
