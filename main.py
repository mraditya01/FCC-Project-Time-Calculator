# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main


print(add_time("11:59 PM", "24:05"))
print(add_time("8:16 PM", "466:02", "tuesday"))
