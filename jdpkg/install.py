import os, sys, random
import platform

name = 'jdpkg'
version = '0.0.1'
def init():
    global path
    path = "/tmp/ablepm-%s" % random.randint(1, 80000)
    global install_path
    install_path = path + '/git/' + name
    os.mkdir(path) # don't remove this, as it's not integrated into the AblePM app

def error_message(message):
    print('Error: %s' % message)
    input()
    sys.exit(1)

def get_source():
    os.mkdir(install_path)
    # get the source code from github
    os.system('git clone https://github.com/JaydenDev/jdpkg ' + install_path)

def install():
    print("Welcome to the unofficial JDPKG AblePM package!")
    # if the os is NOT linux or MacOS, then throw an error
    if platform.system() != 'Linux' or platform.system() != 'Darwin':
        error_message('JDPKG is only for Linux and MacOS')
    
    # firstly, get the source code
    get_source()

    # then, chmod the main.sh file
    os.system('chmod +x ' + install_path + '/main.sh')

    # then, copy the main.sh file to the /usr/bin/jdpkg folder
    os.system('sudo cp ' + install_path + '/main.sh /usr/bin/jdpkg')

    # then, remove the install folder
    os.system('sudo rm -rf ' + install_path)

    # finally, show a message to the user and open the main.sh file
    print('JDPKG has been installed!')
    print('To use it, type "jdpkg" in the terminal')
    input()
    os.system('jdpkg')

    
def remove():
    # get and kill running processes of jdpkg
    os.system('sudo killall jdpkg')
    # remove the /usr/bin/jdpkg file
    os.system('sudo rm /usr/bin/jdpkg')
    # remove the /tmp/ablepm-* folder
    os.system('sudo rm -rf ' + path)