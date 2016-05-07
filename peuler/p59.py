def read_cipher():
    with open('p059_cipher.txt') as f:
        ciphertext = f.read().split(',')
        ciphertext = [int(a) for a in ciphertext]
        return ciphertext


def is_plain_text_chr(a):
    return 32 <= a <= 126


def is_plain_text(t):
    distribution = {}

    for c in t:
        if not is_plain_text_chr(c):            
            return False
        if c in distribution:
            distribution[c] += 1
        else:
            distribution[c] = 1
    
    # plain text has more alphanumerics than punctuation
    alphas = 0
    numerics = 0
    spaces = 0
    symbols = 0

    for c in distribution:
        if c in str_to_asc('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            alphas += distribution[c]
        elif c in str_to_asc('0123456789'):
            numerics += distribution[c]
        elif c in str_to_asc(' '):
            spaces += distribution[c]
        else:
            symbols += distribution[c]

    if spaces == 0 or symbols + numerics > alphas/8:        
        return False

    return True


def decrypt(cipher, p):    
    plain = [0]*len(cipher)
    
    for i in xrange(0, len(cipher), 3):
        for j in xrange(min(len(p), len(cipher) - i)):
            plain[i+j] = cipher[i+j] ^ p[j]
    return plain


def brute_force_search(cipher):
    # this can be massively optimized
    # we can decrypt every 3rd char once we pick p1
    # and rule out any decryption which produces non plain text chars
    a=0
    for p1 in xrange(ord('a'), ord('z') + 1):
        print 'trying %s**' % chr(p1)
        for p2 in xrange(ord('a'), ord('z') + 1):
            for p3 in xrange(ord('a'), ord('z') + 1):                    
                plain = decrypt(cipher, [p1,p2,p3])                
                if is_plain_text(plain):
                    print asc_to_str([p1, p2, p3])
                    print asc_to_str(plain)
                    a+=1
    print a


def asc_to_str(asc):
    return ''.join(chr(a) for a in asc)

def str_to_asc(s):
    return [ord(c) for c in s]
    
def test_crypt_descrypt():    
    cryptotext = decrypt(str_to_asc('ana are mere si nu pere?'), str_to_asc('bzk'))
    back_plain = decrypt(cryptotext, str_to_asc('bzk'))
    print asc_to_str(back_plain)
    # cryptotext = decrypt(str_to_asc('ana are mere si nu pere?'), str_to_asc('bzk'))
    # brute_force_search(cryptotext)

# test_crypt_descrypt()
cipher = read_cipher()
# brute_force_search(cipher)
plaintext = decrypt(cipher, str_to_asc('god'))
print len(cipher), len(plaintext)
print asc_to_str(plaintext)
print sum(plaintext)
