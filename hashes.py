import sys, time, uuid, hashlib

def hashPassword(password, verbose):
    start_time = time.time()
    #hasheamos la pw
    hashed_pw = hashlib.blake2b(password.encode())

    #generamos una seed
    pre_seed = uuid.uuid4().hex

    #invert array
    left = password[:len(password)//2]
    right =  password[:len(password)//2:]

    unshatedToStore2 = left.encode() + pre_seed.encode() + right.encode()
    #pw2 = hashlib.blake2b(unshatedToStore2.encode())

    #hasheamos la pw agregando la seed al principio 
    unshatedToStore = hashlib.sha512(pre_seed.encode() + hashed_pw.hexdigest().encode())

    passed_time = time.time() - start_time


    if(verbose):
        print("La contraseña hasheada con SHA512 es : " +hashed_pw.hexdigest())
        print("La seed calculada es : " +pre_seed)
        print("El string a hashear es: "+pre_seed+hashed_pw.hexdigest())
        print("El string hasheado con 512 a almacenar es : " +unshatedToStore.hexdigest())
        print(passed_time)
        print("------------------------------------------------------------")

    else:
        print("El hash calculado es : " + unshatedToStore.hexdigest() )


def hashTxt(file, verbose):
    with open(file) as f:
        lines = f.readlines()
        for password in lines:
            hashPassword(password, verbose)

def hashSTD(std,verbose):
    hashPassword(std,verbose)