#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazonrekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)


import boto3


def detect_faces(photo):
    client = boto3.client('rekognition')

    response = client.detect_faces(Image={'Bytes': photo}, Attributes=['ALL'])

    for faceDetail in response['FaceDetails']:
        return faceDetail['Emotions'][0]



def aws_main(face_image):
    photo = face_image

    face_emotion = detect_faces(photo)
    return str(face_emotion['Type'])




if __name__ == "__main__":
    aws_main()
