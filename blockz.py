import hashlib as hasher
import datetime as date

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        sha.update(f"{self.index}{self.timestamp}{self.data}{self.previous_hash}")
        return sha.hexdigest()

def create_genesis_block():
    return Block(0, date.datetime.now(), "Genesis Block", "0")

def next_block(previous_block):
    this_index = previous_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = f"Block {this_index} saying hello!"
    this_hash = previous_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)
