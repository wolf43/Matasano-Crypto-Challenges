"""The module implements solution to challenge2(level1) of matasano crypto challenges."""
# One way is just use the ^ and feed the hex. Python has ability to xor hex
# print hex(0x1c0111001f010100061a024b53535009181c^0x686974207468652062756c6c277320657965)
# But we will assume the hex came in as a string


def get_input_string_into_program(hex_string_input):
    """Get input hex string and return utf-8 string."""
    # In python 3, you have byte strings and unicode stings
    # Always make a unicode sandwich, bytes(input)->unicode(inside the program)->bytes(output)
    # If this confuses you, watch this excellent talk by Ned Batchelder
    # https://www.youtube.com/watch?v=sgHbC6udIqc
    byte_string = bytes.fromhex(hex_string_input)
    utf_string = byte_string.decode('utf-8')
    return utf_string


def xor_strings(string_1, string_2):
    """The function will return xor of 2 stings passed as arguments."""
    # Please refer to ord, chr and zip in python docs if this doesn't make sense
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(string_1, string_2))


def main():
    """The main function."""
    # Get first input and convert to a python3 utf sting
    hex_string_1 = '1c0111001f010100061a024b53535009181c'
    string_1 = get_input_string_into_program(hex_string_1)
    # Get second input and convert to python3 utf string
    hex_string_2 = '686974207468652062756c6c277320657965'
    string_2 = get_input_string_into_program(hex_string_2)
    # XOR the two strings
    xor_result = xor_strings(string_1, string_2)
    # Get the exptected result and convert to python3 utf string
    expected_hex_result = '746865206b696420646f6e277420706c6179'
    string_exptected_result = get_input_string_into_program(expected_hex_result)

    if xor_result == string_exptected_result:
        print("It matches: Challenge 2 complete")

if __name__ == "__main__":
    main()
