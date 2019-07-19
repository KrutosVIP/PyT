log=[]
i1="Imported 'sys'"
i2="Imported 'colorama'"
i3="Imported 'time'"
i4="Imported 'os'"
i5="Imported 'this'"
i6="Imported 'datetime'"
pt1="Issued command 'help'"
pt2="Issued command 'version'"
pt3="Issued command 'time'"
pt4="Issued command 'ltime'"
pt5="Issued command 'print'"
pt6="Issued command 'this'"
pt7="Issued command 'author'"
pt8="Issued command 'calc'"
pt9="Issued command 'editor'"
ptd1="Issued command 'акки'"
off="Console off "
e1="Typed unknown input."
e2="Calculator:Typed unknown input."
e3="FileEditor:Typed unknown input."
f1="FileEditor:Issued command '_prf'"
foff="FileEditor:File Editor off"
f2="FileEditor:Issued command '_r'"
f3="FileEditor:Issued command '_w'"
cm="Calclator:Issued command 'multiply'"
cd="Calclator:Issued command 'divide"
cs="Calclator:Issued command 'subtract'"
ca="Calclator:Issued command 'add'"
coff="Calculator:Calculator off"
def wrlfunc():
	try:
		with open(r"propertiesconsole/logs/log.ptl", "w") as file:
			file.writelines("%s\n" % line for line in log)
	except FileNotFoundError:
		pf.FNFE()
def exfunc():
	try:
		with open(r"propertiesconsole/logs/log.ptl", "w") as file:
			file.writelines("%s\n" % line for line in log)
		sys.exit()
	except FileNotFoundError:
		pf.logfunc()
		pf.FNFE()
		sys.exit()
try:
	import sys
except ModuleNotFoundError:
	print("ERROR:Module 'sys' not found")
	exit(1)
else:
	print("Module 'sys' imported!")
	log.append(i1)
try:
	import pytf.core as pf
except ModuleNotFoundError:
		print("Module 'pytf' not found.To install,go in cmd,go to directory 'pyt-f/dist/' by command cd and when,write in console 'pip install pytf-1.1.tar.gz'")
else:
	print("Custom module \"PyTF\" imported!")
try:
	import colorama
	from colorama import init,deinit
	from colorama import Fore, Back, Style
	init()
except ModuleNotFoundError:
	print("Module 'colorama' not found.")
	pf.MNFENC()
else:
	print("Module 'colorama' imported!")
	log.append(i2)
try:
	import time
except ModuleNotFoundError:
	print("Мodule 'time' not found. ")
	pf.MNFE()
else:
	print("Module 'time' imported!")
	log.append(i3)
try:		
	import os
except ModuleNotFoundError:
	print("Мodule 'os' not found. ")
	pf.MNFE()
else:
	print("Module 'os' imported!")
	log.append(i4)
try:		
	import this
except ModuleNotFoundError:
	print("Мodule 'this' not found. ")
	pf.MNFE()
else:
	print("Module 'this' imported!")
	log.append(i5)
try:		
	import datetime
except ModuleNotFoundError:
	print("Мodule 'datetime' not found. ")
	pf.MNFE()
else:
	print("Module 'datetime' imported!")
	log.append(i6)
print(Style.RESET_ALL)

ConsoleOn="Setup"
NoLogin="Y"
accpass="0"
acclogin="0"
prf="file_ed"
prf2="калк"
prx_input="Y"
ainp1="0"
an="0"
ap="0"
prx_input2="Y"
res="0"
inputsw="1"


disk="0"        
lang="No"
langsetup="No"
langsys="No"
setup="■"
pb="0"
finput="1"
user2_input="0"
punkt1="1.Formatting disk without deleting setup files and old system files"
punkt2="2.Copying files"
punkt3="3.Setupping other programs."

