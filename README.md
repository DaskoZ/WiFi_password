# WiFi Passwords
### Script that returns WiFi passwords stored in your device.
### It will save the output to a file "WiFi_passwords.txt" in the same directory.

## requirements
- python3
- prettytable

## Usage:
Install prettytable:
```
python -m pip install -U prettytable
``` 
Windows command line:
```usage
python .\wifi_password.py
```
Linux terminal:
```
python3 ./wifi_password.py
``` 
### Output examples:
output will be saved in the same directory "WiFi_passwords.txt"

```
+-----+-----------------------+------------------+
| No. |       WiFi-Name       |  WiFi-Password   |
+-----+-----------------------+------------------+
|  1  |        HOME_5G        |    qwert12345    |
|  2  |       HOME_2.4G       |     12345678     |
|  3  |      TP-Link-5Ghz     |    0123456789    |
|  4  |     TP-Link-2.4Ghz    |     12345678     |
+-----+-----------------------+------------------+
```
