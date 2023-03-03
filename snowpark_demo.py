import configparser
from snowflake.snowpark import Session

config = configparser.ConfigParser()
data = config.read("snowpark_demo.ini")

connection_parameters = {
     "account": config['default']['account'],
     "user": config['default']['user'],
     "warehouse": config['default']['warehouse'],   # optional 
     "database": config['default']['database'],     # optional
     "schema": config['default']['schema'],         # optional
     "authenticator": "externalbrowser"
}  

new_session = Session.builder.configs(connection_parameters).create()  
new_session.close()