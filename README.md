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













how to write wiki





text 

굵게 ** ** 또는 __ __
기울임꼴 * * 또는 _ _
취소선~~ ~~ 
굵게 및 중첩된 기울임꼴	** ** 및 _ _
모든 굵게 및 기울임꼴	*** ***
아래 첨자	<sub> </sub>
위 첨자	<sup> </sup>

텍스트 인용 : >
title : # or ## or ###


리스트 : 
1.
2.
    1.
    2.

images ![Tux, the Linux mascot](/assets/images/tux.png)

images : ![img](<link>)

code block : four spaces or one tab. When they’re in a list, indent them eight spaces or two tabs.




