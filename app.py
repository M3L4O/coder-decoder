from base64 import decode
from cgi import print_arguments
import sys


def coder(msg):
    codified = ''
    for letter in msg:
        codified += chr(ord(letter) + 3)
    return codified


def decoder(msg):
    decodied = ''
    for letter in msg:
        decodied += chr(ord(letter) - 3)
    return decodied

if __name__ == '__main__':
    method = sys.argv[1]
    msg = sys.argv[2]

    if method == 'coder':
        print(coder(msg))
    elif method == 'decoder':
        print(decoder(msg))
    else:
        raise Exception('Método desconhecido.')
