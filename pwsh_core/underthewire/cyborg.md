# Cyborg
1. The password for cyborg2 is the state that the user Chris Rogers is from as stated within Active Directory: 
   Get-ADUser -Filter {Name -like '*rogers*'} -Properties st
   Password: kansas

2. The password for cyborg3 is the host A record IP address for CYBORG718W100N PLUS the name of the file on the desktop:
   Resolve-DnsName CYBORG718W100N
   172.31.45.167_ipv4

3. The password for cyborg4 is the number of users in the Cyborg group within Active Directory PLUS the name of the file on the desktop:
   (Get-ADGroupMember -Identity Cyborg).count
   88_objects

4. The password for cyborg5 is the PowerShell module name with a version number of 8.9.8.9 PLUS the name of the file on the desktop: