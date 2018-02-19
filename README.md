<h1 align="center">NanoNets Object Detection Python Sample</h1>

<div align="center">
  <a href="https://nanonets.com/objectdetection/">
    <img src="https://nanonets.com/logo.png" alt="NanoNets Object Detection Python Sample" width="100"/>
    </a>
</div>

** **

## Tracking the Millenium Falcon

Images and annotations taken from - https://github.com/bourdakos1/Custom-Object-Detection

Images consists of frames taken from a clip from Star Wars: The Force Awakens.
[![Watch the video](https://github.com/bourdakos1/Custom-Object-Detection/raw/master/screenshots/starwars_small.gif)](https://www.youtube.com/watch?v=xW2hpkoaIiM)

Annotations are present for each frame and have the same name as the image name. You can find the example to train a model in python and node, by updating the api-key and model id in corresponding file. There is also a pre-processed json annotations folder that are ready payload for nanonets api, the script used is node/xml-to-json.js .


** **

# Build an Object Detector for the Millenium Falcon

>**Note:** Make sure you have python installed on your system if you don't visit https://www.python.org/downloads/release/python-2714/
 
### Step 1: Clone the Repo
```bash
cd $GOPATH/src
git clone https://github.com/NanoNets/object-detection-sample-python.git
cd object-detection-sample-python
```

### Step 2: Get your free API Key
Get your free API Key from http://app.nanonets.com/user/api_key

### Step 3: Set the API key as an Environment Variable
```bash
export NANONETS_API_KEY=YOUR_API_KEY_GOES_HERE
```

### Step 4: Create a New Model
```bash
python ./code/create-model.py
```
 >_**Note:** This generates a MODEL_ID that you need for the next step

### Step 5: Add Model Id as Environment Variable
```bash
export NANONETS_MODEL_ID=YOUR_MODEL_ID
```
 >_**Note:** you will get YOUR_MODEL_ID from the previous step

### Step 6: Upload the Training Data
The training data is found in images (image files) and annotations (annotations for the files)
```bash
python ./code/upload-training.py
```

### Step 7: Train Model
Once the Images have been uploaded, begin training the Model
```bash
python ./code/train-model.py
```

### Step 8: Get Model State
The model takes ~2 hours to train. You will get an email once the model is trained. In the meanwhile you check the state of the model
```bash
python ./code/model-state.py
```

### Step 9: Make Prediction
Once the model is trained. You can make predictions using the model
```bash
python ./code/prediction.py PATH_TO_YOUR_IMAGE.jpg
```

**Sample Usage:**
```bash
python ./code/prediction.py ./images/videoplayback0051.jpg
```


*Note the python sample uses the comverted json instead of the xml payload for convenience purposes, hence it has no dependencies.*