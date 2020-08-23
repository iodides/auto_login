import logging, requests
from bs4 import BeautifulSoup


def init(id, pw):
    log = logging.getLogger('auto_login')
    baseUrl = 'http://www.filesun.com'

    with requests.Session() as s:
        # 로그인
        login_info = {
            'user_id': id,
            'password': pw
        }
        login = s.post(baseUrl + '/login/login_check.php', data=login_info)

        if login.status_code:
            log.info('파일썬 로그인 성공')

            # 마이페이지
            myPage = s.get(baseUrl + '/attendance/index.php')

            bs = BeautifulSoup(myPage.text, 'html.parser')
            myPoint = bs.select_one('#leftLogin > div > div.info > dl > dd > dl > dd.point > a.td').get_text()
            myBonus = bs.select_one('#leftLogin > div > div.info > dl > dd > dl > dd:nth-child(2) > a.td').get_text()
            myAttend = bs.select_one('#calendarForm > div.user_attend').get_text()
            log.info('파일썬 포인트 : %s', myPoint)
            log.info('파일썬 보너스 : %s', myBonus)
            log.info(myAttend)

            attendance_data = {
                'mode': 'attendance',
                'rurl': 'http://www.filesun.com/attendance/index.php'
            }
            attend = s.post(baseUrl + '/attendance/save.php', data=attendance_data)

            if '지급되었' in attend.text:
                log.info('파일썬 출석완료')
            elif '내일 다시' in attend.text:
                log.info('파일썬 이미 출석됨')
            else:
                log.info('파일썬 에러')
            # log.info(attend.text)
        else:
            log.info('파일썬 로그인 실패')
    # log.info('===== Filesun 완료')

if __name__ == '__main__':
    init()


"""
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<script type="text/javascript">
        alert("출석이 완료되어 10포인트가 지급되었습니다.");
        location.replace('http://www.filesun.com/attendance/index.php');
</script>
"""
"""
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<script type="text/javascript">
alert("1일 1회 IP입니다. 내일 다시 출석해 주세요!");
location.href = 'http://www.filesun.com/attendance/index.php';
</script>
"""
