import datetime

log_file = 'Data/log.txt'


def log_process(message):
    current_time = datetime.datetime.now()
    format_date = current_time.strftime('%Y-%m-%d %H:%M:%S.%f')
    logtext = format_date + ' - ' + message
    print(logtext)
    with open(log_file, 'a') as f:
        f.write(logtext+'\n')
