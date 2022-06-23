import math
import argparse
import sys

def overpayment(total, principal):
    return total - principal
    
def monthly_payments(P, A, interest):
    i = (interest / 100) / 12
    
    n = math.log(A / (A - i * P), 1 + i)
    n = math.ceil(n)
    
    years, months = divmod(n, 12)
    plurality = months != 1
    
    op = overpayment(A * n, P)
    
    if years == 0: print(f"It will take {months} month{'s' * plurality} to repay this loan!")
    elif months == 0: print(f"It will take {years} years to repay this loan!")
    else: print(f"It will take {years} years and {months} month{'s' * plurality} to repay this loan!")
    
    print(f'Overpayment = {op}')
    
def annuity_monthly_payment(P, n, interest):
    i = (interest / 100) / 12
    
    A = P * ((i * (1 + i) ** n) / ((1 + i) ** n - 1))
    A = math.ceil(A)
    
    op = overpayment(A * n, P)
    
    print(f'Your annuity payment = {A}')
    print(f'Overpayment = {op}')
    
def loan_principal(A, n, interest):
    i = (interest / 100) / 12
    
    P = A / ((i * (1 + i) ** n) / ((1 + i) ** n - 1))
    P = math.ceil(P)
    
    op = overpayment(A * n, P)
    
    print(f'Your loan principal = {P}!')
    print(f'Overpayment = {op}')

def diff_payments(P, n, interest):
    i = (interest / 100) / 12
    dps = []
    
    for m in range(1, n + 1):
        dp = (P / n) + (i * (P - ((P * (m - 1)) / n)))
        rounded_dp = math.ceil(dp)
        dps.append(rounded_dp)
        print(f'Month {m}: payment is {rounded_dp}')
    
    op = overpayment(sum(dps), P)
    print(f'Overpayment = {op}')

# MAIN
parser = argparse.ArgumentParser()
parser.add_argument('--type', choices = ['annuity', 'diff'])
parser.add_argument('--payment', type=int)
parser.add_argument('--principal', type=float)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)
args = parser.parse_args()

# error checking
error_conditions = (
    len(sys.argv) < 4
    or args.type not in ['annuity', 'diff']
    or args.type == 'diff' and args.payment
    or not args.interest
    or any(arg < 0 for arg in vars(args).values() if type(arg) in [float, int])
)

if error_conditions:
    print('Incorrect parameters')
    exit()
    
if args.type == 'diff':
    diff_payments(args.principal, args.periods, args.interest)
elif args.type == 'annuity' and not args.payment:
    annuity_monthly_payment(args.principal, args.periods, args.interest)
elif args.type == 'annuity' and not args.principal:
    loan_principal(args.payment, args.periods, args.interest)
elif args.type == 'annuity' and not args.periods:
    monthly_payments(args.principal, args.payment, args.interest)