class Array():
    def __init__(self,size=4):
        self.__size = size  # 记录容器大小
        self.__item = [None]*size  # 分配空间
        self.__length = 0
    
    def __setitem__(self,key,value):
        self.__item[key] = value
        self.__length += 1

    def __getitem__(self,key):
        return self.__item[key]
    
    def __len__(self):
        return self.__length
    
    def __iter__(self):
        for value  in self.__item:
            yield value

class Heap():
    def __init__(self):
        self.item = Array(8)
        self.count = 0
    
    def add(self,value):
        self.item[self.count] = value
        self.siftup(self.count)
        self.count += 1
    
    
    def siftup(self,index):
        if index > 0:
            parent = int((index-1)/2)
            if self.item[index] > self.item[parent]:
                self.item[index],self.item[parent] = self.item[parent],self.item[index]
                self.siftup(parent)
    
    def pop(self,index =0):
        if self.count <= 0:
            return None
        else:
            value = self.item[0]
            self.count -= 1
            self.item[0] = self.item[self.count]
            self.item[self.count] = None
            self.siftdown(0)
            return value
    def siftdown(self,index):
        left = index*2+1
        right = index*2+2

        largest = index
        if right < self.count:
            if self.item[right] > self.item[largest] and self.item[right]> self.item[left]:
                largest = right
            elif self.item[right] >self.item[largest] and self.item[right] < self.item[left]:
                largest = left
            elif self.item[right] < self.item[largest] and self.item[left] >self.item[largest]:
                largest = left
        elif left < self.count:
            if self.item[left] > self.item[largest]:
                largest = left
        if largest != index:
            self.item[index],self.item[largest] = self.item[largest],self.item[index]
            self.siftdown(largest)
if __name__ == "__main__":
    
    heap= Heap()
    heap.add(10)
    heap.add(15)
    heap.add(20)
    heap.add(30)
    heap.add(40)
    heap.add(18)

    for i in heap.item:
        if i:
            print(i)
    print('-'*30)
    print(heap.pop())
    print(heap.pop())
    print(heap.pop())
    print(heap.pop())
    print(heap.pop())
    print(heap.pop())
