# RaspberryPiGPIOCheck
这是一个适用于检测树莓派GPIO接口状态的项目，理论上你仅需要连接你的传感器到GPIO4的引脚上，运行sensertest.py，并且操作你的传感器的状态为一，你就可以在logs文件中查看到相应的日志。
#How to Run this Project
(if u dont wanna Run this project when ur Pi boot)
## 1. Download This Prject(highly recommend download to /home/pi/Desktop)
```bash
git clone https://github.com/malker97/RaspberryPiGPIOCheck.git
```
## 2.Connnect Ur sensor to GPIO PIN (Defult is 4)
Depend on ur senser
## 3. Start this Python3 Project
```bash
python3 sensertest.py
```
or
``` bash
python3 sensertest.py
```
## 4. Change ur senser status
## 5. Check the status logs at the ./logs/txt/[date]-logs.txt file
```
S,2020-11-09 17:00:52.539541
E,2020-11-09 17:00:52.834041
T,['0.0 hours 0.0 mins 1.9621720314 seconds']
S,2020-11-09 17:00:53.473674
E,2020-11-09 17:00:53.767058
T,['0.0 hours 0.0 mins 2.25555300713 seconds']
S,2020-11-09 17:00:54.362899
E,2020-11-09 17:00:54.557410
T,['0.0 hours 0.0 mins 2.45006489754 seconds']
S,2020-11-09 17:00:55.056313
E,2020-11-09 17:00:55.464145
T,['0.0 hours 0.0 mins 2.85789585114 seconds']
S,2020-11-09 17:00:56.029540
E,2020-11-09 17:00:56.926030
T,['0.0 hours 0.0 mins 3.75438475609 seconds']
S,2020-11-09 17:03:15.892553
E,2020-11-09 17:03:15.895225
T,['0.0 hours 0.0 mins 0.00297808647156 seconds']
S,2020-11-09 17:03:15.947402
E,2020-11-09 17:03:16.496892
T,['0.0 hours 0.0 mins 0.552560091019 seconds']
S,2020-11-09 17:03:22.832717
E,2020-11-09 17:03:23.195852
T,['0.0 hours 0.0 mins 0.915808200836 seconds']

```
S mean StarTime
E mean EndTime
T mean TotalTimeofToday
## if u wanna run this file when ur pi booted
## 1. Download This Prject(highly recommend download to /home/pi/Desktop)
```bash
git clone https://github.com/malker97/RaspberryPiGPIOCheck.git
```
## 2.Connnect Ur sensor to GPIO PIN (Defult is 4)
Depend on ur senser
## 3. Start this Python3 Project
change sensertest.py level to sudo
```bash
sudo chmod 777 sensertest.py
```
```bash
sudo chmod 777 start.sh
```
```
sudo vim /etc/rc.local
```
add "su pi -c "exec /home/pi/testboot.sh"" before the "exit 0"
then 
```
sudo reboot
```