punkt11="1.Форматирование диска без удаления установщика и старых файлов системы."
punkt22="2.Копирование файлов."
punkt33="3.Установка других программ."
try:            
        setupdatas=open("propertiesconsole/setupprop.txt","r")
        setupdatalang=open("propertiesconsole/setuplang.txt","r")
        languagea = setupdatalang.read()
        setupsdata= setupdatas.read()
        setupdatas.close()
        setupdatalang.close()
        adn = open("propertiesconsole/accs/admin/name.txt","r")
        adminacc=adn.read()
        adn.close()
        adp = open("propertiesconsole/accs/admin/pass.txt","r")
        adminp=adp.read()
        adp.close()
        ConsoleOn="0"
        print(Back.BLACK)
        print(Fore.WHITE)
        print(Style.DIM)
        
except FileNotFoundError:
        print(Fore.WHITE)
        print(Back.BLUE)
        print("Your setup is starting...")
        setupsdata="0"

else:
        if languagea=="1":
                langsys="En/En"
                langsetup="En/En"
        if languagea=="2":
                langsys="Ru/Ru"
                langsetup="Ru/Ru"
        print("Loading Console...")
        ConsoleOn="0"

while setupsdata=="0":
        print("Setup is loading files")
        for i in range(1,101,1):
                print(setup * i ,i,"%")
        for i in range(1,100,2):
                print( i,"%")
        print("Welcome to setup of PYTHON CONSOLE v1.")
        print("Do  you agree with our terms and politics?")
        while finput=="1":
                inputa=input("Yes/No:")
                if inputa=="Yes":
                        print("Okay.Going to the other part...")
                        finput="0"
                        setup="2"
                elif inputa=="No":
                        finput="0"
                        pb="1"
                else:
                        print("Invalid input")

                if pb=="1":
                        pf.bfunx()

                user2="0"
        while user2=="0":
                print("Select your license:")
                print("1 - Python Console Home Edition")
                print("Dev - Python Console Razrab Edition")
                user2_input=input("Write your license name here:>>>")
                if user2_input=="1":
                        print("Python Console Home Edition is selected.")
                        license="home"
                        licensewrite
                        user2="1"
                if user2_input=="MLG":
                        print("Python Console MLG Edition is selected.")
                        licensewrite = open("propertiesconsole/license/l.txt","w")
                        license="MLG"
                        user2="1"
                if user2_input=="Dev":
                        print("Python Console Razrab Edition is selected.")
                        license="2"
                        user2="1"
                else:
                        print("Invalid license name.")
        while user2=="1":
                print("Select your languge:")
                print("Ru/Ru - Normal Russian language.")
                print("En/En - Normal English language")
                lang=input("Select:>>>")
                if lang=="Ru/Ru":
                        print("Русский установлен как обычный язык..")
                        langsetup="Ru/Ru"
                        langsys="Ru/Ru"
                        user2="0"
                        setupsdata=="2"
                
                elif lang=="En/En":
                        print("English language is set to usual language.")
                        langsetup="En/En"
                        langsys="En/En"
                        break
                
                else:
                        print("Invalid language")

        if pb=="0"and langsetup=="En/En" :
                print("Name your disk.")
                try:
                        disk=input("Name disk:>>>")
                        os.mkdir(disk)
                        os.mkdir("Local Disk С")
                except FileExistsError:
                        print("Critical Error:File 'D' or 'C' exists!")
                        sys.exit()
                print("Now:Installation is starting...")
                print(punkt1)
                print(punkt2)
                print(punkt3)
                for i in range(1,100,2):
                        print(punkt1,i,"%")
                print(punkt1,"...100%")
                for i in range(1,100,2):
                        print(punkt2,i,"%")
                print(punkt2,"...100%")
                for i in range(1,100,2):
                        print(punkt3,i,"%")
                print(punkt3,"...100%")
                print("Restarting...")
                for i in range(1,120,1):
                        if i == "120":
                                print("Restarting is in progress...")
                print("Setup is loading files")
                setup2="■"
                for i in range(1,101,1):
                        print(setup2 * i ,i,"%")
                print("Setup is ending now...")
                print(punkt1,"...100%")
                print(punkt2,"...100%")
                print(punkt3,"...100%")
                for i in range(1,100,1):
                        print("Ending...",i,"%")
                print("Setup is ended.Going in console...3")
                print("Setup is ended.Going in console...2")
                print("Setup is ended.Going in console...1")
                ConsoleOn="reg"

        if pb=="0"and langsetup=="Ru/Ru" :
                print("Дайте имя диску")
                try:
                        disk=input("Имя диска:>>>")
                        disk2="Локальный диск "
                        disk2+=disk
                        os.mkdir(disk2)
                        os.mkdir("Локальный диск С")
                except FileExistsError:
                        print("Critical Error:File '",disk,"' or 'C' exists!")
                        sys.exit()
                else:
                        print("Папки дисков сделан")
                print("Сейчас:Установка начинается")
                print(punkt11)
                print(punkt22)
                print(punkt33)
                for i in range(1,100,2):
                        print(punkt11,i,"%")
                print(punkt11,"...100%")
                for i in range(1,100,2):
                        print(punkt22,i,"%")
                print(punkt22,"...100%")
                for i in range(1,100,2):
                        print(punkt33,i,"%")
                print(punkt33,"...100%")
                print("Перезагрузка...")
                for i in range(1,120,1):
                        if i == "120":
                                print("Перезагрузка в прогрессе...")
                print("Установщик загружает файлы...")
                setup2="■"
                for i in range(1,101,1):
                        print(setup2 * i ,i,"%")
                print("Установка заканчивается сейчас...")
                print(punkt1,"...100%")
                print(punkt2,"...100%")
                print(punkt3,"...100%")
                for i in range(1,100,1):
                        print("Окончание...",i,"%")
                print("Установка окончена.Переход в консоль...3")
                print("Установка окончена.Переход в консоль...2")
                print("Установка окончена.Переход в консоль...1")
                ConsoleOn="reg"
        
        
        
        if ConsoleOn=="reg" and langsys=="En/En":
                print("Now,register admin account")
                adminacc=input("Name:")
                adminp=input("Password:")
                print("Done!Activating Console...")
                ConsoleOn="0"
                try:
                        os.makedirs("propertiesconsole/accs/admin")
                except OSError:
                        print("Error...")

                else:
                        print("Directories done.")
                try:
                        setupdatas=open("propertiesconsole/setupprop.txt","w")
                        setupdatalang=open("propertiesconsole/setuplang.txt","w")
                        setupdatas.write(str("1"))
                        setupdatalang.write(str("1"))
                        setupdatas.close()
                        setupdatalang.close()
                        adac=open("propertiesconsole/accs/admin/name.txt","w")
                        adac.write(adminacc)
                        adpas=open("propertiesconsole/accs/admin/pass.txt","w")
                        adpas.write(adminp)
                        adac.close()
                        adpas.close()
                        pf.logfunc()
                except FileNotFoundError:
                        print(Back.RED)
                        print(Fore.WHITE) 
                        print("CRITICAL ERROR (FNF):STOPPING PROGRAM!!!")
                        print("If you delete directory 'propertiesconsole' ,please,create it and then,try one more time.")
                        pf.FNFE()
                        
                else:
                        setupsdata="1"

        if ConsoleOn=="reg" and langsys=="Ru/Ru":
                print("Теперь,зарегестрируйте аккаунт админа.")
                adminacc=input("Имя:")
                adminp=input("Пароль:")
                print("Готово!Активирование консоли...")
                ConsoleOn="0"
                try:
                        os.makedirs("propertiesconsole/accs/admin")
                except OSError:
                        print("Ошибка:propertiesconsole/accs/admin cannot be created.")
                        pf.OSE()

                else:
                        print("Директории сделаны.")
                try:
                        setupdatas=open("propertiesconsole/setupprop.txt","w")
                        setupdatalang=open("propertiesconsole/setuplang.txt","w")
                        setupdatas.write(str("1"))
                        setupdatalang.write(str("2"))
                        setupdatas.close()
                        setupdatalang.close()
                        adac=open("propertiesconsole/accs/admin/name.txt","w")
                        adac.write(adminacc)
                        adpas=open("propertiesconsole/accs/admin/pass.txt","w")
                        adpas.write(adminp)
                        adac.close()
                        adpas.close()
                        pf.logfunc()
                except FileNotFoundError:
                        print(Back.RED)
                        print(Fore.WHITE) 
                        print("CRITICAL ERROR (FNF):STOPPING PROGRAM!!!")
                        print("If you delete directory 'propertiesconsole' ,please,create it and then,try one more time.")
                        sys.exit()
                else:
                        setupsdata="1"
