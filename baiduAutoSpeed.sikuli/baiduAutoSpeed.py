# coding=utf-8
from threading import Thread

RetryTimer = 4 #*10
SuccessWaitTimer = 5#25*6

   
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
     print 'Already FAST SPEED! Deep sleep'       
     time.sleep(SuccessWaitTimer)  # deep sleep if success    
   except:
     print 'Success button not found?'          
   time.sleep(2)
    

      
def wait_and_click_this_button_or_that():
   i =0

   while True:
      if(i%5==0):   
         try:   
            click("transferButton.png")
            print 'Clicked! transfer button'
            time.sleep(2)
         except:
            print 'transfer button not found '+ str(i)
            time.sleep(2)

      try:        
         click("highSpeedButton.png")  
         print 'Clicked! High Speed button!'
     
      except:
         print 'High Speed button not found '+ str(i)
      
      
      time.sleep(2)

      
      # if you see "success button then just deep sleep!
      try:
        wait("successButton.png")
       
        print 'Already FAST SPEED! Deep sleep'       
        time.sleep(SuccessWaitTimer)
         
      except:
         print 'Success button not found?'          
      if (i>5000):
         i=0
      i=i+1
      print 'sleeping for 60 seconds and retry'
      time.sleep(RetryTimer)



def automationBaiduCloudSpeed():
   i =0
    
   while True:
      if(i%5==0):   
         tryToClickTransferButton()
         
      tryToClickTryHighSpeedButton()

      # if you see "success button then just deep sleep!
      deepSleepIfSuccess()
      
      if (i>5000):
         i=0
      i=i+1
      print 'sleeping for 60 seconds and retry '+ str(i)
      time.sleep(RetryTimer)





def main():
     
   
   automationBaiduCloudSpeed()
    
         

# switchApp(u"欢迎使用百度云管家")
   #openApp(u"欢迎使用百度云管家")
   #wait_and_click_transferButton()
   #wait_and_click_try_highspeed_button()
   #wait_and_click_this_button_or_that()

   

main()

