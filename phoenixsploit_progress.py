#!/usr/bin/env python3

# Version 0.0.6 already? finished for today

import os
import time
import shutil
import random
import argparse
from sys import platform

def phoenixparse():
    parser = argparse.ArgumentParser(usage="phoenixsploit [--sudo / --update / --remove / --version]")
    parser.add_argument("--sudo", help="uh instantly starting tool with admin rigths!", action="store_true")
    parser.add_argument("--update", help="uh installs or updates phoenixsploit (if everything is running well lmao)", action="store_true")
    parser.add_argument("--remove", help="uh it uninstalls phoenixsploit (I hope it works OmO)", action="store_true")
    parser.add_argument("--ilovecats", help="find it out lmao", action="store_true")
    parser.add_argument("--version", help="checks current version", action="store_true")
    return parser.parse_args()

def first_time():
    global root
    root = "/usr/share/phoenixthrush/"

    global phoenixsploit_root
    phoenixsploit_root = root + "phoenixsploit/"
    
    global bin_phoenixsploit_root
    bin_phoenixsploit_root = "/usr/bin/phoenixsploit"

    global config_root
    config_root = root + "config/phoenixsploit/"

    global phoenixmc_root
    phoenixmc_root = root + "phoenixMC/"

    global bin_phoenixmc_root
    bin_phoenixmc_root = "/usr/bin/phoenixMC"

    global blackeye_root
    blackeye_root = root + "blackeye/"

    global bin_blackeye_root
    bin_blackeye_root = "/usr/bin/blackeye"

    global alis_root
    alis_root = root + "alis/"

    global bin_alis_root
    bin_alis_root = "/usr/bin/alis"

    if os.path.exists(root):
        pass
    else:
        os.system("sudo mkdir -p " + root)
        os.system("sudo chmod -R 777 " + root)

    if os.path.exists(phoenixsploit_root):
        pass
    else:
        os.system("sudo mkdir -p " + phoenixsploit_root)
        os.system("sudo chmod -R 777 " + phoenixsploit_root)

    if os.path.exists(config_root):
        pass
    else:
        os.system("sudo mkdir -p " + config_root)
        os.system("sudo chmod -R 777 " + config_root)

    global run_method

    if os.path.exists(bin_phoenixsploit_root):
        if not os.path.exists(phoenixsploit_root + "sourced"):
            run_method = "repo"
        else:
            run_method = "source"
    elif os.path.exists(phoenixsploit_root + "sourced"):
        run_method = "source"
    else:
        run_method = "directly"

def install_or_update():
    clear()
    check_sudo(True, True)
    print()
    print("\033[31mChecking dependency\033[00m")
    check_package("wget")
    check_package("curl")
    check_package("nano")
    clear()
    if run_method == "repo":
        print("\033[31mRunning apt script!\033[0m\n")
        os.system("sudo apt update >/dev/null 2>&1")
        os.system("sudo apt install phoenixsploit -y >/dev/null 2>&1")
        os.system("sudo apt install --only-upgrade phoenixsploit >/dev/null 2>&1")
    elif run_method == "source":
        print("\033[31mRunning source install script!\033[0m\n")
        os.system("sudo apt install phoenixsploit -y >/dev/null 2>&1")
        print("\033[96mUpdated! \033[00m\033[31m^^\033[00m\n")
    else:
        print("\033[31mInstalling phoenixsploit over apt!\033[0m\n")
        os.system("curl -sSL phoenixthrush.com/phoenixsploit-install.sh | bash")
        print("\033[96mUpdated! \033[00m\033[31m^^\033[00m\n")

def uninstall_phoenixsploit():
    clear()
    input("debug here")
    check_sudo(True, True)
    input("debug checked sudo")

    if run_method == "repo":
        print("\033[31mRemoving phoenixsploit over apt script!\033[0m\n")
        os.system("sudo apt remove phoenixsploit -y  >/dev/null 2>&1")
    elif run_method == "source":
        print("\033[31mRemoving phoenixsploit over source remove script!\033[0m\n")
        os.system("sudo rm -rf " + phoenixsploit_root)
        print("\033[96mRemoved! \033[00m\033[31m^^\033[00m\n")
    else:
        print("\033[96mbug? wtf\n")
        exit()

    clear()
    print("\033[31mSuccessfully uninstalled it! \033[00m\033[96m^^\033[00m")
    print()
    print("\033[96mWe had a good time, see ya!\033[31m")
    print("\033[96mAnd have a nice Day!\033[31m \033[31m<3\033[00m")
    exit()
        
def clear():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

def user_exit():
    clear()
    print("\033[96mThanks for using!")
    print("Have a nice Day!\033[00m \033[31m<3\033[31m")
    print(r"""
               ___
              (___)
       ____
     _\___ \  |\_/|
    \     \ \/ , , \ ___
     \__   \ \ ="= //|||\
      |===  \/____)_)||||
      \______|    | |||||
          _/_|  | | =====
         (_/  \_)_)
      _________________
     (                _)
      (__   '          )
        (___    _____)
            '--'
        """)
    print("\033[00m")
    time.sleep(2)
    exit()

