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
   RetryTimer = 6 #*10
   SuccessWaitTimer = 5#30*60
   
   while True:
      if(i%2==0):   
         try:   
            click("transferButton.png")
            print 'Clicked! transfer button'
            time.sleep(2)
         except:
            print 'transfer button not found '+ str(i)
            time.sleep(2)

      try:
         time.sleep(5) 
         wait("1447172037894.png")
         print 'Prog wait and have it !!!!'
         
         click("highSpeedButton.png")  
         print 'Clicked! High Speed button! Entering deep sleep!!!!!!!!!'
         
         time.sleep(SuccessWaitTimer)
      except:
         print 'High Speed button not found '+ str(i)
         time.sleep(RetryTimer)
      
      try:
       
        print 'Doc wait and have it !!!!'
          
        time.sleep(SuccessWaitTimer)
         
      except:
         print 'Success button not found?'          

      i=i+1



def main():
   print 'sleeping 80'
   time.sleep(80)
   print 'sleeping 80 done!!!'  

   while True:
      try :
         wait("1447174054868.png")
         print 'doc is found'
      except : 
         print 'doc not found?'          
      
      time.sleep(5)     
      

# switchApp(u"欢迎使用百度云管家")
   #openApp(u"欢迎使用百度云管家")
   #wait_and_click_transferButton()
   #wait_and_click_try_highspeed_button()
   #wait_and_click_this_button_or_that()

main()

