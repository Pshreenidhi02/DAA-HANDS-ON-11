class DynamicArray:
    def __init__(self, initial_capacity=2):
        self.capacity = initial_capacity  
        self.size = 0                     # Number of elements in the array
        self.data = [None] * self.capacity  

    def resize(self):
        self.capacity *= 2                  
        new_data = [None] * self.capacity   
        for i in range(self.size):
            new_data[i] = self.data[i]      
        self.data = new_data                

    def add(self, value):
        if self.size == self.capacity:
            self.resize()                   
        self.data[self.size] = value        
        self.size += 1

    def get(self, index):
        if 0 <= index < self.size:
            return self.data[index]
        raise IndexError("Index out of range")

    def get_size(self):
        return self.size

    def get_capacity(self):
        return self.capacity



if __name__ == "__main__":
    arr = DynamicArray()

    
    for i in range(10):
        arr.add(i)
        print(f"Added {i}, Size: {arr.get_size()}, Capacity: {arr.get_capacity()}")

    
    try:
        for i in range(arr.get_size()):
            print(f"Element at index {i}: {arr.get(i)}")
    except IndexError as e:
        print(e)

    
    try:
        print(f"Element at index 20: {arr.get(20)}")
    except IndexError as e:
        print(e)

