def convert_base10_to_base58(num: int) -> str:
    alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
    base_count = len(alphabet)
    encoded = ''

    if num == 0:
        return alphabet[0]

    while num > 0:
        num, rem = divmod(num, base_count)
        encoded = alphabet[rem] + encoded

    return encoded
