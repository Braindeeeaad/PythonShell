import sys

def repl():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        command = input()

        sys.stdout.write(f"{command}: command not found\n")


def main():
    repl()



if __name__ == "__main__":
    main()
