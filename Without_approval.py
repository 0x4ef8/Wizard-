# Code by Betrayal Bishesh

# ────────────────[Imports]─────────────────
import requests
import re
import uuid
import random
import os
import time
import threading
import json
import base64
import platform
import logging
from datetime import datetime
from time import sleep


import random
from atexit import register
from time import sleep
import os,json,re,sys
import threading,base64
import os,time,re,json,random
from datetime import datetime
from time import sleep,strftime
import requests
from concurrent.futures import ThreadPoolExecutor as loda
from bs4 import BeautifulSoup
import requests
from time import strftime


def check_install_requests():
    try:
        import requests
    except ModuleNotFoundError:
        os.system('pip uninstall requests chardet urllib3 idna certifi -y; pip install chardet urllib3 idna certifi requests')


check_install_requests()
# ────────────────[Gitpull]─────────────────

try:
    os.system('clear')
    print("\033[1;36mCHECKING UPDATES....")
    os.system("git pull > /dev/null 2>&1")
except:
    pass
    
# ────────────────[Colours]─────────────────
red = '\033[1;91m'
ye = '\033[1;93m'
blue = '\033[1;94m'
mage = '\033[1;95m'
cyan = '\033[1;96m'
c = '\033[1;96m'
w = '\033[1;97m'
wh = '\033[1;97m'
reset = '\033[0m'
r = '\033[0m'

# ────────────────[Logo]─────────────────

logo = (f''' 
       \033[1;96m   ╔═╗╔═╗ ╦ ╦╔═╗  ╔╗ ╔═╗╔═╗╔═╗╔╦╗
       \033[1;96m   ╠═╣║═╬╗║ ║╠═╣  ╠╩╗║ ║║ ║╚═╗ ║ 
       \033[1;97m   ╩ ╩╚═╝╚╚═╝╩ ╩  ╚═╝╚═╝╚═╝╚═╝ ╩  {c}「{red}v•1{c}」{r} \n''')



# ────────────────[Linex]─────────────────

