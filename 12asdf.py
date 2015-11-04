import requests
res = requests.get("https://searchcode.com/api/codesearch_I/?q="+badword)
json_data = json.loads(res.text)
