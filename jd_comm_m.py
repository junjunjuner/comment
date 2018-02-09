import requests
from bs4 import BeautifulSoup as soup
import random
import time
import csv

def comment_func(page,filename,productId,write_row):
    for i in range(0,page):
        print(i)
        try:
            time.sleep(random.randint(10,15))
            url="https://sclub.jd.com/comment/productPageComments.action?productId="+str(productId)+"&score=1&sortType=5&page="+str(i)+"&pageSize=10"
            comment_page=requests.get(url,headers=headers,timeout=1000).json()
            comments=comment_page["comments"]
            print(len(comments))
            for comment in comments:
                comment_text=comment["content"]
                print(comment_text)
                with open(filename, "a") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([comment_text])
        except ConnectionError:
            time.sleep(random.randint(60, 120))
            url="https://sclub.jd.com/comment/productPageComments.action?productId=117835&score=1&sortType=5&page="+str(i)+"&pageSize=10"
            comment_page=requests.get(url,headers=headers,timeout=1000).json()
            comments=comment_page["comments"]
            print(len(comments))
            for comment in comments:
                comment_text=comment["content"]
                print(comment_text)
                with open(filename, "a") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([comment_text])
        except:
            url="https://sclub.jd.com/comment/productPageComments.action?productId=117835&score=1&sortType=5&page="+str(i)+"&pageSize=10"
            print(url)

if __name__ == '__main__':

    jd_user_agent = [
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]
    agent = random.choice(jd_user_agent)
    headers = {
        'referer': 'https://item.jd.com/117835.html',
        'user-agent': agent,
    }
    filename = "jd_comment.csv"
    productId_list=[]
    kind="电油汀"
    comment_text=''
    url=''
    source='京东'
    for productId in productId_list:
        with open(filename, "w") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["productID","comment","qnq_kind","product_commenturl","source"])
        write_row=[productId,comment_text,kind,url,source]