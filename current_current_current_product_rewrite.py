#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Phoenixthrush"
__license__ = "GNU General Public License v3.0"
__version__ = "0.1.0"
__email__ = "contact@phoenixthrush.com"
__status__ = "Production"

# Importing some needed python librarys
import os
import sys
import platform
import argparse
import subprocess
from sys import platform


# Setting up global variables
def global_vars():
    global version
    version = "v.0.1.2"

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

    # Config that values inside the phoenixthrush_blackeye.py file
    # global blackeye_root
    # blackeye_root = root + "blackeye/"

    # global bin_blackeye_root
    # bin_blackeye_root = "/usr/bin/blackeye"

    global alis_root
    alis_root = root + "alis/"

    global bin_alis_root
    bin_alis_root = "/usr/bin/alis"

    global modules_path
    modules_path = root + "modules/"


# Creating a clear function
def clear():
    os.system("clear")


# Checking if the script can be run inside the current environment
def checking_env_compatibility(verbose=True):
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

    if checking_os_platform == "arch":
        print("\033[31mThis Script doesn´t support arch based distros anymore!\033[00m")
        print("\033[31mPress Enter to exit!\033[00m")
        input()
        exit()


# Checking if install path exists and creating it if needed
def checking_paths():
    # Creating root and install directory and managing access permissons
    if os.path.exists(root):
        pass
    else:
        os.system(f"sudo mkdir -p {root}")
        os.system(f"sudo chmod -R 777 {root}")

    if os.path.exists(phoenixsploit_root):
        pass
    else:
        os.system(f"sudo mkdir -p {phoenixsploit_root}")
        os.system(f"sudo chmod -R 777 {phoenixsploit_root}")

    if os.path.exists(config_root):
        pass
    else:
        os.system(f"sudo mkdir -p {config_root}")
        os.system(f"sudo chmod -R 777 {config_root}")

    # Checking its current run state
    global run_method
    if os.path.exists(bin_phoenixsploit_root):
        if not os.path.exists(f"{phoenixsploit_root}sourced"):
            run_method = "repo"
        else:
            run_method = "source"
    elif os.path.exists(f"{phoenixsploit_root}sourced"):
        run_method = "source"
    else:
        run_method = "directly"


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


# Declaring the parser arguments
def phoenixparse():
    parser = argparse.ArgumentParser(usage="phoenixsploit [--sudo / --update / --remove / --version]")
    parser.add_argument("--sudo", help="uh instantly starting tool with admin rigths!", action="store_true")
    parser.add_argument("--update", help="uh installs or updates phoenixsploit (if everything is running well lmao)", action="store_true")
    parser.add_argument("--remove", help="uh it uninstalls phoenixsploit (I hope it works OmO)", action="store_true")
    parser.add_argument("--ilovecats", help="find it out lmao", action="store_true")
    parser.add_argument("--version", help="checks current version", action="store_true")
    return parser.parse_args()


# Checking for sudo rights
def check_for_sudo(verbose=False, req_perm=False, admin=True):
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
                    rerun_sudo(False)
                    exit()
                else:
                    print("\033[31mRunning with \033[96mnormal \033[31muser rights!\033[00m")
            else:
                if req_perm is True:
                    rerun_sudo(False)
                    exit()
                else:
                    return sudo


# Checking if debian package is installed
def check_package(package):
    retval = subprocess.call(["which", package])
    if retval != 0:
        return False
    else:
        return True


# Debug for some function that are needed like
def check_or_update():
    print()


def install_or_update():
    print()


# Creating an uninstall script
def uninstall_phoenixsploit():
    clear()
    check_for_sudo(True, True)

    if run_method == "repo":
        print("\033[31mRemoving phoenixsploit over apt!\033[0m\n")
        os.system("sudo apt remove phoenixsploit -y  >/dev/null 2>&1")
        exit()
    elif run_method == "source":
        print("\033[31mRemoving phoenixsploit (source)!\033[0m\n")
        os.system(f"sudo rm -rf {phoenixsploit_root}")
        print("\033[96mRemoved! \033[00m\033[31m^^\033[00m\n")
        exit()
    else:
        print("\033[96mbug? wtf\n")
        exit()


# Rerunning the script with additional options
def rerun_sudo(sudo=True, argparse1=None):
    if sudo is True:
        if not argparse1 is None:
            current = (os.path.abspath(__file__))
            current = "sudo python3 " + current + " " + argparse1
            os.system(f"sudo touch {phoenixsploit_root}rerunned")
            os.system(current)
            exit()
        else:
            current = (os.path.abspath(__file__))
            current = "sudo python3 " + current
            os.system(f"sudo touch {phoenixsploit_root}rerunned")
            os.system(current)
            exit()
    else:
        clear()
        print("\033[31mPlease run that script without admin rights!")
        exit()


