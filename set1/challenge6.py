"""The module implements solution to challenge6(level1) of matasano crypto challenges."""
import argparse
import base64
from collections import namedtuple
from challenge3 import break_single_char_xor, combined_score


def get_cl_arguments():
    """Get the command line arguments passed by user."""
    parser = argparse.ArgumentParser(prog='vigenere breaker', description='Break vigenere cipher')
    # print parser.prog  # Prints the name of the program(default sys.argv[0])
    parser.add_argument('-m', '--maxkeylength', default=40, type=int, nargs='?', help='Max keylength to try - default is 40 if no key passed')
    parser.add_argument('-i', '--path_to_ciphertext_file', required=True, help='Ciphertext file to break')
    args = parser.parse_args()
    return vars(args)['path_to_ciphertext_file'], vars(args)['maxkeylength']


def read_file(path_to_file):
    """Read file and return ciphertext."""
    with open(path_to_file, 'r') as file_handle:
        ciphertext = file_handle.read()
    return ciphertext


def splice_to_keylenght_strings(string, keylength):
    """Split a string into keylength number of splices."""
    splices = [None] * keylength
    for i in range(keylength):
        splices[i] = string[i:len(string):keylength]
    # This takes care of step 5 and 6 in a much simpler way :)
    return splices


def get_ciphertext_as_string(ciphertext_file):
    """Get the ciphertext in a string format."""
    ciphertext_b64 = read_file(ciphertext_file)
    ciphertext_bytes = base64.b64decode(ciphertext_b64)
    ciphertext = ciphertext_bytes.decode('utf-8')
    return ciphertext


def xor_string_with_key(string_to_xor, key):
    """Function to xor string with key."""
    xor = [None] * len(string_to_xor)
    for i in range(len(string_to_xor)):
        j = i % len(key)
        xor[i] = chr(ord(string_to_xor[i]) ^ ord(key[j]))
    xor_s = ''.join(xor)
    return xor_s


def get_plaintext(ciphertext, key):
    """Get the plaintext from ciphertext and key."""
    return xor_string_with_key(ciphertext, key)


def get_list_of_possible_keys(ciphertext, max_key_len):
    """Get list of possible key for each key length in max_key_len."""
    list_of_possible_decryption_keys = []

    for keylength in range(1, max_key_len + 1):
        splices = splice_to_keylenght_strings(ciphertext, keylength)
        possible_decryption_key = ''
        for block_number in range(len(splices)):
            list_of_one_char_keys = break_single_char_xor(splices[block_number])
            list_of_one_char_keys = sorted(list_of_one_char_keys, key=lambda x: x.score)
            possible_decryption_key += str(list_of_one_char_keys[0].key)
        # print('Possible key:', possible_decryption_key)
        list_of_possible_decryption_keys.append(possible_decryption_key)
    return list_of_possible_decryption_keys


def get_results_for_keys(ciphertext, list_of_possible_decryption_keys):
    """Pass the keys and get results for those keys."""
    decrypted_result = namedtuple('decrypted_result', ['key', 'plaintext', 'score'])
    list_of_results = []
    for key in list_of_possible_decryption_keys:
        plaintext = get_plaintext(ciphertext, key)
        score = combined_score(plaintext)
        decrypted_res = decrypted_result(key, plaintext, score)
        list_of_results.append(decrypted_res)
    return list_of_results


def main():
    """The main function."""
    input_ciphertext_file, max_key_len = get_cl_arguments()
    ciphertext = get_ciphertext_as_string(input_ciphertext_file)

    list_of_possible_decryption_keys = get_list_of_possible_keys(ciphertext, max_key_len)

    list_of_results = get_results_for_keys(ciphertext, list_of_possible_decryption_keys)

    sorted_results_list = sorted(list_of_results, key=lambda x: x.score)
    print('---------- Most likely result ----------')
    result = sorted_results_list[0]
    print('Key:', result.key)
    print('Plaintext:\n', result.plaintext)

if __name__ == "__main__":
    main()
