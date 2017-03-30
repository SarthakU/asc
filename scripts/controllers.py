#!/usr/bin/env python3

import os
import sys
from subprocess import Popen, PIPE, STDOUT, check_call
from termcolor import colored
from .models import Lang
# os.chdir(os.path.dirname(__file__))

c_build_commmand = lambda b: 'gcc ' + b + ' -o ' + b.split('.')[0]
cpp_build_commmand = lambda b: 'g++ ' + b + ' -o ' + b.split('.')[0]
java_build_commmand = lambda b: 'javac ' + b

interpreted_langs = {
    'php'       : Lang('PHP', 'php'),
    'perl'      : Lang('Perl', 'perl'),
    'python2'   : Lang('Python 2', 'python'),
    'python3'   : Lang('Python 3', 'python3'),
    'ruby'      : Lang('Ruby', 'ruby'),
    'node'      : Lang('Javascript', 'node'), 
    'bash'      : Lang('Bash', 'bash')
}

compiled_langs = {
    'c'         : Lang('C', None, c_build_commmand),
    'cpp'       : Lang('C++', None, cpp_build_commmand),
    'java'       : Lang('Java', 'java', java_build_commmand)
}




def submit(lang, file=None, input=None):
    lang = lang.replace(' ','').lower()

    if lang in interpreted_langs:
        interpreted_langs[lang].run(file, 'asf')
    elif lang in compiled_langs:
        if lang == 'java':
            compiled_langs[lang].compile(file, 'aaa', True)    
        else:
            compiled_langs[lang].compile(file, 'aaa')    
    else: 
        pass
    
def run(lang, file=None, input=None):
    lang = lang.replace(' ','').lower()
    # print(lang in interpreted_langs)
    # print(interpreted_langs)
    if lang in interpreted_langs:
        interpreted_langs[lang].run_output(file, 'asf')
    elif lang in compiled_langs:
        if lang == 'java':
            compiled_langs[lang].compile(file, 'aaa', True)    
        else:
            compiled_langs[lang].compile(file, 'aaa')    
    else: 
        pass
        
def init_lang():
    language_msg = '''Python 3 : python3
    Python 2 : python2
    Javascipt : node
    C++ : cpp
    C : c
    Perl : perl
    Ruby : ruby
    PHP : php
    Java : java
    Bash : bash'''
    
    print('Supported Languages\n' + language_msg)
    
    # lang = ''
    
    while True:
        
        lang = input('\n\nEnter the code in front of language you wish to use\n')
        if lang in [i.split(':')[1].strip() for i in language_msg.split('\n')]:
            break
        else:
            print(colored('\nInvalid Choice! Try again...', 'red'))    
    
    print(colored('\nYou chose ' + lang, 'green'))
    print('\nRun following command to change language anytime:\n')
    print('\tenigma changelang\n')
    return lang
# run('cp p')
# run('python 2')





# lang_c.compile('hello.c', a)



# from random import shuffle
# def mmmm():
#     cases = {1 : 'yes', 2: 'no', 4: 'no', 21: 'yes', 423: 'yes', 140210: 'no'}
#     # print(list(cases.keys()))
#     asc = list(cases.keys())
#     shuffle(asc)
#     print(asc[:3])
#     case_num = 0
#     for i in asc[:3]:
#         print('\nTrying input case ' + str(case_num) +  '...\n')
#         if lang_ruby.run('hello.rb', str(i)) == cases[i]:
#             print(colored(':) ', 'green'), end='')
#             print('Correct Answer')
#         else:
#             print(colored(':| ', 'yellow'), end='')
#             print('Wrong Answer')
#         case_num += 1
    
    
    
# mmmm()