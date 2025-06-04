import math
letters = r"0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,?!@#$%^&*()[]{}\|/<>+-=`~:;' "
c = math.floor(len(letters)/2)
def encode(a):
    out = ""
    c = math.floor(len(letters)/2)
    for b in a:
        out += letters[(letters.index(b)-c)%len(letters)]
        c += letters.index(b)
    return out
def decode(a):
    out = ""
    c = math.floor(len(letters)/2)
    for b in a:
        out += letters[(letters.index(b)+c)%len(letters)]
        c += letters.index(b)+c
    return out
while 1:
    proc = input("ENCODE OR DECODE: ").lower()
    while proc != "encode" and proc != "decode":
        proc = input("ENCODE OR DECODE: ").lower()
    if proc == "encode":
        print(encode(input("STRING TO ENCODE: ")))
    elif proc == "decode":
        print(decode(input("STRING TO DECODE: ")))
