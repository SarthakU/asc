import sys
from subprocess import Popen, PIPE, STDOUT
from termcolor import colored

class Lang():
    def __init__(self, name, run_command=None, build_command=None):
        self.name = name
        self.run_command = run_command
        self.build_command = build_command
        
    def run(self, file_name, inp, java=False):
        args = []
        
        if self.run_command:
            args = [self.run_command, file_name]
        else:
            args = ['./' + file_name.split('.')[0]]
        if java:
            file_name = file_name.split('.')[0]
            
        process = Popen(args, stdout=PIPE, stdin=PIPE, stderr=STDOUT)
        # print(process.stdout.readlines())
        # print(args)
        stdout = process.communicate(input=str.encode(inp))[0]
        output = ''
        if process.returncode != 0:
            print(colored('): ', 'red'), end='')
            print('Following error while running:\n')
            print(stdout.decode())
            sys.exit()
        else:
            print(colored('(: ', 'green'), end='')
            print('Ran Successfully')
            try:
                output = stdout.decode()
            except UnicodeDecodeError:
                output = str(stdout)[2:-1].replace('\\n', '\n')
            # print(output)
            
        return output
        
    def compile(self, file_name, inp, java=False):
        
        args = self.build_command(file_name).split(' ')
        
        process = Popen(args, stdout=PIPE)
        # print(process.returncode)
        return_code = process.wait()
        
        if return_code == 0:
            print(colored('(: ', 'green'), end='')
            print('Compilation Sucesseful! I\'ll try run now.')
            return self.run(file_name, inp, java)
        else:
            print(colored('): ', 'red'), end='')
            print('Compilation Failed')
            sys.exit()
            # print(process.communicate()[0].decode())
            
    def run_output(self, file_name, inp, java=False):
        args = []
        
        if self.run_command:
            args = [self.run_command, file_name]
        else:
            args = ['./' + file_name.split('.')[0]]
        if java:
            file_name = file_name.split('.')[0]
            
        process = Popen(args, stdout=PIPE, stderr=STDOUT)

        for i in process.stdout.readlines():
            try: 
                print(i.decode(), end='')
            except UnicodeDecodeError:
                output = str(i)[2:-1].replace('\\n', '\n')


    def compile_output(self, file_name, inp, java=False):
        args = self.build_command(file_name).split(' ')
        
        process = Popen(args, stdout=PIPE)
        # print(process.returncode)
        return_code = process.wait()
        
        if return_code == 0:
            print(colored('(: ', 'green'), end='')
            print('Compilation Sucesseful! I\'ll try run now.')
            self.run_output(file_name, inp, java)
        else:
            print(colored('): ', 'red'), end='')
            print('Compilation Failed')
            sys.exit()
            # print(process.communicate()[0].decode())
