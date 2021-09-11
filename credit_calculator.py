
import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--type', choices=['annuity', 'diff'], help='Incorrect parameters')
parser.add_argument('--principal')
parser.add_argument('--payment')
parser.add_argument('--periods')
parser.add_argument('--interest')
args = parser.parse_args()

all_parameters = [args.type, args.principal, args.payment, args.periods,
                  args.interest]
if args.principal == None:
    pass
else:
    args.principal = int(args.principal)

if args.payment == None:
    pass
else:
    args.payment = int(args.payment)

if args.periods == None:
    pass
else:
    args.periods = int(args.periods)

if args.interest == None:
    pass
else:
    args.interest = float(args.interest)

if args.type != 'diff' and args.type != 'annuity':
    print('Incorrect parameters')

if args.type == 'diff' and args.payment == None:
    print('Incorrect parameters.')

if len(all_parameters) < 4:
    print('Incorrect parameters.')

if args.type == 'annuity' and args.interest == None:
    print('Incorrect parameters.')

if args.type == 'diff':
    if args.interest == None:
        print('Incorrect parameters.')
    else:
        i = args.interest / (12 * 100)
        m = 0
        month_payment_counter = 0
        while m <= args.periods:
            m += 1
            month = math.ceil((args.principal / args.periods) + i * (
                        args.principal - ((args.principal * (m - 1)) / args.periods)))
            month_payment_counter += month - (args.principal / args.periods)
           # month_payment_counter = month_2 - args.principal
            print(f'Month {m}: payment is {month}')
        print()
        print(f'Overpayment = {int(month_payment_counter)}')

if args.type == 'annuity':
    if args.interest == None:
        print('Incorrect parameters.')
    else:
        if args.periods and args.principal != None:
            i = args.interest / (100 * 12)
            annuity_payment = math.ceil(
                args.principal * ((i * (1 + i)**args.periods)) / ((1 + i)**args.periods - 1))
            overpayment = annuity_payment * args.periods - args.principal
            print(f'Your annuity payment = {annuity_payment}!')
            print(f'Overpayment = {overpayment}')
        if args.payment and args.periods != None:
            i = args.interest / (100 * 12)
            loan_principal = args.payment / (
                        (i * pow(1 + i, args.periods)) / (pow(1 + i, args.periods) - 1))
            overpayment = int(math.ceil(args.periods * args.payment - loan_principal))
            print(f'Your loan principal = {loan_principal}!')
            print(f'Overpayement = {overpayment}')
        if args.principal and args.payment != None:
            i = args.interest / (100 * 12)
            num_of_months = math.ceil(
                math.log((args.payment / (args.payment - i * args.principal)), 1 + i))
            if num_of_months == 12:
                years = 1
                print(f'It will take {years} year to repay this loan!')
            elif num_of_months % 12 == 0:
                years = int(num_of_months / 12)
                print(f'It will take {years} years to repay this loan!')
            elif num_of_months == 1:
                print(f'It will take {num_of_months} month to repay this loan!')
            elif num_of_months < 12:
                print(f'It will take {num_of_months} months to repay this loan!')
            else:
                years = math.floor(num_of_months / 12)
                months = int((num_of_months / 12 - years) * 12)
                print(f'It will take {years} years and {months} months to repay this loan!')
            overpayment = int(math.ceil(num_of_months * args.payment - args.principal))
            print(f'Overpayment = {overpayment}')
