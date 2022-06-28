# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 10:30:17 2022

@author: Yash Kumar
"""
import os,sys
username = os.getlogin()
persistent_regkeys = ['C:\\Users\\'+username+'\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup',
                      'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp',
                      'HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run', 
                      'HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunOnce',
                      'HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run',
                      'HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnce',
                      'HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnceEx',
                      'HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnceEx\0001\Depend', 
                      'HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\\User', 
                      'HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\\Shell', 
                      'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\\Shell', 
                      'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\\User', 
                      'HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunServicesOnce', 
                      'HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunServicesOnce', 
                      'HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunServices', 
                      'HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunServices', 
                      'HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run',
                      'HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run', 
                      'HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\\Userinit', 
                      'HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\Shell', 
                      'HKEY_CURRENT_USER\Software\Microsoft\Windows NT\CurrentVersion\Windows', 
                      'HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session Manager', 
                      'HKEY_CURRENT_USER\Software\Microsoft\Windows NT\CurrentVersion\Windows\load', 
                      'HKLM\SYSTEM\CurrentControlSet\Control\Lsa\\',
                      'HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\W32Time\TimeProviders\\', 
                      
                      
                      ]           
print(persistent_regkeys)
                      
                      
                      
                      
