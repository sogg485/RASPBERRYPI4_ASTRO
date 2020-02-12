# Giritharan Script (Created on: 12/02/2020) Github user: sogg485

read -p "Do you want to create a WIFI Hotspot?(Y/N)" uniquehotspot
if [ "$uniquehotspot" == "y" ]
then
		echo "Please fill in the information for WIFI Hotspot ")
		read -p "Ssid name: " uniquehotspot_ssid
		read -p "Password: " uniquehotspot_password
		
		display "Creating $(uniquehotspot_ssid -s) Hotspot Wifi"
		if [ -z "$(ls /etc/NetworkManager/system-connections/ | grep $(uniquehotspot_ssid -s))" ]
		then
	
			nmcli connection add type wifi ifname '*' con-name $(uniquehotspot_ssid -s) autoconnect yes ssid $(uniquehotspot_ssid -s)
			nmcli connection modify $(uniquehotspot_ssid -s) 802-11-wireless.mode ap 802-11-wireless.band bg ipv4.method shared
			nmcli connection modify $(uniquehotspot_ssid -s) 802-11-wireless-security.key-mgmt wpa-psk 802-11-wireless-security.psk $(uniquehotspot_password -s)
		
		else
			echo "$(uniquehotspot_ssid -s) is already setup."
		fi
else
	echo "Selected No, moving on to ZRAM installation"
fi
