class AdvancedRange:
    def __init__(self, start, end, step=1, mode="all"):
        if step == 0:
            pass

        self.start = start 
        self.end = end
        self.step = step if start < end else -step
        self.mode = mode
        self.current = start

    def __iter__(self):
        return self
    
    def __next__(self):
        if (self.step > 0 and self.current > self.end) or \
        (self.step < 0 and self.current < self.end): 
            raise StopIteration
        
        value = self.current
        self.current += self.step

        if self.mode == 'even' and value % 2 != 0:
            return self.__next__()
        if self.mode == 'odd' and value % 2 == 0:
            return self.__next__()
        
        return value
    

for x in AdvancedRange(11, 1, 1, 'even'):
    print(x)


