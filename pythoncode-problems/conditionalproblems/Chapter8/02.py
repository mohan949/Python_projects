f  = int(input('enter the temperature: '))


def convertFtoC(f):
    c = 5*(f-32)/9
    return c



print(f'converted values is: {round(convertFtoC(f), 2)}')