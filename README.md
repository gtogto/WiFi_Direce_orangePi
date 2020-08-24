Wi-Fi Direct communication setup between Linux and Android
======
# Target devices
  - Raspberry Pi 3 B+
  - OrangePi Zero
  - BananaPi M2 & P2 Zero
  - Android Devices (up to API 26 lev)

## 1. set-up
 1. This command disables the wlan0 interface so that it can be executed for Wi-Fi Direct.
```linux
wpa_cli -i wlan0 terminate -B
```
 2. add a new wpa_supplicant.conf
 - sudo cat /etc/wpa_supplicant.conf
```linux
ctrl_interface=/var/run/wpa_supplicant
update_config=1

ap_scan=1

device_name=hello
device_type=1-0050F204-1

# If you need to modify the group owner intent, 0-15, the higher
# number indicates preference to become the GO. You can also set
# this on p2p_connect commands.
p2p_go_intent=15

# optional, can be useful for monitoring, forces
# wpa_supplicant to use only channel 1 rather than
# 1, 6 and 11:
p2p_listen_reg_class=81
p2p_listen_channel=1
p2p_oper_reg_class=81
p2p_oper_channel=1
```
 3. This command disables the wlan0 interface so that it can be executed for Wi-Fi Direct.
```linux
sudo wpa_supplicant -d -Dnl80211 -c /etc/wpa_supplicant.conf -iwlan0 -B
```

 4. Start a new wpa_supplicant for wlan0 with the settings written in the /etc/wpa_supplicant.conf file.
```linux
sudo wpa_supplicant -d -Dnl80211 -c /etc/wpa_supplicant.conf -iwlan0 -B
```

 5. A new interface p2p-wlan0-0 is created. You can check it with the ifconfig command as follows:
```linux
sudo wpa_cli -i wlan0 p2p_group_add
```

 6. You can also assign a static IP address of the PC that becomes the group owner (server).
```linux
sudo ifconfig p2p-wlan0-0 192.168.1.2
```

 7. /etc/udhcpd.conf configuration
 - udhcpd is a tool used to dynamically allocate IP addresses of Wi-Fi Direct clients.

```linux
# Sample udhcpd configuration file (/etc/udhcpd.conf)
# The start and end of the IP lease block
start 		192.168.1.20	#default: 192.168.0.20
end		192.168.1.254	#default: 192.168.0.254
# The interface that udhcpd will use
interface   p2p-wlan0-0		#default: eth0
#Examles
opt	dns	8.8.8.8  8.8.4.4 # public google dns servers
option	subnet	255.255.255.0
opt	router	192.168.1.2
option	lease	864000		# 10 days of
```

 8. Write Wi-Fi Direct setup script and run
```linux
python direct.py
```



