#!./.venv/bin/python

import time, json, logging
import filesun, etoland

log = logging.getLogger('auto_login')
log.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
fh = logging.FileHandler(filename='logfile.log')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
log.addHandler(ch)
log.addHandler(fh)

if __name__ == '__main__':
    log.info('=== Main Process Start')

    with open('config.json') as json_file:
        json_data = json.load(json_file)

        filesun_data = json_data["filesun"]
        filesun_id = filesun_data["id"]
        filesun_pw = filesun_data["pw"]
        filesun.init(filesun_id, filesun_pw)

        etoland_data = json_data["etoland"]
        etoland_id = etoland_data["id"]
        etoland_pw = etoland_data["pw"]
        etoland.init(etoland_id, etoland_pw)


    # while True:
    #     filesun.init()
    #     etoland.init()
    #     break
    #     time.sleep(1*60*60) # hour
    log.info('=== Main Process Stop')