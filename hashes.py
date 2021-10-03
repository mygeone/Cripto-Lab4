

import sys, time, uuid, hashlib

def hashPassord(password, verbose):

    #hasheamos la pw
    hashed_pw = hashlib.sha512(password.encode())

    #generamos una seed
    pre_seed = uuid.uuid4().hex

    #hasheamos la pw agregando la seed al principio 
    unshatedToStore = hashlib.sha512(pre_seed.encode() + hashed_pw.hexdigest().encode())
    print("El hash calculado es :" + unshatedToStore.hexdigest() )
    print('Number of arguments: {}'.format(len(sys.argv)))
    print('Argument(s) passed: {}'.format(str(sys.argv)))