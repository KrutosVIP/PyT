import random, os, datetime

def welcome_text(info, self, Style):
    print(info[11]["pyt"]["welcome"].replace("{%s}", self.color(random.choice(["{fore.black}","{fore.blue}",
"{fore.cyan}","{fore.green}","{fore.lightblack_ex}","{fore.lightblue_ex}","{fore.lightcyan_ex}","{fore.lightgreen_ex}","{fore.lightmagenta_ex}",
"{fore.lightred_ex}","{fore.lightwhite_ex}","{fore.lightyellow_ex}","{fore.magenta}","{fore.red}","{fore.reset}","{fore.white}","{fore.yellow}"]))).replace("{%d}", Style.RESET_ALL) + "\n(/cpkg/fargparse) (https://ru.stackoverflow.com/questions/1252352/%d0%9f%d0%b0%d1%80%d1%81%d0%b8%d0%bd%d0%b3-%d1%81%d1%82%d1%80%d0%be%d0%ba-%d0%bd%d0%b0-python-3-x)")


def pytrc(self, info):
    if os.path.isfile(f"{info[14].basefs}/../data/{self.info['user']}/.pytrc"):
        with open(f"{info[14].basefs}/../data/{self.info['user']}/.pytrc", "r") as f:
            print(self.color(
                    f.read().replace("{time}", str(datetime.datetime.now())).replace("{user}", self.info['user'])
                ))
    else:
        if not os.path.isdir(f"{info[14].basefs}/../data"):
            os.mkdir(f"{info[14].basefs}/../data")
        if not os.path.isdir(f"{info[14].basefs}/../data/{self.info['user']}"):
            os.mkdir(f"{info[14].basefs}/../data/{self.info['user']}")
        with open(f"{info[14].basefs}/../data/{self.info['user']}/.pytrc", "w") as f:
            f.write("\n{fore.yellow}Using default .pytrc for user.{style.reset_all}\n{style.bright}Welcome to {fore.lightblue_ex}PyT {fore.red}v2{style.reset_all}{style.bright}\nCurrent user: {fore.cyan}{user}{style.reset_all}{style.bright}\nCurrent date: {fore.green}{time}{style.reset_all}")
        self.pytrc(info)
