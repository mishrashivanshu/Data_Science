from urllib.request import urlopen
android_url="https://en.wikipedia.org/wiki/Android_version_history"
android_data=urlopen(android_url)
android_html=android_data.read()
android_data.close()
from bs4 import BeautifulSoup as soup
android_soup=soup(android_html,'html.parser')
tables=android_soup.findAll('table',{'class':'wikitable'})
android_table=tables[0]
headers=android_table.findAll('th')
column_titles=[ct.text[:-1] for ct in headers]
rows_data=android_table.findAll('tr')[1:]
first_row=rows_data[0].findAll('td',{})
table_rows=[]
for row in rows_data:
    current_row=[]
    row_data=row.findAll('td',{})
    if len(row_data)==5:
            lp="No Official Codename"
            current_row.append(lp)
    for idx,data in enumerate(row_data):
        current_row.append(data.text[:-1])
    table_rows.append(current_row)
filename='android_version_history.csv'
with open(filename,'w',encoding='utf-8') as f:
    # Writing the header
    header_string=','.join(column_titles)
    header_string+='\n'
    f.write(header_string)
    
    for row in table_rows:
        row_string=" "
        for w in row:
            w=w.replace(',',' ')
            row_string+=w+','
        row_string=row_string[:-1]
        #row_string=','.join(row)
        row_string+='\n'
        f.write(row_string)
import pandas as pd
df=pd.read_csv('android_version_history.csv')
df.head(n=18)
