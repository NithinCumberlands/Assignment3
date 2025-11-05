# Hash Table with Chaining Implementation

class HashTable:
    def __init__(self, size=10):
        # Initialize the table with given size and create empty chains (lists)
        self.size = size
        self.table = [[] for _ in range(size)]  # Each index holds a list for chaining

    def hash_function(self, key):
        # Simple hash function using modulo operator
        return hash(key) % self.size

    def insert(self, key, value):
        # Insert key-value pair into the hash table
        idx = self.hash_function(key)  # Get the index from the hash function
        # Check if the key already exists in the chain and update its value if so
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                self.table[idx][i] = (key, value)  # Update the value if key exists
                return
        # If key does not exist, append the key-value pair to the chain
        self.table[idx].append((key, value))

    def search(self, key):
        # Search for a key in the hash table and return its value if found
        idx = self.hash_function(key)
        # Iterate through the chain at the hashed index and check for the key
        for k, v in self.table[idx]:
            if k == key:
                return v
        return None  # If key is not found

    def delete(self, key):
        # Delete a key-value pair from the hash table
        idx = self.hash_function(key)
        # Look for the key in the chain and remove it if found
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                del self.table[idx][i]
                return
        print("Key not found")  # If key is not in the table

# Example Usage
if __name__ == "__main__":
    ht = HashTable(10)  # Create a hash table with 10 slots

    # Insert some key-value pairs
    ht.insert("name", "John")
    ht.insert("age", 30)
    ht.insert("city", "New York")
    
    # Search for some keys
    print("Search for 'name':", ht.search("name"))  # Should return 'John'
    print("Search for 'age':", ht.search("age"))    # Should return 30
    print("Search for 'country':", ht.search("country"))  # Should return None

    # Delete a key-value pair
    ht.delete("age")
    print("Search for 'age' after deletion:", ht.search("age"))  # Should return None

    # Re-insert a key with a new value
    ht.insert("age", 25)
    print("Search for 'age' after re-insertion:", ht.search("age"))  # Should return 25

    # Handle a collision (inserting multiple items with the same hash)
    ht.insert("city", "Los Angeles")
    ht.insert("state", "California")
    print("Search for 'city':", ht.search("city"))  # Should return 'Los Angeles'
