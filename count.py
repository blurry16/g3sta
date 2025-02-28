from sys import argv

from g3sta import G3STA_PATH


def readdata():
    with open(G3STA_PATH, "r", encoding="UTF-8") as g3sta_file:
        return g3sta_file.read().split("\n")


if __name__ == "__main__":
    argv = [i.lower() for i in argv[1:]]

    with open(G3STA_PATH, "r", encoding="UTF-8") as g3sta_file:
        c = len(g3sta_file.read().split("\n"))

    if "-n" not in argv and "--no-paste" not in argv:
        with open("readme", "r", encoding="utf-8") as readme_file:
            d = readme_file.read().split("\n")
        with open("readme", "w", encoding="UTF-8") as readme_file:
            d[1] = f"quotes count: {c}"
            print(d[1])
            readme_file.write("\n".join(d))
