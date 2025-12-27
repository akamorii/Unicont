import enum

import hashlib
# passf = input('input passphrase')
def hash_word(word):
    word = bytearray(word, "utf-8")
    sha = hashlib.sha1(word).hexdigest()
    return sha

class hash_algos(enum.Enum):
    sha = hashlib.sha1
    md5 = hashlib.md5
    


def check_acces(inputed):
    if hash_word(inputed) == 'aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d':
        print ('u has been hacked')

if __name__ == '__main__':
    # print(hash_word('hello'))
    # check_acces(passf)
    
    for i in hash_algos:
        # print(type(i.value))
        print(i.value(bytearray('hello', 'utf-8')).hexdigest())
        
    