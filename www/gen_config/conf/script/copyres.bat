if exist ..\..\config\ del /f /s /q ..\..\config\*.php
if exist ..\..\config\ copy /y ..\outputServer\*.php ..\..\config\
