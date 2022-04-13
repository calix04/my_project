import tkinter
import requests
from bs4 import BeautifulSoup
from tkinter import*
from tkinter import messagebox as msg

def scrape_school():
    url ="https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=blBI&pkid=682&os=24929523&qvt=0&query=%EC%84%9C%EC%9A%B8%EC%95%84%EC%9D%B4%ED%8B%B0%EA%B3%A0%EB%93%B1%ED%95%99%EA%B5%90"
    res = requests.get(url)
    soup = BeautifulSoup(res.text,"lxml")
    date_1 = soup.find("strong", attrs={"class":"cm_date"}).get_text()
    today = soup.find("ul", attrs={"class":"item_list"}).get_text()
    
    
    message = ('{}{}'.format(date_1, today))
    print(message)
    tkinter.messagebox.showinfo('급식',message)
scrape_school()