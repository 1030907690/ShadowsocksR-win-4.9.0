@Echo Off
Title ��GitHub�ƶ˸��� SSR �����ļ�
cd /d %~dp0
wget --no-check-certificate https://fastly.jsdelivr.net/gh/Alvin9999/pac2@latest/ssconfig.txt

if exist ssconfig.txt goto startcopy
echo ip����ʧ�ܣ�����������һ��
pause
exit
:startcopy

del "..\gui-config.json_backup"
ren "..\gui-config.json"  gui-config.json_backup
b64 -d ssconfig.txt gui-config.json
copy /y "%~dp0gui-config.json" ..\gui-config.json
del "%~dp0ssconfig.txt"
del "%~dp0gui-config.json"
ECHO.&ECHO.�Ѹ���SSR�����ļ�,������SSR���� &PAUSE >NUL 2>NUL
exit