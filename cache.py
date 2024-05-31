class Cache:
    def __init__(self):
        self.cache_enabled = True
        self.data = {}
    
    def load(self, address):
        if self.cache_enabled and address in self.data:
            return self.data[address]
        else:
            return None
    
    def store(self, address, value):
        if self.cache_enabled:
            self.data[address] = value
    
    def flush(self):
        self.data = {}

    def print_state(self):
        print()
        print("Cache State:")
        print("Enabled:", self.cache_enabled)
        print("Data:", self.data)
        print()
