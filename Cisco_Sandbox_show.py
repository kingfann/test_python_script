#!/usr/bin/python

import netmiko
import json
# go to python installed folder and run "pip list" - It shows the installed modules
# install the list python modules 
# python -m pip install pandas
# python -m pip install dataframe


def switch_showoutput():

    username = "admin"
    password =  "C1sco12345"



    devices = '''
sbx-iosxr-mgmt.cisco.com
    '''.strip().splitlines()
    
    netmiko_exceptions = (netmiko.ssh_exception.NetMikoAuthenticationException,
                        netmiko.ssh_exception.NetMikoTimeoutException)
    
    
 
    for device in devices:
       try:

           print('~'*20)
           connection = netmiko.ConnectHandler(ip=device, device_type='cisco_xr',username=username,password=password,port='8181')

           output1 = connection.send_command('show ip int brief')
           print(output1)
          
           print('disconnecting device', device)     
           connection.disconnect()
    
 
       except netmiko_exceptions as error_message:
           print('failed to ', device, error_message)
           print('#'*40) 

if __name__ == '__main__':
   switch_showoutput()

          
         