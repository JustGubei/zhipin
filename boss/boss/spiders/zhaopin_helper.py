"""__author__ =侯晨皓"""
import json
import requests

# db = get_connection()
# cursor = get_cursor(db)

#获取网页
def get_page():
    url = 'https://www.zhipin.com/common/data/city.json'
    headers = {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",

    }
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return response.content.decode('utf-8')
    return None




#解析网页
def parse_page(html):

    # result = html.split('(')[1].split(')')[0]
    # json.loads(result)


    result1 = html
    result_dict = json.loads(result1)
    result_list = result_dict['data']['cityList']

    citylist = []

    for result in result_list:

        item = result['subLevelModelList']

        for i in item:

            print(i['code'],i['name'])

            citylist.append({i['name']:i['code']})

    print(citylist)

    return citylist






def main():
    html = get_page()
    result = parse_page(html)

    with open('../zhaopin.txt', 'w',encoding='utf-8') as f:
        f.write(str(result))

if __name__ == '__main__':
    main()