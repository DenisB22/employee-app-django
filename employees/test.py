number = 'a'
try:
    number = int(number)
except ValueError:
    number = None

print(number)

if type(number) == int:
    print('Yes')