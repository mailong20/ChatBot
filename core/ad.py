import requests
import urllib.parse
import html
import json


def encode_address(address):
    # Sử dụng hàm quote() để mã hóa địa chỉ sang chuẩn URL
    return urllib.parse.quote(address)


def search_address(address_text):
    url_address = encode_address(address_text)
    url = f"https://www.google.com/s?tbm=map&gs_ri=maps&suggest=p&authuser=0&hl=en&pb=!2i6!4m9!1m3!1d19270.715323104596!2d108.178457!3d16.0564886!2m0!3m2!1i788!2i965!4f13.1!7i20!10b1!12m13!1m1!18b1!2m3!5m1!6e2!20e3!10b1!16b1!17m1!3e1!20m2!5e2!6b1!19m4!2m3!1i360!2i120!4i8!20m57!2m2!1i203!2i100!3m2!2i4!5b1!6m6!1m2!1i86!2i86!1m2!1i408!2i240!7m42!1m3!1e1!2b0!3e3!1m3!1e2!2b1!3e2!1m3!1e2!2b0!3e3!1m3!1e8!2b0!3e3!1m3!1e10!2b0!3e3!1m3!1e10!2b1!3e2!1m3!1e9!2b1!3e2!1m3!1e10!2b0!3e3!1m3!1e10!2b1!3e2!1m3!1e10!2b0!3e4!2b1!4b1!9b0!22m2!1sdOdAZLmHJYOm2roPpraI6AQ!7e81!23m2!4b1!10b1!24m80!1m28!13m9!2b1!3b1!4b1!6i1!8b1!9b1!14b1!20b1!25b1!18m17!3b1!4b1!5b1!6b1!9b1!12b1!13b1!14b1!15b1!17b1!20b1!21b1!22b0!25b0!27m1!1b0!28b0!2b1!5m6!2b1!3b1!5b1!6b1!7b1!10b1!10m1!8e3!11m1!3e1!14m1!3b1!17b1!20m2!1e3!1e6!24b1!25b1!26b1!29b1!30m1!2b1!36b1!39m3!2m2!2i1!3i1!43b1!52b1!54m1!1b1!55b1!56m2!1b1!3b1!65m5!3m4!1m3!1m2!1i224!2i298!71b1!72m4!1m2!3b1!5b1!4b1!89b1!113b1!26m4!2m3!1i80!2i92!4i8!34m18!2b1!3b1!4b1!6b1!8m6!1b1!3b1!4b1!5b1!6b1!7b1!9b1!12b1!14b1!20b1!23b1!25b1!26b1!37m1!1e81!47m0!49m6!3b1!6m2!1b1!2b1!7m1!1e3!67m2!7b1!10b1!69i643&q={url_address}&tch=1&ech=10&psi=dOdAZLmHJYOm2roPpraI6AQ.1681975159206.1"
    respone = requests.get(url)
    texts = respone.text.replace('/*""*/', '')
    dictionary = json.loads(texts)
    x = dictionary["d"].split('\n')[1]
    address_info = html.unescape(x)
    address_list = json.loads(address_info)
    address_list = [(j[14][0], j[11]) for i in address_list[0][1] for j in i if j is not None and j[11] is not None]
    return address_list

def search_nearby_venues():
    url = 'https://overpass-api.de/api/interpreter'

    params = dict(
        data='[out:json];'
            'node(around:5000,16.0212462,108.199815399999)[amenity=school];'
            'out;')

    resp = requests.get(url=url, params=params)
    data = resp.json()
    result = []
    for item in data["elements"]:
        # print(item)
        name = item.get("tags", {}).get("name", "N/A")
        if name != "N/A":
            result.append((name, item["lat"], item["lon"]))
    return result

def bds_demo():
   
    kq = '\n------------------------------------------------------------------ \n'
    property_1 = {
        'loại_bất_động_sản': 'chung cư',
        'địa_điểm': 'Đà Nẵng',
        'diện_tích': 70,
        'giá': 1.2e9,
        'mô_tả': 'Căn hộ cao cấp có 2 phòng ngủ và 2 nhà vệ sinh, nằm ở tầng 10 của tòa nhà, với view đẹp nhìn ra thành phố.'
    }

    # Thông tin bất động sản thứ hai
    property_2 = {
        'loại_bất_động_sản': 'nhà riêng',
        'địa_điểm': 'Đà Nẵng',
        'diện_tích': 150,
        'giá': 3.8e9,
        'mô_tả': 'Nhà đẹp mới xây, có 3 phòng ngủ và 3 nhà vệ sinh, nằm trong khu vực yên tĩnh và an ninh tốt.'
    }
    kq += "Thông tin bất động sản 1:"
    for key, value in property_1.items():
        kq += f"{key}: {value} \n"
    kq += '------------------------------------------------------------------ \n'
    kq += "Thông tin bất động sản 2:"
    for key, value in property_2.items():
        kq += f"{key}: {value} \n"
    kq += '------------------------------------------------------------------ \n'
    return kq
# search_nearby_venues()

# while True:
#     new_value = input("Enter a value: ")
#     print(type(search_address(new_value)))
#     print