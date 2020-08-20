import requests

def init(id, pw):
    print('===== etoland 출석')
    baseUrl = 'http://www.etoland.co.kr/'

    with requests.Session() as s:
        loginInfo = {
            'mb_id': id,
            'mb_password': pw,
            'url': baseUrl
        }
        login = s.post(baseUrl + 'bbs/login_check2020.php', data=loginInfo)

        if login.status_code == 200:
            print('로그인 성공')
            mainPage = s.get(baseUrl)
            # print(login.text)

            attendInfo = {
                'at_memo': '오늘도 로그인',
                'at_memo2': '오늘도 로그인'
            }
            attendPage = s.get(baseUrl + 'check/index.php')
            attend = s.post(baseUrl + 'check/attendance-update.php', data=attendInfo)

            if '하루에 한번만' in attend.text:
                print('이미 출석됨')
            elif '출출' in attend.text:
                print('출석체크')
            else:
                print('에러')
        else:
            print('로그인 실패')
    print('===== etoland 완료')


if __name__ == '__main__':
    init()


