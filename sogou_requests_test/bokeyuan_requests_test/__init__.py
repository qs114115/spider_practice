import requests

if __name__ == '__main__':
    url = 'https://www.sogou.com/web';
    # 处理url携带的参数
    kw = input('entry a word: ')
    param = {
        'query': kw
    }
    response = requests.get(url=url, params=param)
    page_text = response.text

    fileName = kw + '.html'
    with open(fileName, 'w',encoding='utf-8') as fl:
        fl.write(page_text)

    print(fileName + '保存成功')
