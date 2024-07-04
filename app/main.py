import sys

def typeResponse(arg):
    builtin_list = ["echo","exit","type"]
    if arg in builtin_list:
        return f"{arg} is a shell builtin\n"
    return f"{arg}: not found\n"
def handle_response(line) -> bool:
    command = line.split(" ")
    match(command[0]):
        case "exit":
            if command[1]=="0":
                return False
        case "echo":
            sys.stdout.write(f"{' '.join(map(str,command[1:]))}\n")
            return True
        case "type":
            sys.stdout.write(typeResponse(command[1]))
            return True

    sys.stdout.write(f"{line}: command not found\n")
    return True
def repl():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        line = input()
        if not handle_response(line):
            return



def main():
    repl()



if __name__ == "__main__":
    main()
