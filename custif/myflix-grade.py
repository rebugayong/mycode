#!/usr/bin/env python3
message = ', your grade is '
messageA = 'Excellent'
messageB = 'Well done'
messageC = 'Good'
print('What is your numeric score?')
connection = float(input())
if connection >= 90:
    message = messageA + message + 'A.'
elif connection >= 80:
    message = messageB + message + 'B.'
elif connection >= 70:
    message = messageC + message + 'C.'
elif connection >= 60:
    message = message + 'D.'
else:
    message = message + 'F - Study harder.'
print(message)