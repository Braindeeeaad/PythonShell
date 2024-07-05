import os
import sys
import subprocess

def logging(text):
    with open('log.text','w') as file:
        file.write(text)

def handle_Path(command,path,line,n):
    full_path = ""
    args = line[n+1]
    for directory in path:
        full_path = os.path.join(directory,command)
        if os.access(full_path, os.X_OK):
            os.system(line)
            return ''
        if os.path.isdir(full_path):
            return f'{command} is {full_path}'
    return f"{command}: not found\n"
def handle_type(command,path):
    builtin_list = ["echo","exit","type"]
    if command in builtin_list:
        return f"{command} is a shell builtin\n"
    return handle_Path(command,path)
def handle_response(line,path) -> bool:
    command = line.split(" ")
    match(command[0]):
        case "exit":
            if command[1]=="0":
                return False
        case "echo":
            sys.stdout.write(f"{' '.join(map(str,command[1:]))}\n")
            return True
        case "type":
            text = handle_type(command[1],path)
            if(text!=''):
                sys.stdout.write(handle_type(command[1],path,command,n=1))
            return True
        case _:
            sys.stdout.write(handle_Path(command[0], path, line, n=0))
            return True

    sys.stdout.write(f"{line}: command not found\n")
    return True



def main():
    while True:
        try:

            sys.stdout.write("$ ")
            sys.stdout.flush()

            # Wait for user input
            path_env = os.environ.get('PATH')
            line = input()
            if not handle_response(line,path_env.split(":")):
                return
        except(EOFError,KeyboardInterrupt):
            break



if __name__ == "__main__":
    main()