def linex():
    print(f'  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

# ────────────────[Clear]─────────────────
def clear():
    os.system('clear')
    print(logo)
    
    
# ────────────────[Create Direc]─────────────────


import os

folder_name = "/sdcard/Aqua"
file_names = ["toka.txt", "tokaid.txt", "tokp.txt", "tokpid.txt", "cok.txt", "cokid.txt"]

# Check if the folder exists, if not, create it
if not os.path.exists(folder_name):
    try:
        os.makedirs(folder_name)
        print(f"Folder '{folder_name}' created.")
    except Exception as e:
        print(f"Failed to create folder '{folder_name}': {e}")
else:
    print(f"Folder '{folder_name}' already exists.")

# Check each file in the list
for file_name in file_names:
    file_path = os.path.join(folder_name, file_name)
    if not os.path.exists(file_path):  # Check if file exists
        try:
            with open(file_path, 'w') as file:
                pass  # Create an empty file if it doesn't exist
            print(f"File '{file_path}' created.")
        except Exception as e:
            print(f"Failed to create file '{file_path}': {e}")
    else:
        print(f"File '{file_path}' already exists.")
        

# ────────────────[Approval]─────────────────

#Removed 

# ────────────────[Approvalf]─────────────────

#Removed 

# ────────────────[Count line]─────────────────

def count_lines(file_path):
   
    try:
        with open(file_path, 'r') as file:
            return sum(1 for line in file)
    except FileNotFoundError:
        return 0

# ────────────────[PSB to post ID]─────────────────

def linktradio(post_link):
    def extract_postid_from_link(post_link):
        pattern = r'https://www\.facebook\.com/\d+/posts/(\d+)/?'
        match = re.match(pattern, post_link)
        if match:
            return match.group(1)
        else:
            return None

    def convert_to_traodoisub(url):
        try:
            response = requests.post('https://id.traodoisub.com/api.php', data={'link': url})
            if response.status_code == 200:
                result = response.json().get('id')
                return result
            else:
                return None
        except Exception as e:
            print(f'An error occurred: {e}')
            return None

    if re.search(r'/posts/\d+', post_link):
        post_id = extract_postid_from_link(post_link)
        if post_id:
            return post_id
    elif 'pfbid' in post_link:
        post_id = convert_to_traodoisub(post_link)
        if post_id:
            return post_id

    return 'Invalid link format or unable to process the link.'

# ────────────────[Overview]─────────────────

def overview():
    print(f"\033[1;96m  ━━━━━━━━━━━━━━━━━━━[{red}OVERVIEW{c}]━━━━━━━━━━━━━━━━━━━━━")
    total_accounts = count_lines("/sdcard/Aqua/toka.txt")
    total_pages = count_lines("/sdcard/Aqua/tokp.txt")
    print(f"  {r}     TOTAL ACCOUNTS: {c}{total_accounts}{r} | TOTAL PAGES: {c}{total_pages} {r}")
    print(f'{c}  ══════════════════════════════════════════════════{wh}')

# ────────────────[Setup - Data]─────────────────

def setup_user_data():
    os.makedirs("data", exist_ok=True)
    
    def create_file_if_not_exists(file_path):
        if not os.path.exists(file_path):
            open(file_path, "w").close()
    
    create_file_if_not_exists("data/nameaq.xml")
    create_file_if_not_exists("data/passwordaq.xml")
    
    def get_user_input(file_path, prompt_message):
        if os.path.getsize(file_path) > 0:
            with open(file_path, "r") as file_obj:
                return file_obj.readline().strip()
        else:
            user_input = input(prompt_message)
            with open(file_path, "w") as file_obj:
                file_obj.write(user_input)
            return user_input
    
    clear()
    uname = get_user_input("data/nameaq.xml", f"  {c}     「{r}•{c}」{r}  Enter your name » ")
    upass = get_user_input("data/passwordaq.xml", f" {c}     「{r}•{c}」{r}   Enter your password » ")

setup_user_data()

# ────────────────[User-Name]─────────────────

def get_user_name():
    with open("data/nameaq.xml", "r") as file_obj:
        return file_obj.readline().strip()

def get_user_password():
    with open("data/passwordaq.xml", "r") as file_obj:
        return file_obj.readline().strip()

# ────────────────[Greet -User]─────────────────

def greet_user():
    current_time = datetime.now()
    user_name = get_user_name()
    if current_time.hour < 12:
        print(f"    Good morning, {c}{user_name}!{wh}")
    elif current_time.hour < 18:
        print(f"    Good afternoon, {c}{user_name}!{r}")
    else:
        print(f"    Good evening, {c}{user_name}!{w}")

# ────────────────[IP]─────────────────

def ip(key):
    statee = unknown
    ip_response = requests.get(
        "http://ip-api.com/json/",
        headers={
            "Referer": "http://ip-api.com/",
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": (
                "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 "
                "Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
            )
        }
    ).json()

    print(f" {c}  「{w}State{c}」{w}:{c}{statee}")
    print(f" {c}  「{w}IP{c}」{w}:{c}{ip_response.get('query', ' ')}")
    print(f"{c}   「{w}country{c}」{w}:{c}{ip_response.get('country', ' ')}")
    print(f"{c}   「{w}ISP{c}」{w}:{c}{ip_response.get('isp', ' ')}")
    print(f"{c}   「{w}s-key{c}」{w}:{c}{key}")
    linex()
    

# ────────────────[Clr]─────────────────
    
def clr():
    os.system('clear')
    print(logo)  
    overview()
    greet_user()
    ip(key)

# ────────────────[Menu]─────────────────
def menu():
    #approval()
    clr()
    left_options = [
        ("1", f"{c}START{r}         "), 
        ("2", f"REACT"), 
        ("3", f"CREATE PAGE"), 
        ("0", f"{red}EXIT{r}          ")
    ]
    right_options = [
        ("4", f"FOLLOW"), 
        ("5", f"COMMENT"), 
        ("6", f"SHARE"), 
        ("7", f"{c}RESET{r}")
    ]
    for (left_option, left_desc), (right_option, right_desc) in zip(left_options, right_options):
        print(f"{c}   「{r}{left_option}{c}」{r} {left_desc:<14}     {c}  「{r}{right_option}{c}」{r} {right_desc}")
    linex()
    choice = input(f'   {c}「{r}Choose {c}」{r}»  ')
    menu_actions = {
        '1': Initialize,
        '2': QuickReact,
        '3': C_page,
        '4': lambda: print(f"{red} Before following get token first .{r}"),
        '5': comment_on_facebook_post,
        '6': AutomaticSharing,
        '7': lambda: reset(),
        '0': lambda: print(' 「✓」 DONE LOGOUT ') or exit()
    }
    menu_actions.get(choice, lambda: print(' 「!」Invalid option. '))()

# ────────────────[Manual]─────────────────

