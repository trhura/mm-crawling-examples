#/usr/bin/env python2
import sys
import os
import codecs
import re
import string
import helper

def main():
    for arg in sys.argv[1:]:
        if not os.path.exists(arg):
            print "%s doesn't exists" %arg
            continue

        with codecs.open(arg, 'r', 'utf-8') as iFile, codecs.open(arg + '.splited', 'w', 'utf-8') as oFile:
            for line in iFile:
                line = line.strip()
                if not line: continue

                splitchars = u"\u104A\u104B" + string.punctuation + string.whitespace
                words = re.split('[' + splitchars + ']', line)
                words = filter(lambda x: bool(x) and helper.is_mainly_myanmar(x), words)
                if not words: continue
                
                oFile.write('\n'.join(words) + '\n')

if __name__ == "__main__":
    main()