def random_cat():
    cat = random.randint(1, 10)
    if cat == 1:
        asian_cat_1()
        exit()
    elif cat == 2:
        asian_cat_2()
        exit()
    elif cat == 3:
        asian_cat_3()
        exit()
    elif cat == 4:
        asian_cat_4()
        exit()
    elif cat == 5:
        asian_cat_5()
        exit()
    elif cat == 6:
        asian_cat_6()
        exit()
    elif cat == 7:
        asian_cat_7()
        exit()
    elif cat == 8:
        asian_cat_8()
        exit()
    elif cat == 9:
        asian_cat_9()
        exit()
    elif cat == 10:
        asian_cat_10()
        exit()
    else:
        print()
        print("\033[31mError bruh how tf did you reach to this error lmao, sorry buddy!\033[00m")
    exit()


def asian_cat_1():
    clear()
    print("\033[31mYou found my easteregg and yeah you could see it because it´s open-source lmao\033[95m")
    print(r"""
        _..---...,""-._     ,/}/)
     .''        ,      ``..'(/-<
    /   _      {      )         \
   ;   _ `.     `.   <         a(
 ,'   ( \  )      `.  \ __.._ .: y
(  <\_-) )'-.____...\  `._   //-'
 `. `-' /-._)))      `-._)))
   `...'            my asian cat <3
    """)
    print("\033[00m")


def asian_cat_2():
    clear()
    print("\033[31mYou found my easteregg and yeah you could see it because it´s open-source lmao\033[95m")
    print(r"""
   |\---/|
   | ,_, |
    \_`_/-..----.
 ___/ `   ' ,""+ \
(__...'   __\    |`.___.';
  (_,...'(_,.`__)/'.....+
    """)
    print("\033[00m")


def asian_cat_3():
    clear()
    print("\033[31mYou found my easteregg and yeah you could see it because it´s open-source lmao\033[95m")
    print(r"""
 ,_     _
 |\\_,-~/
 / _  _ |    ,--.
(  @  @ )   / ,-'
 \  _T_/-._( (
 /         `. \
|         _  \ |
 \ \ ,  /      |
  || |-_\__   /
 ((_/`(____,-'
     """)
    print("\033[00m")


def asian_cat_4():
    clear()
    print("\033[31mYou found my easteregg and yeah you could see it because it´s open-source lmao\033[95m")
    print(r"""
  ,-.       _,---._ __  / \
 /  )    .-'       `./ /   \
(  (   ,'            `/    /|
 \  `-"             \'\   / |
  `.              ,  \ \ /  |
   /`.          ,'-`----Y   |
  (            ;        |   '
  |  ,-.    ,-'         |  /
  |  | (   |            | /
  )  |  \  `.___________|/
  `--'   `--'
     """)
    print("\033[00m")


def asian_cat_5():
    clear()
    print("\033[31mYou found my easteregg and yeah you could see it because it´s open-source lmao\033[95m")
    print(r"""
       _                        
       \`*-.                    
        )  _`-.                 
       .  : `. .                
       : _   '  \               
       ; *` _.   `*-._          
       `-.-'          `-.       
         ;       `       `.     
         :.       .        \    
         . \  .   :   .-'   .   
         '  `+.;  ;  '      :   
         :  '  |    ;       ;-. 
         ; '   : :`-:     _.`* ;
*bug* .*' /  .*' ; .*`- +'  `*' 
      `*-*   `*-*  `*-*'
     """)
    print("\033[00m")


def asian_cat_6():
    clear()
    print("\033[31mYou found my easteregg and yeah you could see it because it´s open-source lmao\033[95m")
    print(r"""
           ___
          (___)
   ____
 _\___ \  |\_/|
\     \ \/ , , \ ___
 \__   \ \ ="= //|||\
  |===  \/____)_)||||
  \______|    | |||||
      _/_|  | | =====
     (_/  \_)_)
  _________________
 (                _)
  (__   '          )
    (___    _____)
        '--'
    """)
    print("\033[00m")


def asian_cat_7():
    clear()
    print("\033[31mYou found my easteregg and yeah you could see it because it´s open-source lmao\033[95m")
    print(r"""
        _,'|             _.-''``-...___..--';)
       /_ \'.      __..-' ,      ,--...--'''
      <\    .`--'''       `     /'
       `-';'               ;   ; ;
 __...--''     ___...--_..'  .;.'
(,__....----'''       (,..--''   *asian meow*
    """)
    print("\033[00m")


