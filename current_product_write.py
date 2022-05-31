#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Phoenixthrush"
__license__ = "GNU General Public License v3.0"
__version__ = "1.0.0"
__email__ = "contact@phoenixthrush.com"
__status__ = "Production"

# Importing Librarys
import os


# Setting up global variables
def global_vars():
    global version
    version = "v.1.0.0"


# Creating a clear function
def clear():
    os.system("clear")


# Creating a user exit function
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
    exit()


# Creating the entry menu
def menu():
    clear()

    # Creating a function which prints the menu
    def printing_menu():
        clear()
        print(f"\033[95mWelcome to Phoenixsploit {version}\033[00m")
        # Debug check_sudo(True, False)
        print("\033[95m  ___                           ___   ")
        print(" (o o)                         (o o)  ")
        print("(  V  ) \033[96mMade by Phoenixthrush\033[95m (  V  )")
        print("--m-m---------------------------m-m--\033[00m\n")
        print("\033[31mThis tool supports debian based distros!")
        print("Support for MacOS will be coming soon!")
        print("Have Fun\033[00m \033[96m<3\033[00m\n")
        print("\033[31m1\033[00m \033[96m-\033[00m \033[92mTools\033[00m \033[31m<3\033[00m")
        print("\033[31m2\033[00m \033[96m-\033[00m \033[92mInstall\033[95m \033[95m  Phoenixsploit")
        print("\033[31m3\033[00m \033[96m-\033[00m \033[92mUpdate\033[95m \033[95m   Phoenixsploit")
        print("\033[31m4\033[00m \033[96m-\033[00m \033[92mUninstall\033[95m \033[95mPhoenixsploit\033[00m")
        print("\033[31m5\033[00m \033[96m-\033[00m \033[00m\033[92mExit!\033[00m\n")

    # Creating a function which is getting the user input for a menu option
    def menu_choice():
        if user_input == "1":
            # Debug More tools function
            status = 0
            return status
        elif user_input == "2":
            # Debug Installing the tool
            status = 0
            return status
        elif user_input == "3":
            # Debug Updating the tool
            status = 0
            return status
        elif user_input == "4":
            # Debug Uninstalling the tool
            status = 0
            return status
        elif user_input == "5":
            user_exit()
        else:
            status = 999
            return status

    # Running the menu
    printing_menu()
    user_input = input("\033[31m$\033[00m \033[95m")

    # Checking if the user entered a right menu option
    while menu_choice() == 999:
        printing_menu()
        print("\033[95mPlease enter a valid option!\033[00m")
        user_input = input("\033[31m$\033[00m \033[95m")


def main():
    # Debug Checking for supported os
    # Debug Checking paths
    global_vars()
    menu()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear()
        print("\033[31mDetected a Keyboard Interrupt!\033[00m")
        print("\033[96mExiting!\033[00m\n")
        exit()
