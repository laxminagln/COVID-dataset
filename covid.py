from selenium import webdriver
import time
import pandas as pd
import os                                                           #importing libraries

browser = webdriver.Chrome('path to chrome driver')                 #give path to chromedriver
browser.get("https://www.worldometers.info/coronavirus/")           #open the website
time.sleep(15)

column_names = ['Rank','Country', 'Total Cases', 'New Cases', 'Deaths', 'New Deaths','Recovered', 'Active Cases', 'Critical']
df = pd.DataFrame(columns= column_names)                            #creates dataframe
print(df)

for i in browser.find_elements_by_xpath('//*[@id="main_table_countries_today"]/tbody/tr'):
    td_list = i.find_elements_by_tag_name('td')
    row = []
    for td in td_list:
        row.append(td.text)
    data = {}
    for j in range(len(df.columns)):
        data[df.columns[j]] = row[j] 
    df = df.append(data, ignore_index=True)

df = df.iloc[1:]
print(df)

base_path = 'path to save dataset'

path = os.path.join(base_path,'Covid_Dataset_.csv')
#os.mkdir(path)
df.to_csv(path, index = False)
print("The dataset has been saved at the location: "+path)
browser.quit()
