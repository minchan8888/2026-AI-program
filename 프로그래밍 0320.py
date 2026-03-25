'''
num = 100
print('num=',num)
num = 200
print('num=',num)
'''
'''
num = 0
for i in range(100):
    num += 100
    print('ith num',i,num)
#0부터 100사이 범위를 배정
# i+=100이면 i=i+10이라는 뜻


#나이가 20세 미만이면 청소년 할인을 출력하는 기능
age = int(input("나이를 입력하세요:"))
if age <20:
    print('청소년 할인')
elif age >=65:
    print('경로 우대')

'''
#input 뒤에 있는 문장을 컴퓨터가 인식할 수 있게 int로 변경해줌
#if+조건문(만약에), elif+조건문(그렇지 않는것들 중에 만약에),
#    else뒤에는 조건문 없어도 됨(그렇지 않으면)
'''

#시간이 12시가 안되면 오전입니다 출력하는 기능
time = int(input('시간을 입력하세요:'))
if time<12:
    print('오전입니다')
else:
    print('오후입니다')
''' 
  
num = int(input('숫자를 입력하세요.'))
if num<0:
    print(num,'은(는) 음수입니다.')
elif num%2 == 0:
    print(num,'은(는) 짝수입니다.')

else:
    print(num,'은(는) 홀수입니다.')


    
    


    
    
    
    