# cloudflare-deldns
> 在一些特殊的情况dns疯狂的解析大量的记录,在删除的时候带来很大的困扰手动删除效率太慢,使用脚本执行效率很快每次可以删除100个记录,从而实现批量删除cloudflare的dns记录节省时间

#### 配置部分
- 以下三个变量必须修改自己的

```shell

API_TOKEN = "你的DNSOKEN"
ZONE_ID = "你的区域ID"
API_ENDPOINT = f"https://api.cloudflare.com/client/v4/zones/你的区域ID/dns_records"
```

#### 前提条件
- 脚本是基于Python实现的需要安装requests和json模块和基本环境,你可以通过 pip 安装：
```shell

# 执行安装依赖
pip install requests
# 执行文件
python cloudflaer.py

```

