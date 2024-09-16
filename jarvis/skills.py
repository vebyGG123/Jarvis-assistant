##############
#			 #
#	 VEBY	 #
#	JARVIS	 #
#			 #
##############



import webbrowser, os, subprocess, pyautogui, sys

from pygame import mixer
from audio import collection_audio
from random import randint
from subprocess import call
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from convector import convertStrInt



def ValumeZvyk(digit: float):
	device = AudioUtilities.GetSpeakers()
	interface = device.Activate(
		IAudioEndpointVolume._iid_,
		CLSCTX_ALL, None,
	)
	valume = cast(interface, POINTER(IAudioEndpointVolume))
	valume.SetMasterVolumeLevelScalar(digit, None)


def speaker():
	name_audio = collection_audio[randint(0, len(collection_audio)-1)]
	mixer.init()
	mixer.music.load(name_audio)
	mixer.music.play()

def browser():
	webbrowser.open("https://www.google.com", new=3)

def youtube():
	webbrowser.open("https://www.youtube.com/", new=3)

def vk():
	webbrowser.open("https://vk.com/vebyx", new=3)

def gratitude():
	speaker()

def goodMorning():
	mixer.init()
	mixer.music.load(r"F:\jarvis\audio/dobroe-utro.wav")
	mixer.music.play()

def howAreYou():
	mixer.init()
	mixer.music.load(r"F:\jarvis\audio/my-podkljucheny-i-gotovy.wav")
	mixer.music.play()

def switch():
	pyautogui.press("nexttrack")

def back():
	pyautogui.press("prevtrack")

def pause():
	pyautogui.press("playpause")

def openRedactor():
	path = "C:/Users/veby/Desktop/"
	name = path + "Sublime Text"
	os.startfile(name)

def openProject():
	path = "C:/Users/veby/Desktop/"
	name = path + "Proekti"
	os.startfile(name)

def openPerevodchik():
	webbrowser.open("https://translate.yandex.ru", new=3)

def offPk():
	call(["shutdown", "/s", "/t", "0"])
	os.system("shutdown now -h")

def pogoda():
	path = r"F:\jarvis\modyleJarvis\Pogoda\main.py"
	call(["python", path])

def generatePassworld():
	path = r"F:\jarvis\modyleJarvis\GeneratePassworld\main.py"
	call(["python", path])

def generateEmail():
	path = r"F:\jarvis\modyleJarvis\GenerateEmail\main.py"
	call(["python", path])

def setValumeZvyk(data: str):
	lenght = len(data.split())
	strValue = data.split()[lenght-2:]
	res = ""
	count = 0

	if len(strValue) == 2:
		for i in strValue:
			res += i
			count += 1
			if count != 2:
				res += " "

	count = 0
	floatRes = convertStrInt(res)
	ValumeZvyk(floatRes)

def calculator():
	path = r"F:\jarvis\modyleJarvis\Calculator\main.py"
	call(["python", path])

def sokrotUrl():
	path = r"F:\jarvis\modyleJarvis\SokratitelUrl\main.py"
	call(["python", path])

def openCMD():
	name =  r"C:\Windows\System32\cmd.exe"
	os.startfile(name)

def openProvodnik():
	name = r"C:\Windows\explorer.exe"
	os.startfile(name)

def pushSms():
	path = r"F:\jarvis\modyleJarvis\PushSms\main.py"
	call(["python", path])

def openUrlPotcha():
	webbrowser.open("https://mail.ru/", new=3)


