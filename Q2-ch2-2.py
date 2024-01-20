def decrypt(text, offset=0):
    decrypted = ""
    for char in text:
        if char.isalpha():
            base_ord = ord('A') if char.isupper() else ord('a')
            decrypted += chr((ord(char) + offset - base_ord) % 26 + base_ord)
        else:
            decrypted += char
    return decrypted

encrypted_text = """VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR V NZ BHG BS PBAGEBY
NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF
URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"""

print("Encrypted text:")
print(encrypted_text)

# Decrypt with a shift of 13
decrypted_text = decrypt(encrypted_text, 13)
print("\nDecrypted text with a shift of 13:")
print(decrypted_text)
