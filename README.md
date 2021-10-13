# Criptografía y Seguridad
# Criptografía y Seguridad
# Laboratorio 4: Hash :lock:

A simple INSECURE Python script to hash passwords.

:no_entry: You must NOT use this algorithm to hash your passwords since it's totally insecure and untested :no_entry:

Supports:
* :small_orange_diamond: String password
* :small_orange_diamond: File with several passwords
* :small_orange_diamond: Entropy calculator

Features:
* ✔️ Produces as output a 1024-bit hash
* ✔️ Each hash lasts 5 minutes
* ✔️ It use operations to input password
* 
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
## Time to hash
It performs several tests to hash 1, 10, 20, 50 and 100 passwords with differents hashing algorithms to test their time performance.
Random strings with 30 characters were used as passwords. For example, ``` M.ygU>M4OaqB)oFS2ysu6mX,=/W6n)Fe``` 
| N tests | Own algorithm  | SHA-1 | SHA-256 | MD5 |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| 1 passwords  | 1.835823059312e-05 seconds |   1.43051109375e-06 seconds | 1.192092895505e-06 seconds | 1.43051147460e-06 seconds |
| 10 passwords | 0.0001015663126562 seconds | 3.814697225e-06 seconds | 3.576278686525e-06 seconds | 3.337860107475e-06 seconds |
| 20 passwords | 0.000704526451172 seconds | 9.7751643164062e-06 seconds | 1.192092895125e-05 seconds | 9.775161764062e-06 seconds | 
| 50 passwords | 0.000645637570312 seconds  | 3.004966796875e-05 seconds | 2.7179718017125e-05 seconds | 2.6941298476562e-05 seconds |
| 100 paswords | 0.001564502714531 seconds  | 5.006790168125e-05 seconds | 4.55379486044e-05 seconds | 4.553794869844e-05 seconds |

## Entropy
With the same password before, it performs test to calculate a numeric value for entropy given a hashed string by differents hashing algorithms.

| Own algorithm  | SHA-1 | SHA-256 | MD5 |
| ------------- | ------------- | ------------- | ------------- |
| 661.750400184616 bits | 206.79 bits | 330.87 bits | 165.43 bits |


