import sys, json, os, importlib, shutil
from colorama import Back, Fore, Style
from colorama import init as cinit
from prompt_toolkit.shortcuts import  radiolist_dialog, message_dialog, checkboxlist_dialog, yes_no_dialog
sys.path.insert(0, "../types")
cinit()
from binary import Binary
#class Binary():
 #   	pass
 
import PyT.acc_utils
importlib.reload(PyT.acc_utils)
passwd_dialog = PyT.acc_utils.passwd_dialog
input_dialog = PyT.acc_utils.input_dialog
create_dialog = PyT.acc_utils.create_dialog

class accmenu(Binary):
    def __init__(self):
        self.info = {
            "name" : "Account editor",
            "version" : "v1",
            "codename": "accmenu",
            "dependencies" : [], # Not Supported.
            "description": "Change accounts settings [ROOT]",
            "run": self.run
        }

    def json_load(self, file):
        with open(file, "r") as f:
            return json.load(f)

    def control_acc(self, info, pyt, acc):
        lang = self.lang
        with open(f"{info.info[14].basefs}/../var/kernel_sets.json", "r") as f:
            d = f.read()
            acc1 = json.loads(d)
        if acc == "create":
            err = 1
            while err == 1:
                opt = create_dialog(lang["create2"], lang["create_pswd"], lang["create_text"], lang["create_root"], lang["ok"], lang["cancel"], lang["create_root2"]).run()
                if opt != None:
                    if opt[1] in acc1["accounts"]:
                        message_dialog(lang["create2"], lang["create_error1"], ok_text = lang["ok"]).run()
                        err = 1
                    elif opt[2][0] != opt[2][1]:
                        message_dialog(lang["create2"], lang["chpass_err"], ok_text = lang["ok"]).run()
                        err = 1
                    elif "root" in opt[0] and not pyt.accs_o[pyt.info["user"]]["root_acc"]:
                        message_dialog(lang["create2"], lang["create_error2"], ok_text = lang["ok"]).run()
                        err = 1
                    else:
                        err = 0
                else:
                    err = 0

            if opt != None :
                acc1["accounts"].update({opt[1]: opt[2][0]})
                rooted = False
                if "root" in opt[0]:
                    rooted = True
                acc1["account_options"].update({opt[1]: {"root_acc": rooted}})
                    
        if not acc == "create":
            if not len(pyt.accs_o) > 1:
                acc_opt = radiolist_dialog(
                title=lang["accmenu2"],
                text=lang["accm_acc"].replace("{acc}", acc),
                values=
                [ ("chpass", lang["chpass"]),
                  ("chname", lang["chname"]),
                  ("chroot", lang["chroot"])
                ], ok_text = lang["ok"], cancel_text=lang["cancel"]).run()
            else:
                acc_opt = radiolist_dialog(
                title=lang["accmenu2"],
                text=lang["accm_acc"].replace("{acc}", acc),
                values=
                [ ("chpass", lang["chpass"]),
                  ("chname", lang["chname"]),
                  ("chroot", lang["chroot"]),
                  ("delete", lang["delete"])
                ], ok_text = lang["ok"], cancel_text=lang["cancel"]).run()
        else:
            acc_opt = None
                


        if acc_opt == "chpass" and not acc == "create":
            err = True
            while err:
                pswd = passwd_dialog(lang["accmenu3"], lang["chpass2"], lang["ok_chpass"], lang["pswd_none"], lang["no_chpass"]).run()
                if pswd == None:
                    err = False
                    break
                if pswd[0] == pswd[1]:
                    acc1["accounts"][acc] = pswd[0]
                    err = False
                else:
                    message_dialog(lang["accmenu3"], lang["chpass_err"], ok_text = lang["ok"]).run()
                    
        elif acc_opt == "chname" and not acc == "create":
            name = input_dialog(lang["chname"], lang["chname_t"], lang["ok"], lang["cancel"]).run()
            if name == None:
                pass
            else:
                if name in acc1["accounts"] or name in acc1["account_options"]:
                    message_dialog(lang["chname"], lang["chname_err"], ok_text = lang["ok"]).run()
                if acc == pyt.info["user"]:
                    pyt.info["user"] = name
                    info.info[14].user = name
                pswd = acc1["accounts"][acc]
                del acc1["accounts"][acc]
                acc1["accounts"].update({name: pswd})

                rooted = acc1["account_options"][acc]
                del acc1["account_options"][acc]
                acc1["account_options"].update({name: rooted})

                shutil.move(f"{info.info[14].basefs}/../data/{acc}", f"{info.info[14].basefs}/../data/{name}")

        elif acc_opt == "chroot" and not acc == "create":
            opt = checkboxlist_dialog(title= lang["chroot"], text = lang["chroot_2"], values =
            [("root", lang["root"])], ok_text= lang["ok"], cancel_text = lang["cancel"]
            ).run()
            if not "root" in opt:
                rooted = []
                for ac in acc1["account_options"]:
                    rooted.append(acc1["account_options"][ac]["root_acc"])
                
                if rooted.count(True) == 1 and acc1["account_options"][acc]["root_acc"]:
                    message_dialog(lang["chroot"], lang["chroot_err"], ok_text = lang["ok"]).run()
                else:
                    acc1["account_options"][acc]["root_acc"] = False

            if "root" in opt:
                if acc1["account_options"][acc]["root_acc"]:
                    message_dialog(lang["chroot"], lang["chroot_err2"], ok_text = lang["ok"]).run()
                else:
                    acc1["account_options"][acc]["root_acc"] = True
                
        elif acc_opt == "delete" and not acc == "create":
            err2 = False
            if acc == pyt.info["user"] and not err2:
                message_dialog(lang["delete"], lang["delete_err"], ok_text = lang["ok"]).run()
                err2 = True
            opt = yes_no_dialog(lang["delete"], lang["delete_text"], yes_text = lang["yes"], no_text = lang["no"])
            if len(acc1["accounts"]) == 1 and not err2:
                message_dialog(lang["delete"], lang["delete_err1"], ok_text = lang["ok"]).run()
                err2 = True
            rooted = []
            for ac in acc1["account_options"]:
                rooted.append(acc1["account_options"][ac]["root_acc"])
                
            if rooted.count(True) == 1 and acc1["account_options"][acc]["root_acc"] and not err2:
                message_dialog(lang["delete"], lang["chroot_err"], ok_text = lang["ok"]).run()
                err2 = True

            if not err2:
                del acc1["account_options"][acc]
                del acc1["accounts"][acc]
                try:
                    shutil.rmtree(f"{info.info[14].basefs}/../data/{acc}")
                except:
                    pass
                
        with open(f"{info.info[14].basefs}/../var/kernel_sets.json", "w") as f:
            json.dump(acc1, f, indent=4)

        pyt.accs = acc1["accounts"]
        pyt.accs_o = acc1["account_options"]
            
        return

        
    
    def run(self, info, pyt):
        lang = self.json_load(f"{info.info[14].basefs}/../var/kernel_sets.json")["lang"]
        if os.path.isfile(f"{info.info[14].basefs}/../lang/accnt_{lang}.json"):
            with open(f"{info.info[14].basefs}/../lang/accnt_{lang}.json", "r") as f:
                lang = json.load(f)
        else:
            lang = {
                    "accmenu": "Select account | AccountMenu",
                    "accmenu2": "Check account | AccountMenu",
                    "accmenu3": "Change password | AccountMenu",
                    "accm_accounts": "Accounts:",
                    "accm_acc": "Account {acc}:",
                    "no_root": "[Error] No root.",
                    "chpass": "Change password",
                    "chroot": "Root account?",
                    "chname": "Change account name",
                    "delete": "Delete account.",
                    "chpass2": "Change password. The second input is for verifying, type your new password two times.",
                    "ok_chpass": "Change",
                    "no_chpass": "No change.",
                    "pswd_none": "No password",
                    "chpass_err": "First password is not matching the second.",

                    "chname_t": "Change name of account.",
                    "chname_err": "Cannot change account name to name of existing account.",
                    "ok": "OK",
                    "cancel": "Cancel",

                    "chroot_2": "Want to root your account?",
                    "root": "Root",
                    "chroot_err": "There is only this account with root!",
                    "chroot_err2": "This account is already rooted!",
                    
                    "delete_text": "Do you want to delete your account?",
                    "yes": "Yes",
                    "no": "No",
                    "delete_err": "Can`t delete active account.",
                    "delete_err1": "You have only one account.",

                    "create": "[Create new account...]",
                    "create2": "Create account",
                    "create_text": "Welcome to account creator. This input under text is your nickname.",
                    "create_root": "Your account will be rooted?",
                    "create_root2": "Root",
                    "create_pswd": "Input password in first input and repeat it in second. Type 'null' in first text field to set password to none and press Cancel.",
                    "create_error1": "Account exists!",
                    "create_error2": "You cannot create root-account without root on your account!"
                }
        self.lang = lang
        
        if not pyt.accs_o[pyt.info["user"]]["root_acc"]:
            d = [(pyt.info["user"], pyt.info["user"])]
        else:
            d = []
            for i in pyt.accs_o:
                d.append((i, i))
        d.append(("create", lang["create"]))
        acc = radiolist_dialog(
        title=lang["accmenu"],
        text=lang["accm_accounts"],
        values=d, ok_text = lang["ok"], cancel_text=lang["cancel"]).run()
        if acc == None:
            return

        self.control_acc(info, pyt, acc)
