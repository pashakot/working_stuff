def encode_morze(text):
    morse_code = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        " ": "*"
    }
    up = text.upper()
    enc_str = list(up)
    recoded_str = []
    end_str = ""
    for i in range(len(enc_str)):
        for j in morse_code:
            if enc_str[i] not in morse_code:
                continue
            if enc_str[i] == j:
                recoded_str.append(morse_code[j])
    for i in range(len(recoded_str)):
        for j in recoded_str[i]:
            if j == ".":
                end_str += "^_"
            elif j == "-":
                end_str += "^^^_"
            else:
                end_str += "__"
        end_str += "__"
    end_str = end_str[:len(end_str)-3]
    return end_str


print(encode_morze("r a t"))
