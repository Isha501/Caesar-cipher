'''
Simple Caesar Cipher
'''

def caesar(text, shift , mode):
    out= []
    for ch in text:
        if ch.isalpha():
            base = 'A' if ch.isupper() else 'a'
            shift_amt = shift % 26

            if mode == 'decrypt':
                shift_amt = -shift_amt
            index = ((ord(ch) - ord(base)) + shift_amt) % 26
            out.append(chr((index) + ord(base)))
        else:
            out.append(ch)
    return ''.join(out)

if __name__ == "__main__":
    print("---CAESAR CIPHER---")
    mode= input("Enter mode (encrypt/ecrypt): ")
    text= input("Enter String: ")
    shift = int(input("Enter shift value: "))

    result = caesar(text, shift, mode)
    print(f"\nResult = {result}\n")
