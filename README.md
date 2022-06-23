<h1 align="center">Screen Recorder </h1>

<p align="center">
  <img src="https://github.com/pedropamn/ScreenRecorder/blob/main/screenrec.png?raw=true" />
</p>

&rarr; __Description__ 
* A simple, fast and light-weight Screen Recorder 

&rarr; __Usage__ 
* Just run the executable available in [Releases section](https://github.com/pedropamn/ScreenRecorder/releases) (Windows)

&rarr; __Contribute & Build__
* If you are a developer and would like to contribute, feel free to send your PR. 
* GUI is made entirely with PyQt5
* The```screenrec.py``` is the main file
* PyInstaller is a good option to create a build. You can install via pip 
(```pip install PyInstaller```)
* To create executable file, run ```pyinstaller --onefile --windowed --icon=record.ico screenrec.py```. 
* If log shows that some library is missing, just install it via ```pip install -r requirements.txt```
* Executable not work so well after build with latest Python version, so Python 3.9.13 was used


&rarr; __To do__ 
* Capture pointer
* HD Recording
