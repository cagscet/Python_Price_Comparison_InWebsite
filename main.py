from bs4 import BeautifulSoup
import requests

#link-1 https://www.trendyol.com/zippo/cakmak-hi-polish-parlak-gri-250-021764-p-32922036?boutiqueId=61&merchantId=351189
#link-2 https://www.trendyol.com/s-t-dupont/cakmak-abstraction-s-urban-limited-edition-p-279154710?boutiqueId=61&merchantId=106316

def extract_price(price_str):
    price_str = price_str.replace("₺", "").replace("TL", "").replace(".", "").replace(",", ".").strip()
    return float(price_str)

url = input("Lütfen ilk ürünün linkini verin : ")

sayfa = requests.get(url)

html_sayfa = BeautifulSoup(sayfa.content,"html.parser")

isim = html_sayfa.find("h1", class_="pr-new-br").getText()
fiyat = html_sayfa.find("div", class_="pr-bx-w").getText()
float_fiyat = extract_price(fiyat)


url2 = input("Lütfen ikinci ürünün linkini verin : ")
sayfa2 = requests.get(url2)

html_sayfa2 = BeautifulSoup(sayfa2.content,"html.parser")
isim2 = html_sayfa2.find("h1",class_="pr-new-br").getText()
fiyat2 = html_sayfa2.find("div",class_="pr-bx-w").getText()
float_fiyat2 = extract_price(fiyat2)

if fiyat > fiyat2:
    print(f"İlk ürün {isim} daha pahalı değeri {float_fiyat} diğer ürün {isim2} değeri {float_fiyat2}")
elif fiyat2 > fiyat:
    print(f"ikinci ürün {isim2} daha pahalı değeri {float_fiyat2} diğer ürün {isim} değeri {float_fiyat}")
else: print(f"{isim2} ve {isim} aynı fiyata sahipler")