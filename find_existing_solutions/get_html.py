import wget 
url="https://pubchem.ncbi.nlm.nih.gov/#query=C1%3DCC%3DC(C%3DC1)C%3DO"
html = wget.download(url)
print(html)

import requests
file_name = "html_query_data.html"
url="https://pubchem.ncbi.nlm.nih.gov/#query=C1%3DCC%3DC(C%3DC1)C%3DO"
with open(file_name, 'wb') as f:
    resp = requests.get(url, verify=False)
    print(resp.content)
    f.write(resp.content)

import requests
file_name = "html_query_data.html"
url="https://pubchem.ncbi.nlm.nih.gov/#query=C1%3DCC%3DC(C%3DC1)C%3DO"
with open(file_name, 'wb') as f:
    resp = requests.get(url, verify=False)
    print(resp.content)
    f.write(resp.content)