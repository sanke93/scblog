pkill gunicorn
gunicorn scblog.wsgi --bind 127.0.0.1:8000  --daemon --log-file ~/sanket-website/logs/scblog_gunicorn.log --workers=3
