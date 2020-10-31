# -*- coding: utf-8 -*-

'''
zhouzhongqing
2020年10月31日14:56:14
ssr帐号更新
'''

import os
import requests
from bs4 import BeautifulSoup
import uuid


# 写入文件
def write_to_file(file_name, txt):
    '''''
        讲txt文本存入到file_name文件中
    '''
    print("正在存储文件" + str(file_name));
    # 1 打开文件
    # w 如果没有这个文件将创建这个文件
    '''
    'r'：读

    'w'：写

    'a'：追加

    'r+' == r+w（可读可写，文件若不存在就报错(IOError)）

    'w+' == w+r（可读可写，文件若不存在就创建）

    'a+' ==a+r（可追加可写，文件若不存在就创建）
    '''
    f = open(file_name, 'a+', encoding='utf-8');
    # 2 读写文件
    f.write(str(txt));
    # 3 关闭文件
    f.close();


if __name__ == '__main__':

    # 传入要读的文件路径
    file = open('ssr_update_upgrade_v2_template1.txt', "r", encoding="utf-8", errors="ignore")
    account_template = "";
    while True:
        mystr = file.readline()  # 表示一次读取一行
        if not mystr:
            # 读到数据最后跳出，结束循环。数据的最后也就是读不到数据了，mystr为空的时候
            break
        account_template += mystr;

    # 传入要读的文件路径
    file = open('ssr_update_upgrade_v2_template2.txt', "r", encoding="utf-8", errors="ignore")
    file_template = "";
    while True:
        mystr = file.readline()  # 表示一次读取一行
        if not mystr:
            # 读到数据最后跳出，结束循环。数据的最后也就是读不到数据了，mystr为空的时候
            break
        file_template += mystr;

    ssr_domain = "https://github.com/Alvin9999/new-pac/wiki/ss免费账号";

    content_string = "";
    content = requests.get(ssr_domain);
    # print(content.status_code)
    if content.status_code == 200:
        # print(content.text)
        # 初始化并制定解析器
        soup = BeautifulSoup(content.text, "lxml");
        tableContent = soup.table;
        tr_arr = tableContent.find_all("tr");
        for tr in tr_arr:
            tds = tr.find_all('td');
            if tds and len(tds) > 6:
                uid = str(uuid.uuid4())
                suid = ''.join(uid.split('-'))
                content_string += account_template.replace("${id}",suid).replace("${server}",str(tds[1].get_text())).replace("${server_port}",tds[2].get_text()).replace("${password}",tds[3].get_text()).replace("${method}",tds[4].get_text()).replace("${protocol}",tds[5].get_text()).replace("${obfs}",tds[6].get_text())+","

        final_content_string = content_string[0:len(content_string) -1]
        json = file_template.replace("${account}",final_content_string);
        #print(json)
        if os.path.exists("../gui-config.json"):
            os.remove("../gui-config.json")
        write_to_file("../gui-config.json",json);
    else:
        print("访问ssr帐号失败!")