def asian_cat_8():
    clear()
    print("\033[31mYou found my easteregg and yeah you could see it because it´s open-source lmao\033[95m")
    print(r"""
(:`--..___...-''``-._             |`._
  ```--...--.      . `-..__      .`/ _\  
            `\     '       ```--`.    />
            : :   :               `:`-'
             `.:.  `.._--...___     ``--...__      
                ``--..,)       ```----....__,) *bug*
    """)
    print("\033[00m")


def asian_cat_9():
    clear()
    print("\033[31mYou found my easteregg and yeah you could see it because it´s open-source lmao\033[95m")
    print(r"""
              __..--''``---....___   _..._    __
    /// //_.-'    .-/";  `        ``<._  ``.''_ `. / // /
   ///_.-' _..--.'_    \                    `( ) ) // //
   / (_..-' // (< _     ;_..__               ; `' / ///
    / // // //  `-._,_)' // / ``--...____..-' /// / //
        """)
    print("\033[00m")


def asian_cat_10():
    clear()
    print("\033[31mYou found my easteregg and yeah you could see it because it´s open-source lmao\033[95m")
    print(r"""
       ,
       \`-._           __
        \\  `-..____,.'  `.
         :`.         /    \`.
         :  )       :      : \
          ;'        '   ;  |  :
          )..      .. .:.`.;  :
         /::...  .:::...   ` ;
         ; _ '    __        /:\
         `:o>   /\o_>      ;:. `.
        `-`.__ ;   __..--- /:.   \
        === \_/   ;=====_.':.     ;
         ,/'`--'...`--....        ;
              ;                    ;
            .'                      ;
          .'                        ;
        .'     ..     ,      .       ;
       :       ::..  /      ;::.     |
      /      `.;::.  |       ;:..    ;
     :         |:.   :       ;:.    ;
     :         ::     ;:..   |.    ;
      :       :;      :::....|     |
      /\     ,/ \      ;:::::;     ;
    .:. \:..|    :     ; '.--|     ;
   ::.  :''  `-.,,;     ;'   ;     ;
.-'. _.'\      / `;      \,__:      \
`---'    `----'   ;      /    \,.,,,/
                   `----`              *big catto, big meow*
        """)
    print("\033[00m")

def check_sudo(verbose=False, req_perm=False, admin=True):
    if admin is True:
        sudo = os.getuid()
        if sudo == 0:
            if verbose is True:
                print("\033[96mRunning as \033[31mroot\033[96m!\033[00m")
            else:
                return sudo
        else:
            if verbose is True:
                if req_perm is True:
                    print("\033[31mRequesting admin rights!\033[00m")
                    rerun_sudo()
                    exit()
                else:
                    print("\033[31mRunning with \033[96mnormal \033[31muser rights!\033[00m")
            else:
                if req_perm is True:
                    time.sleep(2)
                    rerun_sudo()
                    exit()
                else:
                    return sudo
    else:
        sudo = os.getuid()
        if sudo != 0:
            if verbose is True:
                print("\033[31mRunning with \033[96mnormal \033[31muser rights!\033[00m")
            else:
                return sudo
        else:
            if verbose is True:
                if req_perm is True:
                    print("\033[31mRequesting normal user rights!\033[00m")
                    time.sleep(2)
                    rerun_sudo(False)
                    exit()
                else:
                    print("\033[31mRunning with \033[96mnormal \033[31muser rights!\033[00m")
            else:
                if req_perm is True:
                    time.sleep(2)
                    rerun_sudo(False)
                    exit()
                else:
                    return sudo

def check_os_platform(verbose=True):
    system = platform

    if system == "darwin":
        if verbose is True:
            print("\033[31mMacOS detected!\033[00m")
            exit()
        else:
            return system
    elif system == "win32":
        if verbose is True:
            print("\033[31mWindows detected!\033[00m")
            exit()
        else:
            return system
    else:
        os.system("grep -m 1 \"^ID=\" /etc/os-release > " + config_root + "os.txt")
        os.system("sudo chmod 777 " + config_root + "os.txt")
        with open(config_root + "os.txt", "r") as f:
            content = f.read()

        if verbose is True:
            if content == "ID=arch\n":
                print("\033[31mArch based Distro detected!\033[00m")
            elif content == "ID=blackarch\n":
                print("\033[31mArch based Distro detected!\033[00m")
            elif content == "ID=debian\n":
                print("\033[31mDebian based Distro detected!\033[00m")
            elif content == "ID=ubuntu\n":
                print("\033[31mDebian based Distro detected!\033[00m")
            elif content == "ID=kali\n":
                print("\033[31mDebian based Distro detected!\033[00m")
            else:
                print("\033[31mCould not detect your distro!\033[00m")
                print("\033[31mExiting!\033[00m")
                user_exit()
        else:
            if content == "ID=arch\n":
                return "arch"
            elif content == "ID=blackarch\n":
                return "arch"
            elif content == "ID=debian\n":
                return "debian"
            elif content == "ID=ubuntu\n":
                return "debian"
            elif content == "ID=kali\n":
                return "debian"
            else:
                print("\033[31mCould not detect your distro!\033[00m")
                print("\033[31mExiting!\033[00m")
                user_exit()

