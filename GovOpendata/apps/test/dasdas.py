from requests import get,put,post,delete
# t1=post('http://127.0.0.1:5000')

params = {
  'aa' : 'aaaaaaaaaaaa',
}
t1=get('http://127.0.0.1:5000', params=params)
print(t1.text)
