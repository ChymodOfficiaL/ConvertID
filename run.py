# -*- coding: utf-8 -*-
# with traodoisub.com
# coded by ChymodOfficiaL

import sys, os, time, json
import requests, platform, random
from time import sleep

class LOGIN:
   
   def __init__(self) -> True:
       self.ses = requests.Session()
       self.Scrape() 

   def terminalClear(self, platform):
       if "linux" in sys.platform.lower():os.system("clear")
       elif "win" in sys.platform.lower():os.system("cls")
       
   def delay(self):
       text = [" [!] CONVERT ID..", " [!] CONVERT ID...", " [!] CONVERT ID....\n" ]
       for xyz in text:
           print(f'\r{xyz}                ', end='\r')
           sleep(1)
   
   def Text(self):
       print('\n\n [+] ALAT UNTUK CONVERT ID FACEBOOK\n [+] ID FACEBOOK, ID HALAMAN, ID POST\n')
   
   def Scrape(self):
       self.terminalClear(platform) ; self.Text()
       xyr = input(' [+] URL -Fb : ') ; self.delay()
       try:
           headers = {
              "Host": "id.traodoisub.com",
              "user-agent": "Mozilla/5.0 (Linux; Android 13; Infinix X6528B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.7049.99 Mobile Safari/537.36",
              "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
              "accept-encoding": "gzip, deflate, br, zstd",
              "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
           }
           data = {
              "link": xyr
           }
           resp = self.ses.post("https://id.traodoisub.com/api.php",headers = headers, data = data).json()
           if "success" in resp:
              uid = resp["id"]
              she = resp["share_type"]
              co = resp["code"]
              print(f"\n [+] UID : {uid}\n [+] TYPE : {she}\n [+] CODE : {co}")
              input("\n [+] KEMBALI") ; self.Scrape()
           else:
              sys.exit(" [!] Link Invalid           ")

       except Exception as e:
           sys.exit(f" [!] ERROR: {str(e).capitalize()}")
       


if __name__=='__main__':
  try:
      os.system('git pull') ; LOGIN()
  except Exception as e:
      sys.exit(f" [!] ERROR: {str(e).capitalize()}")    