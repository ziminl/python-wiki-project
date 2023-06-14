# python-wiki-project

#usage
> python manage.py makemigrations
> python manage.py migrate
> > html in wiki\wiki\templates\articles


edit settings.py 
```
ALLOWED_HOSTS = ['localhost', 'x.x.x.x']
```
for port foward



project with @ptn. ended in 2019


not in port 80, white list port in defender 
제어판\시스템 및 보안\Windows Defender 방화벽 -> 고급설정 -> 인바운드 규칙 -> 새 규칙 -> 포트 -> TCP and 특정 로컬 포트 설정[8000]  -> 연결 허용 설정 -> 도메인/개인/공용 -> 이름 설정하고 마침하면 끝 
