import hashlib


def generate_password(keyword):
    """
    根据关键词生成密码
    """
    # 将关键词和一个随机字符串组合
    salt = "sdf908#sdf0&hj"
    message = keyword + salt

    # 使用SHA-256哈希算法将消息哈希化
    hash_object = hashlib.sha256(message.encode())
    hex_dig = hash_object.hexdigest()

    # 从哈希值中提取指定长度的密码
    password = hex_dig[:16]  # 这里示范提取16位密码，密码越长越好

    return password


# 获取用户输入的关键词，可以是某平台，应用，账号等
keyword = input("输入关键词：")

password = generate_password(keyword)

print("你的密码是：", password)

"""
该程序可以让用户输入关键词来生成随机16位密码，注意：同样的关键词生成的密码相同
根据此特性，应用场景如下：
1. 不同账号设置不同密码，
2. 不同平台设置不同密码，
3. 密码存储库，用户使用不同账号密码，只需要在此程序中输入便可以得到密码，无需记忆或存储于本地的钥匙串
"""
