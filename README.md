# Emotion_detection

사람 감정인식 기능 관련 구현 방법들

<H2>1️⃣ Amazon Rekognition </H2>

- mazon Rekognition에서는 이미지와 비디오에서 얼굴이 나타나는 순간을 쉽게 탐지하고 각 얼굴에서 성별, 연령대, 뜬 눈, 안경, 헤어 스타  일과 같은 속성을 확보할 수 있습니다. 비디오에서 시간이 지나면서 이러한 속성들이 어떻게 변하는지 측정할 수도 있습니다(예: 배우가 표현하는 감정이 변화하는 시간대를 구성).
- Amazon Rekognition API를 통해 얼굴의 Bounding box, 특성, 감정들, 랜드마크와 그 얼굴이 위치 또한 제공
- 여기서 감정인식의 score를 반환하고, 예를 들어 행복의 감정으로 예측된다면 Happy 85% 의 값들로 반환됨
- 장점 : 감정인식 뿐만 아니라 이미지 분석에 관련된 다양한 기능들을 사용할 수 있음, API 문서가 깔끔하게 정리되어 편리한 사용 가능
- 가격
![K-002](https://user-images.githubusercontent.com/54658745/123742414-8e839d80-d8e6-11eb-8dc1-70e4855c8a26.png)

<br/>

<H2>2️⃣ Microsoft Azure </H2>

- Azure에서 Face API에서는 얼굴 감지, 얼굴 확인, 얼굴 인식, 얼굴 그룹화, 인지된 감정 인식의 기능등이 존재  
- 인지된 감정에서 분노, 경멸, 역겨움, 공포, 행복, 무표정, 슬픔, 등 8가지 이상 인지된 표정 감지 가능
- API 사용시, JSON 데이터 형태로 각 Detection된 얼굴의 위치 값과, 감정 인식된 faceAttributes의 emotion 값 반환
- 홈 IoT 장비 컨트롤 : 사용자가 미리 홈 루틴을 정해놓고 특정 상황 및 행동이 인식되면 설정된 루틴에 맞추어 IoT 장치들을 컨트롤한다.
- 가격
![K-003](https://user-images.githubusercontent.com/54658745/123742902-65afd800-d8e7-11eb-9b0a-b06144fecd3b.png)

<br/>

<H2>3️⃣ Google Cloud Vision API </H2>

- JSON 데이터 형테로 요청하면 FACE_DETECTION 응답에는 인식된 모든 얼굴의 경계 상자, 얼굴에서 인식된 특징(눈, 코, 입 등), 얼굴과 이미지 속성(기쁨, 슬픔, 분노, 놀람 등)의 신뢰도 평점이 포함
- 특정인의 얼굴인식은 지원하지 않음
- 가격
![K-004](https://user-images.githubusercontent.com/54658745/123743757-a8be7b00-d8e8-11eb-9361-6d47c1cac351.png)



<br/>

<H2>4️⃣ 직접 모델 구축(현재 상황) </H2>

- 캐글을 통해 Face Emotion dataset를 활용하여 Pytorch를 활용해 모델 학습
- 'Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise' 의 7가지 감정인식 가능
- 모델 학습결과 정확도 54%로 다소 낮은 문제 => 해결 필요
- 학습 loss and accuracy
![K-005](https://user-images.githubusercontent.com/54658745/123744192-5e89c980-d8e9-11eb-8d53-7680d02cd352.png)




