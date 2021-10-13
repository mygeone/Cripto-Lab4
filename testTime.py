import time, hashlib

from hashes import hashPassword

password = 'asdfsgdf213DASD'

startTimeOwn = time.time_ns()
hashPassword(password,False)
endTimeOwn = round(time.time_ns() - startTimeOwn, 9)

startTimeSHA1 = time.time()

print(endTimeOwn / (10 ** 9) )
for i in range(1000):
    a = hashlib.sha1(password.encode())
#print(a.hexdigest())

print(time.time())

endTimeSHA1 = time.time() - startTimeSHA1

