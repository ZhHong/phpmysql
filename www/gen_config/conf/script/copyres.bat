if exist ..\Resources\db\ copy /y ..\outputClient\*.lua ..\Resources\db\
if exist ..\Resources\network\ copy /y ..\outputServer\Protocol.xml ..\Resources\network\
if exist ..\Resources\network\ copy /y ..\outputServer\protocol.version ..\Resources\network\

if exist ..\..\..\super3_server_res\%1\res\scripts\app\config\ del /f /s /q ..\..\..\super3_server_res\%1\res\scripts\app\config\*.xml
if exist ..\..\..\super3_server_res\%1\res\scripts\app\config\ copy /y ..\outputServer\*.xml ..\..\..\super3_server_res\%1\res\scripts\app\config\
if exist ..\..\..\super3_server_res\%1\res\scripts\app\config\ copy /y ..\outputServer\*.version ..\..\..\super3_server_res\%1\res\scripts\app\config\
if exist ..\..\..\super3_server_res\%1\res\scripts\app\common\protocol\ copy /y ..\outputServer\errorData.py ..\..\..\super3_server_res\%1\res\scripts\app\common\protocol\

if exist ..\..\..\super3_share\trunk\skygame\config\ copy /y ..\outputCheckServer\*.lua ..\..\..\super3_share\trunk\skygame\config\
if exist ..\..\..\super3_share\trunk\skygame\logic\check_battle\battle\ copy /y ..\Resources\ui\battlecheck\*.lua ..\..\..\super3_share\trunk\skygame\logic\check_battle\battle\
