#!/usr/bin/env python3

import argparse
import subprocess
import os

#  parse python3 args
parser = argparse.ArgumentParser(description='Generate a github folder with README.md page for the UVa pdf file.')
parser.add_argument('file path', metavar='fp', type=str, nargs='+',
                   help='the pdf file path you want to use')


args = parser.parse_args()
args = vars(args)
filePath = args['file path'][0]
print(filePath)

#  parse pdf file
output = subprocess.run(["pdf2txt.py", filePath], stdout=subprocess.PIPE)
content = output.stdout.decode("utf-8")

#  create readme folder
newDir = "./" + filePath.split('.')[0]     
if not os.path.isdir(newDir):
    os.makedirs(newDir)
    print("Directory %s was created." %newDir)

#  create the file
f = open(newDir + '/README.md', 'w')
f.write(content)


# TODO: markdown format, first step may be add \n newline
# TODO: parse the url, get the title, and add those to content

