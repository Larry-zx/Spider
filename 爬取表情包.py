from bs4 import BeautifulSoup
import requests
import os  # os模块创建文件夹

# 创建文件夹
if not os.path.exists('./biaoqingbao'):
    os.mkdir('./biaoqingbao')
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
}
url = 'https://www.fabiaoqing.com/biaoqing/lists/page/%d.html'
# 爬取不同页码的图片
for page_number in range(1, 11):
    new_url = format(url % page_number)
    # 当前网页的url
    page_text = requests.get(url=new_url, headers=headers).text
    soup = BeautifulSoup(page_text, 'lxml')
    # 得到了图片的链接组成的链表
    url_list = soup.select('.tagbqppdiv >a')
    for pic_url in url_list:
        # 图片的链接
        pic_url = 'https://www.fabiaoqing.com/' + pic_url['href']
        # 产生一个新的对象pic_soup
        pic_text = requests.get(url=pic_url, headers=headers).text
        pic_soup = BeautifulSoup(pic_text, 'lxml')
        # 只有一张图片
        try:
            print(type(pic_soup.find('img', class_='biaoqingpp')))
            pic_src = pic_soup.find('img', class_='biaoqingpp')['src']
        #获取名字
            pic_name=pic_src.split('/')[-1]
            #给予地址
            pic_path = './biaoqingbao/' + pic_name
            # 图片信息提取
            response =requests.get(url=pic_src,headers=headers)
            pic_data=response.content
            #永久存储
            with open(pic_path, 'wb') as fp:  # wb 是对二进制的操作
                fp.write(pic_data)
                print(pic_name+'  爬取成功！')
        except IOError:
            print("这个图片不太行！")
print("爬取顺利结束！！！")
