# BestFourPoint

<pre>
pip env path:
C:\Users\Administrator\AppData\Local\Programs\Python\Python311\Scripts

python.exe -m pip install --upgrade pip
pip install requests
pip install uvicorn
pip install pillow
pip install fastapi
pip install twstock
pip install lxml
pip install matplotlib

uvicorn.run("api:app", host="0.0.0.0", port=8000, log_level="info")
or
python api.py

http://127.0.0.1:8000/docs


download openssl
https://slproweb.com/products/Win32OpenSSL.html
Win64 OpenSSL v3.0.8 Light
EXE | MSI

openssl env:
C:\Program Files\OpenSSL-Win64\bin

generate cert:
openssl req -x509 -newkey rsa:4096 -nodes -out server.crt -keyout server.key -days 365

uvicorn api:app --ssl-keyfile server.key --ssl-certfile server.crt
or
uvicorn.run("api:app", host="0.0.0.0", port=443, log_level="info", ssl_keyfile="server.key", ssl_certfile="server.crt")
or
python api.py
</pre>
