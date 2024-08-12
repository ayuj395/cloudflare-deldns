import requests

# 配置部分
API_TOKEN = "你的cloudflare的DNSTOKEN"
ZONE_ID = "你的区域ID"
API_ENDPOINT = f"https://api.cloudflare.com/client/v4/zones/你的区域ID/dns_records"
PER_PAGE = 600  # 每页处理的 DNS 记录数
page = 1        # 从第一页开始

while True:
    # 获取 DNS 记录
    response = requests.get(API_ENDPOINT, headers={
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }, params={
        "page": page,
        "per_page": PER_PAGE
    })

    if response.status_code == 200:
        dns_records = response.json().get('result', [])
        
        if dns_records:
            # 批量删除 DNS 记录
            for record in dns_records:
                record_id = record['id']
                delete_endpoint = f"{API_ENDPOINT}/{record_id}"
                delete_response = requests.delete(delete_endpoint, headers={
                    "Authorization": f"Bearer {API_TOKEN}",
                    "Content-Type": "application/json"
                })

                # 检查删除操作是否成功
                if delete_response.status_code == 200 and delete_response.json().get('success'):
                    print(f"成功删除 DNS 记录 ID: {record_id}")
                else:
                    print(f"删除 DNS 记录 ID: {record_id} 失败，状态码: {delete_response.status_code}")
                    print(f"错误信息: {delete_response.json().get('errors', '没有错误信息')}")
            
            # 移动到下一页
            page += 1
        else:
            # 如果没有更多的 DNS 记录，退出循环
            print("所有 DNS 记录已删除完成。")
            break
    else:
        print(f"获取 DNS 记录失败，状态码: {response.status_code}")
        print("错误信息:")
        errors = response.json().get('errors', [])
        if errors:
            for error in errors:
                print(f"  错误信息: {error.get('message', '没有错误信息')}")
        else:
            print("没有提供详细的错误信息。")
        break
