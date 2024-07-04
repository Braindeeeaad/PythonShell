import sys

def repl():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        line = input()
        command = line.split(" ")
        if(command[0]=="exit" and command[1]=="0"):
            return
        sys.stdout.write(f"{line}: command not found\n")


def main():
    repl()



if __name__ == "__main__":
    main()
