"""The module implements solution to challenge3(level1) of matasano crypto challenges."""
from collections import namedtuple


def get_input_string_into_program(hex_string_input):
    """Get input hex string and return utf-8 string."""
    # In python 3, you have byte strings and unicode stings
    # Always make a unicode sandwich, bytes(input)->unicode(inside the program)->bytes(output)
    # If this confuses you, watch this excellent talk by Ned Batchelder
    # https://www.youtube.com/watch?v=sgHbC6udIqc
    byte_string = bytes.fromhex(hex_string_input)
    utf_string = byte_string.decode('utf-8')
    return utf_string


def xor_string_with_char(string, char):
    """The function takes a sting and a char and computes xor of entire sting with the char."""
    return "".join(chr(ord(c) ^ ord(char)) for c in string)


def return_english_likelehood_score(string):
    """Get score of string based on frequncy analysis of English text - https://en.wikipedia.org/wiki/Frequency_analysis."""
    char_count_total = 0
    score = 0.0
    string = string.upper()
    for i in range(65, 91):
        char_count_total = char_count_total + string.count(chr(i))
    for i in range(65, 91):
        # print chr(i) + str(string.count(chr(i)))
        # print char_count_total
        if char_count_total:
            score = score + pow(string.count(chr(i)) / float(char_count_total), 2)
    deviation_from_norm = abs(0.065 - score)
    return deviation_from_norm


def fraction_of_english_alpha_in_string(string):
    """Divide the total number of english characters by length of string."""
    # alphabets = filter(lambda x: 'a' <= x <= 'z' or 'A' <= x <= 'Z', string)
    characters_count = sum('a' <= c <= 'z' or 'A' <= c <= 'Z' or c == ' ' or c == '.' or c == ',' or c == ':' for c in string)
    score = abs(1 - float(characters_count) / len(string))
    return score


def combined_score(string):
    """Get score based on both character frequency and fraction of english aplhbet in string."""
    score1 = return_english_likelehood_score(string)
    score2 = fraction_of_english_alpha_in_string(string)
    adjusted_score = score1 + score2 / 2
    return adjusted_score


def break_single_char_xor(input_string):
    """Function to break single key xor and return list of results."""
    # Create a namedtuple for the decryption results
    decrypted_result = namedtuple('decrypted_result', ['key', 'plaintext', 'ciphertext', 'score'])
    # Create a list to store all the decrypted result namedtuples
    list_of_results = []
    # There are a total of 1,111,998 possible unicode characters: 17 planes x 65,536 characters per plane - 2048 surrogates - 66 noncharacters
    # 109,384 code points are assigned in Unicode 6.0.
    # We will assume that it is one of the characters in range(0-128), we can revisit if we don't get any hits
    for int_value in range(256):
        xor_result = xor_string_with_char(input_string, chr(int_value))
        # score = return_english_likelehood_score(xor_result)
        # score = fraction_of_english_alpha_in_string(xor_result)
        score = combined_score(xor_result)
        dec_result = decrypted_result(chr(int_value), xor_result, input_string, score)
        list_of_results.append(dec_result)
    return list_of_results


def main():
    """The main function."""
    hex_string_input = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    input_string = get_input_string_into_program(hex_string_input)

    list_of_results = break_single_char_xor(input_string)

    sorted_results_list = sorted(list_of_results, key=lambda x: x.score)
    print("Top 5 most likely results")
    for result in sorted_results_list[:5]:
        print(result)


if __name__ == '__main__':
    main()
