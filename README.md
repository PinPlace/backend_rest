install tmux
i.e. `sudo yum install tmux`
`tmux`
`cd /opt`
`cd Python-3.9.6`
`python3.9 -V ` to check
on setup for env: `python3.9 -m venv env`
`source env/bin/activate`

cd into backend/pinplace i.e `cd ~/backend_rest/`
`python manage.py runserver 0.0.0.0:8000`

`deactivate` for python env
Then, when you want to disconnect tmux, you do `Ctrl+B`, `D` (ie press Ctrl+B, then release both keys, and then press d)

When you login again, you can run `tmux attach` and you will reconnect to tmux and see all the output that happened.
