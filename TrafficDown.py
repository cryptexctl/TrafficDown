# Пытался сократить код, из-за этого пишет дохуя "ошибок" с неизвестными функциями, не переживайте, скрипт запускается без проблем!!
# Почему не юзаю CustomTkinter, если система не винда: мне пишет ошибку на андроиде, связанную с customtkinter да и похуй мне кажется мне лень тестировать заново мб нет ошибки похуй мне лень тестировать

import os

class threading:...
class tkinter:...
class requests:...
# чтобы VSC не писал, мол, модулей нет

packages = ['requests', 'tkinter', 'threading', 'customtkinter']
for package in packages: 
 installed = True
 exec(f'try:import {package}\nexcept:installed=False') # лучшее решение, которое я нашел
 if not installed:
  os.system(f'python -m pip install {package}') # добавьте --break-system-packages если надо хотя нахуй хз
  if os.name == 'nt' and package == 'customtkiner': os.system(f'python -m pip install {package}') # добавьте --break-system-packages если надо хотя нахуй хз
  if package != 'tkinter' and package == 'customtkiner':exec(f'import {package}')

eat = False

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
    text = f'Кушаем...\nПрочитано {round(readed/1024/1024,1)} МБ'
    print(text)
   
    if useTkinter:
     statuslbl.config(text=text) if os.name != 'nt' else statuslbl.configure(text=text) 
  except:...

def trafficDown():

 global eat, statuslbl, readed

 eat = True
 readed = 0
 
 print('Нажмите ENTER для остановки')
 
 for url in urls:
  
  threading.Thread(target=downloadThread, args=(url,)).start()
 
 if not useTkinter:
  input()
  eat = False

functions = [
 {'name':'traffic', 'description':'начать съедание трафика','handler':trafficDown},
 {'name':'exit','description':'выход','handler':lambda:os._exit(0)}
]

fg = '#008E63'
hover = '#225244'
bg = '#2B2B2B'

def startSpamTkinter():
  global eat, statuslbl
  if eat: 
    startbtn.config(text='Начать')
    statuslbl.config(text='Тут будет статус')
    eat=False
  else:
    startbtn.config(text='Остановить')
    eat = True
    trafficDown()

def startSpamCTkinter():
  global eat, statuslbl
  if eat: 
    startbtn.configure(text='Начать')
    statuslbl.configure(text='Тут будет статус')
    eat=False
  else:
    startbtn.configure(text='Остановить')
    eat = True
    trafficDown()

def checkWifi():
 try:
  r = requests.get('https://google.com')
  return True
 except: return False

while True:
 print('Проверяем доступ в интернет...')
 haveWifi = checkWifi()
 if haveWifi:break

try:
 from tkinter import *
 useTkinter = True
except: useTkinter = False

if useTkinter and os.name !='nt':
 window = Tk()
 window.title('TrafficDown | by Sonys9')
 window.geometry('300x125')
 window.protocol("WM_DELETE_WINDOW", lambda: os._exit(0))
 
 statuslbl = Label(window, text='Тут будет статус', font=('Arial Black', 13))
 statuslbl.pack()
 
 startbtn = Button(window, text='Начать', command=startSpamTkinter)
 startbtn.pack()
 
 window.mainloop()

if useTkinter and os.name =='nt':

  from customtkinter import *
  
  window = CTk()
  window.resizable(False, False)
  set_appearance_mode("dark")
  window.protocol("WM_DELETE_WINDOW", lambda: os._exit(0))
  window.title('TrafficDown | by Sonys9')
  window.geometry('300x130')

  CTkFrame(window, width=280, height=105).place(x=10,y=10)
  
  statuslbl = CTkLabel(window, text='Тут будет статус', font=('Arial Black', 13), bg_color=bg)
  statuslbl.place(relx=0.5, anchor='center', rely=0.25)

  CTkLabel(window, text='Github @Sonys9 | tt @взломщик | tg @freedomleaker2', font=('Arial Black', 8), bg_color=bg).place(x=35, y=108)
  
  startbtn = CTkButton(window, text='Начать', command=startSpamCTkinter, fg_color=fg, bg_color=bg, hover_color=hover)
  startbtn.place(x=85, y=70)
  
  window.mainloop()

else:
 print('Не удалось загрузить GUI. Используем терминальную версию.')
 while True:
  for function in functions:

   print(f'{function["name"]} - {function["description"]}')

  choice = input('Введите название функции:\t')
  
  for function in functions:
   if function['name'] == choice.lower().strip(): function['handler']()

