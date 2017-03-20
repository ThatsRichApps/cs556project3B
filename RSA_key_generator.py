'''
Created on Mar 20, 2017

@author: RJHumphrey
'''
from Crypto.PublicKey import RSA

if __name__ == '__main__':
    key = RSA.generate(2048)

    binPrivKey = key.exportKey('DER')
    binPubKey =  key.publickey().exportKey('DER')

    privKeyObj = RSA.importKey(binPrivKey)
    pubKeyObj =  RSA.importKey(binPubKey)

    p = key.key.p
    q = key.key.q
    n = key.key.n 
    d = key.key.d 
    e = key.key.e 

    print ("p = ", p)
    print ("q = ", q)
    print ("n = ", n)
    print ("d = ", d)
    print ("e = ", e)

    assert (n == (p * q))
    
    plaintext = "attack at dawn!"
    
    
    