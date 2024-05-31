def parse_register(register_str):
    return int(register_str[1:])

def parse_immediate(immediate_str):
    return int(immediate_str)

def parse_memory_address(address_str):
    offset, rs = address_str.split('(')
    offset = int(offset)
    rs = int(rs[1:-1])
    return offset, rs
