import random

from g3sta import G3STA_PATH


def main():
    print("KeyboardInterrupt to quit, ENTER for a new quote\n")
    while True:
        with open(G3STA_PATH, "r", encoding="utf-8") as f:
            input(random.choice(f.read().split("\n")))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        quit(0)
