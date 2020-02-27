from requests import get,put,post,delete
# t1=post('http://127.0.0.1:5000')

# params = {
#   # 'gov_id': 1,
#   'pageIndex': 1,
#   'pageSize': 2,
#   'keyWord': "贵阳"
# }
# t1 = get('http://127.0.0.1:5000/datasetSearch', params=params)
# print(t1.text)


# 用户注册
params = {
  'login_name': 'will',
  'login_password': '123456',
  'real_name': 'kkc',
  'phone_number': '15678301992',
  'email': '272104568@qq.com',
  'career': '自然语言处理算法工程师',
  'id_card': '123456678978979123'
}

t2 = post('http://127.0.0.1:5000/register', params=params)
print(t2.text)

# 用户登陆

# params = {
#   'login_name': 'will',
#   'login_password': '123456',
# }
#
# t3 = post('http://127.0.0.1:5000/login', params=params)
# print(t3.text)