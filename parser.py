from datetime import datetime

import lxml.etree
import lxml.html
import requests


def parse_list():
    url = 'http://forum.poehali.net/index.php?board=12'
    page = lxml.html.fromstring(requests.get(url).content)
    results = []
    for row in page.xpath('//table//table//table//table//tr')[2:][::-1]:
        link = row.xpath('.//td[3]//a')[0]
        results.append(link.attrib['href'])
    return results


def parse_page(url):
    page = lxml.html.fromstring(requests.get(url).content)
    title = ' > '.join(item.text_content().strip() for item in page.xpath('//div[@class="imgheader"]/a/b'))
    date = page.xpath('//font[@class="font1"]')[1].text_content().split(',')[1].strip()
    post = page.xpath('//table//table//table//table//tr')[0].xpath('./td[2]/div[2]')[0]
    return title, datetime.strptime(date, '%d.%m.%Y в %H:%M'), lxml.etree.tostring(post).decode('utf8').strip()


def parse_icon():
    return requests.get('http://poehali.net/images/favicon_poehali_org.ico').content
