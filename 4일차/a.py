inventory = {'팥붕어빵' : 10, '슈크림붕어빵' : 8, '초코붕어빵' : 5}




# ====================================================
# =============================================================
while True:
    fish_order = input('붕어빵의 종류를 입력해주세요. 종료하려면("종료")\n')
    if fish_order == '매니저 모드':
        add_fish = input ('(매니저 모드) 추가할 붕어빵을 입력해주세요. 종료하려면("종료")\n')
        if add_fish == '종료':
            continue
        if add_fish not in inventory.keys():
            print ('유효하지 않은 주문입니다.')
            continue
        add_fish_count = int(input('개수를 입력해주세요.'))
        if add_fish in inventory.keys():
            inventory[add_fish] += add_fish_count
        print(inventory)
        continue
    if fish_order == '종료':
        break
    if fish_order not in inventory.keys():
        print ('유효하지 않은 주문입니다.')
        continue
    fish_count = int(input('개수를 입력해주세요.'))
    order = {fish_order : fish_count}
    if fish_order in inventory.keys() and fish_count <= inventory[fish_order]:
        print(f'{fish_order}이 {fish_count}개 판매 되었습니다.')
        inventory[fish_order] -= fish_count
        print(f'남은 재고는 {inventory}입니다.')
    elif fish_order in inventory.keys() and fish_count > inventory[fish_order]:
        print('재고가 없습니다.')