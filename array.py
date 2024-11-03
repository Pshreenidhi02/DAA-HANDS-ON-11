class DynamicArray:
    def __init__(self):
        self.capacity = 2  # Initial capacity of the array
        self.size = 0      # Current number of elements
        self.data = [0] * self.capacity  # Initialize array with fixed capacity

    def resize(self):
        
        self.capacity *= 2
        new_data = [0] * self.capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data

    def push_back(self, value):
        
        if self.size == self.capacity:
            self.resize()
        self.data[self.size] = value
        self.size += 1

    def pop_back(self):
        
        if self.size > 0:
            self.size -= 1

    def get(self, index):
        
        if 0 <= index < self.size:
            return self.data[index]
        raise IndexError("Index out of range")

    def get_size(self):
        return self.size

    def get_capacity(self):
        return self.capacity

# Example 
arr = DynamicArray()
arr.push_back(5)
arr.push_back(10)
arr.push_back(15)

print("Array elements:", [arr.get(i) for i in range(arr.get_size())])
print("Size:", arr.get_size(), "Capacity:", arr.get_capacity())

arr.pop_back()
print("After pop_back, Size:", arr.get_size())
