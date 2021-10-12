import argparse
from hashes import hashPassword, hashTxt
from entropy import entropy
import time

start_time = time.time()
parser = argparse.ArgumentParser(description='Little program to process hashing password for Cripto')

group = parser.add_mutually_exclusive_group()

#format(results.password)
group.add_argument('-p', action='store',
                    dest='password',
                    help='Process a password to hash')

#format(results.password_file)
group.add_argument('-f', action='store',
                    dest='password_file',
                    help='Process a list of passwords to hash in a .txt file')

#format(results.stdin_text)
group.add_argument('-s', action='store',
                    dest='stdin_text',
                    help='Process a stdin text to hash')

group.add_argument('-e', action='store',
                    dest='password',
                    help='Calculate a estimated entropy for a given password')

parser.add_argument('-v', action='store_true',
                    dest='verbose',
                    help='Verbose mode')


argsValues = parser.parse_args()


if(argsValues.password):
    hashPassword(argsValues.password,argsValues.verbose)
elif(argsValues.password_file):
    hashTxt(argsValues.password_file,argsValues.verbose)
elif(argsValues.entropy):
    entropy(argsValues.entropy,argsValues.verbose)

passed_time = time.time() - start_time

print(passed_time)