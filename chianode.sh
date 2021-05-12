sudo cp chianode.service /etc/systemd/system/
systemctl daemon-reload
systemctl start chianode
systemctl enable chianode

export FLASK_APP=chianode.py
flask run