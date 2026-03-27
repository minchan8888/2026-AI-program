'''
#for문을 이용한 리스트의 문자열 객체 순회
summer_fruits = ['수박', '참외', '체리', '포도']
for fruit in summer_fruits:
    print(fruit, end = ' ')
    
#3-36 중첩 for문을 사용하 구구단 출력
for i in range(2,10): #외부for루프
    for j in range(1,10): #내부for 루프
        print('{}*{} = {:2d}'.format(i,j,i*j),end='')
    print() # 내부 루프 수행 후 줄바꿈을 함

#
n = 7
for i in range(n):
    st = ''
    for j in range(i): # 내부 for 루프는 i번 수행
        st = st + ' ' # 공백을 i개 추가함
    print(st + '#') # 공백 추가 후 '#'출력
    
n = 7
for i in range(n):
    print (' ' * i + '#')
'''
#소수 구하기
n =int(input('수를 입력하세요:'))
is_prime = True
for num in range(2,n):
    if n % num == 0:
        is_prime = False
print(n,'is prime:',is_prime)
#위의 코드는 비효율적임 -> 트루이면 더 할것이 필요하지 않고 break사용
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    