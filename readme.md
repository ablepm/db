# AblePM database

This is the database for the AblePM project.

## Adding a new Package

All packages for AblePM have a `install.py` file in them that looks like this:

```python
import os, sys, random
import platform # only required if you want this to work on a specific os only

name = 'mypackage'
version = '0.0.1' # this follows semver
def init():
    global path
    path = "/tmp/ablepm-%s" % random.randint(1, 80000)
    global install_path
    install_path = path + '/git/' + name
    os.mkdir(path) # don't remove this, as it's not integrated into the AblePM app

# any custom functions go here

def get_source(): # only required if this app is (even partially) open source
    # add your code to get the source here

def install():
    # add your code here

def remove():
    # add your code here
```

