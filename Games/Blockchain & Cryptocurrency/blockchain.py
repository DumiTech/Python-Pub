def lightnin_hash(data):
    return data + '^*^'

# overall blochain relation:


class Block:  # block acts like a storage unit
    def __init__(self, data, hash, last_hash):
        # specifies what the block is soaring (tr: avant, crestere)
        self.data = data
        self.hash = hash  # unique value generated for the block based on all of the blocks data in order to properly generate the hash => you need a cryptographic function
        self.last_hash = last_hash  # creates the link between blocks in the blockchain


class Blockchain:
    def __init__(self):
        genesis = Block('gen_data', 'gen_hash', 'gen_last_hash')

        # the blockchain will create a list of block objects that's held in this chain list
        self.chain = [genesis]
        # every new block will be based on a prior block
        # the very first block: starts with a genesis block (initial hardcoded block created purely to allow the first real add a new block)

    def add_block(self, data):
        last_hash = self.chain[-1].hash
        hash = lightnin_hash(data + last_hash)
        block = Block(data, hash, last_hash)

        self.chain.append(block)


foo_blockchain = Blockchain()
foo_blockchain.add_block('one')
foo_blockchain.add_block('two')
foo_blockchain.add_block('three')

for block in foo_blockchain.chain:
    print(block.__dict__)