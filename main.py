import time, json
import filesun, etoland

if __name__ == '__main__':
    print('Main Process Start')

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
    print('Main Process Stop')