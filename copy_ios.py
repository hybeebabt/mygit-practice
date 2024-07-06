from netmiko import ConnectHandler
import getpass

passwd = getpass.getpass('Please enter the password: ')


device = {
        "device_type": "cisco_ios",
        "host": '100.100.0.50',
        "username": "networks",
        "password": passwd,
        "secret": passwd
    }

connection = ConnectHandler(**device)
connection.enable()
print(f'Connecting to {device["host"]}')
output = connection.send_command('show ip interface brief', use_textfsm=True)
test = 'UP'
print(output)

for interface in output:
    if interface['status'] == test.lower():
        print(interface['intf'])



connection.disconnect()

