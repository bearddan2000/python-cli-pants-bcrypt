#!/usr/bin/env python

import bcrypt

def hashPsw(password):
    return bcrypt.hashpw(password, bcrypt.gensalt(12))

def check_password(password, hashed):
    return bcrypt.checkpw(password, hashed)

def comp(psw1, psw2):
    hash1 = hashPsw(psw1)
    print( "[COMP] psw1 = %s, psw2 = %s" % (psw1, psw2));
    if check_password(psw2, hash1):
        print( "[COMP] true");
    else:
        print( "[COMP] false");

def printPsw(password):
    print( "[INPUT] %s" % password);
    print( "[OUTPUT] %s" % hashPsw(password));

def main():
    psw1 = 'pass123';
    psw2 = '123pass';
    printPsw(psw1)
    printPsw(psw2)
    comp(psw1, psw1)
    comp(psw1, psw2)

if __name__ == '__main__':
    main()
