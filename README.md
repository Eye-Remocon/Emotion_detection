Emotion_Detection
===================================================


개발환경 구축
---------------------------------------------------
- python3 version(Anaconda3 추천) 설치 필수
- 패키지 설치 전 가상환경 생성 후 환경 분리 추천(Linux & Mac)
- 필요 패키지 설치(Linux & Mac)
  1. Pytorch [공식 홈페이지]('https://pytorch.org/get-started/locally/' )에서 조건에 해당하는 pytorch 관련 라이브러리 설치
  2. 
    ```
    $ pip install flask
    $ pip install boto3
    ```
 
AWS 설정
---------------------------------------------------
- [링크](https://docs.aws.amazon.com/ko_kr/rekognition/latest/dg/rekognition-dg.pdf) P.13 참고하여 access key, password 설정
- 지역코드는 ap-northeast-2 로 입력


테스트 방법
---------------------------------------------------
- 위 라이브러리를 설치 후, 사용하는 IDE에 AWS Access Key 적용시키기
- 올린 커밋 들 중에 main.py가 메인 파일이기 때문에 실행시키면 서버가 실행됩니다.

- main.py 내에 host='' 이부분을 localhost또는 자신의 ip로 변경하기
- main.py 파일 실행시키기  
- 아래 테스트 코드 실행시 fileName을 얼굴인식하고 싶은 사진의 경로와 이미지이름으로 변경
- url에 ip부분도 localhost나 자신의 ip번호로 변경 후 실행
```
import requests
import base64
import json


with open(fileName, 'rb') as f:
    im_b64 = base64.b64encode(f.read())

payload = {'image':im_b64}

url = 'http://ip주소:8080/main'

r = requests.post(url, data=payload)

if r.ok:
    emotion = r.json()['emotion']
    print(emotion)
```

API 파일들 설명
---------------------------------------------------
1. main.py  
- flask 서버가 실행되는 메인 소스코드 입니다, 
- 클라이언트로부터 이미지파일을 POST 요청을 받아서, 해당 이미지의 BASE64코드를 이미지로 변환 수행
- 처음으로 HOME Emotion Detection을 수행하기 위해 detection() 함수 호출
- HOME Emotion Detection 수행 시, 감정인식이 되지 않는다면 아무값도 반환되지 않는다면, AWS Emotion Detection 에서 aws_main() 호출
- 반환되는 감정을 담은 json 파일을 클라이언트에게 다시 반환

2. home_emotion_detection.py
- Home Emotion Detection을 위해 존재하는 소스코드입니다.
- 미리 학습된 ResNet9 감정인식모델과 얼굴을 인식하는 모델을 불러옴
- 사진의 얼굴을 인식하여 크롭하고, 감정인식모델에 적용될 수 있도록 이미지 변환 시키고 만약 얼굴이 인식되지 않았다면 No Face 반환
- 학습된 모델을 forward 시켜 7가지 감정의 분류를 할 수 있도록 구현
- 감정이 7가지로 분류된다면 해당 Label를 반환, 감정분류가 안된다면 공백 반환

3. aws_emotion_detection.py
- aws 감정인식 요청 시에, 이미지의 base64코드를 aws 로컬 이미지로 요청
- 여러 FaceDetails 중에 가장 Confidence 높은 Emotions 특징값만 반환
