def exchange_char(str):
    if len(str) <=1:
        return str
    return str[-1] + str[1:-1] + str[0]
input_str = input("Enter a string:")
result = exchange_char(input_str)
print("Modified string:",result)


