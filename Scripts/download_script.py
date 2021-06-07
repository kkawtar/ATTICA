import pandas as pd
import requests
import os
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from fake_useragent import UserAgent
import filetype


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
ua = UserAgent()
headers = {'User-Agent':str(ua.chrome)}


data = pd.read_csv("all_data.csv")



dir_save = "./data/"

if not os.path.exists(dir_save):
    os.makedirs(dir_save)
    
    
    

for index, row in data.iterrows():
    
    if(row['link']!="not found"):
        
        
        url = row['link']
        extension = ""
        file_name = row['name'].split('.')[0]
        
        tmp_name = dir_save+file_name
        
        

        with open("tmp_name", "wb") as file:

            try:
                
                r = requests.get(url, headers=headers,verify=False, timeout=30)
                file.write(r.content)
                
                file_tmp = filetype.guess('tmp_name')

                if (file_tmp is None):
                    print("Error : ",row['name'])
                else:
                    extension = file_tmp.extension

                    with open(tmp_name+"."+extension, "wb") as file:
                        file.write(r.content)
                        

            except requests.exceptions.Timeout:

                print("Timeout : ",row['name'])

            except requests.exceptions.RequestException as e:
                print("exceptions : ",row['name'])
   
