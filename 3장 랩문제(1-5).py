#3-1 if 문의 사용법
'''
game_score = int(input('게임점수를 입력하세요:'))
if game_score >= 1000:
    print('당신은 고수입니다.')
    
num_a = int(input('num_a를 입력하세요:'))
num_b = int(input('num_b를 입력하세요:'))
if num_a == num_b:
    print('두 값이 일치합니다.')
'''

#3-2 변수와 if 조건식 사용하기
'''
n=int(input('정수를 입력하세요:'))

if num<0:
    print(num,'은(는) 음수입니다.')
    
elif num%2 == 0:
    print(num,'은(는) 짝수입니다.')

else:
    print(num,'은(는) 홀수입니다.')
'''

#3-3 if 조건문의 응용
'''
game_score = int(input('게임점수를 입력하세요:'))
if game_score >= 1000:
    print('고수입니다.')
else:
    print('입문자입니다.')
    
    
num_a = int(input('num_a를 입력하세요:'))
num_b = int(input('num_b를 입력하세요:'))
if num_a == num_b:
    print('두 값이 일치합니다.')
else:
    print('두 값이 일치하지 않습니다.')

a= int(input('당신은 성인인가요(성인이면 1, 미성년이면 0):'))
if a == 0:
    print('당신은 미성년자입니다')
elif a==1:
    b= int(input(('결혼을 하셨나요?(기혼이면 1, 미혼이면 0):')))
    
if b ==1:
    print('당신은 결혼한 성인입니다.')
else:
    print('당신은 결혼하지 않은 성인입니다.')
    
'''
    
#3-4 복합 조건식의 이해
'''
num =2
print(1<num<10)

age=int(input('나이를 입력하세요:'))
if 10<age<19:
    print('청소년입니다.')
'''

#3-5 if-elif-else문을 사용한 다중 조건식
speed=int(input('자동차의 속도를 입력하세요(단위:km/h):'))
if speed >= 100 :
    print('고속')
elif 60 <= speed < 100:
    print('중속')
else:
    print('저속')













    