from sys import argv

from g3sta import G3STA_PATH


<<<<<<< HEAD:genreadme.py
readme = """g3sta - g3rm4n pasta, цитаты легенды"""


=======
>>>>>>> 6b6d06c1556889d5674540ad002bcf084efc2a55:count.py
if __name__ == "__main__":
    argv = [i.lower() for i in argv[1:]]

    with open(G3STA_PATH, "r", encoding="UTF-8") as g3sta_file:
        c = len(g3sta_file.read().split("\n"))
    readme += f"\nquotes count: {c}"
    print(readme)
    if "-n" not in argv and "--no-paste" not in argv:
        with open("readme", "w", encoding="UTF-8") as readme_file:
            readme_file.write(readme)
