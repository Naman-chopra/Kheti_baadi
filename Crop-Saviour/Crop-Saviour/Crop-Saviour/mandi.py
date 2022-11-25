import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime as dt, timedelta
import numpy as np
from googletrans import Translator


'''
TESTING CODE BELOW
CHANGE CHAT ID AND TOKEN
CURRENT SUPPORT FOR RUNTIME INPUT NOT THROUGH CHAT INTERFACE
'''
from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime as dt
from googletrans import Translator


# print(soup.prettify())

def send_msg(text,chat_id):
   token = "5212231888:AAE7Wm-esVXOpyckA2W15hhyFvKbshs1QjQ"
   url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + str(chat_id) + "&text=" + text 
   results = requests.get(url_req)
#    print(results.json())

def prices(ans,update,context):
    l=ans.split(', ')
    state=l[0].lower()
    crop=l[1].lower()
    # ###req="https://www.commodityonline.com/mandiprices/{crop}/{state}".format(crop=input("Enter the crop: "),state=input("Enter the state: "))
    req="https://www.commodityonline.com/mandiprices/{crop}/{state}".format(crop=crop,state=state)

    hit=requests.get(req)
    soup=BeautifulSoup(hit.text,"lxml")
    table=soup.find('table',{'main-table2'})
    headers=[]
    for i in table.find_all('th'):
        title=i.text.strip()
        headers.append(title)
    ### headers.remove('Telegram')

    df=pd.DataFrame(columns=headers)
    for i in table.find_all('tr')[1:]:
        data=i.find_all('td')
        rowdata=[td.text.strip() for td in data]
        length=len(df)
        df.loc[length]=rowdata
    ### df.drop(['Telegram'],axis=1)
    delcol=['Telegram', 'Max Price', 'Min Price', 'State', 'Commodity']
    # del df['Commodity']
    # df=df['Arrival Date', 'Variety', 'Market', 'Avg Price']
    df=df.drop(columns=delcol,axis=1)
    ### Uncomment code below to save data tp text file
    ## df.to_csv('mandi_data.txt', sep ='\t')

    print(df)
    return df
    update.message.reply_text(df)
def call_me_for_reply(ans,update,context,chat_id):

    result = prices(ans,update,context).to_string(index = False)
    send_msg(result,update.effective_chat.id)
