import datetime
import os
import sys
import time
import colorama
import sounddevice as sd
from scipy.io.wavfile import write
from speech_engine import casper_speak
from message_functions import casper_alert
from colorama import Fore, Back
colorama.init(autoreset=True)


date = datetime.datetime.now().strftime(f"%h{'('}%d{')'}:%H:%M")
txt_file = str(date).replace(":", "-") + "-Log.txt"
audio_file = str(date).replace(":", "-") + "-Audio.wav"

folder = "Activity Logs"
save_txt_file = os.path.join(folder, txt_file)
save_wav_file = os.path.join(folder, audio_file)

def chronicle_log(write, var):
    if var == 0:
        print_save = sys.stdout
        f = open(save_txt_file, 'a', encoding="utf-8")
        sys.stdout = f
        y = write
        print(y)
        sys.stdout = print_save
        f.close()

    elif var == 1:
        print_save = sys.stdout
        f = open(save_txt_file, 'a', encoding="utf-8")
        sys.stdout = f
        y = write
        pass
        sys.stdout = print_save
        f.close()


def chronicle_audio(voice_var, log):
    print(Fore.RED + "<< ACTIVATED CHRONICLE AUDIO MODE >>".center(100))
    print(Fore.YELLOW + "(●) Recording".center(100))
    chronicle_log(Fore.YELLOW + "(●) Recording".center(100), var=log)
    casper_speak(speak="ACTIVATED CHRONICLE AUDIO MODE", voice=voice_var)
    chronicle_log(Fore.RED + "<< ACTIVATED CHRONICLE AUDIO MODE >>".center(100), var=log)
    casper_alert("ACTIVATED CHRONICLE AUDIO MODE")

    frequency = 44100
    duration = 60
    record_audio = sd.rec(int(duration * frequency), samplerate=frequency, channels=2)
    sd.wait()
    write(save_wav_file, frequency, record_audio)

    print(Fore.GREEN + "Recoding audio completed".center(100))
    chronicle_log(Fore.GREEN + "Recording audio completed".center(100), var=log)
    casper_speak(speak="Recording audio completed", voice=voice_var)
    casper_alert("CHRONICLE AUDIO MODE STOPPED")


def clean_slate(voice_var):
    print(Fore.RED + "<< INITIATING CLEAN SLATE PROTOCOL >>".center(100))
    casper_speak(speak="INITIATING CLEAN SLATE PROTOCOL", voice=voice_var)
    casper_alert("INITIATING CLEAN SLATE PROTOCOL")

    mydir = "Activity Logs"
    txtfiles = [f for f in os.listdir(mydir) if f.endswith(".txt")]
    wavfiles = [f for f in os.listdir(mydir) if f.endswith(".wav")]
    for f in txtfiles:
        os.remove(os.path.join(mydir, f))
    for f in wavfiles:
        os.remove(os.path.join(mydir, f))
        
    time.sleep(1)
    print(Fore.GREEN + "All activity log files has been deleted".center(100))
    casper_speak(speak="All activity log files has been deleted", voice=voice_var)
    casper_alert("ALL ACTIVITY LOG FILES HAS BEEN DELETED")