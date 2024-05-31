# CPU SIMULATOR
CS104: Computer Architecture Project

## Project Overview

This project is a Python-based simulation of a CPU that mimics the basic functionalities of a central processing unit (CPU), cache, and memory bus. The simulator can execute a simplified Instruction Set Architecture (ISA) that includes MIPS-like instructions. Users can interact with the CPU, load instructions and memory initialization values from files, execute the instructions, and inspect the state of the CPU, cache, and memory bus. The repository provide already example files "memory_init.txt" and "instructions.txt"

## Features
1. **CPU Simulation**: Simulates a CPU with registers, a program counter (PC), and instruction execution capabilities.
2. **Cache Simulation**: Simulates a simple cache with enable/disable and flush functionalities.
3. **Memory Bus Simulation**: Simulates memory operations with the ability to initialize memory from a file.
4. **Instruction Set Architecture (ISA)**: Supports a simplified set of MIPS-like instructions.
5. **User Interaction**: Provides a menu for user interaction to load files, execute instructions, and print the state of the CPU, cache, and memory bus.

## Supported Instructions

| Instruction | Operand | Meaning |
|-------------|---------|---------|
| ADD         | Rd, Rs, Rt | Rd <- Rs + Rt |
| ADDI        | Rt, Rs, imm | Rt <- Rs + imm |
| SUB         | Rd, Rs, Rt | Rd <- Rs - Rt |
| SLT         | Rd, Rs, Rt | If (Rs < Rt) then Rd <- 1 else Rd <- 0 |
| BNE         | Rs, Rt, offset | If (Rs not equal Rt) then PC <- (PC + 4) + offset * 4 |
| J           | target | PC <- target * 4 |
| JAL         | target | R7 <- PC + 4; PC <- target * 4 |
| LW          | Rt, offset(Rs) | Rt <- MEM[Rs + offset] |
| SW          | Rt, offset(Rs) | MEM[Rs + offset] <- Rt |
| CACHE       | code | code = 0 (Cache off), code = 1 (Cache on), code = 2 (Flush cache) |
| HALT        | | Terminate execution |

## Project Structure

- `main.py`: Main entry point for the simulation, providing the user menu.
- `cpu.py`: Defines the CPU class and its functionalities.
- `isa.py`: Contains the instruction set architecture and the execution logic for each instruction.
- `cache.py`: Defines the Cache class and its functionalities.
- `memory_bus.py`: Defines the MemoryBus class and its functionalities.

## Usage

### Running the Simulation

1. **Clone the Repository**

   ```sh
   git clone https://github.com/tynip/CPU_Simulator.git
   cd CPU_Simulator

2. **Prepare Input Files**
- Memory Initialization File: Create a file (example: memory_init.txt) with memory address-value pairs.

    ```sh
    0x0 0x5
    0x4 0xA

- Instruction File: Create a file (example: instructions.txt) with the instructions to be executed in MIPS Assembly Language

    ```sh
    ADDI R1, R0, 5
    ADDI R2, R0, 10
    ADD R3, R1, R2
    SUB R4, R3, R1
    SLT R5, R1, R2
    BNE R1, R2, 1
    J 2
    LW R6, 0(R0)
    SW R6, 4(R0)
    CACHE 2
    HALT

3. **Run the Simulator**
    ```sh
    python main.py

4. **Interact with the Simulator**
Follow the on-screen menu to interact with the simulator:
- Load memory initialization file.
- Load instruction file.
- Execute instructions.
- Print the state of the CPU, cache, and memory bus.
- Exit the simulator.

### Usage Example
```sh
    $ python main.py
    CPU Simulation Menu:
    1. Load Memory Bus Initialization File
    2. Load Instruction File
    3. Execute Instructions
    4. Print CPU State
    5. Print Cache State
    6. Print Memory Bus State
    7. Exit
    Enter your choice: 1
    Enter memory initialization file name: memory_init.txt
    Memory initialized successfully.
    CPU Simulation Menu:
    1. Load Memory Bus Initialization File
    2. Load Instruction File
    3. Execute Instructions
    4. Print CPU State
    5. Print Cache State
    6. Print Memory Bus State
    7. Exit
    Enter your choice: 2
    Enter instruction file name: instructions.txt
    Instructions loaded successfully.
    CPU Simulation Menu:
    1. Load Memory Bus Initialization File
    2. Load Instruction File
    3. Execute Instructions
    4. Print CPU State
    5. Print Cache State
    6. Print Memory Bus State
    7. Exit
    Enter your choice: 3
    Executing instruction: ADDI R1, R0, 5
    Executing instruction: ADDI R2, R0, 10
    Executing instruction: ADD R3, R1, R2
    Executing instruction: SUB R4, R3, R1
    Executing instruction: SLT R5, R1, R2
    Executing instruction: BNE R1, R2, 1
    Executing instruction: J 2
    Executing instruction: LW R6, 0(R0)
    Executing instruction: SW R6, 4(R0)
    Executing instruction: CACHE 2
    HALT instruction encountered. Returning to menu.
    CPU Simulation Menu:
    1. Load Memory Bus Initialization File
    2. Load Instruction File
    3. Execute Instructions
    4. Print CPU State
    5. Print Cache State
    6. Print Memory Bus State
    7. Exit
    Enter your choice: 4
    CPU State:
    PC: 11
    Registers:
    R0: 0
    R1: 5
    R2: 10
    R3: 15
    R4: 10
    R5: 1
    R6: 5
    R7: 0
    ...
```

## Considerations
- Project with academic and practical purposes.