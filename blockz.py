import hashlib as hasher
import datetime as date


# ---------------------------------------------------------------#
# --- Define the essential building blocks of our blockchain --- #
# ---------------------------------------------------------------#

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
        # encoding to UTF-8 is necessary for hasher to work properly
        sha.update(f"{self.index}\
                    {self.timestamp}\
                    {self.data}\
                    {self.previous_hash}".encode('utf-8'))

        return sha.hexdigest()


def create_genesis_block():
    """creates the Block that starts the chain without previous hash as input.

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


# -----------------------------------------------#
# --- Create our blockchain, genesis and all --- #
# -----------------------------------------------#

# our tiny blockchain will just be a python list
# creating the genesis block to begin the blockchain
blockchain = [create_genesis_block()]
previous_block = blockchain[0]
print(f"--------------------- TinyBlockchain initiated ---------------------")
print(f"Genesis Block #{previous_block.index} now exists.")
print(f"Hash: {previous_block.hash}\n")

num_of_blocks_to_add = 42  # could be anything

# adding blocks to the chain
for block in range(num_of_blocks_to_add):
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    print(f"Block {block_to_add.index} joined the blockchain.")
    print(f"Hash: {block_to_add.hash}\n")
