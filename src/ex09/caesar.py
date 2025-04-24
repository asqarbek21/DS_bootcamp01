import sys

def is_valid_text(text):
    for char in text:
        if char.isalpha() and not char.isascii():
            return False
    return True

def caesar(text, shift, mode):
    if not is_valid_text(text):
        raise Exception("The script does not support your language yet.")

    if mode not in ('encode', 'decode'):
        raise Exception("Mode must be 'encode' or 'decode'.")

    if mode == 'decode':
        shift = -shift

    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result += new_char
        else:
            result += char
    return result

if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise Exception("Incorrect number of arguments.")
    
    mode = sys.argv[1].lower()
    text = sys.argv[2]
    try:
        shift = int(sys.argv[3])
    except ValueError:
        raise Exception("Shift must be an integer.")

    print(caesar(text, shift, mode))