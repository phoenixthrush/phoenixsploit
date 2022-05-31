#!/usr/bin/env python3
import os
import argparse

def phoenixparse():
    parser = argparse.ArgumentParser(usage="phoenixsploit [--sudo / --update / --remove / --version]")
    parser.add_argument("--sudo", help="uh instantly starting tool with admin rigths!", action="store_true")
    parser.add_argument("--update", help="uh installs or updates phoenixsploit (if everything is running well lmao)", action="store_true")
    parser.add_argument("--remove", help="uh it uninstalls phoenixsploit (I hope it works OmO)", action="store_true")
    parser.add_argument("--ilovecats", help="find it out lmao", action="store_true")
    parser.add_argument("--version", help="checks current version", action="store_true")

    return parser.parse_args()

if __name__ == "__main__":
    phoenixargs = phoenixparse()

    if phoenixargs.sudo is True:
        os.system("python3 /etc/phoenixthrush/phoenixsploit --sudo")
        exit()
    if phoenixargs.update is True:
        os.system("python3 /etc/phoenixthrush/phoenixsploit --update")
        exit()
    if phoenixargs.remove is True:
        os.system("python3 /etc/phoenixthrush/phoenixsploit --remove")
        exit()
    if phoenixargs.ilovecats is True:
        os.system("python3 /etc/phoenixthrush/phoenixsploit --ilovecats")
        exit()
    if phoenixargs.version is True:
        os.system("python3 /etc/phoenixthrush/phoenixsploit --version")
        exit()

    os.system("python3 /etc/phoenixthrush/phoenixsploit")
