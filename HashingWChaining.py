import random
import time

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.a = random.randint(1, size - 1)
        self.b = random.randint(0, size - 1)
        self.p = self.next_prime(2 * size)

    def next_prime(self, n):
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True

        while not is_prime(n):
            n += 1
        return n

    def hash_function(self, key):
        return ((self.a * hash(key) + self.b) % self.p) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def search(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        index = self.hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return True
        return False

# Function to measure the time of operations
def measure_time(hash_table, operation, *args):
    start_time = time.time()
    result = operation(*args)
    end_time = time.time()
    return end_time - start_time, result

# Function to perform the benchmark
def run_benchmark(size, num_operations):
    hash_table = HashTable(size)

    # Insert Benchmark
    insert_time = 0
    for i in range(num_operations):
        key = f"key_{i}"
        value = random.randint(1, 1000)
        time_taken, _ = measure_time(hash_table, hash_table.insert, key, value)
        insert_time += time_taken

    # Search Benchmark
    search_time = 0
    for i in range(num_operations):
        key = f"key_{i}"
        time_taken, _ = measure_time(hash_table, hash_table.search, key)
        search_time += time_taken

    # Delete Benchmark
    delete_time = 0
    for i in range(num_operations):
        key = f"key_{i}"
        time_taken, _ = measure_time(hash_table, hash_table.delete, key)
        delete_time += time_taken

    return insert_time, search_time, delete_time

# Run the benchmark for different table sizes and number of operations
sizes = [10, 50, 100, 500, 1000]
num_operations = 1000  # Number of operations to test

for size in sizes:
    insert_time, search_time, delete_time = run_benchmark(size, num_operations)
    print(f"Size: {size}")
    print(f"Insert time: {insert_time:.6f} seconds")
    print(f"Search time: {search_time:.6f} seconds")
    print(f"Delete time: {delete_time:.6f} seconds")
    print("-" * 40)
