#!/bin/sh
rm -f ../../../super3_server_res/$1/res/scripts/app/config/*.xml

cp -f ../outputServer/*.xml ../../../super3_server_res/$1/res/scripts/app/config/
cp -f ../outputServer/*.version ../../../super3_server_res/$1/res/scripts/app/config/
cp -f ../outputServer/errorData.py ../../../super3_server_res/$1/res/scripts/app/common/protocol/

cp -f ../outputCheckServer/*.lua ../../../super3_share/trunk/skygame/config/
cp -f ../Resources/ui/battlecheck/*.lua ../../../super3_share/trunk/skygame/logic/check_battle/battle/
