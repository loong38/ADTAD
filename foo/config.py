import configparser

# class config:


# 创建一个 ConfigParser 对象
config = configparser.ConfigParser()

# 读取配置文件
config.read('../config/config.ini')

# 获取数据库配置项的值
database_host = config['Database']['Host']
database_port = config['Database']['Port']
database_user = config['Database']['User']
database_password = config['Database']['Password']

# 获取用户配置项的值
user_name = config['User']['Name']
user_email = config['User']['Email']

# 使用配置项的值
print("Database Configuration:")
print(f"Host: {database_host}")
print(f"Port: {database_port}")
print(f"User: {database_user}")
print(f"Password: {database_password}")

print("\nUser Information:")
print(f"Name: {user_name}")
print(f"Email: {user_email}")