def check_os_compatibility(verbose=True):
    system = platform

    if system == "darwin":
        if verbose is True:
            print("\033[31mThis Script doesn´t support MacOS!\033[00m")
            print("\033[31mPress Enter to exit!\033[00m")
            input()
            exit()
        else:
            return system
    elif system == "win32":
        if verbose is True:
            print("\033[31mThis Script doesn´t support Windows nativly!\033[00m")
            print("\033[96mYou can run it through wsl!\033[00m")           
            choice = input("\033[96mEnter \"x\" to visit my instruction page for wsl or only enter to exit!\033[00m ")
            if choice == "x":
            	os.system("start \"\" \"https://github.com/Phoenixthrush#windows\"")
            exit()
        else:
            return system

    if check_os_platform == "arch":
        print("\033[31mThis Script doesn´t support arch based distros anymore!\033[00m")
        print("\033[31mPress Enter to exit!\033[00m")
        input()
        exit()

def check_package(package):
    package_dir = "/usr/bin/" + package
    if os.path.exists(package_dir):
        return True
    else:
        print("\033[96mInstalling the package \033[31m" + package + "\033[96m!\033[00m")
        print()
        os.system("sudo apt update")
        command = "sudo apt install " + package + " -y >/dev/null 2>&1"
        print()
        os.system(command)
        return True

def rerun_sudo(sudo=True, argparse1=None):
    if sudo is True:
        if not argparse1 is None:
            current = (os.path.abspath(__file__))
            current = "sudo python3 " + current + " " + argparse1
            os.system("sudo touch " + phoenixsploit_root + "rerunned")
            os.system(current)
            exit()
        else:
            current = (os.path.abspath(__file__))
            current = "sudo python3 " + current
            os.system("sudo touch " + phoenixsploit_root + "rerunned")
            os.system(current)
            exit()
    else:
        clear()
        print("\033[31mPlease run that script without admin rights!")
        exit()

def update_linux():
    clear()

    print("\033[31mUpdating your Linux!\033[00m")
    print()
    os.system("sudo apt update >/dev/null 2>&1")
    os.system("sudo apt full-upgrade -y >/dev/null 2>&1")
    os.system("sudo apt autoremove -y >/dev/null 2>&1")
    print()
    print("\033[31mUpdated your Linux!\033[00m")

    return True

def crr_ver(verbose=True):
    clear()
    if os.path.exists(bin_phoenixsploit_root):
        if not os.path.exists(phoenixsploit_root + "sourced"):
            if verbose is True:
                print("\033[96mYou currently have phoenixsploit v.0.0.6 (repo) installed!\033[00m")
                print()
            return "repo"
        else:
            if verbose is True:
                print("\033[96mYou currently have phoenixsploit v.0.0.6 (source out of repo) installed!\033[00m")
                print()	
            return "source"
    elif os.path.exists(phoenixsploit_root + "sourced"):
        if verbose is True:
            print("\033[96mYou currently have phoenixsploit v.0.0.6 (source out of repo) installed!\033[00m")
            print()
        return "source"
    else:
        print("\033[96mYou are running phoenixsploit v.0.0.6 directly!\033[00m")
        print("\n\033[31mThere are two options to install phoenixsploit \033[00m(with my repo \033[96m[recommended]\033[00m, or from source)\033[00m \n\n - \"\033[96mcurl -sSL phoenixthrush.com/phoenixsploit-install.sh | bash\033[00m\" \033[31mto install it through my repo\033[00m \n - \"\033[96mcurl -sSL https://raw.githubusercontent.com/phoenixthrush/phoenixsploit/main/install.sh | bash\033[00m\" \033[31m to install it without my repo")
        print()	
        exit()

def menue():
    clear()
    print("\033[95mWelcome to Phoenixsploit v.0.0.6\033[00m")
    check_sudo(True, False)
    print("\033[95m  ___                   ___   ")
    print(" (o o)                 (o o)  ")
    print("(  V  ) \033[96mPhoenixthrush\033[95m (  V  )")
    print("--m-m-------------------m-m--\033[00m")
    print()
    print("\033[31mThis tool has full support for debian based distros!")
    print("Have fun <3\033[0;0m")
    print()
    print("\033[92m1 - watch hentai")
    print("2 - destroy ur pc")
    print("3 - real hacking shit")
    print("4 - Install and Update\033[00m \033[31m<3\033[00m")
    print("\033[92m5 - Remove phoenixsploit")
    print("6 - Run as\033[00m \033[31msudo\033[00m")
    print()
    print("\033[96m0 - exit\033[00m")

    try:
        choice = int(input("\033[34mPlease choose a option! \033[00m"))
    except ValueError:
        clear()
        menue()

    if choice == 1:
        watch_hentai()
        exit()
    elif choice == 2:
        destroy_pc()
        exit()
    elif choice == 3:
        second_menue()
        exit()
    elif choice == 4:
        current = (os.path.abspath(__file__))
        current = "sudo python3 " + current + " --update"        
        os.system(current)
        exit()
    elif choice == 5:
        current = (os.path.abspath(__file__))
        current = "sudo python3 " + current + " --remove"        
        os.system(current)
        exit()
    elif choice == 6:
        rerun_sudo()
        exit()
    elif choice == 666:
        random_cat()
        exit()
    elif choice == 0:
        user_exit()
        exit()
    else:
        menue()
        exit()

