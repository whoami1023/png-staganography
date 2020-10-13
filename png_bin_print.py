#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
以十六进制的形式来输出PNG文件的内容
"""

import sys
import binascii

def readPng(path_nam):
    """ read byte from Png file
    :param str path_name: The path of png file which need to be read
    """
    with open(path_nam, mode='rb') as f:
        content = f.read()
        print "len=" + str(len(content))
        for i in range(len(content)):
            print binascii.b2a_hex(content[i]),
            if ((i + 1) % 16 == 0):
                print


if __name__ == "__main__":
    readPng('./test.png')