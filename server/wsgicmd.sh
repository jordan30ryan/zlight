uwsgi -s /tmp/zlight.sock --manage-script-name --mount /=zlight:app --virtualenv /home/ec2-user/zlight/server/venv --plugin python3 --http :5000
