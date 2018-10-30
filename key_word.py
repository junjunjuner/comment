import requests
import pandas as pd

df = pd.read_csv()

comment_web = "https://sclub.jd.com/comment/productPageComments.action?productId=" + str(ProductID) + "&score=0&sortType=5&page=0&pageSize=10"

urls = requests.get(comment_web, timeout=1000).json()
try:
    comment = urls['hotCommentTagStatistics']
    keyword_list = []
    for i in range(len(comment)):
        keyword_list.append(comment[i]['name'])
    if len(keyword_list) == 0:
        keyword = None
    else:
        keyword = ' '.join(keyword_list)  # 关键词
except:
    keyword = None