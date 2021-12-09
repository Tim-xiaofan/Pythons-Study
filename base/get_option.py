#!/usr/bin/python3
import argparse

class MyParser(argparse.ArgumentParser):
        def error(self, message):
            self.print_help()
            exit(2)

def get_option():
    parser = MyParser()
    parser.add_argument('-corpus', '--corpus', metavar='corpusfile', required=True, 
                        dest='corpus',help='corpus text file')
    
    parser.add_argument('-test', '--test', metavar='testfile', required=True, 
                        dest='test',help='test text file')
    
    parser.add_argument('-encode', '--encode', metavar='encode',required=False,
                        dest='encode', help='encodeing of file, uft-8 is default')
    
    parser.add_argument('-tag', '--tag',action='store_true',required=False,
                        help='corpus is tagged')
    
    parser.add_argument('-lmfile', '--lmfile', metavar='lmfile', required=False,
                       dest='lmfile', help='dump lm to file')
    
    parser.add_argument('-ctfile', '--ctfile', metavar='ctfile', required=False,
                       dest='ctfile', help='dump count to file')

    parser.add_argument('-result', '--result', metavar='result',required=False,
                       dest='result', help='dump result to file')
    
    parser.add_argument('-number', '--number', metavar='number',required=False,
                       dest='number', help='a number', type=int)
    
    args = parser.parse_args()
    
    # Output the collected arguments
    print("corpus", args.corpus)
    print("test", args.test)
    print("encode", args.encode)
    print("tag", args.tag)
    print("lmfile", args.lmfile)
    print("ctfile", args.ctfile)
    print("result", args.result)
    print("number", args.number)
    return args

def main():
    get_option()

if __name__ == '__main__':
    main()
