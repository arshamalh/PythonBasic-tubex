from Ex09_Factorial import factorial
def sin(degree, accuracy):
    result = 0
    j = 0
    for i in range(1, accuracy+1):
        result += degree ** (2*i-1) * (-1) ** j / factorial(2 * i - 1)
        j += 1
    result = round(result, 2)
    return result
if __name__ == '__main__':
    print(sin(float(input('Enter the degree: ')), int(input('Enter the accuracy: '))))