import configparser
import os

# 파일 이름 Default 값
def getInifilename():
    return 'application.ini'

# 
def getIni(as_section, as_key):
    try:
        rtn_value = ''
        ls_filename = getInifilename()

        if os.path.isfile('./' + ls_filename) is False:
            initIni()
            return getIni(as_section, as_key)
        
        config = configparser.ConfigParser()

        config.read(ls_filename)

        rtn_value = config[as_section][as_key]

        return rtn_value

    except KeyError:
        print('Key Error')
        return ''


def setIni(as_section, as_key, as_value = ''):
    try:
        ls_filename = getInifilename()

        if os.path.isfile('./' + ls_filename) is False:
            initIni()
            return -1
        
        config = configparser.ConfigParser()

        config.read(ls_filename)
        sec = config.sections()

        print(sec)
        if as_section not in sec:
            return -1
        
        for i in range(len(sec)):
            if as_key.lower() in config[sec[i]]:
                config.set(sec[i], as_key.lower(), as_value)

                with open(ls_filename, 'w') as f:
                    config.write(f)
                return 1
            
        return -1

    except:
        return -1


def initIni():
    ls_filename = getInifilename()
    if os.path.isfile('./' + ls_filename):
        return

    config_file = configparser.ConfigParser()

    config_file['DataBase'] = {
        'SID' : '',
        'DBID' : '',
        'DBPW' : '',
        'DBIP' : '',
        'DBPORT' : ''
    }
    config_file['Crawling'] = {
        'Interval' : '',
        'USERID' : '',
        'USERPW' : '',
        'Start_All' : '',
        'AUTOSTART' : '',
        'DBPROCESS' : ''
    }
    config_file['Log'] = {
        'LogDeleteYN' : '',
        'LogDeleteDays' : '',
        'LogFileDest' : '',
        'LastLogIn' : '',
        'ErrorEmailFrom' : '',
        'ErrorEmailFromPW' : '',
        'ErrorEmailTo' : '',
        'URL' : '',
        'FULLURL' : '',
    }
    config_file['SOCKET'] = {
        'SOCKIP' : '',
        'SOCKPORT' : '',
        'COMMYN' : ''
    }
    config_file['DetailMch'] = {
        'Thread_1' : '',
        'Thread_2' : '',
        'Thread_3' : '',
        'Thread_4' : '',
        'Thread_5' : '',
        'Thread_6' : '',
        'Thread_7' : '',
        'Thread_8' : ''
    }

    with open(ls_filename, 'w') as f:
        config_file.write(f)

print(setIni('1', '2', '1'))
print(setIni('DataBase', 'SID', 'TEST'))

print(getIni('DataBase', 'SID'))