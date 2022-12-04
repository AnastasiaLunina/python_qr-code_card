## About
### Make your QRcode card

<img src="./my-vcard.png" alt="qr-code">

## How to

1. The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/AnastasiaLunina/python_qr-code_card.git
$ cd qr-code_card
```

2. Create a virtual environment to install dependencies in and activate it:

```sh
$ python3 -m venv ./env

# Mac/Linux
$ source env/bin/activate

# Windows
venv\Scripts\activate.bat

# Exit venv
deactivate
```
3. Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```

5. Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
```
6. Run script

OR write the script yourself using segno package.<br><br>
[See documentation](https://segno.readthedocs.io/en/latest/contact-information.html)

1. Create the virtual environment and install the package
```sh
pip install segno
```
