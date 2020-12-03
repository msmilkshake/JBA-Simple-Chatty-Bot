name = input('Hello! My name is Aid.\n'
             'I was created in 2020.\n'
             'Please, remind me your name.\n')

print(f'What a great name you have, {name}!\n'
      'Let me guess your age.\n'
      'Enter remainders of dividing your age by 3, 5 and 7.')

r3, r5, r7 = (int(input()) for i in range(3))
age = (r3 * 70 + r5 * 21 + r7 * 15) % 105

print(f'Your age is {age}; that\'s a good time to start programming!\n'
      'Now I will prove to you that I can count to any number you want.')

print(*(f'{n} !' for n in range(int(input()) + 1)), sep='\n')

print('Let\'s test your programming knowledge.\n'
      'Why do we use methods?\n'
      '1. To repeat a statement multiple times.\n'
      '2. To decompose a program into several small subroutines.\n'
      '3. To determine the execution time of a program.\n'
      '4. To interrupt the execution of a program.')
while True:
    if int(input()) == 2:
        break
    print('Please, try again.')

print('Completed, have a nice day!\n'
      'Congratulations, have a nice day!')
