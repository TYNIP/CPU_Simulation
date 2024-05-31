class MemoryBus:
    def __init__(self):
        self.memory = {}
    
    def initialize_memory(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                address, value = line.split()
                self.memory[int(address, 16)] = int(value, 16)
        print("Memory initialized successfully.")
        print()
    
    def load(self, address):
        return self.memory.get(address, 0)
    
    def store(self, address, value):
        self.memory[address] = value
    
    def print_state(self):
        print()
        print("Memory Bus State:")
        for address, value in self.memory.items():
            print(f"Address {hex(address)}: {hex(value)}")
        print()
