import Advance_Lab as run

SW1 = {'hostname': '192.168.1.221', 'Port': 22, 'User': 'dhiraj', 'Passwd': 'cisco'}
conn = run.connect(**SW1)
shell = run.get_ssh(conn)
run.send_command(shell, 'terminal length 0')
run.send_command(shell, 'show run')
run.send_command(shell, 'exit')
Output = run.output(shell)
user_list = Output.splitlines()
print(user_list)
user_list = user_list[17:-1]
Join = '\n'.join(user_list)

from datetime import datetime

now = datetime.now()
Year = now.year
Month = now.month
Day = now.day
Hour = now.hour
Min = now.min
File_name = f'{Year}-{Month}-{Day} Switch_{SW1["hostname"]}'
with open(File_name, 'w') as result:
    result.write(Join)
run.close()