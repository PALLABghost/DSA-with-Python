class Dictionary:
    def __init__(self,size):
        self.size = size
        self.slot = [None] * self.size
        self.data = [None] * self.size

    def hash_function(self,key):
        return abs(hash(key)) % self.size   #hash use for string value convert into int format, abs for only positive value

    def rehash(self,old_hash):
        return (old_hash + 1) % self.size   #moduler by size,because while rehashing it should not cross
                                            # maximum index value
    def put(self,key,value):
        hash_value = self.hash_function(key)
        if self.slot[hash_value] is None:   #if index is empty then add the key and value.
            self.slot[hash_value] = key
            self.data[hash_value] = value
        else:
            if self.slot[hash_value] == key:    # if key already present just update new value
                self.data[hash_value] = value
            else:   #if index is not empty or different key present rehash the key and check for later position
                new_hashing_value = self.rehash(hash_value) # check for next index

                while self.slot[new_hashing_value] is not None and self.slot[new_hashing_value] != key: #new index
                    new_hashing_value = self.rehash(new_hashing_value)  #also is not empty or different key present, check next position

                if self.slot[new_hashing_value] is None:    #if new index empty then add all the key and value
                    self.slot[new_hashing_value] = key
                    self.data[new_hashing_value] = value
                else:           # if new index same key available then update the new value
                    self.data[new_hashing_value] = value
    def __setitem__(self, key, value):  # for use D1[key] = value
        self.put(key,value)

    def get(self,key):
        start_position = self.hash_function(key)    #store the starting index
        current_position = start_position
        while self.slot[current_position] is not None:  #we search from start position and is not empty then run the loop and check for every index
            if self.slot[current_position] == key:      #if start position only we found the key then return the data
                return self.data[current_position]
            current_position = self.rehash(current_position)    # if not found in start potion increase the index
            if current_position == start_position:       # if while searching we reached same start position then key not found
                return "Not Found"
        return "None wala Not Found"            # if while searching we found None then we exit from while loop and return None wala not found

    def __getitem__(self, key): # for use D1[key] give value of the key
        return self.get(key)

D1 = Dictionary(3)
#D1.put('python',45)
#D1.put('java', 60)
#D1.put('PHP', 90)
D1['python'] = 56
D1['java'] = 80
D1['php'] = 100
print(D1.slot)
print(D1.data)
print(D1['java'])
print(D1['c'])
