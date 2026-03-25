# 1.대화식 모드에서 출력하기
print('나의 이름은:','홍길동')
print('나의 나이는:','27')
print('나의 키는:',179,'cm입니다')
print('10+20=',10+20)
print('10*20=',10*20)

#원의 반지름, 면적, 둘레를 출력하는 프로그램
# print('원의 반지름',4.0)
# print('원의 면적',3.14*4.0*4.0)
# print('원의 둘레',2.0*3.14*4.0)
# 
#변수를 이용하여 원의 면적과 둘레를 구하는 방법
# radius = 4.0
# print('원의 반지름',radius)
# print('원의 면적',3.14*radius*radius)
# print('원의 둘레',2.0*3.14*radius)


#4. 다음코드를 입력해보고 그 출력결과를 밑줄부분에 적으시오
name = '전우치'
print('나의 이름은:',name)
age = 27
print('나의 나이는:',age)
height =179
print('나의 키는',height,'cm입니다.')
sum=10+20
print('10+20=',sum)
mult=10*20
print('10*20=',mult)

#6. 변수 값의 재지정
width = 20
height = 40
width = 30
area = width * height
print('사각형의 면적',area)


#8.복소수의 연산
c1 = 8+2j
c2 = 4+3j
print(c1+c2)
print(c1-c2)
print(c1*c2)
print(c1/c2)

#9. 비트 연산 활용
a = 1024
print(a>>1)

print(a>>2)

a=a>>1
print(a)

a=1
print(a<<1)

a=a<<1
print(a)

#10. 사용자 입력 받기
name = input('이름을 입력하세요:')
print(name,'님이 입장하셨습니다.')

m=int(input('숫자m을 입력하세요:'))
n=int(input('숫자n을 입력하세요:'))
print('m+n=',m+n)
print('m-n=',m-n)

radius=int(input('radius를 입력하세요:'))
print('원의 면적',3.14*radius*radius)


