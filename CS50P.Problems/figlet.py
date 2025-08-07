import pyfiglet
import sys
import random


def main():
    fonts = pyfiglet.FigletFont.getFonts()

    if len(sys.argv) == 1:
        font = random.choice(fonts)
    elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
        if sys.argv[2] not in fonts:
            sys.exit()
        font = sys.argv[2]
    else:
        sys.exit

    text = input("Input: ")
    figlet = pyfiglet.Figlet(font=font)
    print(figlet.renderText(text))

if __name__ == "__main__":
    main()