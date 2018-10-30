import requests
from bs4 import BeautifulSoup as soup
import random
import time
import csv
import pandas as pd
jd_user_agent=[
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
]
agent = random.choice(jd_user_agent)
headers={
    'user-agent':agent,
}
df=pd.read_excel("电暖气用户评论.xlsx")
id_list=df.ProductID.values
p_Name=df.p_Name.values
X_type=df.X_type.values
product_url=df.product_url.values
with open("jd_comment.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["p_Name","comment","ProductID","product_url","X_type"])
for x in range(len(id_list)):
    id = id_list[x]
    print(p_Name[x],id,product_url[x],X_type[x])
    for i in range(0,50):
        try:
            time.sleep(random.randint(5,8))
            url="https://sclub.jd.com/comment/productPageComments.action?productId="+str(id)+"&score=1&sortType=5&page="+str(i)+"&pageSize=10"
            comment_page=requests.get(url,headers=headers,timeout=1000).json()
            comments=comment_page["comments"]
            print(i,len(comments))
            if len(comments) == 0:
                break
            else:
                for comment in comments:
                    comment_text=comment["content"]
                    # print(comment_text)
                    with open("jd_comment.csv", "a") as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow([p_Name[x],comment_text,id,product_url[x],X_type[x]])
        except ConnectionError:
            time.sleep(random.randint(60, 120))
            url="https://sclub.jd.com/comment/productPageComments.action?productId="+str(id)+"&score=1&sortType=5&page="+str(i)+"&pageSize=10"
            comment_page=requests.get(url,headers=headers,timeout=1000).json()
            comments=comment_page["comments"]
            print(i,len(comments))
            if len(comments) == 0:
                break
            else:
                for comment in comments:
                    comment_text=comment["content"]
                    # print(comment_text)
                    with open("jd_comment.csv", "a") as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow([p_Name[x], comment_text, id, product_url[x], X_type[x]])
        except:
            time.sleep(random.randint(60, 120))
            url="https://sclub.jd.com/comment/productPageComments.action?productId="+str(id)+"&score=1&sortType=5&page="+str(i)+"&pageSize=10"
            comment_page=requests.get(url,headers=headers,timeout=1000).json()
            comments=comment_page["comments"]
            print(i,len(comments))
            if len(comments) == 0:
                break
            else:
                for comment in comments:
                    comment_text=comment["content"]
                    # print(comment_text)
                    with open("jd_comment.csv", "a") as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow([p_Name[x], comment_text, id, product_url[x], X_type[x]])
