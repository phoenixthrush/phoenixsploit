#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Phoenixthrush"
__license__ = "GNU General Public License v3.0"
__version__ = "1.0.0"
__email__ = "contact@phoenixthrush.com"
__status__ = "Production"

import os
import shutil

global root
root = "/usr/share/phoenixthrush/"

global blackeye_root
blackeye_root = root + "blackeye/"

global bin_blackeye_root
bin_blackeye_root = "/usr/bin/blackeye"

def clear():
    os.system("clear")

def website_phishing():
    clear()
    print("\033[31mStarting blackeye!\033[00m")
    print("\033[96mChecking for requests!\033[00m\n")
    if os.path.exists(blackeye_root):
        print("\033[31mFound existing repo!\033[00m")
        choice = input("\033[96mDo you want to redownload the files? [y|n] \033[00m")
        if choice == "y":
            print()
            os.system(f"sudo rm -rf {blackeye_root}")
            print("\033[96mDownloading files from github!\033[00m")
            os.system("git clone https://github.com/phoenixthrush/blackeye blackeye")
            print("\n\033[96mCopying files!\033[00m")

            current_dir = os.getcwd()
            current_dir += "/blackeye/"
            original = current_dir
            target = blackeye_root
            shutil.move(original, target)

            print("\033[96mInstalling files!\033[00m")
            x = open(bin_blackeye_root, "x")
            x.write(f"clear && sudo bash {blackeye_root}/blackeye.sh")
            os.system("sudo chmod +x /bin/blackeye")
            os.system("sudo chmod 777 /bin/blackeye")
            print()
            print("\033[31mYou can start it with blackeye\033[00m")
        elif choice == "n":
            clear()
            os.system(f"sudo bash {blackeye_root}/blackeye.sh")
    else:
        print("\033[96mNo old files found!\033[00m")
        print("\033[96mDownloading files!\033[00m")
        print()
        os.system("git clone https://github.com/phoenixthrush/phoenixthrush.github.io repo")
        print()
        print("\033[96mCopying files!\033[00m")

        current_dir = os.getcwd()
        current_dir += "/repo"
        original = current_dir
        target = "/etc/phoenixthrush/repo"
        shutil.move(original, target)

        print("\033[96mInstalling files!\033[00m")
        x = open("/bin/phoenixphish", "x")
        x.write("clear && sudo bash /etc/phoenixthrush/repo/linux/blackeye/blackeye.sh")
        os.system("sudo chmod +x /bin/phoenixphish")
        os.system("sudo chmod 777 /bin/phoenixphish")
        print()
        print("\033[31mYou can start it with phoenixphish\033[00m")

website_phishing()