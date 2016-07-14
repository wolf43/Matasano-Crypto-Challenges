"""The module implements solution to challenge8(level1) of matasano crypto challenges."""
from collections import Counter


def read_file(path_to_file):
    """Read file and return ciphertext."""
    with open(path_to_file, 'r') as file_handle:
        ciphertext = file_handle.read()
    return ciphertext


def splice_string_into_n_parts(string, splice_size):
    """Split a string into splices of length splice_size."""
    return [string[i:i + splice_size] for i in range(0, len(string), splice_size)]


def main():
    """The main function."""
    hex_encoded_ciphers = read_file("challenge8_ciphertext.txt")
    hex_encoded_ciphers = hex_encoded_ciphers.split('\n')
    for i in hex_encoded_ciphers:
        splices_of_i = splice_string_into_n_parts(bytes.fromhex(i), 16)
        dict_of_i_splices = dict(Counter(splices_of_i))
        if any(v > 1 for v in dict_of_i_splices.values()):
            print('Repetition found')
            print('Input string:', i)
            print('Input string index:', hex_encoded_ciphers.index(i))
            print("value : Number of occurences")
            for k, v in dict_of_i_splices.items():
                if v > 1:
                    print(k.hex(), ':', v)

if __name__ == "__main__":
    main()
