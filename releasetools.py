import common
import edify_generator

def InstallSuperSU(info):
    supersu = info.input_zip.read("META/supersu/supersu.zip")
    common.ZipWriteStr(info.output_zip, "system/supersu/supersu.zip", supersu)

def RawID(info):
    info.script.AppendExtra(('set_metadata("/system/bin/raw_id.sh", "uid", 0, "gid", 0, "mode", 0777, "capabilities", 0x0, "selabel", "u:object_r:system_file:s0");'))

def FlashSUperSU(info):
    info.script.AppendExtra(('ui_print("Flashing SuperSU...");'))
    info.script.AppendExtra(('package_extract_dir("system/supersu", "/tmp/supersu");'))
    info.script.AppendExtra(('run_program("/sbin/busybox", "unzip", "/tmp/supersu/supersu.zip", "META-INF/com/google/android/*", "-d", "/tmp/supersu");'))
    info.script.AppendExtra(('run_program("/sbin/busybox", "sh", "/tmp/supersu/META-INF/com/google/android/update-binary", "dummy", "1", "/tmp/supersu/supersu.zip");'))

def MountData(info):
    info.script.AppendExtra(('run_program("/sbin/busybox", "mount", "/data");'))

def FullOTA_InstallEnd(info):
    InstallSuperSU(info)
    RawID(info)
    FlashSUperSU(info)
    MountData(info)

