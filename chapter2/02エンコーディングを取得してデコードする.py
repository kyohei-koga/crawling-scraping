
# coding: utf-8

# In[1]:


import sys
from urllib.request import urlopen


# In[2]:


f = urlopen('https://sample.scraping-book.com/dp')


# In[4]:


#HTTPヘッダーからエンコーディングを取得する（明示されていない場合はutf-8とする）
encoding = f.info().get_content_charset(failobj='utf-8')
print('encoding:',encoding,file=sys.stderr) #エンコーディングを標準エラー出力に出力する。


# In[5]:


#得られたエンコーディングを指定して文字列にデコードする
text = f.read().decode(encoding)
print(text)

