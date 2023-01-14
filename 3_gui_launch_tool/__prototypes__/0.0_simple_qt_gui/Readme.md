## To make a simple gui script for Qt5

use this to install qt5 on ubuntu 20.04
```
sudo apt install -y qtcreator qtbase5-dev qt5-qmake cmake
```

build command for application. courtesy of chatGPT and stackoverflow.
```
g++ -o  '<your desired app name>' <your desired filename>.cpp -std=c++11 -I/usr/include/x86_64-linux-gnu/qt5 -I/usr/include/x86_64-linux-gnu/qt5/QtWidgets -lQt5Widgets -lQt5Gui -lQt5Core -fPIC
```
https://stackoverflow.com/questions/47958083/how-to-build-qt-with-reduce-relocations