while langsys=="En/En":
        print(Back.BLACK)
        print(Fore.WHITE) 
        while ConsoleOn=="0" and langsys=="En/En":
                print("Turn console 'ON' or 'OFF' by writing this command in console. ")
                Console=input("ON/OFF:>>>")
                if Console=="ON" :
                        print("After you start work with console,please,login!")
                        print("Print account name and login")
                        acclogin=input("Name:>>>")
        
                elif Console=="OFF":
                        print("Turning OFF...")
                        log.append(off)
                        wrlfunc()
                        sys.exit()
                else:
                        print("Invalid command.")               
                if acclogin==adminacc:
                        print("You have been logged as admin.Please ,write password.")
                        accpass=input("Password:>>>")
                else:
                        print("Invalid account")
                if accpass==adminp:
                        print("Done!")
                        NoLogin="N"
                        ConsoleOn="1"
                        break
                else:
                        print("Invalid password")
        
        if NoLogin=="N" and langsys=="En/En":
                print("Done by KrutosVIP and Zazio on Python.")
                print("Libraries:sys,time,this,os,datetime,colorama")
                print("This is a console PyT v1!")
                print(time.ctime())
                print("To see availlible commands,type 'help'")
        
        while langsys=="En/En":
                while ConsoleOn=="1"  and langsys=="En/En":
                        user_input=input("|>>>")
                        if user_input=="help":
                                print("Now availible commands is:")
                                print("help - Print this.")
                                print("version - Prints version of console")
                                print("time - Time")
                                print("ltime -Local Time")
                                print("print - Prints what you type")
                                print("toff - Turn off console")
                                print("author - Prints the console`s author")
                                print("calc - Calculate what you want")
                                print("this - (INFORMATION DELETED)")
                                print("editor - activating FileEditor. ")
                                log.append(pt1)
                                wrlfunc()
                                
                        elif user_input == "version":
                                print("Version of PyT-v.1.1 Language update PRE-RELEASE ^_^")
                                print("Done on Python 3.6.4")
                                log.append(pt2)
                                wrlfunc()
                                
                        elif user_input == "time":
                                print(time.strftime("Today is %B %d, %Y.", time.localtime()))
                                log.append(pt3)
                                wrlfunc()
                                
                        elif user_input == "ltime":
                                print(time.localtime())
                                log.append(pt4)
                                wrlfunc()
                                
                        elif user_input == "print":
                                d_print = input("Write words what you want to print in console")
                                print(d_print)
                                log.append(p5)
                                wrlfunc()
                                
                        elif user_input == "toff":
                                print("Thank you  for usage of our console")
                                log.append(off)
                                deinit()
                                exfunc()
                                
                        elif user_input == "author":
                                print("The authors of console is KrutosVIP(I AM A GLAVA BLIN) and Zazio")
                                log.append(pt7) 
                                wrlfunc()
                                
                        elif user_input == "calc":
                                print("Activating calculator")
                                log.append(pt8)
                                wrlfunc()  
                                ConsoleOn = "2"
                                
                        elif user_input == "this":
                                log.append(pt6)
                                print(this.s)
                                wrlfunc()
                                
                        elif user_input == "editor":
                                print("Activating FileEditor v1...")
                                ConsoleOn="3"
                                log.append(pt9)
                                wrlfunc()
                                        
                        else:
                                print("INVALID COMMAND.If you want to see available commands ,type 'help'.")
                                log.append(e1)
                                wrlfunc()
                                
                while ConsoleOn=="2" :
                        print("Options:")
                        print("Type 'add' to add two numbers")
                        print("Type 'subtract'to subtract two numbers")
                        print("Type 'multiply'to multiply two numbers")
                        print("Type 'divide' to divide two numbers")
                        print("Type 'quit' to end with calculator.")
                        user_input = input(">")
                        try:
                                if user_input == "quit":
                                        log.append(coff)
                                        wrlfunc()
                                        ConsoleOn="1"
                                        
                                
                                elif user_input == "add":
                                        num1 = float(input("Type first number:"))
                                        num2 = float(input("Type another number:"))
                                        log.append(ca)
                                        wrlfunc()
                                        res = str(num1 + num2)
                                        print("Result:" , res)
                                
                                elif user_input == "subtract":
                                        num1 = float(input("Type first number:"))
                                        num2 = float(input("Type another number:"))
                                        log.append(cs)
                                        wrlfunc()
                                        res=str(num1 - num2)
                                        print("Result:" , res)
                                
                                elif user_input == "multiply":
                                        num1 = float(input("Type first number:"))
                                        num2 = float(input("Type another number:"))
                                        log.append(cm)
                                        wrlfunc()
                                        res = str(num1 * num2)
                                        print("Result:" , res)
                                
                                elif user_input == "divide":
                                        num1 = float(input("Type first number:"))
                                        num1 = float(input("Type another number:"))
                                        log.append(cd)
                                        wrlfunc()
                                        res = str(num1 / num2)
                                        print("Result:" , res)
                                else:
                                        log.append(e2)
                                        wrlfunc()
                                        print("Unknown input.")
                                
                        except ZeroDivisionError:
                                print("Cannot divide by zero.")
                                
                while ConsoleOn=="3":
                        print("FileEditor v1:")
                        print("Commands:")
                        print(prf+"_r - Read file in reading mode")
                        print(prf+"_w(Not Working Now) - Edit file in writing mode(Needs administrator permessions!)")
                        print(prf+"_q - Quit")
                        print(prf+"_prf - set new prefix and rewrite this prefix: ",prf)
                        file_ed=input("{FileEditor_v1}>>>")
                        if file_ed==prf+"_prf":
                                log.append(f1)
                                wrlfunc()
                                prf=input("Set your new prefix:")
                        
                        if file_ed==prf+"_q":
                                log.append(foff)
                                wrlfunc
                                ConsoleOn="1"
                        
                        if file_ed==prf+"_r":
                                log.append(f2)
                                wrlfunc()
                                file=input("Type filename:")
                                try:
                                        fileedit=open(file,"r")
                                        f = fileedit.read()
                                        print("File data:")
                                        print(f)
                                        fileedit.close()
                                except FileNotFoundError:
                                        print("ERROR:Invalid file name.")
                        elif file_ed==prf+"_w":
                                log.append(f3)
                                wrlfunc()
                                filew=input("Type File Name:")
                                try:
                                        print("You want to rewrite this file?")
                                        feinp = input("Yes/No:")
                                        inputsw="1"
                                        while inputsw=="1":
                                                if feinp=="Yes" or feinp=="YES" or feinp=="yes":
                                                        print("OK")
                                                        fileeditw=open(filew,"w+")
                                                        dataa=fileeditw.read()
                                                        fewf=input("Type data to rewrite file:")
                                                        fw = fileeditw.write(fewf) 
                                                        inputsw="0"
                                                        fileeditw.close()
                                                elif feinp=="No" or feinp=="NO" or feinp=="no":
                                                        print("Okay :)")
                                                        inputsw="0"
                                                else:
                                                        print("Unknown Input")
                                except FileNotFoundError:
                                        print("ERROR")            
                        else:
                                log.append(e3)
                                print("Unknown Input")
                                wrlfunc()
                                                       
                        

