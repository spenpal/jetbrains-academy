# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):" 
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

msgs = [msg_0, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]
memory = 0

def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2): msg += msg_6
    if (v1 == 1 or v2 == 1) and v3 == '*': msg += msg_7
    if (v1 == 0 or v2 == 0) and (v3 == '*' or v3 == '+' or v3 == '-'): msg += msg_8
    if msg != '': msg = msg_9 + msg
    print(msg)
    
def is_one_digit(v):
    return -10 < v < 10 and v.is_integer()
    
while True:
    calc = input(msg_0)
    x, oper, y = calc.split()
    
    if x == 'M': x = memory
    if y == 'M': y = memory
    
    try:
        x, y = float(x), float(y)
    except ValueError:
        print(msg_1)
        continue
    
    if oper not in ['+', '-', '*', '/']:
        print(msg_2)
        continue
    
    check(x, y, oper)
    
    result = None
    if oper == '+': result = x + y
    elif oper == '-': result = x - y
    elif oper == '*': result = x * y
    elif oper == '/' and y != 0: result = x / y
    else:
        print(msg_3)
        continue
    print(result)
    
    store_result = input(msg_4)
    if store_result == 'y': 
        if not is_one_digit(result): memory = result
        else:
            msg_index = 10
            while True:
                answer = input(msgs[msg_index])
                if answer == 'y':
                    if msg_index < 12: 
                        msg_index += 1
                        continue
                    else: memory = result
                break
        
    continue_calc = input(msg_5)
    if continue_calc == 'y': continue
    
    break