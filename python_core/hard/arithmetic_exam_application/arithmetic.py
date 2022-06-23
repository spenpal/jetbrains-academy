import re
import random

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()
        
def verify_expr(expr):
    return re.search(r'\d [\+\-\*] \d', expr)

def generate_expr():
    left, right = str(random.randint(2, 9)), str(random.randint(2, 9))
    op = random.choice(['+', '-', '*'])
    expr = ' '.join([left, op, right])
    ans = eval(expr)
    return expr, ans

def generate_squares():
    num = random.randint(11, 29)
    sqaure = num ** 2
    return num, sqaure
    
# MAIN #
level_str = """Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29
"""
n = 5

level = input(level_str)
while not (is_integer(level) or level in ['1', '2']):
    print('Incorrect format.')
    level = input()

if level == '1':
    for _ in range(n):
        expr, ans = generate_expr()
        print(expr)
        
        user_ans = input()
        while not is_integer(user_ans):
            print('Incorrect format.')
            user_ans = input()
            
        if int(user_ans) == ans:
            print('Right!')
        else:
            print('Wrong!')
            n -= 1
else:
    for _ in range(n):
        num, ans = generate_squares()
        print(num)
        
        user_ans = input()
        while not is_integer(user_ans):
            print('Incorrect format.')
            user_ans = input()
            
        if int(user_ans) == ans:
            print('Right!')
        else:
            print('Wrong!')
            n -= 1

save = input(f'Your mark is {n}/5. Would you like to save your result to the file? Enter yes or no.\n')
if save in ['yes', 'YES', 'y', 'Yes']:
    name = input('What is your name?\n')
    with open('results.txt', 'a+') as f:
        level_desc = 'simple operations with numbers 2-9' if level == 1 else 'integral squares 11-29'
        f.write(f'{name}: {n}/5 in level {level} ({level_desc}).\n')
        print('The results are saved in "results.txt".')
    f.close()