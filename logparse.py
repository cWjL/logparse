#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os, sys, time
import argparse
from progressbar import ProgressBar
from datetime import datetime

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i",action='store',dest='in_file',help='Process this file only')
    parser.add_argument("-r",action='store',dest='in_dir',help='Process all files in this directory')
    reqd_args = parser.add_argument_group('required arguments')
    reqd_args.add_argument('-a',action='store',dest='arguments',help='Comma separated list of keywords to search for',required=True)
    
    args = parser.parse_args()
    res = []
    arguments = args.arguments.split(',')
    if args.in_file is None and args.in_dir is None:
        print("[ XX ] You must enter an input file or directory")
        sys.exit(1)
    elif args.in_file is not None and args.in_dir is not None:
        print("[ XX ] You must enter a file OR a directory, not both")
        sys.exit(1)
    elif args.in_file and not args.in_dir:
        if os.path.isfile(os.path.abspath(args.in_file)):
            res = _get_data(args.in_file)
        else:
            print("[ XX ] Check your file path, it's incorrect")
            sys.exit(1)
    elif args.in_dir and not args.in_file:
        if os.path.exists(args.in_dir):
            res = _get_data(args.in_dir)
        else:
            print("[ XX ] Check your file path, it's incorrect")
            sys.exit(1)
    print("[ OK ] Total log lines: "+str(len(res)))
    found = _sort_data(res, arguments)
    print("[ OK ] Sorted log lines: "+str(len(found)))
    _write_out(found)
    print("[ OK ] Wrote "+str(len(found))+" lines to \'log_parse.txt\' in current directory")
    
    sys.exit(0)

def _write_out(_res):
    with open('log_parse.txt','w+') as _out_file:
        _out_file.write("[ "+str(datetime.now())+" ]\n")
        for _item in _res:
            _out_file.write("File:"+_item[0]+"::"+_item[1])
        
def _get_data(_in):
    _res_lst = []
    if os.path.isdir(_in):
        for file in os.listdir(_in):
            if file.endswith(".log"):
                with open(_in+file,'r') as log_file:
                    _tmp_lst = log_file.readlines()
                    _i = 0
                    for item in _tmp_lst:
                        _res_lst.append((_in+file+"::Line:"+str(_i), item))
                        _i += 1
    else:
        with open(_in,'r') as log_file:
            _tmp_lst = log_file.readlines()
            _i = 0
            for _item in _tmp_lst:
                _res_lst.append((_in+"::Line:"+str(_i), _item))
                _i += 1
                    
    return _res_lst
    
def _sort_data(_in_lst, _args):
    _found = []
    _bar = ProgressBar(maxval=len(_in_lst)).start()
    for i, _it in enumerate(_in_lst):
        _in = False
        for _wrd in _args:
            if _wrd in _it[1]:
                _in = True
        if _in:
            _found.append(_it)
        _bar.update(i)
    _bar.finish() 
    return _found
    
if __name__ == "__main__":
    main()
