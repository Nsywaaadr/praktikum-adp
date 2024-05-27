from termcolor import colored, cprint
import os
os.system('cls')

cprint(" " * 21, "blue", "on_blue")
cprint(" " * 21, "blue", "on_blue")
cprint(" " * 21, "blue", "on_white")

print(colored("       V", 'blue', 'on_white', attrs=["bold", "blink"]), end="")
print(colored(" I", 'blue', 'on_white', attrs=["bold", "blink"]), end="")
print(colored(" S", 'blue', 'on_white', attrs=["bold", "blink"]), end="")
print(colored(" A       ", 'blue', 'on_white', attrs=["bold", "blink"]))

cprint(" " * 21, "blue", "on_white")
cprint(" " * 21, "yellow", "on_yellow")
cprint(" " * 21, "yellow", "on_yellow")