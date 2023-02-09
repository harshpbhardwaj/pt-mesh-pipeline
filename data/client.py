import requests
import csv
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
}

def step1():

    # for site 1
    url = "http://www.ggzy.gov.cn"
    r = requests.get(url, headers=headers)
    html_content = r.content
    soup = BeautifulSoup(html_content, 'html.parser')
    def get_data_site1(dt,a):
        i=len(a)
        for datas in dt:
            dt_a = datas.find("a")
            if (dt_a and datas.find("span")):
                a[i] = {
                    "url" : url + dt_a.get('href'),
                    "title" : dt_a.text,
                    "time" : datas.find("span").text
                }
                i+=1
        return a
    dt = soup.find("div", class_="lunbo_tw").find_all("li")
    a={}
    a = get_data_site1(dt,a)
    dt_n = soup.find_all("div", class_="main_list_on")
    for dt_new in dt_n:
        dt = dt_new.find_all("li")
        a = get_data_site1(dt,a)
    dt = soup.find("div", class_="cont_on").find_all("li")
    a = get_data_site1(dt,a)

    # for site 2
    url = "https://www.chinabidding.com/en"
    r = requests.get(url, headers=headers, verify=False)
    html_content = r.content
    soup = BeautifulSoup(html_content, 'html.parser')
    dt = soup.find_all("li", class_="ui-list-item")
    i=len(a)
    for datas in dt:
        dt_a = datas.find("a")
        if (dt_a and datas.find("p")):
            a[i] = {
                "url" : dt_a.get('href'),
                "title" : dt_a.text,
                "time" : datas.find("p", class_="float-right gray").text
            }
            i+=1


    # for site 3
    url = "http://en.chinabidding.mofcom.gov.cn/"
    r = requests.get(url, headers=headers, verify=False)
    html_content = r.content
    soup = BeautifulSoup(html_content, 'html.parser')
    dt_all_ul = soup.find_all("ul", class_="txt-02")
    i=len(a)
    for dt_ul in dt_all_ul:
        dt = soup.find_all("li")
        for datas in dt:
            dt_a = datas.find("a")
            if (dt_a and datas.find("span")):
                a[i] = {
                    "url" : url + dt_a.get('href'),
                    "title" : dt_a.text,
                    "time" : datas.find("span", class_="fr").text
                }
                i+=1
                

    # for site 4
    base_url = "https://www.cpppc.org/en"
    def get_data_site4(dt,a):
        i=len(a)
        for datas in dt:
            dt_a = datas.find("a")
            if (dt_a and datas.find("span")):
                a[i] = {
                    "url" : base_url + dt_a.get('href'),
                    "title" : dt_a.text,
                    "time" : datas.find("span", class_="second-list-date").text
                }
                i+=1
        return a

    url = base_url + "/zlk.jhtml"
    r = requests.get(url, headers=headers, verify=False)
    html_content = r.content
    soup = BeautifulSoup(html_content, 'html.parser')
    dt = soup.find_all("li", class_="second-list-item")
    a = get_data_site4(dt,a)

    url = base_url + "/xmjc.jhtml"
    r = requests.get(url, headers=headers, verify=False)
    html_content = r.content
    soup = BeautifulSoup(html_content, 'html.parser')
    dt = soup.find_all("li", class_="second-list-item")
    a = get_data_site4(dt,a)


    # for site 5
    base_url = "https://www.cpppc.org:8082"
    def get_data_site5(dt,a):
        i=len(a)
        for datas in dt:
            dt_a = datas.find("a")
            if (dt_a and datas.find("span")):
                a[i] = {
                    "url" : base_url + dt_a.get('href'),
                    "title" : dt_a.text,
                    "time" : datas.find("span").text
                }
                i+=1
        return a

    url = "https://www.cpppc.org"
    r = requests.get(url, headers=headers)
    html_content = r.content
    soup = BeautifulSoup(html_content, 'html.parser')
    dt = soup.find_all("li", class_="component-short-list-item")
    # print(dt)
    a = get_data_site5(dt,a)
    dt = soup.find_all("li", class_="component-list-item")
    a = get_data_site5(dt,a)



    return a

a = step1()

# step 2 save to file
def step2(a):
    data_file = open('products.csv', 'w', encoding="utf-8")
    csv_writer = csv.writer(data_file)
    csv_writer.writerow(["url", "title", "time"])
    for i in a:
        csv_writer.writerow([a[i]["url"], a[i]["title"], a[i]["time"]])
    data_file.close()

step2(a)