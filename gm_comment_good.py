import requests
from bs4 import BeautifulSoup as soup
import random
import time
import csv
import pymongo
import pandas as pd

gm_user_agent=[
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]
agent = random.choice(gm_user_agent)
headers={
    'authority':'ss.gome.com.cn',
    'user-agent':agent,
}

#配置文件
X_type="壁挂炉"
in_file = "国美商品.xlsx"
out_file = "国美壁挂炉二期好评.csv"
db = 'BiGuaLu'
col = 'good_gm_2'
client=pymongo.MongoClient('172.28.171.13',27017)

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
    source = "国美"
    print(p_Name,id,product_url)
    for i in range(1, 31):
        time.sleep(random.randint(2,3))
        url="https://ss.gome.com.cn/item/v1/prdevajsonp/appraiseNew/"+str(id)+"/"+str(i)+"/good/1/1557/flag/appraise"
        comment_page=requests.get(url,headers=headers,timeout=1000).json()
        comments=comment_page["evaList"]['Evalist']
        print(len(comments))
        if len(comments) == 0:
            break
        else:
            for comment in comments:
                comment_text=comment["appraiseElSum"]
                # print(comment_text)
                with open(out_file, "a") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([p_Name, brand, CommentCount, source, product_url, comment_text])
                try:
                    coll.insert(
                        {'ProductID': str(id), 'p_name': p_Name, 'brand': brand, 'commentcount': str(CommentCount),
                         'source': source, 'link': product_url, 'goodcomment': comment_text, 'X_type': X_type,
                         'ProgramStarttime': ProgramStarttime})
                except Exception as e:
                    print(e)