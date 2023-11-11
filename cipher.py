alpha_shift = {
    "a": "f",
    "b": "g",
    "c": "h",
    "d": "i",
    "e": "j",
    "f": "k",
    "g": "l",
    "h": "m",
    "i": "n",
    "j": "o",
    "k": "p",
    "l": "q",
    "m": "r",
    "n": "s",
    "o": "t",
    "p": "u",
    "q": "v",
    "r": "w",
    "s": "x",
    "t": "y",
    "u": "z",
    "v": "a",
    "w": "b",
    "x": "c",
    "y": "d",
    "z": "e",
    "A": "F",
    "B": "G",
    "C": "H",
    "D": "I",
    "E": "J",
    "F": "K",
    "G": "L",
    "H": "M",
    "I": "N",
    "J": "O",
    "K": "P",
    "L": "Q",
    "M": "R",
    "N": "S",
    "O": "T",
    "P": "U",
    "Q": "V",
    "R": "W",
    "S": "X",
    "T": "Y",
    "U": "Z",
    "V": "A",
    "W": "B",
    "X": "C",
    "Y": "D",
    "Z": "E",
}

plaintext = str(input("Please type a sentence:"))
encrypted = ""

for letter in plaintext:
    if letter in alpha_shift:
        encrypted += alpha_shift[letter]
    else:
        encrypted += letter
      
print("The encrypted sentence is:", encrypted)