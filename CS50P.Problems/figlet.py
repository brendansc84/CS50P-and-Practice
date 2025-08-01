import pyfiglet
import sys
import random

if len(sys.argv) == 1:
    text = input("Input: ")
else:
    text = sys.argv[1]

fonts = pyfiglet.FigletFont.getFonts()
font = random.choice(fonts)
figlet = pyfiglet.Figlet(font=font)

print("Output: \n" + figlet.renderText(text))