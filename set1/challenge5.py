"""The module implements solution to challenge5(level1) of matasano crypto challenges."""


def get_input_string_into_program(hex_string_input):
    """Get input hex string and return utf-8 string."""
    # In python 3, you have byte strings and unicode stings
    # Always make a unicode sandwich, bytes(input)->unicode(inside the program)->bytes(output)
    # If this confuses you, watch this excellent talk by Ned Batchelder
    # https://www.youtube.com/watch?v=sgHbC6udIqc
    byte_string = bytes.fromhex(hex_string_input)
    utf_string = byte_string.decode('utf-8')
    return utf_string


def xor_string_with_key(string_to_xor, key):
    """Function to xor string with key."""
    xor = [None] * len(string_to_xor)
    for i in range(len(string_to_xor)):
        # print('i:', i)
        j = i % len(key)
        # print('\tj:', j)
        xor[i] = chr(ord(string_to_xor[i]) ^ ord(key[j]))
    xor_s = ''.join(xor)
    return xor_s


def main():
    """The main function."""
    # s is the string we need to xor
    s = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = "ICE"
    correct_result = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"

    xor_string_key = xor_string_with_key(s, key)
    correct_result = get_input_string_into_program(correct_result)
    # print(correct_result)

    if correct_result == xor_string_key:
        print('It matches: Challange5 complete')


if __name__ == '__main__':
    main()
