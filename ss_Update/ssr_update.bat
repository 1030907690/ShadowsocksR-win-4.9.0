@Echo Off
Title ��GitHub�ƶ˸��� SS �����ļ�
python ssr_update.py
del "..\gui-config.json_backup"
ren "..\gui-config.json"  gui-config.json_backup
certutil -decode %~dp0ssconfig.txt %~dp0gui-config.json
copy /y "%~dp0gui-config.json" ..\gui-config.json
del "%~dp0ssconfig.txt"
del "%~dp0gui-config.json"
ECHO.&ECHO.�Ѹ���SSR�����ļ�,�밴������˳�,����������. &PAUSE >NUL 2>NUL