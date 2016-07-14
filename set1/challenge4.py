"""The module implements solution to challenge4(level1) of matasano crypto challenges."""

from challenge3 import break_single_char_xor


def read_file(filename):
    """Read file and return the contents."""
    with open(filename, 'r') as file_handle:
        list_of_hex_strings = file_handle.read().split('\n')
    return list_of_hex_strings


def get_input_string_into_program(hex_string_input):
    """Get input hex string and return utf-8 string."""
    # In python 3, you have byte strings and unicode stings
    # Always make a unicode sandwich, bytes(input)->unicode(inside the program)->bytes(output)
    # If this confuses you, watch this excellent talk by Ned Batchelder
    # https://www.youtube.com/watch?v=sgHbC6udIqc
    byte_string = bytes.fromhex(hex_string_input)
    # The input file in this case is hex representation of a latin-1 encoded file, which is not cool as they should be either calling it out explicitly or just sticking to unicode
    utf_string = byte_string.decode('latin-1')
    return utf_string


def main():
    """The main function."""
    list_of_hex_strings = read_file('challenge4_ciphertext.txt')
    list_of_results = []
    for hex_string in list_of_hex_strings:
        input_string = get_input_string_into_program(hex_string)
        list_of_results_for_input = break_single_char_xor(input_string)
        for item in list_of_results_for_input:
            list_of_results.append(item)

    sorted_results_list = sorted(list_of_results, key=lambda x: x.score)
    print("Top 5 most likely results")
    for result in sorted_results_list[:5]:
        print(result)

if __name__ == '__main__':
    main()
