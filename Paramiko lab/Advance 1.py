import Advance as run
import os

SW1={'IP':'192.168.75.10','Port':22,'User':os.environ.get('DB_USER'),'Password':os.environ.get('DB_PWD')}
Conn=run.connect(**SW1)
shell=run.get_ssh(Conn)
# run.send_command(shell,'config t')
# run.send_command(shell,'vlan 100')
# run.send_command(shell,'name Accounts')
# run.send_command(shell,'vlan 200')
# run.send_command(shell,'name Sales')
# run.send_command(shell,'end')
run.send_command(shell,'terminal len 0')
run.send_command(shell,'sh run')

Catch=run.output(shell)

user_list=Catch.splitlines()
user_list=user_list[9:-3]
Join='\n'.join(user_list)
print(Join)

# path="config %s.txt"%SW1['IP']
# import datetime
# Now=datetime.datetime.now()
# path=f"{Now.year}-{Now.month}-{Now.day} Switch_{SW1['IP']}.txt"
#
# with open(path,'w') as W:
#     W.write(Catch)
#     os.startfile(path)

# print(Catch)

run.close()