import base64

def custom_encrypt(text):
    # 将UTF-8格式的文本转换为Base64编码
    base64_encoded = base64.b64encode(text.encode('utf-8')).decode('ascii')

    # 将Base64编码的字符转换为二进制数字
    binary_numbers = ' '.join(format(ord(char), '08b') for char in base64_encoded)

    # 根据二进制数字进行汉字匹配（这里只是一个简单示例，您可以根据需求自定义匹配规则）
    encrypted_text = ''.join(chr(int(binary, 2) % 20901 + 19968) for binary in binary_numbers.split())

    return encrypted_text

def custom_decrypt(encrypted_text):
    # 将汉字还原为二进制数字
    binary_numbers = ' '.join(format(ord(char) - 19968, '013b') for char in encrypted_text)

    # 将二进制数字还原为Base64编码
    base64_encoded = ''.join(chr(int(binary, 2)) for binary in binary_numbers.split())

    # 将Base64编码还原为UTF-8格式的文本
    decrypted_text = base64.b64decode(base64_encoded).decode('utf-8')

    return decrypted_text

# 用户输入正常的中文文本（UTF-8格式）
input_text = input("请输入中文文本：")

# 加密
encrypted_text = custom_encrypt(input_text)
print("加密后:", encrypted_text)

# 解密
decrypted_text = custom_decrypt(encrypted_text)
print("解密后:", decrypted_text)
