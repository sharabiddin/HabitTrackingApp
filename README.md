![BeeWare](https://img.shields.io/badge/🐝_beeware-F09436?style=for-the-badge&logo=beeware&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white) ![scikit-learn](https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white) ![Android](https://img.shields.io/badge/Android-3DDC84?style=for-the-badge&logo=android&logoColor=white) 

![Static Badge](https://img.shields.io/badge/build-android-green) ![Static Badge](https://img.shields.io/badge/build-ios-red) 

![GitHub last commit](https://img.shields.io/github/last-commit/mwilko/Mobile_Health_App) ![Static Badge](https://img.shields.io/badge/status-complete-green)


# Mobile Habit tracking app

Team Thesis project. This project is a mobile application built in BeeWare, which utilises rust integrity for high performance.

## How to install:

Install Python 3.8 (This version is needed to satisfy dependency requirements).
```sh
$ python3 --version
```
If your Python version is stated as 3.8, we can continue, if not create a virual enviroment with that Python version and be sure to select the Python 3.8 interperator:

OSX/Linux:
```sh
$ python3 -m venv venv
$ source venv/bin/activate
```

Windows:
```ps
PS > python3 -m venv venv
PS > ./venv/Scripts/activate
```


You should now have the `(venv)` prefix added to your terminal prompt as shown below.

Next, install Briefcase the library that manages the mobile deployment and development of the application:
```sh
(venv) $ python -m pip install -r requirements.txt
```
If you get an error when trying to install TF Lite, try this:
```
pip3 install --extra-index-url https://google-coral.github.io/py-repo/ tflite_runtime
```

## How to Run:

(Tested on INB1102 PC's, Win11 and Macbook Air/Pro M1, other platforms may behave differently)

You should be able to run the application with the following (you will need to accept android SDK license agreements on auto-setup):
```sh
(venv) $ briefcase run android -r -u
```
This would compile the application where the terminal will take you through the proccess of hosting the app via a virutal device which you select.

#### Windows Bug:
You will find that when first starting the emulator it will hang on:
```sh
[habitapp] Starting emulator Pixel_3a_API_34_extension_level_7_x86_64...
━━━━━━━━━━━━━━━━━━━━ Starting emulator...
```

You must ctr+C to cancel the process and then run the command again (this is a known bug with the emulator NOT US).:
```sh
(venv) $ briefcase run android
```

(Potentially repeating until the emulator starts, this is a known bug with the briefcase library and emulator.)


Thanks for taking the time to visit our application.

