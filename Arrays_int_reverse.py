def reverse_integer(n):
    lis = split_num(n)
    return str(conc_num(lis)).zfill(len(lis))

    


def split_num(num):
    lis = []
    while num > 0:
        lis.append(num % 10)  # Extract last digit
        num //= 10  # Integer division to remove the last digit
    return lis


def conc_num(lis):
    num = 0
    for i in lis:
        num = num *10 + i  # Shift number left and add new digit
    return num


# Test cases
print(reverse_integer(1234))  # Output: 4321
print(reverse_integer(9876))  # Output: 6789
print(reverse_integer(1000))  # Output: 1
print(reverse_integer(0))     # Output: 0
