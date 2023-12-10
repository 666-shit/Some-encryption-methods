import hashlib


def md5_encrypt(message):
    md5 = hashlib.md5()
    md5.update(message.encode())
    return md5.hexdigest()


def main():
    message = input("请输入要加密的消息：")
    hash_string = md5_encrypt(message)
    print("MD5加密后的字符串是：", hash_string)


if __name__ == "__main__":
    main()
