# Criptografía y Seguridad
# Laboratorio 4: Hash :lock:

A simple INSECURE Python script to hash passwords.

:no_entry: You must NOT use this algorithm to hash your passwords since it's totally insecure and untested :no_entry:

Supports:
* :small_orange_diamond: String password
* :small_orange_diamond: File with several passwords
* :small_orange_diamond: Entropy calculator

```
usage: main.py [-h] [-p PASSWORD | -f PASSWORD_FILE | -s STDIN_TEXT] [-v]

Little program to process hashing password for Cripto

optional arguments:
  -h, --help        show this help message and exit
  -p PASSWORD       Proceess a password to hash
  -f PASSWORD_FILE  Proceess a list of passwords to hash in a .txt file
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
# Perfomance Comparative :chart_with_upwards_trend:
| N tests | Time to process |
| ------------- | ------------- |
| 1 passwords |  0.0125945 seconds  |
| 10 passwords | 0.0222277 seconds |  
| 20 passwords | 0.0312312 seconds  |
| 50 passwords | 0.0620050 seconds  |
