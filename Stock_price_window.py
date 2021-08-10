import threading
from tkinter import *
import requests
from bs4 import BeautifulSoup
import winsound
import time

window= Tk()
# Adjust Window Size According to your Desktop else you won't be able to see it... 
# window.geometry("220x160")
window.geometry("220x160+1700+850")
window.title('NSE Stocks')
window.configure(bg="#8B008B")
# window.lift()
# window.wm_iconbitmap('F:\\rated screener\\Auto wala.ico')
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
# liss = [i for i in range(1,19)]
count = 0

print()

def yo(name,alert1 = None):
	# global count
	# if alert1:
	l2 = Label(window,text = name,font = ('LED',18,'bold'))
	l2.place(x = 0,y = 0)
	global count
	window.update()
	window.attributes('-topmost',True)
	l1 = Label(window,text = ' ',font = ('LED',18,'bold'))
	l1.place(x = 50,y = 50)
	# l1.pack(side = TOP)
	url = f'https://query1.finance.yahoo.com/v8/finance/chart/{name}.NS'
	d = requests.get(url, headers = header)
	data = d.json()
	latest = data['chart']['result'][0]['indicators']['quote'][0]['close'][-1]
	if latest == None:
	    latest = data['chart']['result'][0]['indicators']['quote'][0]['close'][-2]

	l1 = Label(window,text = round(latest,3),font = ('LED',22,'bold'))
	# l1 = Label(window,text = i,font = ('LED',18,'bold'))
	l1.place(x = 40,y = 60)

	exit_button = Button(window, text="quit", font=("arial 10 bold"),fg="green",bg='red',command=window.destroy)
	exit_button.place(x = 60,y =120)
	# print(alert, 'alert')
	# print('latest type',type(latest),' alert type',type(alert))
	# if alert == True:
	# 	print('alert baja')

	# try:

	if alert1:
		alert = float(alert1[:-1])
		condition = alert1[-1]
		if condition == '-' and count<=2:
			if latest <=alert:
				# print('alert baja')
				# winsound.PlaySound('D:\\rated screener\\pi.wav',winsound.SND_LOOP)
				# winsound.PlaySound('D:\\GIT submitted\\negative_sound_alert.wav',winsound.SND_LOOP)
				winsound.PlaySound('negative_sound_alert.wav',winsound.SND_LOOP)
				count+=1
		else:
			if latest >= alert and count<=2:
				# print('alert baja jyada ke liye')
				# winsound.PlaySound('D:\\rated screener\\sai.wav',winsound.SND_LOOP)
				# winsound.PlaySound('D:\\GIT submitted\\positive_sound_alert.wav',winsound.SND_LOOP)
				winsound.PlaySound('positive_sound_alert.wav',winsound.SND_LOOP)
				count+=1

	# except:
	# 	pass

def yo1():
	time.sleep(1)



 



# l2 = Label(window,text = name,font = ('LED',18,'bold'))
# l2.pack(side= TOP)
# root = Tk()
# root.geometry('800x100')
# root.configure('')


for i in range(500):

	threading.Thread(target=yo1).start()
	yo(name = 'HDFCBANK',alert1 = '1490+')
	# yo(name = 'ASIANPAINT',alert1 = '2990+')
	# yo(name = 'HCLTECH',alert1 = "970-")
	# yo(alert1 = '')
	# yo(alert1 = '1515+')


	# yo()
	time.sleep(5)
	# try:
