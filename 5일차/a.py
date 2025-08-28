class Bungeoppangshop:
    def __init__(self):
        
        self.stock = {
                "팥붕어빵": 10,
                "슈크림붕어빵": 8,
                "초코붕어빵": 5
            }
        
        self.prices = {
                "팥붕어빵": 1000,
                "슈크림붕어빵": 1200,
                "초코붕어빵": 1500
            }

        self.sales = {
                "팥붕어빵": 0,
                "슈크림붕어빵": 0,
                "초코붕어빵": 0
            }
        
    def check_stock(self):
        for bread, count in self.stock.items():
            print(f'{bread}: {count}개')

    def process_order(self, bread_type, bread_count):

        if bread_type not in self.stock.keys():
            print('없는 메뉴입니다.')
            return

        if bread_count > self.stock[bread_type]:
            print('재고가 부족합니다.')
            return

        else:
            self.stock[bread_type] -= bread_count
            self.sales[bread_type] += bread_count
            print (f'주문이 완료되었습니다.{bread_type} {bread_count}개')

    def admin_mode(self):

            print('관리자 모드를 시작합니다.')

            bread_type = input("추가할 붕어빵 종류:\n")

            bread_count = int(input('추가할 재고량:\n'))

            if bread_type not in self.stock.keys():
                print ('없는 메뉴입니다.')
                return

            if bread_type in self.stock.keys():
                self.stock[bread_type] += bread_count
                print (f'추가가 완료되었습니다. {bread_type}이 {bread_count}개 추가.')

    def calculate_total_sales(self):

        total_sales = 0

        for i,j in self.sales.items():
            total_sales += j * self.prices[i]
            
        print (f'총 매출: {total_sales}원')

def main():
    shop = Bungeoppangshop()

    print ('안녕하세요!')
    
    while True:
        mode = input('원하는 모드를 선택해주세요. (주문, 관리자, 종료)')

        if mode == "주문":
            while True:
                bread_type = input('주문할 붕어빵 종류를 입력해주세요.(종료 입력시 종료):\n')
                if bread_type == '종료':
                    break
                if bread_type in shop.stock.keys():
                    bread_count = int(input('주문할 개수를 입력해주세요\n'))
                    shop.process_order(bread_type,bread_count)
                else:
                    break
            
        if mode == '관리자':
            shop.admin_mode()
            continue

        if mode == "종료":
            break

        else:
            ('잘못된 입력입니다.')
            break

    shop.calculate_total_sales()
    print('종료되었습니다.')

if __name__ == "__main__" :
    main()

