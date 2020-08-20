import requests
from bs4 import BeautifulSoup

def init(id, pw):
    print('===== Filesun 출석')
    baseUrl = 'http://www.filesun.com'

    with requests.Session() as s:
        # 로그인
        login_info = {
            'user_id': id,
            'password': pw
        }
        login = s.post(baseUrl + '/login/login_check.php', data=login_info)

        if login.status_code:
            print('로그인 성공')

            # 마이페이지
            myPage = s.get(baseUrl + '/attendance/index.php')

            bs = BeautifulSoup(myPage.text, 'html.parser')
            myPoint = bs.select_one('#leftLogin > div > div.info > dl > dd > dl > dd.point > a.td').get_text()
            myBonus = bs.select_one('#leftLogin > div > div.info > dl > dd > dl > dd:nth-child(2) > a.td').get_text()
            myAttend = bs.select_one('#calendarForm > div.user_attend').get_text()
            print('포인트 :', myPoint)
            print('보너스 :', myBonus)
            print(myAttend)

            attendance_data = {
                'mode': 'attendance',
                'rurl': 'http://www.filesun.com/attendance/index.php'
            }
            attend = s.post(baseUrl + '/attendance/save.php', data=attendance_data)

            if '지급되어' in attend.text:
                print('출석완료')
            elif '내일 다시' in attend.text:
                print('이미 출석됨')
            else:
                print('에러')
        else:
            print('로그인 실패')
    print('===== Filesun 완료')

if __name__ == '__main__':
    init()
