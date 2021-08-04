import sys
import random

#first=sys.argv[1]
#last=sys.argv[2]
first=1
last=10
print(f'hey user pick a number between {first} and {last}')

try:
    user_choice=int(input('enter your choice '))
except ValueError as e:
    print('enter a number not anything else')
except:
    print('something wrong here......:(')

if user_choice<=0:
    print('enter between 1 and 10 please')
elif user_choice>10:
    print('enter between 1 and 10 please')

op=random.choice(range(first,last+1))

if user_choice == op:
    print('lucky boy')
else:
    print('better luck next time')

print(f'computer guess was {op}')