def Manual():
    user_choice = input(f" {wh} Input y or leave blank if its account.If its a page then input n Input(y/Y/yes/Yes or n/N/no/No or d/D/default/Default): {r}")
    #linex()
    user = input(f"{c}USER ID/EMAIL:{wh} ")
    #linex()
    passw = input(f"{c}PASSWORD:{wh} ")
    linex()
    cuser(user, passw, user_choice)

# ────────────────[Automatic file]─────────────────

def Auto():
    directory = '/sdcard'
    txt_files = [f for f in os.listdir(directory) if f.endswith('.txt')]
    
    if not txt_files:
        print(f'\033[1;31m「!」No .txt files found in {directory}')
        return
    
    for i, filename in enumerate(txt_files, start=1):
        print(f"    {c}「{r}{i}{c}」{wh}  {filename}")
    
    try:
        linex()
        choice = int(input('   Choose: '))
        if 1 <= choice <= len(txt_files):
            selected_file = os.path.join(directory, txt_files[choice - 1])
            if os.path.isfile(selected_file):
                try:
                    user_choice = input(f"{ye} Input y or leave blank if it's an account. If it's a page, input n (y/Y/yes/Yes or n/N/no/No or d/D/default/Default): {r}")
                    with open(selected_file, 'r') as file:
                        for line in file:
                            user_pass = line.strip().split('|')
                            process_users([user_pass], user_choice)
                except Exception as e:
                    print(f'\033[1;31m「!」Error reading the file: {e}')
            else:
                print(f'\033[1;31m「!」File not found ')
        else:
            print(f'{red}「!」Invalid option.{r}')
    except ValueError:
        print(f'{red}「!」Invalid input.{r}')


# ────────────────[Manually using file]─────────────────

def ManFile():
    file = input(' 「?」Put file path: ')
    if os.path.isfile(file):
        try:
            user_choice = input(f" {ye}Input y or leave blank if it's an account. If it's a page, input n (y/Y/yes/Yes or n/N/no/No or d/D/default/Default): {r}")
            with open(file, 'r') as file:
                for line in file:
                    user_pass = line.strip().split('|')
                    process_users([user_pass], user_choice)
        except Exception as e:
            print(f' \033[1;31m「!」Error reading the file: {e}')
    else:
        print(f' \033[1;31m「!」File location not found ')


def process_users(user_list, user_choice):
    for user_pass in user_list:
        if len(user_pass) == 2:
            user, passw = user_pass
            cuser(user, passw, user_choice)
           ### approvalf()
        else:
            print(f"Invalid format in line: {user_pass}")

# ────────────────[Tok+cookie extract]─────────────────

import requests
import uuid
import random

def cuser(user, passw, user_choice):
    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
    data = {
        'adid': f'{uuid.uuid4()}',
        'format': 'json',
        'device_id': f'{uuid.uuid4()}',
        'cpl': 'true',
        'family_device_id': f'{uuid.uuid4()}',
        'credentials_type': 'device_based_login_password',
        'error_detail_type': 'button_with_disabled',
        'source': 'device_based_login',
        'email': user,
        'password': passw,
        'access_token': accessToken,
        'generate_session_cookies': '1',
        'meta_inf_fbmeta': '',
        'advertiser_id': f'{uuid.uuid4()}',
        'currently_logged_in_userid': '0',
        'locale': 'en_US',
        'client_country_code': 'US',
        'method': 'auth.login',
        'fb_api_req_friendly_name': 'authenticate',
        'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
        'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
    }
    headers = {
        'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/en_US;FBBV/135374479;FBCR/SMART;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'graph.facebook.com',
        'X-FB-Net-HNI': str(random.randint(10000, 99999)),
        'X-FB-SIM-HNI': str(random.randint(10000, 99999)),
        'X-FB-Connection-Type': 'MOBILE.LTE',
        'X-Tigon-Is-Retry': 'False',
        'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
        'x-fb-device-group': str(random.randint(1000, 9999)),
        'X-FB-Friendly-Name': 'ViewerReactionsMutation',
        'X-FB-Request-Analytics-Tags': 'graphservice',
        'X-FB-HTTP-Engine': 'Liger',
        'X-FB-Client-IP': 'True',
        'X-FB-Connection-Bandwidth': str(random.randint(20000000, 30000000)),
        'X-FB-Server-Cluster': 'True',
        'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'
    }
    
    pos = requests.post("https://b-graph.facebook.com/auth/login", headers=headers, data=data, allow_redirects=False).json()
    
    if "session_key" in pos:
        print(f"   {c}「success」--> {user} extracted successfully.{wh}")
        
        cookie = ';'.join(i['name'] + '=' + i['value'] for i in pos['session_cookies'])
        c_user_value = [i['value'] for i in pos['session_cookies'] if i['name'] == 'c_user'][0]
        
        if user_choice.lower() in ['n', 'no']:
            with open('/sdcard/Aqua/tokpid.txt', 'a') as f:
                f.write(f'{c_user_value}\n')
            with open('/sdcard/Aqua/tokp.txt', 'a') as f:
                f.write(f'{pos["access_token"]}\n')
        else:
            with open('/sdcard/Aqua/toka.txt', 'a') as f:
                f.write(f'{pos["access_token"]}\n')
            with open('/sdcard/Aqua/tokaid.txt', 'a') as f:
                f.write(f'{c_user_value}\n')
        
        with open('/sdcard/Aqua/cok.txt', 'a') as f:
            f.write(f'{cookie}\n')
        
        with open('/sdcard/Aqua/cokid.txt', 'a') as f:
            f.write(f'{c_user_value}\n')
    else:
        print(f"   {red}「Failed」--> {user} isn't extracted. {w} ")



