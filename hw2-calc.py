import requests
from pyquery import PyQuery

url = 'http://ctf.hackucf.org:4000/calc/calc.php'
r = requests.get(url)
if(r.status_code == 200):
    cookie = r.headers['Set-Cookie']
    html = r.text
    pq = PyQuery(html)
    tag = pq('expression')
    text = tag.text().replace('\n', ' ')
    print text
    result = eval(text)
    print result
    headers = {"Cookie": cookie}
    p = requests.post(url, data={'answer': str(result)}, headers=headers)
    print p.text
