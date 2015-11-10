# coding=utf-8
from threading import Thread


def wait_and_click_transferButton( ):
   print 'waiting for transfer list button'
   for i in range(20):
      try:  
         click("1447114728089.png")
         # not found is not a problem, if found, click and stop while loop.
         break
      except:  
         print 'transfer button not found, continue waiting ' + str(i)
      time.sleep(10)


def wait_and_click_try_highspeed_button( ):
   print 'waiting for try high speed button'
   
   i=0
   while True:  
      try:  
         click("1447114871257.png")     
         print 'Clicked! High Speed button'
         # not found is not a problem, if found, click and stop while loop.
      except:  
         print 'high speed button not found, continue waiting '+ str(i)
      time.sleep(60)
      i=i+1

      
def wait_and_click_this_button_or_that():
   i =0
   while True:
      if(i%2==0):   
         try:  
            click("transferButton.png")
            print 'Clicked! transfer button'
            time.sleep(2)
         except:
            print 'transfer button not found, but OK, keep waiting '+ str(i)
            time.sleep(12)

      try:  
         click("highSpeedButton.png")  
         print 'Clicked! High Speed button'
         time.sleep(5*60 )
      except:
         print 'High Speed button not found, but OK, keep waiting '+ str(i)
         i=i+1
         time.sleep(120)


def main():

   # switchApp(u"欢迎使用百度云管家")
   #openApp(u"欢迎使用百度云管家")
   #wait_and_click_transferButton()
   #wait_and_click_try_highspeed_button()
   wait_and_click_this_button_or_that()

main()

