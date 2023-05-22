if __name__ == "__main__":
    print("bit string start from 0 and |= operator")
    bit_string: int = 0
    print(f"initialization: {bin(bit_string)}")
    bit_string <<= 2
    print(f"shift         : {bin(bit_string)}")
    bit_string |= 0b00
    print(f"or operation  : {bin(bit_string)}")
    print()
    
    # | 연산을 해야 값들이 보존됨
    print("bit string start from 1 and |= operator")
    bit_string: int = 1
    print(f"initialization: {bin(bit_string)}")
    bit_string <<= 2
    print(f"shift         : {bin(bit_string)}")
    bit_string |= 0b00
    print(f"or operation  : {bin(bit_string)}")
    print()

    print("bit string start from 1 and &= operator")
    bit_string: int = 1
    print(f"initialization: {bin(bit_string)}")
    bit_string <<= 2
    print(f"shift         : {bin(bit_string)}")
    bit_string &= 0b00
    print(f"or operation  : {bin(bit_string)}")
    print()

    # OR opertor for 0b00 0b01 0b10 0b11
    print("bit string | (or) operation test")
    print(f"{bin(0b01)} | {bin(0b00)} = {bin(0b01 | 0b00)}")
    print(f"{bin(0b01)} | {bin(0b01)} = {bin(0b01 | 0b01)}")
    print(f"{bin(0b01)} | {bin(0b10)} = {bin(0b01 | 0b10)}")
    print(f"{bin(0b01)} | {bin(0b11)} = {bin(0b01 | 0b11)}")
