import random

# 게임 초기화
def initialize_game(n):

    board_size = n
    x1 = random.randint(1,n-1)
    y1 = random.randint(1,n-1)
    treasure_position = (x1, y1)
    x2 = random.randint(1,n-1)
    y2 = random.randint(1,n-1)
    player_position = (x2, y2)
    return treasure_position, board_size, player_position

# 거리 계산
def calculate_distance(treasure_position, player_position):

    distance = abs(treasure_position[0] - player_position[0]) + abs(treasure_position[1] - player_position[1])

    return distance

# 플레이어 이동
def move_player(board_size, player_position, direction):

    x2, y2 = player_position

    if direction == 'N':
        new_x2, new_y2 = x2, y2 + 1
    elif direction == 'S':
        new_x2, new_y2 = x2, y2 - 1
    elif direction == 'E':
        new_x2, new_y2 = x2 + 1, y2
    elif direction == 'W':
        new_x2, new_y2 = x2 - 1, y2

    if 0 <= new_x2 <= board_size and 0 <= new_y2 <= board_size:
        return new_x2, new_y2
    else:
        print(f'보드의 범위를 벗어났습니다. 현재 위치는 {player_position}')

    

# 게임 실행
def play_game(board_size):

    treasure_position, board_size, player_position = initialize_game(board_size)
    print("🚩 보물 찾기 게임에 오신 것을 환영합니다! 🚩")
    print(f"보드의 크기는 {board_size}x{board_size}입니다.")
    print("북(N), 남(S), 동(E), 서(W) 중 한 방향을 입력하여 보물을 찾아보세요.")
    player_try = 0
    while player_position != treasure_position:
        distance =  calculate_distance(treasure_position, player_position)
        print (f'현재 보물과의 거리는 {distance} 입니다.')
        print (f'현재 플레이어 위치는 {player_position} 입니다.')
        direction = input("어느 방향으로 이동하시겠습니까? (N/S/E/W): ")
        if direction in ['N', 'S', 'E', 'W']:
            player_position = move_player(board_size, player_position, direction)
            player_try += 1
        else:
            print (f'잘못 입력하셨습니다.')

    
    print("축하합니다! 보물을 찾았습니다! ")
    print(f"총 {player_try}번의 시도 끝에 보물을 찾았습니다.")
    print(f"보물의 위치는 {treasure_position}였습니다.")
        
    

# 게임 보드 크기 설정 및 게임 시작
if __name__ == "__main__":
    board_size = 5  # 보드 크기를 5x5로 설정
    
    play_game(board_size)