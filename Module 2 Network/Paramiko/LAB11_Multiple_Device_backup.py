import Advance_Lab as run

SW1 = {'hostname': '192.168.122.101', 'Port': 22, 'User': 'dhiraj', 'Passwd': 'cisco'}
SW2 = {'hostname': '192.168.122.102', 'Port': 22, 'User': 'dhiraj', 'Passwd': 'cisco'}
SW3 = {'hostname': '192.168.122.103', 'Port': 22, 'User': 'dhiraj', 'Passwd': 'cisco'}
SW=[SW1] #,SW2,SW3]

for switch in SW:
    conn = run.connect(**switch)
    shell = run.get_ssh(conn)
    run.send_command(shell, 'terminal length 0')
    run.send_command(shell, 'show run')
    run.send_command(shell, 'exit')
    Output = run.output(shell)
    Str1=Output.index('version')
    user_list = Output[Str1:-14]
    from datetime import datetime

    now = datetime.now()
    Year = now.year
    Month = now.month
    Day = now.day
    Hour = now.hour
    Min = now.min
    File_name = f'{Year}-{Month}-{Day} Switch_{switch["hostname"]}'
    with open(File_name, 'w') as result:
        result.write(user_list)
    run.close()