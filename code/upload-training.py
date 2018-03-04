import os, requests

pathToAnnotations = './annotations/json'
pathToImages = './images'
model_id = os.environ.get('NANONETS_MODEL_ID')
api_key = os.environ.get('NANONETS_API_KEY')

for root, dirs, files in os.walk(pathToAnnotations, topdown=False):
    for name in files:
        annotation = open(os.path.join(root, name), "r")
        filePath = os.path.join(root, name)
        imageName, ext = name.split(".")
        imagePath = os.path.join(pathToImages, imageName + '.jpg')
        jsonData = annotation.read()
        url = 'https://app.nanonets.com/api/v2/ObjectDetection/Model/' + model_id + '/UploadFile/'

        data = {'file' :open(imagePath, 'rb'),  'data' :('', '[{"filename":"' + imageName+".jpg" + '", "object": '+ jsonData+'}]'),   'modelId' :('', model_id)}
        
        response = requests.post(url, auth=requests.auth.HTTPBasicAuth(api_key, ''), files=data)

        print(response.text)





#data = {'file' :open('REPLACE_IMAGE_PATH.jpg', 'rb'),     'data' :('', '[{"filename":"REPLACE_IMAGE_PATH.jpg", "object": [{"name":"category", "bndbox": {"xmin": 1,"ymin": 1,"xmax": 100, "ymax": 100}}]}]'),    'modelId' :('', 'REPLACE_MODEL_ID')}

print("\n\n\nNEXT RUN: python ./code/train-model.py")