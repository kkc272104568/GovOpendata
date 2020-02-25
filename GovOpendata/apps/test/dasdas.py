from requests import get,put,post,delete
# t1=post('http://127.0.0.1:5000')

params = {
  # 'gov_id': 1,
  'pageIndex': 1,
  'pageSize': 2,
  'keyWord': "贵阳"
}
t1 = get('http://127.0.0.1:5000/datasetSearch', params=params)
print(t1.text)