"""""""""
家电一院项目
根据已知商品型号，爬取好、中、差评率，爬取中差评数量，爬取中差评内容
"""""""""

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
in_file = "家电一院.xlsx"
out_file = "家电一院结果.csv"
db = 'JiaDiaYiYuan_Comment'
col = 'jiadianyiyuan'
# client=pymongo.MongoClient('172.28.171.13',27017)
client=pymongo.MongoClient('localhost',27017)

database=client[db]
# print(database.collection_names())
coll=database[col]

df=pd.read_excel(in_file)
id_list=df.ProductID.values
model_list=df.model.values
brand_list = df.brand.values
type_list = df.type.values
ProgramStarttime = time.strftime('%Y-%m-%d', time.localtime(time.time()))
product_urllist=df.ProductURL.values
with open(out_file, "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(
        ['brand','type','model','goodRateShow','generalRateShow','poorRateShow','generalCount','poorCount','generalComment','poorComment','source','link'])
for x in range(len(id_list)):
    id = id_list[x]
    model = model_list[x]
    brand = brand_list[x]
    type = type_list[x]
    product_url = product_urllist[x]
    source = "京东"
    print(model,id,product_url)

    #一星差评
    for i in range(0,100):
        try:
            time.sleep(random.randint(2,3))
            url="https://sclub.jd.com/comment/productPageComments.action?productId="+str(id)+"&score=1&sortType=5&page="+str(i)+"&pageSize=10"
            comment_page=requests.get(url,headers=headers,timeout=1000).json()
            Summary = comment_page['productCommentSummary']
            goodRateShow = Summary['goodRateShow']
            generalRateShow = float(Summary['generalRate'])*100
            poorRateShow = float(Summary['poorRate'])*100
            generalCount = Summary['generalCount']
            poorCount = Summary['poorCount']
            comments=comment_page["comments"]
            print(i,len(comments))
            if len(comments) == 0:
                break
            else:
                for comment in comments:
                    poorComment=comment["content"]
                    generalComment = None
                    # uesrid=comment['id']
                    # guid=comment['guid']
                    # nickname=comment['nickname']
                    # print(uesrid,guid,nickname)
                    # print(comment_text)
                    with open(out_file, "a") as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow([brand,type,model,goodRateShow,generalRateShow,poorRateShow,generalCount,poorCount,generalComment,poorComment,source,product_url])

                    try:
                        coll.insert({
                            'brand':brand,'type':type,'model':model,'goodRateShow':goodRateShow,'generalRateShow':generalComment,
                            'poorRateShow':poorRateShow,'generalCount':generalCount,'poorCount':poorCount,
                            'generalComment':generalComment,'poorComment':poorComment,
                            'source':source,'link':product_url,'ProgramStarttime':ProgramStarttime})
                    except Exception as e:
                        print(e)

        except ConnectionError:
            time.sleep(random.randint(60, 120))
            url="https://sclub.jd.com/comment/productPageComments.action?productId="+str(id)+"&score=1&sortType=5&page="+str(i)+"&pageSize=10"
            comment_page=requests.get(url,headers=headers,timeout=1000).json()
            Summary = comment_page['productCommentSummary']
            goodRateShow = Summary['goodRateShow']
            generalRateShow = float(Summary['generalRate'])*100
            poorRateShow = float(Summary['poorRate'])*100
            generalCount = Summary['generalCount']
            poorCount = Summary['poorCount']
            comments=comment_page["comments"]
            print(i,len(comments))
            if len(comments) == 0:
                break
            else:
                for comment in comments:
                    poorComment=comment["content"]
                    generalComment = None
                    # uesrid=comment['id']
                    # guid=comment['guid']
                    # nickname=comment['nickname']
                    # print(uesrid,guid,nickname)
                    # print(comment_text)
                    with open(out_file, "a") as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow([brand,type,model,goodRateShow,generalRateShow,poorRateShow,generalCount,poorCount,generalComment,poorComment,source,product_url])

                    try:
                        coll.insert({
                            'brand':brand,'type':type,'model':model,'goodRateShow':goodRateShow,'generalRateShow':generalComment,
                            'poorRateShow':poorRateShow,'generalCount':generalCount,'poorCount':poorCount,
                            'generalComment':generalComment,'poorComment':poorComment,
                            'source':source,'link':product_url,'ProgramStarttime':ProgramStarttime})
                    except Exception as e:
                        print(e)
        except:
            time.sleep(random.randint(60, 120))
            url="https://sclub.jd.com/comment/productPageComments.action?productId="+str(id)+"&score=1&sortType=5&page="+str(i)+"&pageSize=10"
            comment_page=requests.get(url,headers=headers,timeout=1000).json()
            Summary = comment_page['productCommentSummary']
            goodRateShow = Summary['goodRateShow']
            generalRateShow = float(Summary['generalRate'])*100
            poorRateShow = float(Summary['poorRate'])*100
            generalCount = Summary['generalCount']
            poorCount = Summary['poorCount']
            comments=comment_page["comments"]
            print(i,len(comments))
            if len(comments) == 0:
                break
            else:
                for comment in comments:
                    poorComment=comment["content"]
                    generalComment = None
                    # uesrid=comment['id']
                    # guid=comment['guid']
                    # nickname=comment['nickname']
                    # print(uesrid,guid,nickname)
                    # print(comment_text)
                    with open(out_file, "a") as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow([brand,type,model,goodRateShow,generalRateShow,poorRateShow,generalCount,poorCount,generalComment,poorComment,source,product_url])

                    try:
                        coll.insert({
                            'brand':brand,'type':type,'model':model,'goodRateShow':goodRateShow,'generalRateShow':generalComment,
                            'poorRateShow':poorRateShow,'generalCount':generalCount,'poorCount':poorCount,
                            'generalComment':generalComment,'poorComment':poorComment,
                            'source':source,'link':product_url,'ProgramStarttime':ProgramStarttime})
                    except Exception as e:
                        print(e)

    #二星中评
    for i in range(0,100):
        try:
            time.sleep(random.randint(2,3))
            url="https://sclub.jd.com/comment/productPageComments.action?productId="+str(id)+"&score=2&sortType=5&page="+str(i)+"&pageSize=10"
            comment_page=requests.get(url,headers=headers,timeout=1000).json()
            Summary = comment_page['productCommentSummary']
            goodRateShow = Summary['goodRateShow']
            generalRateShow = float(Summary['generalRate'])*100
            poorRateShow = float(Summary['poorRate'])*100
            generalCount = Summary['generalCount']
            poorCount = Summary['poorCount']
            comments=comment_page["comments"]
            print(i,len(comments))
            if len(comments) == 0:
                break
            else:
                for comment in comments:
                    poorComment=None
                    generalComment = comment["content"]
                    # uesrid=comment['id']
                    # guid=comment['guid']
                    # nickname=comment['nickname']
                    # print(uesrid,guid,nickname)
                    # print(comment_text)
                    with open(out_file, "a") as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow([brand,type,model,goodRateShow,generalRateShow,poorRateShow,generalCount,poorCount,generalComment,poorComment,source,product_url])

                    try:
                        coll.insert({
                            'brand':brand,'type':type,'model':model,'goodRateShow':goodRateShow,'generalRateShow':generalComment,
                            'poorRateShow':poorRateShow,'generalCount':generalCount,'poorCount':poorCount,
                            'generalComment':generalComment,'poorComment':poorComment,
                            'source':source,'link':product_url,'ProgramStarttime':ProgramStarttime})
                    except Exception as e:
                        print(e)

        except ConnectionError:
            time.sleep(random.randint(60, 120))
            url="https://sclub.jd.com/comment/productPageComments.action?productId="+str(id)+"&score=2&sortType=5&page="+str(i)+"&pageSize=10"
            comment_page=requests.get(url,headers=headers,timeout=1000).json()
            Summary = comment_page['productCommentSummary']
            goodRateShow = Summary['goodRateShow']
            generalRateShow = float(Summary['generalRate'])*100
            poorRateShow = float(Summary['poorRate'])*100
            generalCount = Summary['generalCount']
            poorCount = Summary['poorCount']
            comments=comment_page["comments"]
            print(i,len(comments))
            if len(comments) == 0:
                break
            else:
                for comment in comments:
                    poorComment=None
                    generalComment = comment["content"]
                    # uesrid=comment['id']
                    # guid=comment['guid']
                    # nickname=comment['nickname']
                    # print(uesrid,guid,nickname)
                    # print(comment_text)
                    with open(out_file, "a") as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow([brand,type,model,goodRateShow,generalRateShow,poorRateShow,generalCount,poorCount,generalComment,poorComment,source,product_url])

                    try:
                        coll.insert({
                            'brand':brand,'type':type,'model':model,'goodRateShow':goodRateShow,'generalRateShow':generalComment,
                            'poorRateShow':poorRateShow,'generalCount':generalCount,'poorCount':poorCount,
                            'generalComment':generalComment,'poorComment':poorComment,
                            'source':source,'link':product_url,'ProgramStarttime':ProgramStarttime})
                    except Exception as e:
                        print(e)
        except:
            time.sleep(random.randint(60, 120))
            url="https://sclub.jd.com/comment/productPageComments.action?productId="+str(id)+"&score=2&sortType=5&page="+str(i)+"&pageSize=10"
            comment_page=requests.get(url,headers=headers,timeout=1000).json()
            Summary = comment_page['productCommentSummary']
            goodRateShow = Summary['goodRateShow']
            generalRateShow = float(Summary['generalRate'])*100
            poorRateShow = float(Summary['poorRate'])*100
            generalCount = Summary['generalCount']
            poorCount = Summary['poorCount']
            comments=comment_page["comments"]
            print(i,len(comments))
            if len(comments) == 0:
                break
            else:
                for comment in comments:
                    poorComment=None
                    generalComment = comment["content"]
                    # uesrid=comment['id']
                    # guid=comment['guid']
                    # nickname=comment['nickname']
                    # print(uesrid,guid,nickname)
                    # print(comment_text)
                    with open(out_file, "a") as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow([brand,type,model,goodRateShow,generalRateShow,poorRateShow,generalCount,poorCount,generalComment,poorComment,source,product_url])

                    try:
                        coll.insert({
                            'brand':brand,'type':type,'model':model,'goodRateShow':goodRateShow,'generalRateShow':generalComment,
                            'poorRateShow':poorRateShow,'generalCount':generalCount,'poorCount':poorCount,
                            'generalComment':generalComment,'poorComment':poorComment,
                            'source':source,'link':product_url,'ProgramStarttime':ProgramStarttime})
                    except Exception as e:
                        print(e)
