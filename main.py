
import hashlib
import uuid
import time


password = 'holaa'

#len 128
hashed_pw = hashlib.sha512(password.encode())

#len32
pre_seed = uuid.uuid4().hex


unshatedToStore = hashlib.sha512(pre_seed.encode() + hashed_pw.hexdigest().encode())
print(unshatedToStore.hexdigest() )