# Checking the current platform
def checking_os_platform(verbose=True):
    system = platform

    # Checking if script is ran in MacOS or Windows
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
    # Checking the linux type
    else:
        os.system(f"grep -m 1 \"^ID=\" /etc/os-release > {config_root}os.txt")
        os.system(f"sudo chmod 777 {config_root}os.txt")
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


# Checking the current tool version
def check_current_version(verbose=True):
    clear()
    if os.path.exists(bin_phoenixsploit_root):
        if not os.path.exists(phoenixsploit_root + "sourced"):
            if verbose is True:
                print(f"\033[96mYou currently have phoenixsploit {version} (repo) installed!\033[00m")
                print()
            return "repo"
        else:
            if verbose is True:
                print(f"\033[96mYou currently have phoenixsploit {version} (source out of repo) installed!\033[00m")
                print()
            return "source"
    elif os.path.exists(phoenixsploit_root + "sourced"):
        if verbose is True:
            print(f"\033[96mYou currently have phoenixsploit {version} (source out of repo) installed!\033[00m")
            print()
        return "source"
    else:
        print(f"\033[96mYou are running phoenixsploit {version} directly!\033[00m")
        print("\n\033[31mThere are two options to install phoenixsploit \033[00m(with my repo \033[96m[recommended]\033[00m, or from source)\033[00m \n\n - \"\033[96mcurl -sSL phoenixthrush.com/phoenixsploit/repo-install.sh | bash\033[00m\"   \033[31mto install it through my repo\033[00m \n - \"\033[96mcurl -sSL phoenixthrush.com/phoenixsploit/source-install.sh | bash\033[00m\" \033[31mto install it without my repo")
        print()
        exit()


# Printing the help menu
def show_help():
    print("\033[31mHelp Menu: \033[00m\n")  # Debug
    print("\033[95mGeneral Syntax:\033[00m")
    print("\033[96mYou can always type \033[96m\"\033[00m\033[31mexit\033[00m\033[96m\"\033[00m\033[96m to exit!\033[00m")
    print("\033[96mYou can always type \033[96m\"\033[00m\033[31mhelp\033[00m\033[96m\"\033[00m\033[96m to print this help screen!\033[00m\n")
    print("\033[95mCurrent Syntax:\033[00m")
    print("\033[96mType a number from \033[96m\"\033[00m\033[31m1-5\033[00m\033[96m\"\033[00m\033[96m from one option of the menu!\nThere is a number before every option which holds the name of the funtion!\033[00m\n")
    input("\033[31mPress enter to return!\033[00m\033[96m ")
    print("\033[00m")
    clear()


# Checking if a run parser is given
def checking_parser():
    phoenixargs = phoenixparse()
    if phoenixargs.sudo is True:
        check_for_sudo(True, True)
        exit()
    if phoenixargs.update is True:
        if os.path.exists(phoenixsploit_root + "rerunned"):
            os.system(f"sudo rm {phoenixsploit_root}rerunned")
            install_or_update()
        else:
            rerun_sudo(True, "--update")
            exit()
    if phoenixargs.remove is True:
        if os.path.exists(f"{phoenixsploit_root}rerunned"):
            os.system(f"sudo rm {phoenixsploit_root}rerunned")
            uninstall_phoenixsploit()
        else:
            rerun_sudo(True, "--remove")
            exit()
    if phoenixargs.ilovecats is True:
        function_ilove_cats()
        exit()
    if phoenixargs.version is True:
        check_current_version()
        exit()


