#environment
apt-get install python3-venv
echo "creating venv" &&
python3 -m venv ./venv &&
echo "activating venv" &&
source venv/bin/activate &&
echo "install requirements" &&
pip3 install -r requirements.txt &&

#service
sudo cp chianode.service /etc/systemd/system/ &&
systemctl daemon-reload &&
systemctl start chianode &&
systemctl enable chianode