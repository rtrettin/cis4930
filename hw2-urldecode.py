import urllib

url = '%66%6c%61%67%7b%68%31%64%31%6e%67%5f%31%6e%5f%70%6c%34%31%6e%5f%73%31%74%33%7d'

print urllib.unquote(url).decode('utf8')
