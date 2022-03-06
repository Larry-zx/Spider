from selenium import webdriver
from time import sleep
from lxml import etree
from webdriver_manager.chrome import ChromeDriverManager

# 先登录自己的空间
number_q = input('请输入要点赞的用户的qq号：')

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://i.qq.com/")
elem = driver.find_element_by_class_name('login_wrap')
elem.click()
print("成功登录QQ空间！")
# 进入对方的qq空间
sleep(2)
new_url = 'https://user.qzone.qq.com/' + number_q + '/profile'
driver.get(url=new_url)
sleep(1)
driver.switch_to.frame('app_canvas_frame')
sleep(2)
# 跳转到说说对应的iframe
driver.switch_to.frame('frameFeedList')
# 获取有多少说说
page_text = driver.page_source
tree = etree.HTML(page_text)
li_list = tree.xpath('//*[@id="host_home_feeds"]/li')
count = len(li_list)
print('查找到说说的数量为：', count)
xpath_name = '//*[@id="host_home_feeds"]/li[%d]/div[3]/div[1]/p/a[3]'
shengri = '//*[@id="host_home_feeds"]/li[%d]'
# 开始遍历点赞
for i in range(1, count + 1):
    new_xpath = format(xpath_name % i)
    s_r = format(shengri % i) + '/@id'
    # 提取<Li>标签中id值中的特征 333为系统生日祝福
    panbie = eval(tree.xpath(s_r)[0].split('_')[2])
    if (panbie != 333):
        driver.find_element_by_xpath(new_xpath).click()
        print('第', i, '条说说----点赞成功')
    else:
        print('第', i, '条是系统生日祝福----无法点赞')

sleep(2)
driver.quit()