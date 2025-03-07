import random

from g3sta import G3STA_PATH

if __name__ == '__main__':
    while True:
        with open(G3STA_PATH, "r", encoding="utf-8") as f:
            print(random.choice(f.read().split("\n")))
        if input("continue? y/n ").strip().lower() == "n":
            exit()
        