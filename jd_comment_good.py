import requests
from bs4 import BeautifulSoup as soup
import random
import time
import csv
import pandas as pd
import pymongo
jd_user_agent=[
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
]
agent = random.choice(jd_user_agent)
headers={
    'user-agent':agent,
}

#配置文件
X_type="壁挂式空调三期"
in_file = "壁挂空调三期产品.xlsx"
out_file = "京东壁挂空调三期好评.csv"
db = 'BiGua_KT'
col = 'good_jd_2'
# client=pymongo.MongoClient('172.28.171.13',27017)
client=pymongo.MongoClient('localhost',27017)

database=client[db]
# print(database.collection_names())
coll=database[col]

df=pd.read_excel(in_file)
id_list=df.ProductID.values
p_Namelist=df.p_Name.values
brand_list = df.brand.values
CommentCount_list = df.CommentCount.values
ProgramStarttime = time.strftime('%Y-%m-%d', time.localtime(time.time()))
product_urllist=df.product_url.values
with open(out_file, "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['p_name','brand','commentcount','source','link','goodcomment'])
for x in range(len(id_list)):
    id = id_list[x]
    p_Name = p_Namelist[x]
    brand = brand_list[x]
    CommentCount = CommentCount_list[x]
    product_url = product_urllist[x]
    source = "京东"
    print(p_Name,id,product_url)
    for i in range(0,100):
        try:
            time.sleep(random.randint(2,3))
            url="https://sclub.jd.com/comment/productPageComments.action?productId="+str(id)+"&score=3&sortType=5&page="+str(i)+"&pageSize=10"
            comment_page=requests.get(url,headers=headers,timeout=1000).json()
            comments=comment_page["comments"]
            print(i,len(comments))
            if len(comments) == 0:
                break
            else:
                for comment in comments:
                    comment_text=comment["content"]
                    # uesrid=comment['id']
                    # guid=comment['guid']
                    nickname=comment['nickname']
                    # print(uesrid,guid,nickname)
                    # print(comment_text)
                    with open(out_file, "a") as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow([p_Name,brand,CommentCount,source,product_url,comment_text])

                    try:
                        coll.insert({'ProductID':str(id),'p_name': p_Name,'brand':brand,'commentcount':str(CommentCount),'source':source,'link': product_url, 'goodcomment': comment_text,'X_type':X_type,'ProgramStarttime':ProgramStarttime})
                    except Exception as e:
                        print(e)

        except ConnectionError:
            time.sleep(random.randint(60, 120))
            url="https://sclub.jd.com/comment/productPageComments.action?productId="+str(id)+"&score=3&sortType=5&page="+str(i)+"&pageSize=10"
            comment_page=requests.get(url,headers=headers,timeout=1000).json()
            comments=comment_page["comments"]
            print(i,len(comments))
            if len(comments) == 0:
                break
            else:
                for comment in comments:
                    comment_text=comment["content"]
                    nickname = comment['nickname']
                    # print(comment_text)
                    with open(out_file, "a") as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow([p_Name,brand,CommentCount,source,product_url,comment_text])

                    try:
                        coll.insert({'ProductID':str(id),'p_name': p_Name,'brand':brand,'commentcount':str(CommentCount),'source':source,'link': product_url, 'goodcomment': comment_text,'X_type':X_type,'ProgramStarttime':ProgramStarttime})
                    except Exception as e:
                        print(e)

        except:
            try:
                time.sleep(random.randint(60, 120))
                url="https://sclub.jd.com/comment/productPageComments.action?productId="+str(id)+"&score=3&sortType=5&page="+str(i)+"&pageSize=10"
                comment_page=requests.get(url,headers=headers,timeout=1000).json()
                comments=comment_page["comments"]
                print(i,len(comments))
                if len(comments) == 0:
                    break
                else:
                    for comment in comments:
                        comment_text=comment["content"]
                        nickname = comment['nickname']
                        # print(comment_text)
                        with open(out_file, "a") as csvfile:
                            writer = csv.writer(csvfile)
                            writer.writerow([p_Name,brand,CommentCount,source,product_url,comment_text])

                        try:
                            coll.insert({'ProductID':str(id),'p_name': p_Name,'brand':brand,'commentcount':str(CommentCount),'source':source,'link': product_url, 'goodcomment': comment_text,'X_type':X_type,'ProgramStarttime':ProgramStarttime})
                        except Exception as e:
                            print(e)
            except Exception as e:
                print(e)
                continue

