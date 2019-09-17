# Travel Assistant

I wanted to create a simple project that would detect text in the environment and translate it to any language specified.

## Introduction

This application was developed for the DragonBoard 410c from Arrow Electronics using Python. The application captures an image using the webcam, detects text in the image, detects the language of the text, and outputs the original text detected as well as that text translated (when there is internet connection). 

## Equipment
The necessary equipment for the assembly of the appication are:
* DragonBoard 410c
* 12V Wall adapter
* USB Webcam (the Creative Webcam was used)
* USB Keyboard
* USB Mouse
* HDMI Monitor

## Installation
*fswebcam* is used to interface with the webcam connected using code. To install run the following command in the terminal:

```bash
sudo apt-get install fswebcam
```

*pytesseract* is used to perform the Optical Character Recognition. To install run the following commands in the terminal:

```bah
sudo pip install pytesseract
```

- *If a **"Memory Error"** is thrown, then run the following command:*

```bash
sudo pip --no-cache=dir install matplotlib
```

*googletrans* is used to perform the translation from the detected language of the text to any specified language (which in this case is French). To install run the following commands in the terminal:

```bash
sudo pip install googletrans
```

- *If a **"Memory Error"** is thrown, then run the following command:*

```bash
sudo pip --no-cache=dir install googletrans
```

## Running the Code
To run the program, first make sure the camera is pointed directly at something that contains text. Next run the following command in the terminal:

```bash
./run.sh
```

The detected text will be displayed in the terminal output in both the detected lanuage of the text as well as in French. If you would like to change the language the text is translated to, then follow these steps:

1. open the file **ocr.py** in your preferred text editor
2. go to line **21** in the file: 
  > translation = translator.translate(word, dest='fr')
3. change `fr` to any language you would like by using the corresponding language codes which can be found at [this link](https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages)

## Examples

<div align="center">
    <figure>
        <img width="360" height="300" src="/Example Pictures/Hello.jpg">
        <img width="460" height="300" src="/Example Pictures/Hello-output.jpg">
        <p align="center">Figure 1. A simple example of text being translated</p>
    </figure>
</div>

<div align="center">
    <figure>
        <img width="460" height="300" src="/Example Pictures/danger.jpg">
        <img width="360" height="300" src="/Example Pictures/danger-output.jpg">
        <p align="center">Figure 2. Real world example of a Construction Sign being detected and translated</p>
    </figure>
</div>

## Limitations
If the camera is pointed at an angle, the text detection may be inconsistent. Running the program creates an image file *test.jpg* which is the image that the camera captures. You can use this to understand what your camera saw and can adjust the camera position and orientation accordingly to produce a better result.

As shown in the example below (Figure 3), another limitation of the program is the inability to consolidate text across multiple lines into a single phrase. Due to ***Construction*** and ***Zone*** being on separate lines, the program translates those words separately into ***Construction*** and ***Région***. Instead, the correct interpretation should be ***Construction Zone*** which translates to ***Zone de construction*** in `French`.


<div align="center">
    <figure>
        <img width="460" height="300" src="/Example Pictures/danger.jpg">
        <img width="360" height="300" src="/Example Pictures/danger-output.jpg">
        <p align="center">Figure 3. Line by Line translation instead of translating one phrase</p>
    </figure>
</div>
