def execute_instruction(cpu, instruction):
    parts = instruction.split()
    opcode = parts[0]
    
    if opcode == "ADD":
        rd = int(parts[1][1:].replace(',', ''))
        rs = int(parts[2][1:].replace(',', ''))
        rt = int(parts[3][1:].replace(',', ''))
        cpu.registers[rd] = cpu.registers[rs] + cpu.registers[rt]
    
    elif opcode == "ADDI":
        rt = int(parts[1][1:].replace(',', ''))
        rs = int(parts[2][1:].replace(',', ''))
        imm = int(parts[3])
        cpu.registers[rt] = cpu.registers[rs] + imm
    
    elif opcode == "SUB":
        rd = int(parts[1][1:].replace(',', ''))
        rs = int(parts[2][1:].replace(',', ''))
        rt = int(parts[3][1:].replace(',', ''))
        cpu.registers[rd] = cpu.registers[rs] - cpu.registers[rt]
    
    elif opcode == "SLT":
        rd = int(parts[1][1:].replace(',', ''))
        rs = int(parts[2][1:].replace(',', ''))
        rt = int(parts[3][1:].replace(',', ''))
        cpu.registers[rd] = 1 if cpu.registers[rs] < cpu.registers[rt] else 0
    
    elif opcode == "BNE":
        rs = int(parts[1][1:].replace(',', ''))
        rt = int(parts[2][1:].replace(',', ''))
        offset = int(parts[3])
        if cpu.registers[rs] != cpu.registers[rt]:
            cpu.pc += offset * 4
    
    elif opcode == "J":
        target = int(parts[1])
        cpu.pc = target * 4 - 4 
    
    elif opcode == "JAL":
        target = int(parts[1])
        cpu.registers[7] = cpu.pc + 4
        cpu.pc = target * 4 - 4 
    
    elif opcode == "LW":
        rt = int(parts[1][1:].replace(',', ''))
        offset, rs = parts[2].replace(')', '').split('(')
        offset = int(offset)
        rs = int(rs[1:])
        address = cpu.registers[rs] + offset
        value = cpu.cache.load(address)
        if value is None:
            value = cpu.memory_bus.load(address)
            cpu.cache.store(address, value)
        cpu.registers[rt] = value
    
    elif opcode == "SW":
        rt = int(parts[1][1:].replace(',', ''))
        offset, rs = parts[2].replace(')', '').split('(')
        offset = int(offset)
        rs = int(rs[1:])
        address = cpu.registers[rs] + offset
        value = cpu.registers[rt]
        cpu.memory_bus.store(address, value)
        cpu.cache.store(address, value)
    
    elif opcode == "CACHE":
        code = int(parts[1])
        if code == 0:
            cpu.cache.cache_enabled = False
        elif code == 1:
            cpu.cache.cache_enabled = True
        elif code == 2:
            cpu.cache.flush()
    
    elif opcode == "HALT":
        print("HALT instruction encountered. Returning to menu.")
        print()
        cpu.halted = True
