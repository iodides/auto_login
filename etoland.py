import logging, requests

def init(id, pw):
    log = logging.getLogger('auto_login')
    baseUrl = 'http://www.etoland.co.kr/'

    with requests.Session() as s:
        loginInfo = {
            'mb_id': id,
            'mb_password': pw,
            'url': baseUrl
        }
        login = s.post(baseUrl + 'bbs/login_check2020.php', data=loginInfo)

        if login.status_code == 200:
            log.info('이토랜드 로그인 성공')
            mainPage = s.get(baseUrl)
            # print(login.text)

            attendInfo = {
                'at_memo': '오늘도 로그인',
                'at_memo2': '오늘도 로그인'
            }
            attendPage = s.get(baseUrl + 'check/index.php')
            attend = s.post(baseUrl + 'check/attendance-update.php', data=attendInfo)

            if '출석체크완료' in attend.text:
                log.info('이토랜드 출석체크')
            elif '하루에 한번만' in attend.text:
                log.info('이토랜드 이미 출석됨')
            else:
                log.info('이토랜드 에러')
            # log.info(attend.text)
        else:
            log.info('이토랜드 로그인 실패')


if __name__ == '__main__':
    init()



"""
<meta http-equiv="content-type" content="text/html; charset=euc-kr"><script language='javascript'>alert('출석체크완료\n금일 지급포인트는 50 포인트이며\n개근은 49 일째 입니다');</script><script language='JavaScript'> location.replace('attendance.php'); </script>
"""
"""
<meta http-equiv="content-type" content="text/html; charset=euc-kr"><script language='javascript'>alert('출석체크는 하루에 한번만 가능합니다.');history.go(-1);</script>
"""

