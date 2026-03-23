import requests
import urllib.parse
from config import config as cfg

# URL que queremos converter
targetUrl = "https://andrewbeatty1.pythonanywhere.com/bookviewer.html"

# API key
apiKey = cfg["htmltopdfkey"]

# Endpoint
apiurl = "https://api.html2pdf.app/v1/generate"

# Parâmetros exigidos pela API
params = {
    "url": targetUrl,
    "apiKey": apiKey
}

# Codifica parâmetros na query string
query_string = urllib.parse.urlencode(params)

# Monta URL final
request_url = f"{apiurl}?{query_string}"

print("Request URL:", request_url)

# Faz a requisição
response = requests.get(request_url)

print("Status:", response.status_code)

# Se sucesso, salva o PDF
if response.status_code == 200:
    with open("output.pdf", "wb") as f:
        f.write(response.content)
    print("PDF saved as output.pdf")
else:
    print("Error generating PDF")