def watch_hentai():
    check_package("firefox")
    check_sudo(True, True, False)

    clear()
    print("\033[96mOkay buddy let me help you!\033[00m")
    os.system("firefox -new -tab https://hentaihaven.com")
    os.system("firefox -new -tab https://nhentai.net/")
    os.system("firefox -new -tab https://hanime.tv/")
    exit()

def destroy_pc():
    clear()
    print("\033[96mdon't do it bud!\033[0m")
    exit()

def second_menue():
    clear()
    print("\033[95mHack Menue\033[00m")
    check_sudo(True)
    print()
    print("\033[96m1 - Create a Minecraft-Server\033[00m")
    print("\033[96m2 - Create a hidden hotspot      \033[31m[Coming soon!]\033[00m")
    print("\033[96m3 - Website Phishing (blackeye)\033[00m")
    print("\033[96m4 - Update Linux\033[00m")
    print("\033[96m5 - Install Arch Linux\033[00m \033[31m<3\033[00m")
    print("\033[96m6 - Change MAC Address           \033[00m\033[31m[Coming soon!]\033[00m")
    print()
    print("\033[34m0 - Back to menue!\033[00m")
    print()

    try:
        choice = int(input("\033[92mPlease choose a option! \033[00m"))
    except ValueError:
        clear()
        second_menue()

    if choice == 1:
        minecraft()
        exit()
    elif choice == 2:
        clear()
        print("\033[96mcoming soon, sorry buddy!\033[00m\n")
        exit()
    elif choice == 3:
        website_phishing()
        exit()
    elif choice == 4:
        update_linux()
        exit()
    elif choice == 5:
        arch_install()
        exit()
    elif choice == 6:
        clear()
        print("\033[96mcoming soon, sorry buddy!\033[00m\n")
        exit()
    elif choice == 666:
        random_cat()
        exit()
    elif choice == 0:
        menue()
        exit()
    else:
        second_menue()
        exit()

def minecraft():
    clear()
    print("\033[31mStarting Minecraft Server installation!\033[00m")
    choice = input("\033[96mDo you want Install a normal or a Forge Server (Forge supports Mods) [normal|forge] ? \033[00m")
    if choice == "normal":
        minecraft_server_setup()
        exit()
    elif choice == "forge":
        forge_minecraft_server_setup()
        exit()
    else:
        minecraft()
        exit()

def minecraft_server_setup():
    clear()
    check_sudo(False, True)
    os.system("sudo apt update >/dev/null 2>&1")
    os.system("sudo apt install default-jre -y >/dev/null 2>&1")
    if os.path.exists(phoenixmc_root):
        choice = input("\033[96mDo you want to overwrite or remove the old Server files? [overwrite|uninstall] \033[00m")
        if choice == "overwrite":
            os.system("sudo rm -rf " + phoenixmc_root)
            os.system("sudo rm " + bin_phoenixmc_root)
            minecraft_server_setup_1()
            exit()
        elif choice == "uninstall":
            os.system("sudo rm -rf " + phoenixmc_root)
            os.system("sudo rm " + bin_phoenixmc_root)
            clear()
            print("\033[31mRemoved Server!\033[00m")
            print()
            exit()
        else:
            minecraft_server_setup()
            exit()
    else:
        minecraft_server_setup_1()
        exit()

def minecraft_server_setup_1():
    minecraft_server_setup_2()
    exit()

def minecraft_server_setup_2():
    clear()
    print("\033[96mDownloading Minecraft Server Vanilla jar\033[00m")
    print("\033[96mVersion 1.17.1\033[00m")
    print()

    os.system("sudo mkdir -p " + phoenixmc_root)
    os.system("sudo chmod -R 777 " + phoenixmc_root)
    os.system("wget https://launcher.mojang.com/v1/objects/a16d67e5807f57fc4e550299cf20226194497dc2/server.jar")
    os.system("wget https://phoenixthrush.com/assets/code/server.properties")
    print("\033[96mDownloaded the minecraft jar file!\033[00m")

    current_dir = os.getcwd()
    current_jar = current_dir + "/server.jar"
    target_jar = phoenixmc_root + "server.jar"
    shutil.move(current_jar, target_jar)

    current_prop = current_dir + "/server.properties"
    target_prop = phoenixmc_root + "server.properties"
    shutil.move(current_prop, target_prop)

    os.system("sudo chmod 777 " + phoenixmc_root + "server.jar")
    os.system("sudo chmod 777 " + phoenixmc_root + "server.properties")

    print("\033[96mMoved jar to " + phoenixmc_root + " \033[00m")
    minecraft_server_setup_3()
    exit()

