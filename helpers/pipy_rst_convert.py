#!/usr/bin/env python
import pypandoc
import codecs
from os import path
if __name__ == '__main__':
    """
        Simple script to generate the rst file for pipy
    """
    parent = path.abspath(path.dirname(path.dirname(__file__)))
    readmemd_path = path.join(parent, 'README.md')
    readmerst_path = path.join(parent, 'README.rst')
    output = pypandoc.convert_file(readmemd_path, 'rst')
    with codecs.open(readmerst_path, 'w+', encoding='utf8') as f:
        f.write(output)
