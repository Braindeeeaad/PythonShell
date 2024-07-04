import sys


def main():
    # Uncomment this block to pass the first stage
     sys.stdout.write("$ ")
     sys.stdout.flush()

    # Wait for user input
     command = input()

     sys.stdout.write(f"\n{command}: command not found")


if __name__ == "__main__":
    main()
