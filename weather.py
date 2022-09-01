import requests
from bs4 import BeautifulSoup

#deger = input("İl Girini: ")
#deger1 = input("İlçe Giriniz: ")

koord={
"Adana"	: "37,35.32",
"Adıyaman" :	"37.764751,38.278561",
"Afyonkarahisar" : "38.750714, 30.556692",
"Ağrı" :	"39.626922,43021596",
"Aksaray" :	"38.36869,34.03698",
"Amasya" : 	"40.64991,35.83532",
"Ankara" :	"39.92077,32.85411",
"Antalya" :	"36.88414,30.70563",
"Ardahan" :	"41.110481,42.702171",
"Artvin" :	"41.18277,41.818292",
"Aydın" :	"37.856041,27.841631",
"Balıkesir" :	"39.648369,27.88261",
"Bartın" :	"41.581051,32.460979",
"Batman" :	"37.881168,41.13509",
"Bayburt" :	"40.255169,40.22488",
"Bilecik" :	"40.056656,30.066524",
"Bingöl" :	"39.062635,40.76961",
"Bitlis" :	"38.393799,42.12318",
"Bolu" :	"40.575977,31.578809",
"Burdur" :	"37.461267,30.066524",
"Bursa" :	"40.266864,29.063448",
"Çanakkale" :	"40.155312,26.41416",
"Çankırı" :	"40.601343,33.613421",
"Çorum"	:       "40.550556,34.955556",
"Denizli" :	"37.77652,29.08639",
"Diyarbakır" :  "37.91441,40.230629",
"Düzce"	 :      "40.843849,31.15654",
"Edirne" :	"41.681808,26.562269",
"Elazığ" :      "38.680969,39.226398",
"Erzincan" :	"39.75,39.5",
"Erzurum" :	"39.9,41.27",
"Eskişehir" :	"39.776667,30.520556",
"Gaziantep" :	"37.06622,37.38332",
"Giresun" :	"40.912811,38.38953",
"Gümüşhane" :	"40.438588,39.508556",
"Hakkari" :	"37.583333,43.733333",
"Hatay"  :      "36.401849,36.34981",
"Iğdır" :	"39.887984,44.004836",
"Isparta" :	"37.764771,30.556561",
"İstanbul" :	"41.00527,28.97696",
"İzmir" :	"38.41885,27.12872",
"Kahramanmaraş" : "37.585831,36.937149",
"Karabük" :	"41.2061,32.62035",
"Karaman" :	"37.17593,33.228748",
"Kars" :	"40.616667,43.1",
"Kastamonu" :	"41.38871,33.78273",
"Kayseri" :	"38.73122,35.478729",
"Kırıkkale" :	"39.846821,33.515251",
"Kırklareli" :	"41.733333,27.216667",
"Kırşehir" :	"39.14249,34.17091",
"Kilis" :	"36.718399,37.12122",
"Kocaeli" :	"40.85327,29.88152",
"Konya" :	"37.866667,32.483333",
"Kütahya" :	"39.416667,29.983333",
"Malatya" :	"38.35519,38.30946",
"Manisa" :	"38.619099,27.428921",
"Mardin" :	"37.321163,40.724477",
"Mersin" :	"36.8,34.633333",
"Muğla" :	"37.215278,28.363611",
"Muş" :	        "38.946189,41.753893",
"Nevşehir" :	"38.69394,34.685651",
"Niğde" :	"37.966667,34.683333",
"Ordu" :	"40.983879,37.876411",
"Osmaniye" :	"37.213026,36.176261",
"Rize" :	"41.02005,40.523449",
"Sakarya" :	"40.693997,30.435763",
"Samsun" :	"41.292782,36.33128",
"Siirt" :	"37.933333,41.95",
"Sinop" :	"42.02314,35.153069",
"Sivas" :	"39.747662,37.017879",
"Şanlıurfa" :	"37.159149,38.796909",
"Şırnak" :	"37.418748,42.491834",
"Tekirdağ" :	"40.983333,27.516667",
"Tokat" :	"40.316667,36.55",
"Trabzon" :	"41.00145,39.7178",
"Tunceli" :	"39.307355,39.438778",
"Uşak" :	"38.682301,29.40819",
"Van" :	        "38.48914,43.40889",
"Yalova" :	"40.65,29.266667",
"Yozgat" :	"39.818081,34.81469",
"Zonguldak" :	"41.456409,31.798731"
}
il=input("Lütfen plaka numarası giriniz: ")

SELECTOR = "#WxuCurrentConditions-main-eb4b02cb-917b-45ec-97ec-d4eb947f6b6a > div > section > div > div.CurrentConditions--body--8sQIV > div.CurrentConditions--columns--3KgfN > div.CurrentConditions--primary--2SVPh > span"

#URL = f"https://www.mgm.gov.tr/?il={deger}&ilce={deger1}"
URL = f"https://weather.com/weather/today/l/{koord[il]}"

html = requests.get(
    URL,
    headers={
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.58',
    }
).text.encode("utf-8")
soup = BeautifulSoup(html, "html.parser")
fderece = soup.select_one(SELECTOR).text
fderece = fderece.rstrip("°")
cderece = (int(fderece)-32)*5/9
print(round(cderece))