def minecraft_server_setup_3():
    print()
    try:
        ram = int(input("\033[31mHow much GB ram do you want for your minecraft server? [1,2,3...,16] \033[00m"))
    except ValueError:
        print("\033[31mError wrong input!\033[00m")
        minecraft_server_setup_3()
        exit()

    if ram < 17 and not ram == 0:
        print("\033[31mSetting ram to " + str(ram) + "GB\033[00m")
    else:
        print("\033[31mError wrong input!\033[00m")
        minecraft_server_setup_3()
        exit()

    phoenix_mc_start_command = "cd " + phoenixmc_root + " && sudo java -Xmx" + str(ram) + "G -Xms" + str(ram) + "G -jar ./server.jar nogui"
    print()
    print("\033[96mUsing \"" + phoenix_mc_start_command + "\" as start trigger!\033[00m")

    java_start = str(phoenix_mc_start_command)
    java_start = "clear && " + java_start

    x = open("/usr/bin/phoenixMC", "x")
    x.write(java_start)
    x.close()
    os.system("sudo chmod +x /bin/phoenixMC")
    os.system("sudo chmod 777 /bin/phoenixMC")
    minecraft_server_setup_4()

def minecraft_server_setup_4():
    print()
    choice = input("\033[96mDo you want to manually edit settings? (recommended) [y|n] \033[00m")
    if choice == "y":
        minecraft_server_config_manually()
        exit()
    elif choice == "n":
        minecraft_server_config()
        exit()
    else:
        minecraft_server_setup_4()
        exit()

def minecraft_server_config():
    os.system("phoenixMC")
    minecraft_eula()
    print()
    print("\033[96mThe Error above is normal!\033[00m")
    print("\033[31mYou can start the Server with phoenixMC\033[00m")
    print()
    exit()

def minecraft_server_config_manually():
    print()
    os.system("nano " + phoenixmc_root + "server.properties")
    os.system("phoenixMC")
    minecraft_eula()
    print("\033[96mThe Error above is normal!\033[00m")
    print("\033[31mYou can start the Server with phoenixMC\033[00m")
    print()
    exit()

def minecraft_eula():
    eula = open(phoenixmc_root + "eula.txt", "w")
    eula.write("eula=true")
    eula.close()

def forge_minecraft_server_setup():
    clear()
    check_sudo(False, True)
    check_package("nano")
    os.system("sudo apt install default-jdk -y")
    os.system("sudo apt install default-jre -y")

    if os.path.exists(phoenixmc_root):
        choice = input(
            "\033[96mDo you want to overwrite or remove the old Server files? [overwrite|uninstall] \033[00m")
        if choice == "overwrite":
            os.system("sudo rm -rf " + phoenixmc_root)
            os.system("sudo rm /usr/bin/phoenixMC")
            forge_minecraft_server_setup_1()
            exit()
        elif choice == "uninstall":
            os.system("sudo rm -rf " + phoenixmc_root)
            os.system("sudo rm /usr/bin/phoenixMC")
            print("\033[31mRemoved Server!\033[00m")
            print()
            exit()
        else:
            forge_minecraft_server_setup()
            exit()
    else:
        forge_minecraft_server_setup_1()
        exit()

def forge_minecraft_server_setup_1():
    time.sleep(3)
    clear()
    print("\033[96mDownloading Minecraft Server Vanilla jar\033[00m")
    print("\033[96mVersion 1.17.1\033[00m")
    print()

    os.system("sudo mkdir -p " + phoenixmc_root)
    os.system("sudo chmod -R 777 " + phoenixmc_root)
    os.system("wget https://phoenixthrush.com/assets/code/forge-installer.jar")
    os.system("wget https://phoenixthrush.com/assets/code/server.properties")
    print("\033[96mDownloaded the minecraft jar file!\033[00m")

    current_dir = os.getcwd()
    current_jar = current_dir + "/forge-installer.jar"
    target_jar = phoenixmc_root + "server.jar"
    shutil.move(current_jar, target_jar)

    current_prop = current_dir + "/server.properties"
    target_prop = phoenixmc_root + "server.properties"
    shutil.move(current_prop, target_prop)

    os.system("sudo chmod 777 " + phoenixmc_root + "server.jar")
    os.system("sudo chmod 777 " + phoenixmc_root + "server.properties")

    print("\033[96mMoved jar to " + phoenixmc_root + "\033[00m")
    forge_minecraft_server_setup_3()
    exit()