# ────────────────[1• Initizalize]─────────────────

def Initialize():
    print(f"  {red} Please choose how you want to Extract.\n")
    print(f"{c}     「{r}1{c}」{r} Manual through input")
    print(f"{c}     「{r}2{c}」{r} Manual through File")
    print(f"{c}     「{r}3{c}」{r} Automatic through option")
    
    me = input(f'   {c}「{r}Choose {c}」{r}»  ')
    if me == '1':
        Manual()
    if me == '2':
    	ManFile()
    elif me == '3':
        Auto()
    else:
        print(f' {red}「!」Invalid option. ')

# ────────────────[2• React]─────────────────

def Reaction(actor_id:str, post_id:str, react:str, token:str):
    rui    = requests.Session()
    var  = {"input":{"feedback_referrer":"native_newsfeed","tracking":[None],"feedback_id":str(base64.b64encode(('feedback:{}'.format(post_id)).encode('utf-8')).decode('utf-8')),"client_mutation_id":str(uuid.uuid4()),"nectar_module":"newsfeed_ufi","feedback_source":"native_newsfeed","attribution_id_v2":"NewsFeedFragment,native_newsfeed,cold_start,1710331848.276,264071715,4748854339,,","feedback_reaction_id":react,"actor_id":actor_id,"action_timestamp":str(time.time())[:10]}}
    data = {'access_token':token,'method':'post','pretty':False,'format':'json','server_timestamps':True,'locale':'id_ID','fb_api_req_friendly_name':'ViewerReactionsMutation','fb_api_caller_class':'graphservice','client_doc_id':'2857784093518205785115255697','variables':json.dumps(var),'fb_api_analytics_tags':["GraphServices"],'client_trace_id':str(uuid.uuid4())}
    pos  = rui.post('https://graph.facebook.com/graphql', data=data).json()
    try:
        if react in str(pos): print(f"{c}「Success」»  {w} Reacted with » {c}{actor_id} to {c}{post_id} ")
        else: print(f"{red}「Failed」»  {red} Reacted with » {red}{actor_id} to {red}{post_id} ")
    except Exception: print('')

def choose_reaction():
    print(f"{red}Please choose the reaction you want to use.\n")
    print(f"{c}     「{r}1{c}」{r} Like")
    print(f"{c}     「{r}2{c}」{r} Love")
    print(f"{c}     「{r}3{c}」{r} Haha")
    print(f"{c}     「{r}4{c}」{r} Wow")
    print(f"{c}     「{r}5{c}」{r} Care")
    print(f"{c}     「{r}6{c}」{r} Sad")
    print(f"{c}     「{r}7{c}」{r} Angry")

    rec = input(f'   {c}「{r}Choose {c}」{r}»  ')
    reactions = {
        '1': '1635855486666999',  # Like
        '2': '1678524932434102',  # Love
        '3': '115940658764963',   # Haha
        '4': '478547315650144',   # Wow
        '5': '613557422527858',   # Care
        '6': '908563459236466',   # Sad
        '7': '444813342392137'    # Angry
    }
    return reactions.get(rec, None)

