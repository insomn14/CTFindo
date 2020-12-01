import string, random
alphabet = dict(zip([x for x in range(len(string.printable[:-6]))],[x for x in string.printable[:-6]]))

def get_key(val): 
    for key, value in alphabet.items():
         if val == value:
             return key

def my_heart(number):
    try:
        return [i for i in range(94) if i*number%94==1][0]
    except:
        return None

def i_am_a_ffine(plaintext, k1, k2):
    return ''.join(tuple(map(lambda x: alphabet[(k1 * int(get_key(x)) + k2) % 94], plaintext)))

while True:
    your_heart = my_heart(random.randrange(0, 94))
    if your_heart is not None:
        break

print(i_am_a_ffine("Fine is actually everything gonna be fine", your_heart, random.randrange(0,94)))
