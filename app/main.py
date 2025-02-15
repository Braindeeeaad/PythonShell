import os
import sys
from pathlib import Path

def change_directory_protected(changeTo):
    try:
        if(changeTo=="~"):
            home = str(Path.home())
            os.chdir(home)
        else:
            os.chdir(changeTo)
    except:
        sys.stdout.write(f"{changeTo}: No such file or directory\n")

def handle_Path(command,path,line):

    for directory in path:
        full_path = os.path.join(directory,command)
        if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
            try:
                os.system(line)
                return ''
            except:
                return f'{command} is {full_path}'
    return f"{command}: not found\n"

def handle_type(command,path,line):
    builtin_list = ["echo","exit","type"]
    if command in builtin_list:
        return f"{command} is a shell builtin\n"
    return handle_Path(command,path,line)


def handle_response(line,path) -> bool:
    commands = line.split(" ")
    match(commands[0]):
        case "exit":
            if commands[1]=="0":
                return False
        case "echo":
            sys.stdout.write(f"{' '.join(map(str,commands[1:]))}\n")
            return True
        case "type":
            text = handle_type(commands[1],path,line)
            if(text!=''):
                sys.stdout.write(handle_type(commands[1],path,line))
            return True
        case "pwd":
            sys.stdout.write(os.getcwd()+"\n")
            return True
        case "cd":
            change_directory_protected(commands[1])
            return True
        case _:
            sys.stdout.write(handle_Path(commands[0], path, line))
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
