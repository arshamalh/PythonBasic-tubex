# Write a Python class to convert an integer to a roman numeral.
# Write a Python class to convert a roman numeral to an integer.
class RoInt:
    val = [1000,
           900, 500, 400, 100,
           90, 50, 40, 10,
           9, 5, 4, 1]
    syb = ["M",
           "CM", "D", "CD", "C",
           "XC", "L", "XL", "X",
           "IX", "V", "IV", "I"]

    def __init__(self, number):
        self.isint = True
        try:
            self.number = int(number)
        except ValueError:
            self.number = number
            self.isint = False

    def convert(self):
        if self.isint:
            roman_num = ''
            i = 0
            while self.number > 0:
                for _ in range(self.number // self.val[i]):
                    roman_num += self.syb[i]
                    self.number -= self.val[i]
                i += 1
            return roman_num
        else:
            pass



for i, num in enumerate(range(1, 30), start=1):
    print(f'{i}: {RoInt(num).convert()}')
