# coding=utf-8
from threading import Thread
import time
import sys

ShortWaitTime  =4
RetryTimer = 1*30
SuccessWaitTimer = 30
waitForHalfHours = 1800
waitForOneHours = 3600
waitForFiveMinutes = 5*60
waitingForTwoAmTimer = 10

GOODHOUR = 2
GOODMIN = 0


   
def tryToClickTransferButton():
   try:  
      hover("transferButton.png")
      time.sleep(10)
      click("transferButton.png")
      print 'Clicked! transfer button'

   except:
      print 'transfer button not found '
   time.sleep(ShortWaitTime)

def tryToClickTryHighSpeedButton():
   try:
      hover("highSpeedButton.png")  
      time.sleep(ShortWaitTime)
      click("highSpeedButton.png")  
      print 'Clicked! High Speed button!'
     
   except:
      print 'High Speed button not found '           
   time.sleep(ShortWaitTime)

def deepSleepIfSuccess():
   try:
     wait("successButton.png")
     print 'Already FAST SPEED! Deep sleep ' + str(SuccessWaitTimer)+' seconds'
     time.sleep(SuccessWaitTimer)  # deep sleep if success    
   except:
     print 'Success button not found?'          
   time.sleep(ShortWaitTime)
    
def tryToClickDownloadingTab():
   try:
      hover("downloadingTab.png")
      time.sleep(ShortWaitTime)
      click("downloadingTab.png")
      print 'Clicked Downloading Tab'
   except:
     print 'Downloading tab not found?'   
   time.sleep(ShortWaitTime)
      
def isGoodDownloadTime():
    
   isgood = False
   timestruct = time.localtime()
      
   print timestruct
   print timestruct.tm_hour
   print timestruct.tm_min

   if (timestruct.tm_hour == Constant.HOUR and timestruct.tm_min<=Constant.MIN):
      print 'good time'
   else:
      print 'no good time'
   return False

#click("1447335357440.png")



def automationBaiduCloudSpeed():
   i =0
    
   
   while True:

        
      tryToClickTransferButton()

      tryToClickDownloadingTab()

      tryToClickTryHighSpeedButton()

      # if you see "success button then just deep sleep!
      deepSleepIfSuccess()
      
      if (i>5000):
         i=0
      i=i+1
      print 'sleeping for ' +  str(RetryTimer) +' seconds and retry '+ str(i)
      time.sleep(RetryTimer)





def main():
   while True:  
     timestruct = time.localtime()
     print timestruct
     if (timestruct.tm_hour== 23):
       print 'sleeping for one hour, long long time'
       time.sleep( waitForOneHours )  
     elif (timestruct.tm_hour== 0):
       print 'sleeping for half hour long long time'
       time.sleep( waitForHalfHours )  
     else:
       break
   automationBaiduCloudSpeed()
    
         

# switchApp(u"欢迎使用百度云管家")
   #openApp(u"欢迎使用百度云管家")
   #wait_and_click_transferButton()
   #wait_and_click_try_highspeed_button()
   #wait_and_click_this_button_or_that()

   

main()

