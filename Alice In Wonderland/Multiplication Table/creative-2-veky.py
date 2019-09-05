checkio=lambda f,s,l=int.bit_length:l(f)*s+bin(f).count("1")*(2**l(s)+~s)<<1
