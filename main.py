import argparse
from hashes import hashPassord

parser = argparse.ArgumentParser(description='Little program to process hashing password for Cripto')
subparsers = parser.add_subparsers(help='sub-commands help')


group = parser.add_mutually_exclusive_group()


#format(results.password)
group.add_argument('-p', action='store',
                    dest='password',
                    help='Proceess a password to hash')

#format(results.password_file)
group.add_argument('-f', action='store',
                    dest='password_file',
                    help='Proceess a list of passwords to hash in a .txt file')

#format(results.stdin_text)
group.add_argument('-s', action='store',
                    dest='stdin_text',
                    help='Proceess a stdin text to hash')

parser.add_argument('-v', action='store',
                    dest='verbose',
                    help='Verbose mode')


argsValues = parser.parse_args()


print(argsValues)



