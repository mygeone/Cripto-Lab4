# Criptografía y Seguridad
# Laboratorio 4: Hash :lock:

A simple INSECURE Python script to hash passwords.

:no_entry: You must NOT use this algorithm to hash your passwords since it's totally insecure and untested :no_entry:

Supports:
* String password
* File with several passwords
* STDIN text
* Entropy calculator

```
usage: main.py [-h] [-p PASSWORD | -f PASSWORD_FILE | -s STDIN_TEXT] [-v]

Little program to process hashing password for Cripto

optional arguments:
  -h, --help        show this help message and exit
  -p PASSWORD       Proceess a password to hash
  -f PASSWORD_FILE  Proceess a list of passwords to hash in a .txt file
  -s STDIN_TEXT     Proceess a stdin text to hash
  -e PASSWORD       Calculate a estimated entropy for a given password
  -v                Verbose mode

Examples:
main.py -p my_pass_to_hash -v
main.py -f file_with_passwords.txt
```

Dockerfile is included to run as a container.

First, build Dockerfile
```
docker build . -t criptolab4
```
Run criptolab4 container generated:
```
docker run criptolab4 [-p PASSWORD | -f PASSWORD_FILE | -s STDIN_TEXT | -e PASSWORD] [-v]
```
Example
```
docker run criptolab4 -f passwords.txt -v
```
