import sys
def MNFENC():
		print("..................................................................")
		print("..................................................................")
		print("..............................Error...............................")
		print("..................................................................")
		print("..................................................................")
		print("......................Module Not Found ERROR.......................")
		print("..................................................................")
		print("..................................................................")
		print("..................................................................")
		sys.exit()
try:
	import colorama
	from colorama import init,deinit
	from colorama import Fore, Back, Style
	init()
except ModuleNotFoundError:
	print("Module 'colorama' not found.")
	MNFENC()
else:
	print("Module 'colorama' imported!")
def MNFE():
		print(Back.BLUE)
		print(Fore.WHITE)
		print("..................................................................")
		print("..................................................................")
		print("..............................Error...............................")
		print("..................................................................")
		print("..................................................................")
		print("......................Module Not Found ERROR......................")
		print("..................................................................")
		print("..................................................................")
		print("..................................................................")
		print(Style.RESET_ALL)
		deinit()
		sys.exit()
try:
	import time
except ModuleNotFoundError:
	print("Мodule 'time' not found. ")
	MNFE()
try:		
	import os
except ModuleNotFoundError:
	print("Мodule 'os' not found. ")
	MNFE()
try:		
	import this
except ModuleNotFoundError:
	print("Мodule 'this' not found. ")
	MNFE()
try:		
	import datetime
except ModuleNotFoundError:
	print("Мodule 'datetime' not found. ")
	MNFE()
print(Style.RESET_ALL)

def bfunx():
		print(Fore.RED)
		print("Stopping the setup...")
		sys.exit()
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
                        bfunx()

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
                except FileNotFoundError:
                        print(Back.RED)
                        print(Fore.WHITE) 
                        print("CRITICAL ERROR (FNF):STOPPING PROGRAM!!!")
                        print("If you delete directory 'propertiesconsole' ,please,create it and then,try one more time.")
                        sys.exit()
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
                                print("editor - activating FileEditor." )
                                
                        elif user_input == "version":
                                print("Version of PyT-v.1.0 Language update :)")
                                print("Done on Python 3.6.4")
                                
                        elif user_input == "time":
                                print(time.strftime("Today is %B %d, %Y.", time.localtime()))
                                
                        elif user_input == "ltime":
                                print(time.localtime())
                                
                        elif user_input == "print":
                                d_print = input("Write words what you want to print in console")
                                print(d_print)
                                
                        elif user_input == "toff":
                                print("Thank you  for usage of our console")
                                deinit()
                                sys.exit()
                                
                        elif user_input == "author":
                                print("The authors of console is KrutosVIP(I AM A GLAVA BLIN) and Zazio")
                                
                        elif user_input == "calc":
                                print("Activating calculator")
                                ConsoleOn = "2"
                                
                        elif user_input == "this":
                                print(this.s)
                                
                        elif user_input == "editor":
                                print("Activating FileEditor v1...")
                                ConsoleOn="3"
                                        
                        else:
                                print("INVALID COMMAND.If you want to see available commands ,type 'help'.")
                                
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
                                        ConsoleOn="1"
                                        break
                                
                                elif user_input == "add":
                                        num1 = float(input("Type first number:"))
                                        num2 = float(input("Type another number:"))
                                        res = str(num1 + num2)
                                        print("Result:" , res)
                                
                                elif user_input == "subtract":
                                        num1 = float(input("Type first number:"))
                                        num2 = float(input("Type another number:"))
                                        res=str(num1 - num2)
                                        print("Result:" , res)
                                
                                elif user_input == "multiply":
                                        num1 = float(input("Type first number:"))
                                        num2 = float(input("Type another number:"))
                                        res = str(num1 * num2)
                                        print("Result:" , res)
                                
                                elif user_input == "divide":
                                        num1 = float(input("Type first number:"))
                                        num1 = float(input("Type another number:"))
                                        res = str(num1 / num2)
                                        print("Result:" , res)
                                else:
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
                                prf=input("Set your new prefix:")
                        
                        if file_ed==prf+"_q":
                                ConsoleOn="1"
                        
                        if file_ed==prf+"_r":
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
                                print("Unknown Input")                                          
                                      
                        

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
                                
                        elif user_input == "версия":
                                print("Версия-v.1.0 Language update :З")
                                print("Done on Python 3.6.4")
                                
                        elif user_input == "время":
                                print(time.strftime("Today is %B %d, %Y.", time.localtime()))
                                
                        elif user_input == "лвремя":
                                print(time.localtime())
                                
                        elif user_input == "вывод":
                                d_print = input("Напишите слова,которые хотите вывести:")
                                print(d_print)
                                
                        elif user_input == "это":
                                print(this.s)
                        
                        elif user_input == "выкл":
                                print("Спасибо за использование консоли")
                                
                                ConsoleOn="0"
                                deinit()
                                sys.exit()
                                
                        elif user_input=="акки" and license=="2":
                                print("Желаете создать новый аккаунт?(NWN)")
                                ainp1=input("Да/Нет:")
                                if ainp1=="Да":
                                        an=input("Имя аккаунта:")
                                        ap=input("Пароль аккаунта:")
                                
                        elif user_input == "автор":
                                print("Автор консоли - KrutosVIP(Я ГЛАВА),Zazio")
                                
                        elif user_input == "калк":
                                print("Включение калькулятора")
                                ConsoleOn = "2"
                        
                        elif user_input == "эдитор":
                                print("Включение FileEditor v1...")
                                ConsoleOn="3"
                                                                
                        else:
                                print("Неизвестная команда.Если вы хотите увидеть доступные команды ,введите 'помощь'.")
                                
                while ConsoleOn=="2" :
                        print("Опции:")
                        print("Введите '",prf2+"_добавить' чтобы сложить два числа")
                        print("Введите'",prf2+" _вычесть' чтобы вычесть два числа")
                        print("Введите '",prf2+"_умножить'чтобы умножить два числа")
                        print("Введите '",prf2+"_разделить'чтобы разделить два числа")
                        print("Введите '",prf2+"выйти' чтобы закончить работу с калькулятором.")
                        print("Введите '",prf2+"прф'' чтобы изменить префикс")
                        user_input = input(">")
                        try:
                                if user_input == prf2+"_выйти":
                                        ConsoleOn="1"
                                
                                elif user_input == prf2+"_добавить":
                                        num1 = float(input("Введите первое число:"))
                                        num2 = float(input("Введите второе число:"))
                                        res = str(num1 + num2)
                                        print("Результат:" , res)
                                
                                elif user_input == prf2+"_вычесть":
                                        num1 = float(input("Введите первое число:"))
                                        num2 = float(input("Введите второе число:"))
                                        res=str(num1 - num2)
                                        print("Результат:" , res)
                                
                                elif user_input == prf2+"умножить":
                                        num1 = float(input("Введите первое число:"))
                                        num2 = float(input("Введите второе число:"))
                                        res = str(num1 * num2)
                                        print("Результат:" , res)
                                
                                elif user_input ==prf2+"разделить":
                                        num1 = float(input("Введите первое число:"))
                                        num1 = float(input("Введите второе число:"))
                                        res = str(num1 / num2)
                                        print("^_^,Результат:" , res)
                                        
                                elif user_input==prf2+"_прф":
                                        prf2=input("Введите новый префикс команд калькулятора:")
                                        print("Готово!")
                                else:
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
                                prf=input("Поставте свой новый префикс:")
                        
                        elif file_ed==prf+"_q":
                                ConsoleOn="1"
                                

                        elif file_ed==prf+"_r":
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
                                print("Неизвестный ввод.")
                        
    

         
        
