class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, key):
        # Sum of the Unicode code points of every character
        total = 0
        for char in key:
            total += ord(char)
        return total

    def add(self, key, value):
        hash_value = self.hash(key)
        # Create the inner dictionary the first time this hash appears
        if hash_value not in self.collection:
            self.collection[hash_value] = {}
        # Store the pair inside it (keys with the same hash share it)
        self.collection[hash_value][key] = value

    def remove(self, key):
        hash_value = self.hash(key)
        # Only act if both the hash and the exact key exist
        if hash_value in self.collection and key in self.collection[hash_value]:
            del self.collection[hash_value][key]
            # Drop the inner dictionary when it becomes empty
            if not self.collection[hash_value]:
                del self.collection[hash_value]

    def lookup(self, key):
        hash_value = self.hash(key)
        # .get returns None instead of raising an error when something is missing
        return self.collection.get(hash_value, {}).get(key)

ht = HashTable()

print(ht.hash('golf'))          # expected: 424

ht.add('rose', 'flower')
print(ht.collection)            # expected: {441: {'rose': 'flower'}}

ht.add('fcc', 'coding')
ht.add('cfc', 'chemical')
print(ht.collection[300])       # expected: {'fcc': 'coding', 'cfc': 'chemical'}

print(ht.lookup('rose'))        # expected: flower
print(ht.lookup('nothing'))     # expected: None

ht.remove('fcc')
print(ht.lookup('cfc'))         # expected: chemical (still there)
print(ht.lookup('fcc'))         # expected: None
ht.remove('nothing')            # expected: no error