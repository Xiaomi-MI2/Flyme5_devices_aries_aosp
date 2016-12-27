#!/system/bin/sh
RAW_ID=`cat /sys/devices/system/soc/soc0/raw_id`
case "$RAW_ID" in
     "1812")
     sed -i 's/MI 2/MI 2S/g' /system/build.prop     
     ;;
esac
