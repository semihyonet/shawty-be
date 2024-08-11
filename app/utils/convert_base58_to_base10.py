def convert_base58_to_base10(encoded):
    alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
    base_count = len(alphabet)
    num = 0

    for char in encoded:
        num = num * base_count + alphabet.index(char)

    return num
