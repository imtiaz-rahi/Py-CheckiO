# https://py.checkio.org/mission/morse-decoder/publications/Tinus_Trotyl/python-3/the-binair-interpretation/
# replace . and - by 0 and 1, then use as a binair index number for the lookup table

MORSE = [ "",
          "et",
          "ianm",
          "surwdkgo",
          "hvf*l*pjbxcyzq**",
          "54*3***2**+****16=/*****7***8*90" ]


def morse_decoder(code):
    return ' '.join(''.join(MORSE[len(ch)][int(ch, 2)] for ch in word.split(' '))
                    for word in code.replace('.', '0').replace('-', '1').split('   ')).capitalize()
