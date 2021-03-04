import json
import urllib.request

# API Client ID & Client Secret
_client_id = "puwoNLecLPrJvn3nrDqk" # "gzV6zVQmtuaovnofYwpw"  # "puwoNLecLPrJvn3nrDqk"
_client_secret = "I03viXDR_G" # "46Bgk9Ycx2"  # "I03viXDR_G"


def check_language(txt):
    # encode txt to url format
    encQuery = urllib.parse.quote(txt)
    data = "query=" + encQuery

    # detecting language url
    url = "https://openapi.naver.com/v1/papago/detectLangs"

    # 인증 정보 추가
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", _client_id)
    request.add_header("X-Naver-Client-Secret", _client_secret)
    request.add_header("Content-Type", "application/x-www-form-urlencoded")

    try:
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))

        if response.getcode() is 200:
            language = json.loads(response.read())['langCode']
            return language
        else:
            print("Error Code:" + rescode)

    except urllib.error.HTTPError as e:
        print(e.code)
        print(str(e.read().decode('utf-8')))

    return False


def translate(txt, src_lang, tgt_lang):
    encText = urllib.parse.quote(txt)
    data = "source=" + src_lang + "&target=" + tgt_lang + "&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", _client_id)
    request.add_header("X-Naver-Client-Secret", _client_secret)
    request.add_header("Content-Type", "application/x-www-form-urlencoded")

    try:
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        if  response.getcode() is 200:
            # message > result > translateText가 번역된 문자열
            trans_text = json.loads(response.read())['message']['result']['translatedText']
            return trans_text
        else:
            print("Error Code:" + rescode)

    except urllib.error.HTTPError as e:
        print(e.code)
        print(str(e.read().decode('utf-8')))

    return False


if __name__ == "__main__":

    txt = 'ハードウェア機能要件'
    #언어 체크
    lang = check_language(txt)
    if lang is not False:
        #언어가 확인이 되었다면
        #해당 언어를 한국어로 번역해서 출력!
        print(translate(txt, lang, 'ko'))
