# https://py.checkio.org/mission/morse-decoder/publications/martin_b/python-3/gets-it-done-by-refindall/
import re

REMORSE = {'.-': 'A', '-...': 'B', '-.-.': 'C',
           '-..': 'D', '.': 'E', '..-.': 'F',
           '--.': 'G', '....': 'H', '..': 'I',
           '.---': 'J', '-.-': 'K', '.-..': 'L',
           '--': 'M', '-.': 'N', '---': 'O',
           '.--.': 'P', '--.-': 'Q', '.-.': 'R',
           '...': 'S', '-': 'T', '..-': 'U',
           '...-': 'V', '.--': 'W', '-..-': 'X',
           '-.--': 'Y', '--..': 'Z', '   ': ' ',
           '-----': '0', '.----': '1', '..---': '2',
           '...--': '3', '....-': '4', '.....': '5',
           '-....': '6', '--...': '7', '---..': '8',
           '----.': '9'
           }

def morse_decoder(c):
    return "".join(REMORSE[i] for i in re.findall("([.-]+| {3})", c)).capitalize()
