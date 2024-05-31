import cpu
import memory_bus
import isa

def print_menu():
    print("CPU Simulation Menu:")
    print("1. Load Memory Bus Initialization File")
    print("2. Load Instruction File")
    print("3. Execute Instructions")
    print("4. Print CPU State")
    print("5. Print Cache State")
    print("6. Print Memory Bus State")
    print("7. Exit")
    print()

def main():
    cpu_instance = cpu.CPU()
    memory_bus_instance = memory_bus.MemoryBus()
    
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            filename = input("Enter memory initialization file name: ")
            memory_bus_instance.initialize_memory(filename)
        elif choice == "2":
            filename = input("Enter instruction file name: ")
            cpu_instance.load_instructions(filename)
        elif choice == "3":
            cpu_instance.execute()
        elif choice == "4":
            cpu_instance.print_state()
        elif choice == "5":
            cpu_instance.cache.print_state()
        elif choice == "6":
            memory_bus_instance.print_state()
        elif choice == "7":
            print('CPU OFF')
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    print(""" 
CPU SIMULATOR
------------------------------
By Tynip
------------------------------  
    """)
    main()
