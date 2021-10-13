import sys, time, hashlib


def intercalate(larger, shorter):
    for i in range((len(larger)-len(shorter))):
        shorter+=('0')
    
    return ''.join([str(elem) for elem in [*sum(zip(larger,shorter),())]])

def hashPassword(password, verbose, flag):
    #generamos una seed
    pre_seed =  str(int(time.time())//5*60)

    starTimeSingle = time.time()
    
    """ 
    hasheamos un str generado a partir de intercalar la password y un string basado en una seed con padding
    Ejemplo:
    password  = HolaSoyUnaPassword
    seed      = 128312983
    strToHash = H1o2l8a3S1o2y9U8n3a0P0a0s0s0w0o0r0d0
    """

    if (len(pre_seed)>len(password)):
        strToHash = intercalate(pre_seed,password).encode()
        hashedPassword = hashlib.sha512(strToHash)
    else:
        strToHash = intercalate(password,pre_seed).encode()
        hashedPassword = hashlib.sha512(strToHash)

    if (flag == 'q'):
        return -1
    else:
        if(verbose):
            print("La contraseña a hashear es    :",password)
            print("La seed calculada es          :",pre_seed)
            print("El string a hashear es        :",strToHash)
            print("La password hasheada es       :",hashedPassword.hexdigest())
            print("El tiempo de procesado fue de :", time.time()-starTimeSingle,"segundos ")
        
        else:
            print("El hash calculado es : " + hashedPassword.hexdigest() )
        
    


def hashTxt(file, verbose):
    startTimeFiles = time.time()
    with open(file) as f:
        lines = f.readlines()
        for password in lines:
            hashPassword(password, verbose, 'f')
    print("---------------------------------------------------------------------------")
    print("El tiempo de ejecucion total fue",time.time() - startTimeFiles,"segundos")

