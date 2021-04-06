import sys, json, os, importlib
from colorama import Back, Fore, Style
from colorama import init as cinit
import argparse
sys.path.insert(0, "../types")
cinit()
from binary import Binary

import zlib, random
# Double Alphabet Encoding - 2.0

class dae2:
    def __init__(self):
        self.alphabet = list("абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz1234567890-+/*:!.,?()_= ") # Default Alphabet without keys.
        self.symbols = list("1234567890-+/*:!.,?()_= ")  # Symbols without letters.
        self.dictionary2 = {'а': '1101000010110000', 'б': '1101000010110001', 'в': '1101000010110010', # Default alphabet with all symbols.
        'г': '1101000010110011', 'д': '1101000010110100', 'е': '1101000010110101',
        'ё': '1101000110010001', 'ж': '1101000010110110', 'з': '1101000010110111',
        'и': '1101000010111000', 'й': '1101000010111001', 'к': '1101000010111010',
        'л': '1101000010111011', 'м': '1101000010111100', 'н': '1101000010111101',
        'о': '1101000010111110', 'п': '1101000010111111', 'р': '1101000110000000',
        'с': '1101000110000001', 'т': '1101000110000010', 'у': '1101000110000011',
        'ф': '1101000110000100', 'х': '1101000110000101', 'ц': '1101000110000110',
        'ч': '1101000110000111', 'ш': '1101000110001000', 'щ': '1101000110001001',
        'ъ': '1101000110001010', 'ы': '1101000110001011', 'ь': '1101000110001100',
        'э': '1101000110001101', 'ю': '1101000110001110', 'я': '1101000110001111',
        'a': '01100001', 'b': '01100010', 'c': '01100011',
        'd': '01100100', 'e': '01100101', 'f': '01100110',
        'g': '01100111', 'h': '01101000', 'i': '01101001',
        'j': '01101010', 'k': '01101011', 'l': '01101100',
        'm': '01101101', 'n': '01101110', 'o': '01101111',
        'p': '01110000', 'q': '01110001', 'r': '01110010',
        's': '01110011', 't': '01110100', 'u': '01110101',
        'v': '01110110', 'w': '01110111', 'x': '01111000',
        'y': '01111001', 'z': '01111010', '1': '00110001',
        '2': '00110010', '3': '00110011', '4': '00110100',
        '5': '00110101', '6': '00110110', '7': '00110111',
        '8': '00111000', '9': '00111001', '0': '00110000',
        '-': '00101101', '+': '00101011', '/': '00101111',
        '*': '00101010', ':': '00111010', '!': '00100001',
        '.': '00101110', ',': '00101100', '?': '00111111',
        '(': '00101000', ')': '00101001', '_': '01011111',
        '=': '00111101', ' ': '00100000'}
        
        self.dictionary = {v:k for k, v in self.dictionary2.items()} # Inverting keys with their values: {"a": "b", ...} => {"b":"a", ...}

    def _check_integrity(self, text):
        text = list(text.lower())
        return all([element in self.alphabet for element in text]) # Check if all of symbols in standart alphabet. If they are standart, it will write out a list, for example, [True, True, True].
        #And when, creating one boolean from all list. If where is one False, this function return False, else True.

    def _invert_stage(self, text): # Invert letter
        text = list(text)
        for i in range(0, len(text)):
            if text[i] == "0":
                text[i] = "1"
            elif text[i] == "1":
                text[i] = "0"
        return "".join(text)

    def _key_stage_1(self, text):
        key = random.randint(0, len(text)-1)
        text = list(text)
        first_part, second_part = text[:key], text[key:]
        second_part+= first_part
        print(second_part, first_part)
        return "".join(second_part), key

    def _unkey_stage_1(self, text, key):
        key = len(text)-int(key)
        first_part, second_part = text[:key], text[key:]
        second_part += first_part
        print(second_part, first_part)
        return "".join(second_part)
    
    def _text_to_bits(self, text, encoding='utf-8', errors='surrogatepass'):
        bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
        return bits.zfill(8 * ((len(bits) + 7) // 8))

    def _text_from_bits(self, bits, encoding='utf-8', errors='surrogatepass'):
        n = int(bits, 2)
        return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

    def to_text(self, text, #keys,
                compression = True):
        if compression:
            # Uncompressing from zlib
            text = zlib.decompress(self.hexstr(text)).decode("utf-8")

        #Using unkeys stages to decrypt all data
        #letter = self._unkey_stage_1(text, keys[0])
        
        #Using inverting stage
        text = self._invert_stage(text)
        
        text = text.split(" "); result = [] # Splitting text to letters: "01001... 010010.." => ["01001...", "010010..."] and creating var for end result
            
        for letter in text: # Using iterator to iterate all letters. For example, "01001..."
            letter = list(letter) # Creating list: "01001..." => ["0", "1", "0", "0", "1", ...] for comfort
                
            if letter[0] == "1" and letter[1] == "0": # If first bit == 1 (First bit showing us, this is letter(1) or specific symbol(0)) and second == 0 (Second showing us, if it is upper-(1) or lower-(0)case)
                # ["1", "1", "0", "0", "1", ...] => 1 - Symbol, 1 -> upper case
                letter = self.dictionary["".join(letter[2:])] # If it is lower case, getting base letter after first and second bits and getting letter from dictionary: ["0", "1", "0", "0", "1", ...] => ["0", "0", "1", ...] 
            elif letter[0] == "1" and letter[1] == "1": # If first bit == 1 (First bit showing us, this is letter(1) or specific symbol(0)) and second == 1 (Second showing us, if it is upper-(1) or lower-(0)case)
                letter = self.dictionary[ "".join(letter[2:])] .upper() # If it is upper case, getting base letter after first and second bits and getting letter from dictionary and then upper-casing it: ["0", "1", "0", "0", "1", ...] => ["0", "0", "1", ...]
                    
            elif letter[0] == "0": # If letter is specific symbol, getting the base after first bit. Spec symbols don`t have in themselves second bit with upper or lower case.
                letter = self.dictionary[ "".join(letter[1:])] # Getting letter from dict
            
            result.append(letter) # Appending letter to result
        return "".join(result) # Creating sentence

    def to_bits(self, text, compression = True):
        if not self._check_integrity(text): # Checking text
            return ""
        
        text = list(text); result = [] # Splitting text to letters: "abc" => ["a", "b", "c"] and creating var for end result
        for letter in text: # Iterate letters.
            if letter not in self.symbols and letter.isupper(): # If letter is not specefic symbol and is upper:
                    letter = "1" + "1" + self.dictionary2[letter.lower()] # Adding first bit(letter(1) or spec(0)) and second(upper(1) or not(0))
                    
            elif letter not in self.symbols and not letter.isupper(): # If letter is not spec symbol and is not upper
                    letter = "1" + "0" + self.dictionary2[letter.lower()] # Adding first bit(letter(1) or spec(0)) and second(upper(1) or not(0))
                    
            elif letter in self.symbols: # If letter is spec
                letter = "0" + self.dictionary2[letter.lower()] # Adding only first bit -> letter(1) or spec(0)

            #Using inverting stage
            letter = self._invert_stage(letter)

            #Using keys stages
            #letter, key1 = self._key_stage_1(letter)
            
            result.append(letter)
        # print("".join(result))
        if compression:
            return zlib.compress(" ".join(result).encode("utf-8"), level=9).hex() #, [key1]
        else:
            return " ".join(result) #, [key1]
    
    def hexstr(self, data:str): 
        if type(data).__name__ == "bytes":
            try:
                s = data.decode("utf-8")
                s = bytes.fromhex(s)
                return s
            except ValueError:
                return None
        if type(data).__name__ == "str":
            try:
                s = bytes.fromhex(data)
                return s
            except ValueError:
                return None

class Encode(Binary):
    def __init__(self):
        self.info = {
            "name" : "Encode to DAE v2.",
            "version" : "v2",
            "codename": "encode",
            "dependencies" : [], # Not Supported.
            "run": self.run,
            "on_load": self.on_load
        }
    

    def on_load(self, info):
        pass

    def run(self, info, pyt):
        dae = dae2()
        args = info.info[15].split(" ")[1:]
        if len(args) > 0:
            try:
                print(dae.to_bits(info.info[15].replace("encode", "")))
            except:
                print()
        else:
                print()
class Decode(Binary):
    def __init__(self):
        self.info = {
            "name" : "Decode from DAE v2.",
            "version" : "v2",
            "codename": "decode",
            "dependencies" : [], # Not Supported.
            "run": self.run,
            "on_load": self.on_load
        }
    

    def on_load(self, info):
        pass

    def run(self, info, pyt):
        dae = dae2()
        args = info.info[15].split(" ")[1:]
        if len(args) > 0:
            try:
                print(dae.to_text(info.info[15].replace("decode", "")))
            except:
                print()
        else:
                print()

