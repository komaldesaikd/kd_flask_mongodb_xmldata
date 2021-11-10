import yaml

article_info = {'db_conn_url':r'mongodb+srv://Komal:S24hd0IDRsWjnKHZ@cluster0.drkve.mongodb.net/test',
     'base_path':r'D:\\Python_programs\\Flask\\backend_challenge_chemovator\\',
     'db_nm':'API',
         }

with open("ip_data.yaml", 'w') as yamlfile:
    data = yaml.dump(article_info, yamlfile)
    print("Write successful")