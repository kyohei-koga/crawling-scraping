
# coding: utf-8

# In[1]:


import MySQLdb


# In[2]:


#MySQLサーバーに接続し、コネクションを取得する。
#ユーザー名とパスワードを指定してscrapingデータベースを使用する。接続に使用する文字コードはutf8mb4とする。
conn = MySQLdb.connect(db='scraping',user='scraper',passwd='password',charset='utf8mb4')

