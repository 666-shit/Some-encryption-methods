import base64


def encrypt(message):
    """
    将消息加密为字母和数字的组合
    """
    # 将消息编码为字节串
    message_bytes = message.encode('utf-8')

    # 对字节串进行base64编码
    base64_bytes = base64.b64encode(message_bytes)

    # 将base64编码后的字节串转换为字符串
    encrypted_message = base64_bytes.decode('utf-8')

    return encrypted_message


def decrypt(encrypted_message):
    """
    将加密消息解密为原始消息
    """
    # 将加密消息转换为字节串
    encrypted_bytes = encrypted_message.encode('utf-8')

    # 对字节串进行base64解码
    decrypted_bytes = base64.b64decode(encrypted_bytes)

    # 将解码后的字节串转换为字符串
    decrypted_message = decrypted_bytes.decode('utf-8')

    return decrypted_message


# 获取用户选择的操作：加密或解密
operation = input("请选择要进行的操作（1.加密/2.解密）：")

if operation == "1":
    # 获取要加密的消息
    message = input("请输入要加密的消息：")

    # 加密消息并输出结果
    encrypted_message = encrypt(message)
    print("加密后的消息是：", encrypted_message)

elif operation == "2":
    # 获取要解密的消息
    encrypted_message = input("请输入要解密的消息：")

    # 解密消息并输出结果
    decrypted_message = decrypt(encrypted_message)
    print("解密后的消息是：", decrypted_message)

else:
    print("无效的操作。请重新运行程序并输入“加密”或“解密”。")