def forge_minecraft_server_setup_3():
    print()
    try:
        ram = int(input("\033[31mHow much GB ram do you want for your minecraft server? [1,2,3...,16] \033[00m"))
    except ValueError:
        print("\033[31mError wrong input!\033[00m")
        forge_minecraft_server_setup_3()
        exit()

    if ram < 17 and not ram == 0:
        print("\033[31mSetting ram to " + str(ram) + "GB\033[00m")
    else:
        print("\033[31mError wrong input!\033[00m")
        forge_minecraft_server_setup_3()
        exit()

    phoenix_mc_start_command = "cd " + phoenixmc_root + " && sudo java -Xmx" + str(ram) + "G -Xms" + str(ram) + "G -jar ./forge-1.17.1-37.0.78-installer.jar nogui"
    print()
    print("\033[96mUsing " + phoenix_mc_start_command + " as start trigger!\033[00m")

    java_start = str(phoenix_mc_start_command)
    java_start = "clear && " + java_start

    x = open("/usr/bin/phoenixMC", "x")
    x.write(java_start)
    x.close()
    os.system("sudo chmod +x /usr/bin/phoenixMC")
    os.system("sudo chmod 777 /usr/bin/phoenixMC")
    forge_minecraft_server_setup_4()

def forge_minecraft_server_setup_4():
    print()
    choice = input("\033[96mDo you want to manually edit settings? (recommended) [y|n] \033[00m")
    if choice == "y":
        forge_minecraft_server_config_manually()
        exit()
    elif choice == "n":
        forge_minecraft_server_config()
        exit()
    else:
        forge_minecraft_server_setup_4()
        exit()

def forge_minecraft_server_config():
    print()
    os.system("cd " + phoenixmc_root + " && sudo java -jar ./server.jar --installServer")
    minecraft_eula()
    print()
    print("\033[96mThe Error above is normal!\033[00m")
    print("\033[31mYou can start the Server with phoenixMC\033[00m")
    print()
    exit()

def forge_minecraft_server_config_manually():
    print()
    os.system("nano " + phoenixmc_root + "server.properties")
    os.system("cd " + phoenixmc_root + " && sudo java -jar ./server.jar --installServer")
    minecraft_eula()
    print()
    print("\033[96mThe Error above is normal!\033[00m")
    print("\033[31mYou can start the Server with phoenixMC\033[00m")
    print()
    exit()

def website_phishing():
    clear()
    check_sudo(False, True)
    print("\033[31mStarting blackeye!\033[00m")
    print("\033[96mChecking for requests!\033[00m")
    check_package("wget")
    check_package("php")
    check_package("unzip")
    print()
    if os.path.exists(blackeye_root):
        print("\033[31mFound existing repo!\033[00m")
        choice = input("\033[96mDo you want to overwrite it? [y|n] \033[00m")
        if choice == "y":
            print()
            os.system("sudo rm -rf " + blackeye_root)
            os.system("sudo rm " + bin_blackeye_root)

            print("\033[96mCreating dir in " + blackeye_root + "!\033[00m")
            os.system("mkdir -p ")
            print("\033[96mDownloading files!\033[00m")
            os.system("wget https://phoenixthrush.com/projects/zipped/blackeye.zip -P " + blackeye_root)
            print()
            print("\033[96mUnzipping files!\033[00m")
            os.system("unzip " + blackeye_root + "blackeye.zip -d " + blackeye_root)

            print("\033[96mInstalling files!\033[00m")
            x = open(bin_blackeye_root, "x")
            x.write("clear && sudo bash " + blackeye_root + "blackeye.sh")
            os.system("sudo chmod +x " + bin_blackeye_root)
            os.system("sudo chmod 777 " + bin_blackeye_root)
            print()
            print("\033[31mYou can start it with \"blackeye\"\033[00m")
        elif choice == "n":
            clear()
            os.system(bin_blackeye_root)
    else:
        print("\033[96mCreating dir in " + blackeye_root + "!\033[00m")
        os.system("mkdir -p ")
        print("\033[96mDownloading files!\033[00m")
        os.system("wget https://phoenixthrush.com/projects/zipped/blackeye.zip -P " + blackeye_root)
        print()
        print("\033[96mUnzipping files!\033[00m")
        os.system("unzip " + blackeye_root + "blackeye.zip -d " + blackeye_root)

        print("\033[96mInstalling files!\033[00m")
        x = open(bin_blackeye_root, "x")
        x.write("clear && sudo bash " + blackeye_root + "blackeye.sh")
        os.system("sudo chmod +x " + bin_blackeye_root)
        os.system("sudo chmod 777 " + bin_blackeye_root)
        print()
        print("\033[31mYou can start it with \"blackeye\"\033[00m")

