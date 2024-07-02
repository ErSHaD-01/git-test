import requests
from bs4 import BeautifulSoup
import socket

class recon:
    def links(self , url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        links = []
        for link in soup.find_all("a"):
            href = link.get("href")        
            if href is not None and href.startswith("http"):
                links.append(href)
        print(links)
    def sub_domain(self , url):
        if url.startswith('http'):
            url = url.replace("https://","")

        with open("word.txt", "r") as file:
            for line in file:    
                subdomain_ = line.strip()
                subdomain_ += '.' + url
        try:
            answers = socket.gethostbyname(subdomain_)
            print(subdomain_ , '-' , answers)
        except:
            pass                    
    def status(self , url):
        response = requests.get(url)
        if response.status_code == 200:
            print("Success!")
        elif response.status_code == 404:
            print("Page not found.")
        elif response.status_code == 500:
            print("Internal server error.")
        else:
            print("Unknown status code:", response.status_code)                   
    def ip(self , url):
        if url.startswith('http'):
            url = url.replace("https://","")
        ip_address = socket.gethostbyname(url)
        print(ip_address)
    def port(self , url):
        if url.startswith('http'):
            url = url.replace("https://","")
        ip = socket.gethostbyname(url)
        common_ports = [21, 22, 23, 25, 53, 80, 110, 119, 123, 143, 161, 194, 443, 445, 993, 995]
        for port in common_ports:  
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print("Port {} is open".format(port))
            else:
                print("Port {} is closed".format(port))
            sock.close()        


url = input('Enter the url : ')


print('The Recon Tool :)')

recon_py = recon()
recon_py.links(url)
recon_py.status(url)
recon_py.sub_domain(url)
recon_py.ip(url)
recon_py.port(url)