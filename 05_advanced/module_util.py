BASE_URL="https://kh-academy.co.kr/"

def clean_price(text):
    """ '1,000원' 같은 문자열에서 숫자만 추출하는 함수 -> 1000 """
    return int( text.replace(",","").replace("원","").strip())

def to_code(number):
    """
        숫자가 전달되면 앞에 0을 채워서 6자리 문자열로 반환하는 함수
        5123 -> 005123
    """
    return f"{number:06d}"
print("== modeule_util 모듈이 로드되었습니다. ==")

