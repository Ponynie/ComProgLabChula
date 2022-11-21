def sum_digits(s) :
    Number = [str(i) for i in range(0,10)]
    Number_in_string = [int(i) for i in s if i in Number]
    result = sum(Number_in_string)

    return result

print(sum_digits("zz1xa2d3"))
print(sum_digits("bb11c33"))
print(sum_digits("5432d"))
print(sum_digits("Hello"))