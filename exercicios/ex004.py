from curses.ascii import isblank, isupper


str = input("Digite algo: ")
print(type(str))
print(str.isspace())
print(str.isnumeric())
print(str.isalpha())
print(str.isalnum())
print(str.isupper())
print(str.islower())
print(str.istitle)