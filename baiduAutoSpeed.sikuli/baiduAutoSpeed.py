# coding=utf-8
from threading import Thread

RetryTimer = 1*30
SuccessWaitTimer = 25*60

waitingForTwoAmTimer = 10

GOODHOUR = 2
GOODMIN = 0


   
def tryToClickTransferButton():
   try:   
      click("transferButton.png")
      print 'Clicked! transfer button'

   except:
      print 'transfer button not found '
   time.sleep(2)

def tryToClickTryHighSpeedButton():
   try:        
      click("highSpeedButton.png")  
      print 'Clicked! High Speed button!'
     
   except:
      print 'High Speed button not found '           
   time.sleep(2)

def deepSleepIfSuccess():
   try:
     wait("successButton.png")
     print 'Already FAST SPEED! Deep sleep ' + str(SuccessWaitTimer)+' seconds'
     time.sleep(SuccessWaitTimer)  # deep sleep if success    
   except:
     print 'Success button not found?'          
   time.sleep(2)
    

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

click("1447335357440.png")

def automationBaiduCloudSpeed():
   i =0
    
   
   while True:

      if(i%3==0):   
         tryToClickTransferButton()
         
      tryToClickTryHighSpeedButton()

      # if you see "success button then just deep sleep!
      deepSleepIfSuccess()
      
      if (i>5000):
         i=0
      i=i+1
      print 'sleeping for ' +  str(RetryTimer) +' seconds and retry '+ str(i)
      time.sleep(RetryTimer)





def main():
     

      
   automationBaiduCloudSpeed()
    
         

# switchApp(u"欢迎使用百度云管家")
   #openApp(u"欢迎使用百度云管家")
   #wait_and_click_transferButton()
   #wait_and_click_try_highspeed_button()
   #wait_and_click_this_button_or_that()

   

main()

