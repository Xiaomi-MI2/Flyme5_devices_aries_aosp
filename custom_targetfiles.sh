echo ">>> in $0"
OUT_DIR=out/merged_target_files

rm -v -rf $OUT_DIR/SYSTEM/data
cp -v -rf other/data $OUT_DIR/SYSTEM
cp -v -rf other/supersu $OUT_DIR/META