def QuickReact():
    def get_ids_tokens(file_path):
        with open(file_path, 'r') as file:
            return [line.strip() for line in file]

    actor_ids = get_ids_tokens('/sdcard/Aqua/tokaid.txt')
    tokens = get_ids_tokens('/sdcard/Aqua/toka.txt')
    post_link = input('Enter the Facebook post link: ')
    post_id = linktradio(post_link)

    react = choose_reaction()
    if react:
        for actor_id, token in zip(actor_ids, tokens):
            Reaction(actor_id=actor_id, post_id=post_id, react=react, token=token)
    else:
        print(' 「!」Invalid option. ')


# ────────────────[3•Create-pages]─────────────────

class reg_pro5():
    def __init__(self, cookies, name) -> None:
        self.cookies = cookies
        self.name = name  # Store the name in an instance variable
        self.id_acc = self.cookies.split('c_user=')[1].split(';')[0]
        headers = {
            'authority': 'www.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'vi',
            'cookie': self.cookies,
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '""',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'viewport-width': '980',
        }
        url_profile = requests.get('https://www.facebook.com/me', headers=headers).url
        profile = requests.get(url_profile, headers=headers).text
        try:
            self.fb_dtsg = profile.split('{"name":"fb_dtsg","value":"')[1].split('"},')[0]
        except:
            self.fb_dtsg = profile.split(',"f":"')[1].split('","l":null}')[0]

    def Reg(self):
        headers = {
            'authority': 'www.facebook.com',
            'accept': '*/*',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            # Requests sorts cookies= alphabetically
            'cookie': self.cookies,
            'origin': 'https://www.facebook.com',
            'referer': 'https://www.facebook.com/pages/creation?ref_type=launch_point',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '""',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'viewport-width': '980',
            'x-fb-friendly-name': 'AdditionalProfilePlusCreationMutation',
            'x-fb-lsd': 'ZM7FAk6cuRcUp3imwqvHTY',
        }

        data = {
            'av': self.id_acc,
            '__user': self.id_acc,
            '__a': '1',
            '__dyn': '7AzHxq1mxu1syUbFuC0BVU98nwgU29zEdEc8co5S3O2S7o11Ue8hw6vwb-q7oc81xoswIwuo886C11xmfz81sbzoaEnxO0Bo7O2l2Utwwwi831wiEjwZwlo5qfK6E7e58jwGzE8FU5e7oqBwJK2W5olwuEjUlDw-wUws9ovUaU3qxWm2Sq2-azo2NwkQ0z8c84K2e3u362-2B0oobo',
            '__csr': 'gP4ZAN2d-hbbRmLObkZO8LvRcXWVvth9d9GGXKSiLCqqr9qEzGTozAXiCgyBhbHrRG8VkQm8GFAfy94bJ7xeufz8jK8yGVVEgx-7oiwxypqCwgF88rzKV8y2O4ocUak4UpDxu3x1K4opAUrwGx63J0Lw-wa90eG18wkE7y14w4hw6Bw2-o069W00CSE0PW06aU02Z3wjU6i0btw3TE1wE5u',
            '__req': 't',
            '__hs': '19296.HYP:comet_pkg.2.1.0.2.1',
            'dpr': '1',
            '__ccg': 'EXCELLENT',
            '__rev': '1006496476',
            '__s': '1gapab:y4xv3f:2hb4os',
            '__hsi': '7160573037096492689',
            '__comet_req': '15',
            'fb_dtsg': self.fb_dtsg,
            'jazoest': '25404',
            'lsd': 'ZM7FAk6cuRcUp3imwqvHTY',
            '__aaid': '800444344545377',
            '__spin_r': '1006496476',
            '__spin_b': 'trunk',
            '__spin_t': '1667200829',
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'AdditionalProfilePlusCreationMutation',
            'variables': '{"input":{"bio":"","categories":["181475575221097"],"creation_source":"comet","name":"'+self.name+'","page_referrer":"launch_point","actor_id":"'+self.id_acc+'","client_mutation_id":"1"}}',
            'server_timestamps': 'true',
            'doc_id': '5903223909690825',
        }

        response = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data).json()
        try:
            return response['data']['additional_profile_plus_create']['additional_profile']['id']
        except:
            return (f'「Failed  」to create page.')


# ────────────────[5•Comment]─────────────────
def get_ids_tokens(file_path):
        with open(file_path, 'r') as file:
            return [line.strip() for line in file]

