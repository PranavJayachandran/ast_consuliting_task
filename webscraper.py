from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from db import get_database

items=[]

def scrap(url,driver):
    driver.get(url)
    soup=BeautifulSoup(driver.page_source,'html.parser')

    class_name='slider_item'
    div_elements=soup.find_all('div',class_=class_name)

    for div_element in div_elements:
        title=div_element.find('h2',class_="jobTitle").find('a')
        companyLocation=div_element.find('div',class_="company_location")
        jobRequirement=[]
        metadata=[]
        jd=div_element.find('div',class_='job-snippet')
        if jd.ul and jd.ul.li:
            jd=jd.ul.li
        else :
            jd=[]
        md=div_element.find_all('div',class_="metadata")
        for l in md:
            metadata.append(l.div.text)
        for l in jd:
            jobRequirement.append(l.text)
        items.append({
            "jobTitle":title.span.text,
            "companyLocation":companyLocation.text,
            "jobRequirement":jobRequirement,
            "metadata":metadata
        })

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

urls=[
    "https://in.indeed.com/jobs?q=python+developer&pp=gQAAAAABi001xLIAAAACFLDNDAADAAABAAA&vjk=9bb6f4cd1c51ab8d",
     "https://in.indeed.com/jobs?q=python+developer&start=10&pp=gQAPAAABi001xLIAAAACFLDNDAApAQAA26hojr9Q7aUGderTEyuT5vG5cijek9DLMFG_zh1gP9iqynVhZW4AAA",
     "https://in.indeed.com/jobs?q=python+developer&start=20&pp=gQAeAAABi001xLIAAAACFLDNDABBAQEBCQFpRToUWG6ZVcPWnxzW1I8uYhTZFKJt4UcBxv4G1QRC6WILyAiBzLJ5c0E3JzW1HIzvvflcTuwRodUUMpkAAA",
     "https://in.indeed.com/jobs?q=python+developer&start=30&pp=gQAtAAABi001xLIAAAACFLDNDABbAQIBCRoJAKiL-kXVNfeLbNqCSjf91DebCLsGKt9d-Q-pLOA2yNSoxhMcO_shfA0Nz1wOusk341ZaJzt0NvkHaNlbE-XdPpUv5ZXGAqCXGHMZhXalilf-zCds8gAA",
     "https://in.indeed.com/jobs?q=python+developer&start=40&pp=gQA8AAABi001xLIAAAACFLDNDABwAQIBCRQMBinijsNqzsYcvSqTrEyJ0S9sN-R90-EB8JbFSQERXs-gmsKCwUyc4NUy3zjhKEZumavL1NxXpoPEYg_GQ5QQy4eozZaSCEurrA1wBGrR33Uk9_KFxheBzbwW6n4HX0RTy4x-Aq5JKAwpnQAA",
     "https://in.indeed.com/jobs?q=python+developer&start=50&pp=gQBLAAABi001xLIAAAACFLDNDACIAQIBCRQPFCZKjb-U0Zq5FyFQPdLxxl37liQQtsVUTwQDBdaS1uybwj5qB-v2pgOhGQ9Zc52AVPcb1EnVOjMSzKhug1My_PaXQLwpFkQvj6GBCEvb9RarGuEm5etAjcZSD1XgV15l6iHBuuyb56yHKaP1O5c2IVJeIvEX-iUnPph0KMKsigELNAAA",
     "https://in.indeed.com/jobs?q=python+developer&start=60&pp=gQBaAAABi001xLIAAAACFLDNDACcAQEBHwUSQLTxexbrHQHB65Y1Ip-aCNzD7XqlKXEGBCqxnRxfHky12YtR95mm25lBfBOz1rKD-T2tAnicpik2HMWfJ-hqZJwMZ_ERc8Sglhp-47ahPzNvkxjtI5Ttg2BC1EM3bB37qzjqT60EuCpBKRtOqpPvwyHUV57aPCfaOJ45sbZzyEVcyATu7kVaWbzhjvR8R4qWMm8jkHr7AAA&vjk=36d0a5fc70b96d66",
     "https://in.indeed.com/jobs?q=python+developer&start=70&pp=gQBpAAABi001xLIAAAACFLHIHQCqAQEBHy2WfDm5SzA4XEjNgxQM1meH0vAjcnSBX_B6kzybbq1sj8P2cj26bdzH7PQuJ5VWQ5-kywGoSlYMo_Exc_kl1exnoGzQcUhQKs5G2dDx0XqOmAsykTWYCqJOHTYDNdeL1V_2SfJ010Ji3u2eqGXIp8AsY2yx_Zex0zIQp2M9weSmQYNlRbqfPoITA-GHlUu7EXT1uP2eEl4w-qeHQM9WU7e_MdTviREAAA",
     "https://in.indeed.com/jobs?q=python+developer&start=80&pp=gQB4AAABi001xLIAAAACFLDNDAC5AQIBH24JKbihH-V1qFUDL_As0beWNXK2bo4DoN24BHy7uG3i_vwd9mGSge2nl0JkbvN-jSyhRqZT0jSKxXKS503shWPtW0fdO8Z_GEsts5YKxyXNPyMxcnykJB4wHgciVB75UlhIhHjVvuC9klUbYzBGWnIxoAa7xsZsJTmHHaK0LOO_OhVMrzdsil_y9ox5v3wdvjtGx9CdEQumdXK_wu_gwqhN1LqtDoJ8UtYJR0qKdia3rs3YfKwAAA&vjk=9cd13a8abe68b53d",
     "https://in.indeed.com/jobs?q=python+developer&start=90&pp=gQCHAAABi001xLIAAAACFLDNDADFAQMBI2wKQAZXzjCCbn0eO3hFVNhYvmva0s2xDgzoGQ1Ld1RIEp_HeQ9UgofTjEIgw9ucflnkKTrw6_3iTcO4wuInCjU21JE4-eGy0fJVtcy2hm45LKCmlC9sxvmlyLvaabjLnZfxhaOdGN6gBKNXPowJKCNCJ7kHa1AiHUYYl3KUuesgfvCGk8XRIX4kg1x1FtsaF48-_5Xs9PqMF5_CwM9VqOKQ9MXyvJH9qBpzrCffLbE5CU_-RO30TrkOjYvWNuKXmssAAA"
     ]

for url in urls:
    scrap(url,driver)


dbname=get_database()
collection_name=dbname["pythonDeveloperJobs"]
collection_name.delete_many({})
collection_name.insert_many(items)