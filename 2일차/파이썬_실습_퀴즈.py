# 난수 생성
import random

# 시작 문구
print ('숫자 맞추기 게임...')
print ('1~100까지의 수들 중 무작위로 선택된 수를 맞춰보세요...')

# 랜덤 선택
answer_num = random.randint(1,100)

# 시도 횟수
player_try = 0

# 성공할때까지 반복
while True:
    guess = int(input('숫자를 입력하세요...(1~100)'))
    player_try += 1
    
    #결과
    if guess == answer_num:
        print('축하드립니다 정답입니다!')
        print(f'기록은 {player_try} 번입니다!')
        break #이 시점에서 반복문 종료
    elif guess > answer_num:
        print('틀렸습니다. 더 작은 숫자입니다.')
    elif guess < answer_num:
        print('틀렸습니다. 더 큰 숫자입니다.')