
# coding=utf-8
from threading import Thread
import time
import sys

ShortWaitTime  =3 
 

def main():

    
   while True:	  
  

     print("to click yes")

     click("yes.png")
     
     print("to click Vote")
     click("vote.png")
     
     print("to click return")
     time.sleep( 1 )   
     try:
        click("return.png")
     except:
         sleep(1)
         click("return.png")
  
    


main()

