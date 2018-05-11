import hashlib as hasher
import datetime as date


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        """initializes a unique Block with the input data.

        Args:
            index (int): the Block's number
            timestamp (datetime): datetime of Block creation
            data (str, int, etc.): data value that this Block carries
            previous_hash (str): hash of the previous Block
        """
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        """creates a unique hash from Block's input variables.

        Returns:
            str: new unique Block hash
        """
        sha = hasher.sha256()
        sha.update(f"{self.index}{self.timestamp}{self.data}{self.previous_hash}")
        return sha.hexdigest()

def create_genesis_block():
    """creates the Block that starts the chain without a previous hash as input.

    Returns:
        Block: the genesis Block, the one and only.
    """
    return Block(0, date.datetime.now(), "Genesis Block", "0")

def next_block(previous_block):
    """creates the next block.

    Args:
        previous_block (Block): the previous block in the blockchain

    Returns:
        Block: new Block hashed with all the necessary spices.
    """
    this_index = previous_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = f"Block {this_index} saying hello!"
    this_hash = previous_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)
