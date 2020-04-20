cd /etc/openvpn
cp /usr/share/doc/openvpn/examples/sample-config-files/client.conf client.ovpn
echo "key-direction 1" >> client.ovpn
echo "<ca>" >> client.ovpn
sed -n '/BEGIN CERTIFICATE/,/END CERTIFICATE/p' < ca.crt >> client.ovpn
echo "</ca>" >> client.ovpn
echo "<cert>" >> client.ovpn
sed -n '/BEGIN CERTIFICATE/,/END CERTIFICATE/p' < client.crt >> client.ovpn
echo "</cert>" >> client.ovpn
echo "<key>" >> client.ovpn
sed -n '/BEGIN PRIVATE KEY/,/END PRIVATE KEY/p' < client.key >> client.ovpn
echo "</key>" >> client.ovpn
