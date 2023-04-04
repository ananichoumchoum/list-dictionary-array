#Anne-Marie Smith
#January 27th, 2022

import ipaddress
from prettytable import PrettyTable
x = PrettyTable()

Dict = {
  "Comp477": ["Gigabyte", 9133.27, "70561924KIQqzw", "68.192.163.42/255.255.240.0"], 
  "Comp678": ["Asus", 7264.42, "56024371IQCewb", "198.78.85.109/255.255.248.0"], 
  "Comp894": ["Acer", 4564.22, "41928367UHPkxu", "192.167.55.136/255.255.240.0"], 
  "Comp592": ["Dell", 9378.82, "20451398MFWusg", "192.167.86.14/255.255.255.128"], 
  "Comp397": ["Acer", 8115.08, "74189306HKLvwu", "176.33.145.182/255.255.248.0"], 
  "Comp697": ["Asus", 8941.52, "17892534DZOlru", "10.0.252.127/255.255.192.0"], 
  "Comp966": ["Dell", 9539.92, "46193287TYIurw", "10.0.222.132/255.255.252.0"], 
  "Comp964": ["Dell", 4274.43, "04237918UTSdkj", "200.3.34.67/255.255.192.0"], 
  "Comp634": ["Google", 5182.86, "95430287FCQfbk", "68.192.177.108/255.255.192.0"], 
  "Comp565": ["Toshiba", 1904.33, "57018243JPYtpu", "192.167.63.98/255.255.240.0"], 
  "Comp906": ["Dell", 5228.37, "96134827IHGibu", "176.33.20.163/255.255.192.0"], 
  "Comp481": ["Asus", 7790.58, "05793218BRZjgl", "198.78.237.73/255.255.248.0"], 
  "Comp370": ["Dell", 9251.70, "89531276LIMqby", "68.192.129.199/255.255.192.0"], 
  "Comp703": ["Toshiba", 7520.04, "53179426FUXqjz", "200.3.191.102/255.255.192.0"], 
  "Comp493": ["Google", 4621.55, "06514398WINzou", "198.78.59.119/255.255.240.0"]
}
#find the ip subnet from the IPs giving in the dictionary by importing ipaddress module
for i in Dict.values():
    
    net = ipaddress.ip_network(i[-1], strict=False)
    subnet = net.network_address
    net = str(net)
    new = net[:-3]
    subnet= str(subnet)
    
    i.pop()
    i.append(new)
    i.append(subnet)

#how to print without pretty table {is for the number of space}
print('\n'*2)
print ("{:<10} | {:<15} | {:<9} | {:<17} | {:<15} | {:<15}".format('Computer','Manufacturer','Price','Asset Tag','IP Address', 'IP Subnet'))
print('______________________________________________________________________________________________', end = '\n'*2)
#for keys and values in dictionary, make the value give values name and format them in a table
for k, v in Dict.items():
    man, price, asset, ip, sub = v
    print ("{:<10} | {:<15} | {:<9} | {:<17} | {:<15} | {:<15}".format(k, man, price, asset, ip, sub))
print("\n\n")

#how to print with prettytable
x.field_names = ['Computer','Manufacturer','Price','Asset Tag','IP Address', 'IP Subnet']
for k, v in Dict.items():
    man, price, asset, ip, sub = v
    x.add_row([k, man, price, asset, ip, sub])
print(x)