# Calling the ascii cat script
def function_ilove_cats():
    try:
        # Importing needed phoenixthrush_ilovecats library
        sys.path.append(modules_path)
        import phoenixthrush_ilovecats
        # Calling the main function inside the ilovecats lib
        phoenixthrush_ilovecats.main()
        exit()
    except ModuleNotFoundError:
        clear()
        print("\033[31mCould not import the ilovecats library!\033[00m\n")
        print("\033[96mPlease make sure that the \"modules\" folder inside the root of the current script file contains the \"phoenixthrush_ilovecats.py\" file!\033[00m\n")

        def ilovecats_show_help():  # Printing the help menu
            print("\033[31mHelp Menu: \033[00m\n")
            print("\033[95mGeneral Syntax:\033[00m")
            print("\033[96mYou can always type \033[96m\"\033[00m\033[31mexit\033[00m\033[96m\"\033[00m\033[96m to exit!\033[00m")
            print("\033[96mYou can always type \033[96m\"\033[00m\033[31mhelp\033[00m\033[96m\"\033[00m\033[96m to print this help screen!\033[00m\n")
            print("\033[95mCurrent Syntax:\033[00m")
            print("\033[96mType \033[96m\"\033[00m\033[31myes or y\033[00m\033[96m\"\033[00m\033[96m to install the missing module!\033[00m")
            print("\033[96mType \033[96m\"\033[00m\033[31mno or n\033[00m\033[96m\"\033[00m\033[96m to exit out!\033[00m\n")
            input("\033[31mPress enter to return!\033[00m\033[96m ")
            print("\033[00m")
            clear()

        def ilovecats_printing_menu():  # Printing the menu
            print("\033[31mDo you want to download the file?\033[00m")

        # Creating a function which is getting the user input for a menu option
        def ilovecats_menu_choice():
            if user_input.upper() == "YES" or user_input.lower() == "y":  # "YES" is big because idk its a bug idk why
                print("\033[00m")
                clear()
                print(f"\033[96mDownloading the module to {modules_path}!\033[00m")
                os.system(f"sudo wget -P {modules_path} https://phoenixthrush.com/phoenixsploit/modules/phoenixthrush_ilovecats.py >/dev/null 2>&1")
                print("\033[31mPlease rerun to take changes!\033[00m\n")
                exit()
            elif user_input.upper() == "NO" or user_input.lower() == "n":  # Same here for "NO"
                print("\033[00m")
                clear()
                user_exit()
            elif user_input.lower() == "help" or user_input.lower() == "h":
                print("\033[00m")
                clear()
                ilovecats_show_help()
                function_ilove_cats()
            elif user_input.lower() == "quit" or user_input.lower() == "exit" or user_input.lower() == "q":
                print("\033[00m")
                clear()
                user_exit()
            else:
                print("\033[00m")
                clear()
                status = 999
                return status

        # Running the menu
        ilovecats_printing_menu()
        user_input = input("\033[31m$\033[00m \033[96m")

        # Checking if the user entered a right menu option
        while ilovecats_menu_choice() == 999:
            ilovecats_printing_menu()
            print("\033[95mPlease enter a valid option!\033[00m")
            user_input = input("\033[31m$\033[00m \033[96m")


# Calling the minecraft installer script
def function_minecraft():  # Debug coming soon
    user_exit()


# Calling the arch installer script
def function_arch_installer():  # Debug coming soon
    user_exit()
    

# Calling the blackeye script
def function_blackeye():
    user_exit()  # Debug coming soon
    

# Creating the entry menu
def menu():
    clear()

    # Creating a function which prints the menu
    def printing_menu():
        clear()
        print(f"\033[95mWelcome to Phoenixsploit {version}\033[00m")
        check_for_sudo(True, False)
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
            print("\033[00m")
            clear()
            status = 0
            return status
        elif user_input == "2":
            # Debug Installing the tool
            print("\033[00m")
            clear()
            status = 0
            return status
        elif user_input == "3":
            # Debug Updating the tool
            print("\033[00m")
            clear()
            status = 0
            return status
        elif user_input == "4":
            # Debug Uninstalling the tool
            print("\033[00m")
            clear()
            status = 0
            return status
        elif user_input == "5":
            print("\033[00m")
            clear()
            user_exit()
        elif user_input == "ilovecats":
            print("\033[00m")
            clear()
            function_ilove_cats()
        elif user_input.lower() == "help" or user_input.lower() == "h":
            print("\033[00m")
            clear()
            show_help()
            menu()
        elif user_input.lower() == "quit" or user_input.lower() == "exit" or user_input.lower() == "q":
            print("\033[00m")
            clear()
            user_exit()
        else:
            print("\033[00m")
            clear()
            status = 999
            return status

    # Running the menu
    printing_menu()
    user_input = input("\033[31m$\033[00m \033[96m")

    # Checking if the user entered a right menu option
    while menu_choice() == 999:
        printing_menu()
        print("\033[95mPlease enter a valid option!\033[00m")
        user_input = input("\033[31m$\033[00m \033[96m")


# Entry point, calling every function to start the script
def main():
    global_vars()
    checking_env_compatibility()
    checking_paths()
    checking_os_platform()
    checking_parser()
    menu()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear()
        print("\033[31mDetected a Keyboard Interrupt!\033[00m")
        print("\033[96mExiting!\033[00m\n")
        exit()
