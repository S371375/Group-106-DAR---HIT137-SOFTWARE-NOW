def decrypt(text, key):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) - key
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

# Given encrypted code
encrypted_code = "tybony_inevnoyr = 100\nzl_qvpg = {'xrl1': 'inyhr1', 'xrl2': 'inyhr2', 'xrl3': 'inyhr3'}\n\nqrs cebprff_ahzoref():\n    tybony tybony_inevnoyr\n    ybpny_inevnoyr = 5\n    ahzoref = [1, 2, 3, 4, 5]\n\n    juvyr ybpny_inevnoyr > 0:\n        vs ybpny_inevnoyr % 2 == 0:\n            ahzoref.erzbir(ybpny_inevnoyr)\n        ybpny_inevnoyr -= 1\n\n    erghea ahzoref\n\nzl_frg = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}\nerfhyg = cebprff_ahzoref(ahzoref=zl_frg)\n\nqrs zbqvsl_qvpg():\n    ybpny_inevnoyr = 10\n    zl_qvpg['xrl4'] = ybpny_inevnoyr\n\nzbqvsl_qvpg(5)\n\nqrs hcqngr_tybony ():\n    tybony tybony_inevnoyr\n    tybony_inevnoyr += 10\n\nsbe v va enatr (5):\n    cevag (v)\n    v += 1\n\nvs zl_frg vf abg Abar naq zl_qvpg['xrl4'] == 10:\n    cevag('Pbaqvgvba zrg!')\n\nvs 5 abg va zl_qvpg:\n    cevag('5 abg sbhaq va gur qvpgvbanel!')\n\ncevag(tybony_inevnoyr)\ncevag(zl_qvpg)\ncevag(zl_frg)"

# Decrypting the code
decrypted_code = decrypt(encrypted_code, 13)
print(decrypted_code)
