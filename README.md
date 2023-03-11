# BestFourPoint
<pre>
1. 下載 Python SDK
https://www.python.org/downloads/
進行安裝

2. 下載 openssl
https://slproweb.com/products/Win32OpenSSL.html
Win64 OpenSSL v3.0.8 Light
EXE | MSI <-- 選擇 MSI
進行安裝

3. 環境變數設定(關鍵字: env)
C:\Users\Administrator\AppData\Local\Programs\Python\Python311
C:\Users\Administrator\AppData\Local\Programs\Python\Python311\Scripts
C:\Program Files\OpenSSL-Win64\bin

4. 開啟 cmd 依序執行下列指令
python.exe -m pip install --upgrade pip
pip install requests
pip install uvicorn
pip install pillow
pip install fastapi
pip install twstock
pip install lxml
pip install matplotlib

5. 將 BestForPoint 程式複製到桌面上

6. 開啟 cmd 執行
cd desktop/BestForPoint

7. 在 console 執行
python api.py
or
uvicorn.run("api:app", host="0.0.0.0", port=8000, log_level="info")

8. 打開瀏覽器
http://127.0.0.1:8000/docs

----------------------------------------------------------------------




generate cert:
openssl req -x509 -newkey rsa:4096 -nodes -out server.crt -keyout server.key -days 365

uvicorn api:app --ssl-keyfile server.key --ssl-certfile server.crt
or
uvicorn.run("api:app", host="0.0.0.0", port=443, log_level="info", ssl_keyfile="server.key", ssl_certfile="server.crt")
or
python api.py

test:
https://127.0.0.1/docs
</pre>
