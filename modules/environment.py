#! /usr/bin/env python
# -*- coding=utf-8 -*-
# author === hushpuppy

import os


def run(**args):
    a = os.environ
    print '\033[1;32;40m'
    print "[*] show the encvironment"
    print('\033[0m')

    return str(a)
