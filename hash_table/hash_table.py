# Initialize amount of hashes in the table
MAX_HASH_TABLE_SIZE = 4096 

def get_index(data_list, string):
    """Hashing algorithm that converts strings into numeric list indices"""
    # Variable to store the result (is updated after each iteration)
    result = 0

    for char in string:
        # Convert the char to a number using ord
        num = ord(char)
        # Update the result by adding the number
        result += num

    # Initialize the index of the list by taking the remainder of the result
    # by the length of the original list(data_list)
    list_index = result % len(data_list)
    return list_index

# Testing for get_index function

# Create an empty hash table
data_list2 = [None] * MAX_HASH_TABLE_SIZE
# Insert a key-value pair for the key 'listen'
data_list2[get_index(data_list2, 'listen')] = ('listen', 99)


def get_valid_index(data_list, key):
    """Handles collisons using linear probing"""
    # Initialize an index that is got from the get_index function
    idx = get_index(data_list, key)

    # Keep looping until breaking or returning
    while True:
        # Get the key-value pair which is stored at the idx
        kv = data_list[idx]

        # If kv is None (meaning there was no key-value pair) then return the index
        if kv is None:
            return idx
    
        # If the stored key matches the given key then return the index
        k, v = kv 
        if k == key:
            return idx
        
        # Move to the next index
        idx += 1

        # Go back to the start if it has reached the end of the array
        if idx == len(data_list):
            idx = 0

class BasicHashTable:
    """Class that represents a basic hash table"""
    def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
        #  Create a list of size `max_size` with all values set to None
        self.data_list = [None] * max_size

    # Inserts a hash which contains a key and value 
    def insert(self, key, value):
        # Find the index for the key using get_index
        idx = get_index(self.data_list, key)
        
        # Store the key-value pair at the corresponding index
        self.data_list[idx] = (key, value)
    
    # Finds a hashes value
    def find(self, key):
        # Find the index for the key using get_index
        idx = get_index(self.data_list, key)
        
        # Retrieve the data stored at the index
        kv = self.data_list[idx]
        
        # Return the value if found, else return None
        if kv is None:
            return None
        else:
            key, value = kv
            return value
    
    # Updates each hashes key and value
    def update(self, key, value):
        # Find the index for the key using get_index
        idx = get_index(self.data_list, key)
        
        # Store the new key-value pair at the corresponding index 
        self.data_list[idx] = (key, value)

    # List each hashes key and value at a specific index
    def list_all(self):
        # Extract the corresponding key and value from each hash 
        return [kv[0] for kv in self.data_list if kv is not None]
    
# Testing for BasicHashTable class

# Create an instance
basic_table = BasicHashTable(max_size=1024)
# Test insert function 
basic_table.insert('Aakash', '9999999999')
basic_table.insert('Hemanth', '8888888888')
basic_table.insert('listen', 99)
basic_table.insert('silent', 200)
    
class ProbingHashTable:
    """Represents a hash table protected from collison via using the get_valid_index function that uses linear probing"""
    def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
        # Create a data list that is size of MAX_HASH_TABLE_SIZE which all values set to None
        self.data_list = [None] * max_size

    # Function that inserts a hash into the table
    def insert(self, key, value):
        # Find the index for the key using get_valid_index function
        idx = get_valid_index(self.data_list, key)

        # Store the key, value pair at the right index
        self.data_list[idx] = (key, value)

    # Function that searches for a hash in the table
    def find(self, key):
        # Find the index for the key using get_valid_index function
        idx = get_valid_index(self.data_list, key)

        # Retrive the key-value pair stored at the index/hash
        kv = self.data_list[idx]

        # Return the value of the key-value pair if found, else return None
        return None if kv is None else kv[1]
    
    # Function that updates a hash
    def update(self, key, value):
        # Find the index for the key using the get_valid_index function
        idx = get_valid_index(self.data_list, key)

        # Store the key-value pair at the right index
        self.data_list[idx] = (key, value)

    # List all of the hashes currently in the table
    def list_all(self):
        # Extract the key from every key-value pair
        return [kv[0] for kv in self.data_list if kv is not None]
    
# Testing for ProbingHashTable Class
probing_table = ProbingHashTable()
# Insert a value
probing_table.insert('listen', 99)
# Insert a colliding key
probing_table.insert('silent', 200)
    
class HashTable:
    """Hash table that implements dictionaries"""
    def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
        # Initialize the table as a list of None values set to the max size
        self.data_list = [None] * max_size

    # Hash function that hashes a key
    def get_valid_index(self, key):
        max_size = MAX_HASH_TABLE_SIZE
        idx = hash(key) % max_size
        return idx
    
    # Uses __getitem__ & __setitem to use indexing syntax to grab values of keys 
    def __getitem__(self, key):
        # Finds the valid index/hash
        idx = self.get_valid_index(key)

        # Gets the key-value pair assocaited with the hash
        kv = self.data_list[idx]

        # Returns None if there is no key-pair else, returns the value
        return None if kv is None else kv[1]
    
    def __setitem__(self, key, value):
        # Grabs the hash/index of a key
        idx = self.get_valid_index(key)
        # Initializes an index correlating to the hash to be the key-value pair
        self.data_list[idx] = (key, value)
    
    # Iterates through the table (same purpose for list_all from previous classes)
    def __iter__(self):
        return (x for x in self.data_list if x is not None)
    
    # Returns the number of key-value pairs in the hash table
    def __len__(self):
        return len[(x for x in self)]
    
    def __repr__(self):
        from textwrap import indent
        pairs = [indent("{} : {}".format(repr(kv[0]), repr(kv[1])), '  ') for kv in self]
        return "{\n" + "{}".format(',\n'.join(pairs)) + "\n}"
    
    def __str__(self):
        return repr(self)

# Testing for HashTable Class
table = HashTable()

# Insert some key-value pairs
table['a'] = 1
table['b'] = 34

# Update a value
table['a'] = 99

if list(table) == [('a', 99), ('b', 34)]:
    print("True")