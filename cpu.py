import cache
import isa
import memory_bus

class CPU:
    def __init__(self):
        self.registers = [0] * 32
        self.pc = 0
        self.instructions = []
        self.cache = cache.Cache()
        self.memory_bus = memory_bus.MemoryBus()
    
    def load_instructions(self, filename):
        with open(filename, 'r') as f:
            self.instructions = f.readlines()
        print("Instructions loaded successfully.")
        print()
    
    def execute(self):
        while self.pc < len(self.instructions):
            instruction = self.instructions[self.pc].strip()
            print(f"Executing instruction: {instruction}")
            isa.execute_instruction(self, instruction)
            if instruction.split()[0] != "J" and instruction.split()[0] != "JAL":
                self.pc += 1

    def print_state(self):
        print()
        print("CPU State:")
        print(f"PC: {self.pc}")
        print("Registers:")
        for i, reg in enumerate(self.registers):
            print(f"R{i}: {reg}")
        print()

