"""The module implements solution to challenge1(level1) of matasano crypto challenges."""
import base64

# hex_string is basically a string representaion of some hex bytes. So just taking hex bytes and putting them in ""


def hex_to_base64(hex_string):
    """Input hex string and return base64 encoded string."""
    decoded_string = bytes.fromhex(hex_string).decode('utf-8')
    base64_string = base64.b64encode(bytes(decoded_string, 'utf-8'))
    return base64_string


def main():
    """The main function."""
    hex_string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    # print(type(hex_string))
    expected = b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
    if hex_to_base64(hex_string) == expected:
        print('It matches: Challenge 1 complete')

if __name__ == '__main__':
    main()
