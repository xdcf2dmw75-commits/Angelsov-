import requests
import socket
import hashlib
import ssl

# Баннер
print("""
================================
        ANGEL KOROL TOOL
================================
""")

def hash_checker():
    text = input("Введите текст: ")
    print("MD5:", hashlib.md5(text.encode()).hexdigest())
    print("SHA1:", hashlib.sha1(text.encode()).hexdigest())
    print("SHA256:", hashlib.sha256(text.encode()).hexdigest())

def subdomain_scan():
    domain = input("Домен: ")
    subs = ["www", "mail", "ftp", "api", "test", "dev"]
    for sub in subs:
        try:
            ip = socket.gethostbyname(f"{sub}.{domain}")
            print(f"{sub}.{domain} -> {ip}")
        except:
            pass

def http_headers():
    url = input("URL: ")
    try:
        r = requests.get(url)
        print(r.headers)
    except:
        print("Ошибка")

def url_status():
    url = input("URL: ")
    try:
        r = requests.get(url)
        print("Статус:", r.status_code)
    except:
        print("Ошибка")

def dns_reverse():
    ip = input("IP: ")
    try:
        print(socket.gethostbyaddr(ip))
    except:
        print("Нет данных")

def ssl_info():
    domain = input("Домен (без https): ")
    try:
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=domain) as s:
            s.settimeout(3)
            s.connect((domain, 443))
            cert = s.getpeercert()
            print("Сертификат выдан для:", cert.get('subject'))
            print("Действителен до:", cert.get('notAfter'))
    except:
        print("Ошибка SSL")

def port_check():
    ip = input("IP: ")
    port = int(input("Порт: "))
    sock = socket.socket()
    sock.settimeout(1)
    result = sock.connect_ex((ip, port))
    print("Открыт" if result == 0 else "Закрыт")
    sock.close()

def site_title():
    url = input("URL: ")
    try:
        r = requests.get(url)
        start = r.text.lower().find("<title>")
        end = r.text.lower().find("</title>")
        if start != -1 and end != -1:
            print("Title:", r.text[start+7:end])
        else:
            print("Не найдено")
    except:
        print("Ошибка")

while True:
    print("""
1. Хеширование
2. Поиск поддоменов
3. HTTP заголовки
4. Статус сайта
5. Reverse DNS
6. SSL информация
7. Проверка порта
8. Title сайта
9. Выход
""")
    c = input("Выбор: ")

    if c == "1":
        hash_checker()
    elif c == "2":
        subdomain_scan()
    elif c == "3":
        http_headers()
    elif c == "4":
        url_status()
    elif c == "5":
        dns_reverse()
    elif c == "6":
        ssl_info()
    elif c == "7":
        port_check()
    elif c == "8":
        site_title()
    elif c == "9":
        break
    else:
        print("Неверный выбор")
