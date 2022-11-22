ques = 'What is the Capital of India?'
oA = 'A. Delhi'
oB = 'B. Mumbai'
oC = 'C. Kolkata'
oD = 'D. Chennai'

print('Welcome to the quiz')
print(ques)
print('-' * 10)
print(f'a){oA}')
print(f'b){oB}')
print(f'c){oC}')
print(f'd){oD}')
print('-' * 10)

ans = input('Enter your answer: ')
if ans == 'A' or ans == 'a':
  print('Correct✅')
else:
  print('Incorrect ❌🤔')
