# Пытался сократить код, из-за этого пишет много "ошибок" с неизвестными функциями, не переживайте, скрипт запускается без проблем!!
# Ответ на вопрос, почему тут пробелы вместо табов встречаются: я начинал делать на телефоне, а там табы не поставишь, вот по этому пробелы и использовал, ведь с ними точно также

import os
import time
import sys
import importlib.util

class threading:...
class tkinter:...
class requests:...
class colorama:...
class socket:...
# чтобы VSC не писал, мол, модулей нет

packages = ["requests", "tkinter", "threading", "customtkinter"]
for package in packages:
    installed = importlib.util.find_spec(package)
    if not installed:
      os.system(f"python -m pip install {package}")
      importlib.util.find_spec(package)

if int(sys.version.split(' ')[0].split('.')[1])<13: 
  input('Для запуска скрипта обновите Python до версии 3.13 и выше!')
  os._exit(0)

eat = False
killwifi = False

urls = [
'https://speedtest.rastrnet.ru/1GB.zip',

'https://speedtest.rastrnet.ru/500MB.zip',

'https://speedtest.selectel.ru/10GB',

'https://speedtest.selectel.ru/1GB',

] # большие файлы

def downloadThread(url):
	
 global eat, statuslbl, readed
 while eat:

  try:
   r = requests.get(url, stream=True, timeout=3)
   chunkSize = 5024000
   for chunk in r.iter_content(chunk_size=chunkSize): 
    if not eat: break
    #print(len(chunk))
    readed+=len(chunk)
    text = f'Прочитано {round(readed/1024/1024,1)} МБ'
    print(f'{" "*(x//2-len(text)//2)}{text}')
   
    if useTkinter:statuslbl.configure(text=text) 
  except:...

logo = '''████████╗██████╗░░█████╗░███████╗███████╗██╗░█████╗░██████╗░░█████╗░░██╗░░░░░░░██╗███╗░░██╗
╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██╔════╝██║██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║████╗░██║
░░░██║░░░██████╔╝███████║█████╗░░█████╗░░██║██║░░╚═╝██║░░██║██║░░██║░╚██╗████╗██╔╝██╔██╗██║
░░░██║░░░██╔══██╗██╔══██║██╔══╝░░██╔══╝░░██║██║░░██╗██║░░██║██║░░██║░░████╔═████║░██║╚████║
░░░██║░░░██║░░██║██║░░██║██║░░░░░██║░░░░░██║╚█████╔╝██████╔╝╚█████╔╝░░╚██╔╝░╚██╔╝░██║░╚███║
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░╚═╝░╚════╝░╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝░░╚══╝'''
logoweight = 91

def trafficDown():

 global eat, statuslbl, readed

 eat = True
 readed = 0
 text = 'Нажмите ENTER для остановки'
 
 for url in urls:
  
  threading.Thread(target=downloadThread, args=(url,)).start()
 
 if not useTkinter:
  print(f'{" "*(x//2-len(text)//2)}{text}')
  input()
  eat = False

def sendpackets():
 global killwifi
 while killwifi:
  try:threading.Thread(target=makepacket).start()
  except:...

def killWifiF():
  global killwifi
  killwifi = True
  text = 'Нажмите ENTER для остановки'
  if not useTkinter:
    print(f'{" "*(x//2-len(text)//2)}{text}')
    threading.Thread(target=sendpackets).start()
    input()
    killwifi = False

functions = [
 {'name':'traffic', 'description':'начать съедание трафика','handler':trafficDown},
 {'name': 'wifikill', 'description':'убить интернет','handler':killWifiF},
 {'name':'exit','description':'выход','handler':lambda:os._exit(0)}
]

fg = '#008E63'
hover = '#225244'
bg = '#2B2B2B'

def startEatCTkinter():
  global eat, statuslbl
  if eat: 
    startbtn.configure(text='Начать')
    statuslbl.configure(text='Тут будет статус')
    eat=False
  else:
    startbtn.configure(text='Остановить')
    eat = True
    trafficDown()

