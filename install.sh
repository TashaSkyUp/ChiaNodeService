#environment
python3 -m venv ./venv &&
source venv/bin/activate &&
pip3 install -r requirements.txt &&

#service
sudo cp chianode.service /etc/systemd/system/ &&
systemctl daemon-reload &&
systemctl start chianode &&
systemctl enable chianode