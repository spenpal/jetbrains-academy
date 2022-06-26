import sys
import random


num_of_friends = int(input('Enter the number of friends joining (including you):\n'))
print()

if num_of_friends < 1: 
    print('No one is joining for the party')
    sys.exit()
    
print('Enter the name of every friend (including you), each on a new line:')
friends = [input().strip() for _ in range(num_of_friends)]
print()

total_bill = float(input('Enter the total bill value:\n'))
print()

lucky_feature = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:') == 'Yes'
print()

if lucky_feature:
    lucky_friend = random.choice(friends)
    print(f'{lucky_friend} is the lucky one!\n')
    
    bill_split_value = round(total_bill / (num_of_friends - 1), 2)
    bills = dict.fromkeys(friends, bill_split_value)
    bills[lucky_friend] = 0
else:
    print('No one is going to be lucky\n')
    
    bill_split_value = round(total_bill / num_of_friends, 2)
    bills = dict.fromkeys(friends, bill_split_value)

print(bills)