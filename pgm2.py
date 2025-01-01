def change_char(str):
    char=str[0]
    str=str.replace(char,'$')
    str=char+str[1:]
    return str
str=input("Enter the word:")
s=change_char(str)
print(s)



