from predict import *
from ad import *
ner_bert = NER_BERT()
import time
def check(text):
    yes = 'có Có Đúng'
    for i in text.split(' '):
        if i in yes.split(' '):
            return True
    return False
print('Đây là chatbot, hỗ trợ tìm kiếm và cung cấp một số thông tin về bất đông động sản bạn cần tìm!')
while True:
    new_value = input("Enter: ")
    if len(new_value)> 0:
        kq =ner_bert.evaluate_one_text(new_value)
        print(kq)
        if len(kq) >0:
            print(f'Bạn tìm bất động sản xung quanh {kq}?')

            new_value = input("Enter chat: ")
            if check(new_value):
                print(f'Sau đây một số kết quả tìm kiếm được ...')
                time.sleep(2)
                print('------------------------------------------------------------------')
                property_1 = {
                    'loại_bất_động_sản': 'chung cư',
                    'địa_điểm': 'Hà Nội',
                    'diện_tích': 70,
                    'giá': 1.2e9,
                    'mô_tả': 'Căn hộ cao cấp có 2 phòng ngủ và 2 nhà vệ sinh, nằm ở tầng 10 của tòa nhà, với view đẹp nhìn ra thành phố.'
                }

                # Thông tin bất động sản thứ hai
                property_2 = {
                    'loại_bất_động_sản': 'nhà riêng',
                    'địa_điểm': 'Hồ Chí Minh',
                    'diện_tích': 150,
                    'giá': 3.8e9,
                    'mô_tả': 'Nhà đẹp mới xây, có 3 phòng ngủ và 3 nhà vệ sinh, nằm trong khu vực yên tĩnh và an ninh tốt.'
                }
                print("Thông tin bất động sản 1:")
                for key, value in property_1.items():
                    print(f"{key}: {value}")
                print('------------------------------------------------------------------')
                print("\nThông tin bất động sản 2:")
                for key, value in property_2.items():
                    print(f"{key}: {value}")
                print('------------------------------------------------------------------')
                time.sleep(2)
                print('Bạn có muốn xem các trường học xung quanh bất động sản số 1 không?')
                new_value = input("Enter chat: ")
                if check(new_value):
                    time.sleep(2)
                    print('Sau đây mốt số trường xung quanh bất động sản bạn chọn ...')
                    search_nearby_venues()
                else:
                    print("Tôi có thể giúp gì bạn?")
            else:
                print("Tôi có thể giúp gì bạn?")




    # for i in search_address(new_value):
    #     print(i)
