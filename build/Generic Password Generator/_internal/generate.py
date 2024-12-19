from random import randrange

lower: str = 'qwertyuiopasdfghjklçzxcvbnm'
upper: str = 'QWERTYUIOPASDFGHJKLÇZXCVBNM'
numbers: str = '0123456789'
special: str = r'!@#$%&*()_+={}[]:;?-/'

char_bases = dict(lower=lower, upper=upper, numbers=numbers, special=special)

def gen(base: dict = char_bases, length: int = 8, lower: bool = True, upper: bool = True, numbers: bool = True, special: bool = True) -> str:
    password_base: str = ''
    password: str = ''

    if lower == True:
        password_base += str(base.get('lower'))
    if upper == True:
        password_base += str(base.get('upper'))
    if numbers == True:
        password_base += str(base.get('numbers'))
    if special == True:
        password_base += str(base.get('special'))
    
    i = length
    while i > 0:
        password += password_base[randrange(0, len(password_base))]
        i -= 1
    
    return password