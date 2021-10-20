
def convert_integer_to_roman(x):
    integer_to_roman = {"1": "I", "4": "IV", "5": "V", "9": "IX", "10": "X",
    "40": "XL", "50": "L", "90": "XC", "100": "C", "400": "CD", "500": "D",
    "900": "CM", "1000": "M"}

    integer_keys_reverse = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    temp = ''
    x = int(x)
    for i in integer_keys_reverse:
        if x != 0:
            if i <= x:
                x = x- i
                temp = temp + str(integer_to_roman.get(i))

    return temp


#num = input('Enter a number: ' )
#result = convert_integer_to_roman(num)
#print(result)
