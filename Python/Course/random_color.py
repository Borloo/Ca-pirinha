import random
from sty import fg

def getTextColored(text):
    r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    return fg(r,g,b) + text + fg.rs

print(getTextColored("hello"))