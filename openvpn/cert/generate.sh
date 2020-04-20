# https://chichivica.github.io/2017/08/02/Install-OpenVPN-on-Fedora-26/
# install openvpn easy-rsa

DIR="/home/oche/Configuration/OpenVPN/cert/rsa"
TARGET="/home/oche/Configuration/OpenVPN/cert/cert"
#TARGET="/etc/openvpn/server"

# Init

mkdir $DIR
mkdir $TARGET

cp -ai /usr/share/easy-rsa/3/* $DIR
cd $DIR

./easyrsa init-pki
./easyrsa build-ca nopass

# Server
./easyrsa build-server-full server nopass

# Client
./easyrsa build-client-full client nopass

./easyrsa gen-dh
openvpn --genkey --secret pki/ta.key

# Copy

cp $DIR/pki/issued/server.crt   $TARGET
cp $DIR/pki/private/server.key  $TARGET
cp $DIR/pki/issued/client.crt   $TARGET
cp $DIR/pki/private/client.key  $TARGET
cp $DIR/pki/private/ca.key      $TARGET
cp $DIR/pki/ca.crt              $TARGET
cp $DIR/pki/dh.pem              $TARGET
cp $DIR/pki/ta.key              $TARGET
