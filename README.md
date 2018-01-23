Technology used:
virtualenv- to keep a consist package version in our development as well as isolating foreign environment variables

Installation Guide for Unix-like system:

1. Be sure to have the latest python3, pip, and virtualenv. The link should provide all the instruction for both windows and unix-like systems. https://packaging.python.org/guides/installing-using-pip-and-virtualenv/

2. Create a virtual environment
```python
python3 -m virtualenv env
```

3. activate the virtual environment.
```
cd env
source bin/activate
```

4. git clone https://github.com/jchan40/DeliverMe.git

5. install the packages.
```
pip install -r requirements.txt
```

6. run the development server.
```
python3 manage.py runserver
```
