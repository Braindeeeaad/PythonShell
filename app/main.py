import os
import sys

def logging(text):
    with open('log.text','w') as file:
        file.write(text)

def handle_Path(command,path):
    for directory in path:
        full_path = os.path.join(directory,command)
        logging(f"Full Path:{full_path}")
        if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
            return f"{command} is {full_path}\n"
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
            sys.stdout.write(handle_type(command[1],path))
            return True

    sys.stdout.write(f"{line}: command not found\n")
    return True



def main():
    while True:
        try:

            sys.stdout.write("$ ")
            sys.stdout.flush()

            # Wait for user input
            path_env = os.environ.get('Path', '')
            logging(f"Path Recieved: {path_env}")
            line = input()
            if not handle_response(line,path_env.split(":")):
                return
        except(EOFError,KeyboardInterrupt):
            break



if __name__ == "__main__":
    main()