def arch_install():
    clear()
    check_sudo(False, True)
    check_package("nano")
    print()
    print("\033[31mStarting Arch installation!\033[00m")
    print()
    if os.path.exists(alis_root):
        print("\033[31mOld files for Arch installation detected!\033[00m")
        choice = input("\033[96mDo you want to remove the old files? [y|n] \033[00m")
        if choice == "y":
            print()
            os.system("rm -rf " + alis_root)
            os.system("rm " + bin_alis_root)
            print("\033[31mOld files removed!\033[00m")
            arch_install_step_2()
            exit()
        elif choice == "n":
            print()
            print("\033[31mexiting!\033[00m")
            time.sleep(3)
            user_exit()
            exit()
    else:
        arch_install_step_2()
        exit()

def arch_install_step_2():
    print()
    print("Credits picodotdev")
    print("https://github.com/picodotdev")
    print()
    print("WARNING! All data will be erased!")
    print("Unplug all Drives that are not needed!")
    print()
    print("Please burn the official Arch Live ISO to the USB!")
    print("Boot into it and type: loadkeys [ur keymap like de-latin1 for germany]")
    print()
    print("Edit the alis.conf and alis-packages.conf")
    print("Default password is phoenixthrush")
    print()
    input("\033[95mPress Enter to continue! \033[00m")
    arch_install_step_3()
    exit()


def arch_install_step_3():
    print()
    print("\033[96mCreating new Directory at " + alis_root + "\033[00m")
    os.system("mkdir -p " + alis_root)
    os.system("sudo chmod -R 777 " + alis_root)
    print("\033[96mDownloading files that are needed to " + alis_root + "\033[00m")
    print()
    os.system("cd " + alis_root + " && curl -sL https://raw.githubusercontent.com/picodotdev/alis/master/download.sh | bash")
    os.system("cd " + alis_root + " && rm alis.conf")
    os.system("cd " + alis_root + " && rm alis-packages.conf")
    os.system("cd " + alis_root + " && wget https://raw.githubusercontent.com/Phoenixthrush/phoenixsploit/main/alis-configs/alis.conf")
    os.system("cd " + alis_root + " && wget https://raw.githubusercontent.com/Phoenixthrush/phoenixsploit/main/alis-configs/alis-packages.conf")

    print()
    print("\033[96mEditing config files for you!\033[00m")
    choice = input("\033[96mDo you want to manually edit them? [y|n] \033[00m")
    if choice == "y":
        print("\033[96mEditing Files!\033[00m")
        os.system("nano " + alis_root + "alis.conf")
        os.system("nano " + alis_root + "alis-packages.conf")
        print("\033[96mManually edited files!\033[00m")
        print()
        input("\033[95mPress Enter to start installation! \033[00m")
        arch_install_step_4()
        exit()
    elif choice == "n":
        print("\033[96mUsing default configs!\033[00m")
        arch_install_step_4()
        exit()
    else:
        arch_install_step_3()
        exit()

def arch_install_step_4():
    print()
    os.system("cd " + alis_root + " && sudo ./alis.sh")
    print()
    print("\033[96mCleaning up files!\033[00m")
    os.system("rm -rf " + alis_root)
    print("\033[96mCleaned up files!\033[00m")

def beta():
    if os.path.exists(config_root + "agree"):
        pass
    else:
        clear()
        print("\033[31mThis script is currently unstable!")
        print("Are you sure that you wanna run it?")
        print("Some functions wont work like planned rn.")
        choice = input("\nEnter y to continue or hit strg + c to exit! \033[0m")
        if choice == "y":
            os.system("sudo touch " + config_root + "agree")
        else:
            beta()

if __name__ == "__main__":
    phoenixargs = phoenixparse()
    check_os_compatibility()

    first_time()
    try:
        beta()
    except KeyboardInterrupt:
        clear()
        print("\033[31mDetected a Keyboard Interrupt!\033[00m")
        print("\033[96mexiting!\033[00m")
        time.sleep(2)
        user_exit()

    if phoenixargs.sudo is True:
        check_sudo(True, True)
        exit()
    if phoenixargs.update is True:
        if os.path.exists(phoenixsploit_root + "rerunned"):
            os.system("sudo rm " + phoenixsploit_root + "rerunned")
            install_or_update()
        else:
            rerun_sudo(True, "--update")
            exit()
    if phoenixargs.remove is True:
        if os.path.exists(phoenixsploit_root + "rerunned"):
            os.system("sudo rm " + phoenixsploit_root + "rerunned")
            uninstall_phoenixsploit()
        else:
            rerun_sudo(True, "--remove")
            exit()
    if phoenixargs.ilovecats is True:
        random_cat()
        exit()
    if phoenixargs.version is True:
        crr_ver()
        exit()
    try:
        menue()
    except KeyboardInterrupt:
        clear()
        print("\033[31mDetected a Keyboard Interrupt!\033[00m")
        print("\033[96mexiting!\033[00m")
        time.sleep(2)
        user_exit()
