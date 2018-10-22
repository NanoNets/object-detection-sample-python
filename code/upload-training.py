import os
import requests
from tqdm import tqdm
import xmltodict
import json


pathToAnnotations = './annotations/xmls'
pathToImages = './images'
model_id = os.environ.get('NANONETS_MODEL_ID')
api_key = os.environ.get('NANONETS_API_KEY')


def postprocessor(path, key, value):
    try:
        if key in ['xmin', 'ymin', 'xmax', 'ymax']:
            return key, int(value)
        else:
            return key, value
    except (ValueError, TypeError):
        return key, value


for root, dirs, files in os.walk(pathToAnnotations, topdown=False):
    for name in tqdm(files):
        annotation = open(os.path.join(root, name), "r")
        filePath = os.path.join(root, name)
        imageName, ext = name.split(".")
        imagePath = os.path.join(pathToImages, imageName + '.jpg')
        annotation_dict = xmltodict.parse(
            annotation.read(), force_list=('object',), postprocessor=postprocessor)
        if not annotation_dict:
            print(annotation_dict)
            continue
        url = 'https://app.nanonets.com/api/v2/ObjectDetection/Model/' + \
            model_id + '/UploadFile/'
        data = {'file': open(imagePath, 'rb'),  'data': (
            '', '[{"filename":"' + imageName+".jpg" + '", "object": ' + json.dumps(annotation_dict['annotation']['object'])+'}]'),
            'modelId': ('', model_id)}
        response = requests.post(
            url, auth=requests.auth.HTTPBasicAuth(api_key, ''), files=data)
        if response.status_code > 250 or response.status_code < 200:
            print(response.text), response.status_code

print("\n\n\nNEXT RUN: python ./code/train-model.py")