while langsys=="Ru/Ru":
        print(Back.BLACK)
        print(Fore.WHITE) 
        while ConsoleOn=="0" and langsys=="Ru/Ru":
                print("Включите или выключите консоль командами 'ON' или 'OFF' ")
                Console=input("ON/OFF:>>>")
                if Console=="ON" :
                        print("Перед началом работы с консолью,Пожалуйста,зайдите в свой аккаунт!")
                        print("Введите имя аккаунта и пароль от него")
                        acclogin=input("Имя:>>>")
                        if acclogin==adminacc:
                                print("Вы зашли как админ.Пожалуйста,введите пароль от аккаунта.")
                                accpass=input("Пароль:>>>")
                                if accpass==adminp:
                                        print("Готово!")
                                        NoLogin="N"
                                        ConsoleOn="1"
                                        break
                                else:
                                        print("Неправильный пароль.")
                        else:
                                print("Неизвестный аккаунт")
        
                elif Console=="OFF":
                        print("Выключение...")
                        log.append(off)
                        wrlfunc()
                        sys.exit()

                else:
                        print("Неизвестная команда")
        
        if NoLogin=="N" and langsys=="Ru/Ru":
                print("Сделано KrutosVIP и Zazio на Python.")
                print("Библеотеки:sys,time,this,os,datetime,colorama")
                print("Это консоль PyT v1!")
                print(time.ctime())
                print("Чтобы увидеть известные команды,введите 'помощь'")
        while True:
                while ConsoleOn=="1"  and langsys=="Ru/Ru":
                        user_input=input("|>>>")
                        if user_input=="помощь":
                                print("Сейчас доступны команды:")
                                print("помощь - Выводит это.")
                                print("версия - Выводит версию консоли")
                                print("время - Время")
                                print("лвремя -Локальное время")
                                print("вывод -  Выводит то,что вы напишете")
                                print("выкл - Выключить консоль")
                                print("автор - Выводит автора консоли")
                                print("калк - Считайте то,что хотите")
                                print("это  - (ИНФОРМАЦИЯ УДАЛЕНА)")
                                print("эдитор - запускает FileEditor")
                                if license=="2":
                                        print("акки  - аккаунты(Not working now)")
                                log.append(pt1)
                                wrlfunc()
                                
                        elif user_input == "версия":
                                print("Версия-v.1.1 Language update PRE-RELEASE :З")
                                print("Done on Python 3.6.4")
                                log.append(pt2)
                                wrlfunc()
                                
                        elif user_input == "время":
                                print(time.strftime("Today is %B %d, %Y.", time.localtime()))
                                log.append(pt3)
                                wrlfunc()
                                
                        elif user_input == "лвремя":
                                print(time.localtime())
                                log.append(pt4)
                                wrlfunc()
                                
                        elif user_input == "вывод":
                                d_print = input("Напишите слова,которые хотите вывести:")
                                print(d_print)
                                log.append(pt5)
                                wrlfunc()
                                
                        elif user_input == "это":
                                import this
                                print(this.s)
                                log.append(pt6)
                                wrlfunc()
                        
                        elif user_input == "выкл":
                                print("Спасибо за использование консоли")
                                ConsoleOn="0"
                                log.append(off)
                                deinit()
                                exfunc()
                                
                        elif user_input=="акки" and license=="2":
                                print("Желаете создать новый аккаунт?(NWN)")
                                ainp1=input("Да/Нет:")
                                if ainp1=="Да":
                                        an=input("Имя аккаунта:")
                                        ap=input("Пароль аккаунта:")
                                log.append(ptd1)
                                wrlfunc()
                                
                        elif user_input == "автор":
                                print("Автор консоли - KrutosVIP(Я ГЛАВА),Zazio")
                                log.append(pt7)
                                wrlfunc()
                                
                        elif user_input == "калк":
                                print("Включение калькулятора")
                                ConsoleOn = "2"
                                log.append(pt8)
                                wrlfunc()
                        
                        elif user_input == "эдитор":
                                print("Включение FileEditor v1...")
                                ConsoleOn="3"
                                log.append(pt9)
                                wrlfunc()
                                                                
                        else:
                                print("Неизвестная команда.Если вы хотите увидеть доступные команды ,введите 'помощь'.")
                                log.append(e1)
                                wrlfunc()
                                
                while ConsoleOn=="2" :
                        print("Опции:")
                        print("Введите 'добавить' чтобы сложить два числа")
                        print("Введите'вычесть' чтобы вычесть два числа")
                        print("Введите 'умножить'чтобы умножить два числа")
                        print("Введите 'разделить'чтобы разделить два числа")
                        print("Введите 'выйти' чтобы закончить работу с калькулятором.")
                        user_input = input(">")
                        try:
                                if user_input == "выйти":
                                        log.append(coff)
                                        ConsoleOn="1"
                                
                                elif user_input == "добавить":
                                        num1 = float(input("Введите первое число:"))
                                        num2 = float(input("Введите второе число:"))
                                        res = str(num1 + num2)
                                        log.append(ca)
                                        wrlfunc()
                                        print("Результат:" , res)
                                
                                elif user_input == "вычесть":
                                        num1 = float(input("Введите первое число:"))
                                        num2 = float(input("Введите второе число:"))
                                        res=str(num1 - num2)
                                        log.append(cs)
                                        wrlfunc()
                                        print("Результат:" , res)
                                
                                elif user_input == "умножить":
                                        num1 = float(input("Введите первое число:"))
                                        num2 = float(input("Введите второе число:"))
                                        res = str(num1 * num2)
                                        log.append(cm)
                                        wrlfunc()
                                        print("Результат:" , res)
                                
                                elif user_input =="разделить":
                                        num1 = float(input("Введите первое число:"))
                                        num1 = float(input("Введите второе число:"))
                                        res = str(num1 / num2)
                                        log.append(cd)
                                        wrlfunc()
                                        print("^_^,Результат:" , res)
                                        
                                else:
                                        log.append(e2)
                                        wrlfunc()
                                        print("Неизвестный ввод :с")
                                
                        except ZeroDivisionError:
                                print("На ноль делить нельзя :с")
                                
                while ConsoleOn=="3":
                        print("FileEditor v1:")
                        print("Команды:")
                        print(prf+"_r - Прочитать файл в режиме чтения")
                        print(prf+"_w - Изменить файл в режиме записи(НЕОБХОДИМ АДМИН)")
                        print(prf+"_q - Выйти")
                        print(prf+"_prf - установить новый префикс,заместо ",prf)
                        file_ed=input("{FileEditor_v1_prf}>>>")

                                
                        if file_ed==prf+"_prf":
                                log.append(f1)
                                prf=input("Поставте свой новый префикс:")
                                wrlfunc()
                        
                        elif file_ed==prf+"_q":
                                ConsoleOn="1"
                                log.append(foff)
                                wrlfunc()
                                

                        elif file_ed==prf+"_r":
                                log.append(f2)
                                wrlfunc()
                                filee=input("Введите имя файла:")
                                try:
                                        fileedit=open(filee,"r")
                                        f = fileedit.read()
                                        print("Данные файла:")
                                        print(f)
                                        fileedit.close()
                                except FileNotFoundError:
                                        print("ERROR:Имя файла не правильное")

                        elif file_ed==prf+"_w":
                                log.append(f3)
                                wrlfunc()
                                filew=input("Введите имя файла(Не забудьте расширение файла :З):")
                                try:
                                        print("Вы точно хотите изменить файл?")
                                        feinp = input("Да/Нет:")
                                        inputsw="1"
                                        while inputsw=="1":
                                                if feinp=="Да" or feinp=="ДА" or feinp=="да":
                                                        print("OK")
                                                        fileeditw=open(filew,"w+")
                                                        dataa=fileeditw.read()
                                                        fewf=input("Ввод данных в файл:")
                                                        fw = fileeditw.write(fewf) 
                                                        inputsw="0"
                                                        fileeditw.close()
                                                elif feinp=="Нет" or feinp=="НЕТ" or feinp=="нет":
                                                        print("Хорошо,ввода не будет")
                                                        inputsw="0"
                                                else:
                                                        print("Неизвестный ввод") 
                                except FileNotFoundError:
                                        print("ERROR")
                        else:
                                log.append(e3)
                                print("Неизвестный ввод.")
                        
    

         
        