def comment_on_facebook_post():
    user_ids = get_ids_tokens('/sdcard/Aqua/tokaid.txt')
    access_tokens = get_ids_tokens('/sdcard/Aqua/toka.txt')
    current_time = datetime.now()
    user_name = get_user_name()
    post_link = input('Enter the Facebook post link: ')
    post_id = linktradio(post_link)
    comment_text = input('Enter the comment text (or leave blank for auto comment): ')
    num_comments = int(input('Enter the number of comments to make: '))

    if not comment_text:
        current_time = datetime.now().strftime("%I:%M %p")
        current_date = datetime.now().strftime("%Y-%m-%d")
        comment_text = f'Time:「{current_time}」「{current_date}」\n-「Auto comment by {user_name}」'

    def has_commented(post_id, access_token, user_id):
        try:
            url = f'https://graph.facebook.com/v18.0/{user_id}_{post_id}/comments'
            params = {'access_token': access_token}
            response = requests.get(url, params=params)
            response.raise_for_status()
            comments = response.json().get('data', [])
            
            for comment in comments:
                if comment.get('from', {}).get('id') == user_id:
                    return True
        except requests.exceptions.RequestException as error:
            print(f" {red}「Failed  」to comment on {post_id}")
        return False

    comments_count = 0
    user_count = len(user_ids)

    for _ in range(num_comments):
        for i in range(user_count):
            user_id = user_ids[i]
            access_token = access_tokens[i]

            try:
                if not has_commented(post_id, access_token, user_id):
                    url = f'https://graph.facebook.com/v19.0/{user_id}_{post_id}/comments'
                    params = {'access_token': access_token, 'message': comment_text}
                    response = requests.post(url, params=params)
                    
                    if response.status_code == 200:
                        comments_count += 1
                        print(f"{c}「success 」{w} commented on {c} {post_id}")
                        if comments_count >= num_comments:
                            print(f"{c}「successfully  」{w} commented {c} {num_comments} {w}times.")
                            return
                    else:
                        print(f"{red}「Failed  」to comment on {post_id}")
            except requests.exceptions.RequestException as error:
                print(f"{red}「Failed  」to comment on {post_id}")


def C_page():
    print("miewwwww")

# ────────────────[6•Share]─────────────────

def AutomaticSharing():
    access_token = input('Enter the access token: ') # ACCESS TOKEN HERE
    share_url = input('Enter the Facebook post link: ')
    share_count = 22200
    time_interval = 1.5
    delete_after = 60 * 60

    shared_count = 0
    timer = None

    headers = {
        'authority': 'graph.facebook.com',
        'cache-control': 'max-age=0',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
    }

    def share_post():
        nonlocal shared_count, timer

        try:
            response = requests.post(
                f'https://graph.facebook.com/me/feed?access_token={access_token}&fields=id&limit=1&published=0',
                json={
                    'link': share_url,
                    'privacy': {'value': 'SELF'},
                    'no_story': True,
                },
                headers=headers
            )

            shared_count += 1
            post_id = response.json().get('id')
            print(f' {c}「Success」»  {c}「{wh}{shared_count}{c}」» {wh} ID:{c}{post_id or "Unknown"}{wh}')

            if shared_count == share_count:
                timer.cancel()
                print('Finished sharing posts.')

                if post_id:
                    threading.Timer(delete_after, delete_post, args=(post_id,)).start()

        except requests.exceptions.RequestException as error:
            print('Failed to share post:', error.response.json() if error.response else str(error))

    def delete_post(post_id):
        try:
            requests.delete(f'https://graph.facebook.com/{post_id}?access_token={access_token}')
            print(f'Post deleted: {post_id}')
        except requests.exceptions.RequestException as error:
            print('Failed to delete post:', error.response.json() if error.response else str(error))

    def start_sharing():
        nonlocal timer
        timer = threading.Timer(time_interval, share_post)
        timer.start()

    for _ in range(share_count):
        start_sharing()
        time.sleep(time_interval)

    
    time.sleep(share_count * time_interval)
    if timer:
        timer.cancel()
        print('Loop stopped.')

# ────────────────[7• Reset]─────────────────

def reset():
    folder_name = "Aqua"
    file_names = ["toka.txt", "tokaid.txt", "tokp.txt", "tokpid.txt", "cok.txt", "cokid.txt"]
    
    if os.path.exists(folder_name):
        for root, dirs, files in os.walk(folder_name, topdown=False):
            for name in files:
                file_path = os.path.join(root, name)
                os.remove(file_path)
            for name in dirs:
                dir_path = os.path.join(root, name)
                os.rmdir(dir_path)
        os.rmdir(folder_name)
        print(f"{c}Successfully Reset.{r}")
    else:
        print(f"{red}Failed to reset.")




menu()
