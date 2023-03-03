import configparser
config = configparser.ConfigParser()
config['default'] = {'account': 'your_account_name',
                     'user': 'your@username.com',
                     'role': 'public',
                     'warehouse': 'test_wh',
                     'database': 'test_db',
                     'schema': 'public'}
with open('snowpark_demo.ini', 'w') as configfile:
  config.write(configfile)