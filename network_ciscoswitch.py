from netmiko import Netmiko
from netmiko import ConnectHandler
from datetime import datetime
from getpass import getpass

device_id = input("network device ip: ")
username = input("enter your username: ")
password = getpass("password: ")

router1 = {
    'device_type': 'cisco_ios',
    'ip': device_id,
    'username': username,
    'password': password,
#     'port': '22',
    'secret': 'test1234',
    'verbose': True
}

#router2 = {
#    'device_type': 'cisco_ios',
#    'ip': '10.0.0.2',
#    'username': 'test',
#    'password': 'test123',
#     'port': '22',
#    'secret': 'test1234',
#    'verbose': True
#}
##add the extra line
#router3 = {
#     'device_type': 'cisco_ios',
#    'ip': '10.1.0.3',
#    'username': 'test',
#    'password': 'test123',
#     'port': '22',
#    'secret': 'test1234',
#    'verbose': True
#}
all_devices = [router1]

start_time = datetime.now()
print(start_time)
for a_device in all_devices:
    net_connect = ConnectHandler(**a_device)
   
    output_wr = net_connect.send_command_expect('write memory')
    print(output_wr)
    output_showhostname = net_connect.send_command('show run | in hostname')
    output_showipintbrief = net_connect.send_command('show run | in NVRAM')
    print(f"\n\n----------Device {a_device['ip']}-show run | in NVRAM  ----\n\n")
    print(output_showhostname)
    print(output_showipintbrief)
    print(f"\n\n------------END-----------")
    net_connect.disconnect()

end_time = datetime.now()

print(end_time)

total_time = end_time - start_time

print(f"total time taken: {total_time}")

#connection = ConnectHandler(**router2)
#connection.enable()
#commands = ['int fa0/1', 'no shutdown', 'ip address 10.1.0.2 255.255.255.0', 'description**dummy test interface***']
#connection.send_config_set(commands)

#output = connection.send_command_expect('write memory')
#print(output)
#connection.disconnect()