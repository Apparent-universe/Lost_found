import requests
import json

# API 基础URL
BASE_URL = "http://localhost:8000"  # 根据你的实际地址修改

# 1. 注册接口测试
def test_register():
    url = f"{BASE_URL}/users/register/"
    data = {
        "username": "testuser",
        "password": "123456",
        "role": "agent"
    }
    response = requests.post(url, json=data)
    print("注册结果:")
    print(response.json())
    return response.json().get("token")

# 2. 登录接口测试
def test_login():
    url = f"{BASE_URL}/users/login/"
    data = {
        "username": "testuser",
        "password": "123456"
    }
    response = requests.post(url, json=data)
    print("登录结果:")
    print(response.json())
    return response.json().get("token")

# 3. 获取探员信息
def test_get_profile(token):
    url = f"{BASE_URL}/users/profile/"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    print("获取探员信息结果:")
    print(response.json())

# 4. 更新探员信息
def test_update_profile(token):
    url = f"{BASE_URL}/users/profile/"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "contact": "123456789",
        "free_time": "晚上",
        "personal_info": "我是一个热心人"
    }
    response = requests.put(url, json=data, headers=headers)
    print("更新探员信息结果:")
    print(response.json())

# 5. 上传微信二维码
def test_upload_qrcode(token):
    url = f"{BASE_URL}/users/upload_qrcode/"
    headers = {"Authorization": f"Bearer {token}"}
    
    # 注意：需要替换为实际的本地图片路径
    with open("wechat_qrcode.jpg", "rb") as file:
        files = {"file": file}
        response = requests.post(url, headers=headers, files=files)
    
    print("上传微信二维码结果:")
    print(response.json())

if __name__ == "__main__":
    # 先注册获取token
    token = test_register()
    
    # 如果注册失败，尝试登录获取token
    if not token:
        token = test_login()
    
    if token:
        # 使用token测试其他接口
        test_get_profile(token)
        test_update_profile(token)
        
        # 注意：上传二维码需要本地有图片文件
        # 请确保当前目录下有 wechat_qrcode.jpg 文件
        # 或者修改代码中的文件路径
        # test_upload_qrcode(token)
    else:
        print("获取token失败，无法继续测试")