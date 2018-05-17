import re

def print_complex(a=0, b=0):
    a = str(a)
    b = str(b)
    if b == 0:
        im = re.findall(r'\d*i', a)
        print('found')
    real = b
    return real, im[0][:-1]

if __name__ == '__main__':
    print(print_complex(356i))