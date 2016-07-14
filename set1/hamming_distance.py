"""This module contains functions dealing with hamming distance for Challange 6."""
from collections import namedtuple


def find_possible_key_size(ciphertext, max_key_len):
    """Find possible key sizes based on hamming distance calulation on ciphertext."""
    list_of_possible_keylengths = []
    possible_keylen = namedtuple('possible_keylength', ['keylength', 'hamming_distance'])
    for i in range(1, max_key_len + 1):
        key_length = i

        s1 = ciphertext[:i]
        s2 = ciphertext[i:i * 2]

        hamming_dist = (hamming_distance_bits(s1, s2)) / float(key_length)

        possible_keylength = possible_keylen(i, hamming_dist)
        # print(possible_keylength)
        list_of_possible_keylengths.append(possible_keylength)
    sorted_list_of_possible_keylengths = sorted(list_of_possible_keylengths, key=lambda x: x.hamming_distance)
    for i in sorted_list_of_possible_keylengths:
        print(i)
    # This gives us the possible keylengths based on hamming distance
    # This is actually just a waste of time, even with multiple iterations, the right keysize is ~ the 10 most probable size
    # So it is just easier to brute force for all key sizes and rely on frequency analysis on the plaintext for possible keys
    return sorted_list_of_possible_keylengths


def number_of_1_in_string(string):
    """Convert string to binary stream."""
    string_bin = ''.join(format(ord(x), 'b') for x in string)
    # Count the number of 1's in binary
    return string_bin.count("1")


def xor_strings(string1, string2):
    """Xor two string and return."""
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(string1, string2))


def hamming_distance_bits(string1, string2):
    """Find hamming distance between string1 and string2."""
    return number_of_1_in_string(xor_strings(string1, string2))

# print(hamming_distance_bits('this is a test', 'wokka wokka!!!'))
