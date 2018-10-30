"""""""""
检测中心项目
爬取智能魔方售后数据
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
# in_file = "家电一院.xlsx"
out_file1 = "智能魔方好评.csv"
out_file2 = "智能魔方中评.csv"
out_file3 = "智能魔方差评.csv"
db = 'JianCeZhongXin_Comment'
col = 'zhinengmofang'
# client=pymongo.MongoClient('172.28.171.13',27017)
client=pymongo.MongoClient('localhost',27017)

database=client[db]
# print(database.collection_names())
coll=database[col]

id_list = ['7306935','7331957','12858141664','1646462042']
brand_list = ['绿米Aqara','绿米Aqara','欧瑞博','欧瑞博']
ProgramStarttime = time.strftime('%Y-%m-%d',time.localtime(time.time()))

#好评
with open(out_file1,"w") as file1:
    writer = csv.writer(file1)
    writer.writerow(['brand','name','productSize','productColor','goodRateShow','goodcomment','link','source'])

#中评
with open(out_file2,"w") as file1:
    writer = csv.writer(file1)
    writer.writerow(['brand','name','productSize','productColor','generalRateShow','generalcomment','link','source'])

#差评
with open(out_file3,"w") as file1:
    writer = csv.writer(file1)
    writer.writerow(['brand','name','productSize','productColor','poorRateShow','poorcomment','link','source'])

for i in range(len(id_list)):
    id = id_list[i]
    brand = brand_list[i]
    link  = "https://item.jd.com/"+str(id)+".html"
    source = '京东'
    #五星好评
    for i in range(0,100):
        time.sleep(random.randint(2,3))
        url="https://sclub.jd.com/comment/productPageComments.action?productId="+str(id)+"&score=3&sortType=5&page="+str(i)+"&pageSize=10"
        comment_page=requests.get(url,headers=headers,timeout=1000).json()
        Summary = comment_page['productCommentSummary']
        goodRateShow = Summary['goodRateShow']
        # generalRateShow = float(Summary['generalRate'])*100
        # poorRateShow = float(Summary['poorRate'])*100
        comments=comment_page["comments"]
        print(i,len(comments))
        if len(comments) == 0:
            break
        else:
            for comment in comments:
                content = comment['content']  # 评论
                creationTime = comment['creationTime']  # 评论时间
                referenceName = comment['referenceName']  # 商品名称
                score = comment['score']  # 评价等级
                # showOrderComment = comment['showOrderComment']   #订单评价
                productSize = comment['productSize']  # 系列
                productColor = comment['productColor']  # 匹数
                with open(out_file1, "a") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([brand,referenceName,productSize,productColor,goodRateShow,content,link,source])

                try:
                    coll.insert({
                        'brand':brand,'name':referenceName,'goodRateShow':goodRateShow,'productSize':productSize,
                        'productColor':productColor,'goodcomment':content,'source':source,'link':link,'ProgramStarttime':ProgramStarttime})
                except Exception as e:
                    print(e)

    #一星差评
    for i in range(0,100):
        time.sleep(random.randint(2,3))
        url="https://sclub.jd.com/comment/productPageComments.action?productId="+str(id)+"&score=1&sortType=5&page="+str(i)+"&pageSize=10"
        comment_page=requests.get(url,headers=headers,timeout=1000).json()
        Summary = comment_page['productCommentSummary']
        # goodRateShow = Summary['goodRateShow']
        # generalRateShow = float(Summary['generalRate'])*100
        poorRateShow = float(Summary['poorRate'])*100
        comments=comment_page["comments"]
        print(i,len(comments))
        if len(comments) == 0:
            break
        else:
            for comment in comments:
                content = comment['content']  # 评论
                creationTime = comment['creationTime']  # 评论时间
                referenceName = comment['referenceName']  # 商品名称
                score = comment['score']  # 评价等级
                # showOrderComment = comment['showOrderComment']   #订单评价
                productSize = comment['productSize']  # 系列
                productColor = comment['productColor']  # 匹数
                with open(out_file3, "a") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([brand,referenceName,productSize,productColor,poorRateShow,content,link,source])

                try:
                    coll.insert({
                        'brand':brand,'poorRateShow':poorRateShow,'productSize':productSize,
                        'productColor':productColor,'poorComment':content,'source':source,'link':link,'ProgramStarttime':ProgramStarttime})
                except Exception as e:
                    print(e)

    #二星中评
    for i in range(0,100):
        time.sleep(random.randint(2,3))
        url="https://sclub.jd.com/comment/productPageComments.action?productId="+str(id)+"&score=2&sortType=5&page="+str(i)+"&pageSize=10"
        comment_page=requests.get(url,headers=headers,timeout=1000).json()
        Summary = comment_page['productCommentSummary']
        # goodRateShow = Summary['goodRateShow']
        generalRateShow = float(Summary['generalRate'])*100
        # poorRateShow = float(Summary['poorRate'])*100
        comments=comment_page["comments"]
        print(i,len(comments))
        if len(comments) == 0:
            break
        else:
            for comment in comments:
                content = comment['content']  # 评论
                creationTime = comment['creationTime']  # 评论时间
                referenceName = comment['referenceName']  # 商品名称
                score = comment['score']  # 评价等级
                # showOrderComment = comment['showOrderComment']   #订单评价
                productSize = comment['productSize']  # 系列
                productColor = comment['productColor']  # 匹数
                with open(out_file2, "a") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([brand,referenceName,productSize,productColor,generalRateShow,content,link,source])

                try:
                    coll.insert({
                        'brand':brand,'generalRateShow':generalRateShow,'productSize':productSize,
                        'productColor':productColor,'generalComment':content,'source':source,'link':link,'ProgramStarttime':ProgramStarttime})
                except Exception as e:
                    print(e)