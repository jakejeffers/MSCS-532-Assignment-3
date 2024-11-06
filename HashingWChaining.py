import random

class HashTable:
    def __init__(self, size=10):
        # Initialize the hash table with a fixed number of buckets
        self.size = size
        self.table = [[] for _ in range(size)]
        # Choose random coefficients for the hash function to mimic universal hashing
        self.a = random.randint(1, size - 1)
        self.b = random.randint(0, size - 1)
        self.p = self.next_prime(2 * size)  # Use a prime number greater than the table size

    def next_prime(self, n):
        # A helper method to find the next prime number greater than or equal to n
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
        # A universal hashing function: (a * key + b) % p % table_size
        return ((self.a * hash(key) + self.b) % self.p) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        # Check if the key already exists, and if so, update its value
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        # Otherwise, insert the new key-value pair
        self.table[index].append([key, value])

    def search(self, key):
        index = self.hash_function(key)
        # Search for the key in the bucket
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None  # Key not found

    def delete(self, key):
        index = self.hash_function(key)
        # Look for the key in the bucket and remove it if found
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return True  # Deletion successful
        return False  # Key not found

    def __str__(self):
        # Display the hash table for debugging purposes
        table_str = ""
        for i, bucket in enumerate(self.table):
            table_str += f"Bucket {i}: {bucket}\n"
        return table_str

# Example usage:
hash_table = HashTable(size=7)

# Insert key-value pairs
hash_table.insert("apple", 100)
hash_table.insert("banana", 200)
hash_table.insert("grape", 300)

print("Hash Table after insertions:")
print(hash_table)

# Search for values
print("Search 'apple':", hash_table.search("apple"))  # Output: 100
print("Search 'banana':", hash_table.search("banana"))  # Output: 200

# Delete a key-value pair
hash_table.delete("banana")
print("Hash Table after deletion of 'banana':")
print(hash_table)

# Attempt to search for a deleted key
print("Search 'banana':", hash_table.search("banana"))  # Output: None
