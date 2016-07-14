"""The module implements solution to challenge7(level1) of matasano crypto challenges."""

import argparse
import base64
from Crypto.Cipher import AES


def read_file(path_to_file):
    """Read file and return ciphertext."""
    with open(path_to_file, 'r') as file_handle:
        ciphertext = file_handle.read()
    return ciphertext


def base_64_decode(base64_encoded_string):
    """Take base 64 encoded string and return decoded string."""
    return base64.b64decode(base64_encoded_string)


def get_cl_arguments():
    """Get the command line arguments passed by user."""
    parser = argparse.ArgumentParser(prog='AES ECB decryptor', description='Decrypt ECB in AES mode with key YELLOW SUBMARINE')
    parser.add_argument('-i', '--path_to_ciphertext_file', required=True, help='Ciphertext file to break - Base64 encoded')
    args = parser.parse_args()
    return vars(args)['path_to_ciphertext_file']


def ecb_decrypt(ciphertext, key):
    """Decrypt using pycrypto."""
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(ciphertext)


def main():
    """The main function."""
    path_to_ciphertext_file = get_cl_arguments()
    base64_encoded_cipher = read_file(path_to_ciphertext_file)
    decoded_cipher = base_64_decode(base64_encoded_cipher)
    key = b'YELLOW SUBMARINE'
    decrypted_byte_string = ecb_decrypt(decoded_cipher, key)
    decrypted_string = decrypted_byte_string.decode('utf-8')
    print(decrypted_string)


if __name__ == "__main__":
    main()
