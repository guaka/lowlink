#!/usr/bin/env python
"""
lowlink.py

Recursively creates lower case symlinks to filenames with uppercase letters.

(c) 2013 Kasper Souren
See LICENSE
"""

import os

        
def lowlink(path = '.'):
    cwd = os.getcwd()  # os.walk can't handle path changes very well 
    for root, dirs, files in os.walk(path):
        # change directory for symlink creation
        os.chdir(os.path.join(cwd, root))
        for name in files + dirs:
            lowname = name.lower()
            if name != lowname and not os.path.exists(lowname):
                os.symlink(name, lowname)
        os.chdir(cwd) # restore path for os.walk


def gen_test(path = '.'):
    import random, string
    cwd = os.getcwd()
    for root, dirs, files in os.walk(path):
        os.chdir(os.path.join(cwd, root))
        print root
        for i in range(3):
            # generate random string, could be more pythonic
            random_string = ''.join([random.choice(string.ascii_letters) for i in range(10)])
            n = random_string
            print n
            file(n, 'w').close()
        os.chdir(cwd)

# gen_test()
lowlink()
