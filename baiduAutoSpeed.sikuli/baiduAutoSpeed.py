# coding=utf-8
from threading import Thread


def wait_and_click_transferButton( ):
   print 'waiting for transfer list button'
   for i in range(20):
      try:  
         click("transferButton.png")
         # not found is not a problem, if found, click and stop while loop.
         break
      except:  
         print 'transfer button not found, continue waiting ' + str(i)
      time.sleep(3)


def wait_and_click_try_highspeed_button( ):
   print 'waiting for try high speed button'
   
   i=0
   while True:  
      try:  
         click("highSpeedButton.png")       
         print 'Clicked! High Speed button'
         # not found is not a problem, if found, click and stop while loop.
      except:  
         print 'high speed button not found, continue waiting '+ str(i)
      time.sleep(60)
      i=i+1









      
def wait_and_click_this_button_or_that():
   i =0
   RetryTimer = 60 #*10
   SuccessWaitTimer = 25*60
   
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

      
def main():
     
      

# switchApp(u"欢迎使用百度云管家")
   #openApp(u"欢迎使用百度云管家")
   #wait_and_click_transferButton()
   #wait_and_click_try_highspeed_button()
   wait_and_click_this_button_or_that()

main()

