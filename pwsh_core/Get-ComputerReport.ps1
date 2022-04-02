$OS = Get-CimInstance -ClassName Win32_OperatingSystem 
# Client/Server
if ($OS.Caption -like "*Server*") {$server = $true} else {$server = $false}
# IP: Interface, ip, gateway, dns
$Network = Get-NetAdapter | Where-Object {$_.Status -eq "Up"} | Get-NetIPConfiguration
# Last Updates
$Updates = Get-Hotfix | Sort InstalledOn -Descending | Select-Object -First 5
# It would be nice if I could run this remotely

# Creating our own object
$props = [PSCustomObject]@{
    'OS_Name' = $OS.Caption
    'OS_Version' = $OS.Version
    'OS_Install_Date' = $OS.InstallDate
    'IsServer'= $server
    'IPv4Address' = $Network.IPv4Address.IPAddress
    'Gateway' = $Network.IPv4DefaultGateway.NextHop
    'DNS' = $Network.DNSServer | Where-Object {$_.AddressFamily -eq '2'} | Select-Object ServerAddresses -ExpandProperty ServerAddresses
    'Updates' = $Updates.HotfixID | Out-String
}

# Network: Can I ping gateway, dns server, website
$pingGateway = Test-NetConnection -ComputerName $props.Gateway -InformationLevel Quiet
$pingDNS = Test-NetConnection -ComputerName $props.DNS -InformationLevel Quiet
$pingWebsite = Test-NetConnection -ComputerName 'Kamilpro.com' -InformationLevel Quiet

$props | Add-Member -MemberType NoteProperty -Value $pingGateway -Name "PingGateway"
$props | Add-Member -MemberType NoteProperty -Value $pingDNS -Name "PingDNS"
$props | Add-Member -MemberType NoteProperty -Value $pingWebsite -Name "PingWebsite"

# Installed roles - server only

$props