def startKillCTkinter():
  global killwifi
  if killwifi: 
    killwifibtn.configure(text='Начать')
    killwifi=False
  else:
    killwifibtn.configure(text='Остановить')
    killwifi = True
    while killwifi: 
     try:threading.Thread(target=makepacket).start()
     except:...

#def checkWifi():
# try:
#  r = requests.get('https://google.com')
 # return True
 #except: return False

#while True:
# print(f'{colorama.Fore.CYAN}Проверяем доступ в интернет...{colorama.Fore.WHITE}')
# haveWifi = checkWifi()
# if haveWifi:break
# else:print(f'{colorama.Fore.RED}Доступ к интернету не обнаружен, пробуем снова...{colorama.Fore.WHITE}') 

try:
 from tkinter import *
 useTkinter = True
except: useTkinter = False

#useTkinter = False

#if useTkinter and os.name =='nt':
size = os.get_terminal_size()
x,y = size.columns,size.lines

def makepacket():
  global killwifi
  if killwifi: #доп. проверка на всякий случай
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
      s.connect(('8.8.8.8', 443)) 
      s.close()
    except:... # оно срет ошибками

def addwidjets():
 
 global startbtn, statuslbl, killwifibtn
 
 screen_width = window.winfo_width()
 screen_height = window.winfo_height()

 CTkFrame(window, width=screen_width-20, height=screen_height-20).place(x=10,y=10)

 statuslbl = CTkLabel(window, text='Тут будет статус', font=('Arial Black', 13), bg_color=bg)
 statuslbl.place(relx=0.5, anchor='center', rely=0.25)

 CTkLabel(window, text='Github @Sonys9 | tt @взломщик | tg @freedomleaker2', font=('Arial Black', 8), bg_color=bg).place(x=screen_width//2-120, y=screen_height-20)
  
 startbtn = CTkButton(window, text='Есть трафик', command=startEatCTkinter, fg_color=fg, bg_color=bg, hover_color=hover)
 startbtn.place(relx=0.5, anchor='center', rely=0.55)

 killwifibtn = CTkButton(window, text='Убить интернет', command=lambda:threading.Thread(target=startKillCTkinter).start(), fg_color=fg, bg_color=bg, hover_color=hover)
 killwifibtn.place(relx=0.5, anchor='center', rely=0.75)

 

if useTkinter:

  from customtkinter import *
  
  window = CTk()
  window.resizable(False, False)
  set_appearance_mode("dark")
  window.protocol("WM_DELETE_WINDOW", lambda: os._exit(0))
  window.title('TrafficDown | by Sonys9')
  window.geometry('300x170')

  window.after(200, addwidjets)
  
  window.mainloop()

else:
 print(f'{colorama.Fore.RED}Не удалось загрузить GUI. Используем терминальную версию.{colorama.Fore.WHITE}')
 time.sleep(2)

 while True:

  os.system('cls' if os.name == 'nt' else 'clear')

  size = os.get_terminal_size()
  x,y = size.columns,size.lines
  if x>=91:
    print(f'{colorama.Fore.WHITE}{"\n".join([" "*(x//2-logoweight//2)+line for line in logo.split("\n")])}')
  else:
    text = f'{colorama.Fore.WHITE}(увеличь окно или уменьши размер текста)'
    print(f'{" "*(x//2-len(text)//2)}{text}')

  num_of_functions = len(functions)

  for function in functions:
   
   text = f'{colorama.Fore.WHITE}[{colorama.Fore.CYAN}{function["name"]}{colorama.Fore.WHITE}] - {function["description"]}'
   print(f'{" "*(x//2-len(text)//2+6)}{text}')

  text = 'Введите название функции:\t'
  choice = input(f'{" "*(x//2-len(text)//2)}{text}{colorama.Fore.GREEN}')
  
  for function in functions:
   if function['name'] == choice.lower().strip(): function['handler']()
