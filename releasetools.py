import common
import edify_generator

def InstallSuperSU(info):
    supersu = info.input_zip.read("META/supersu/supersu.zip")
    common.ZipWriteStr(info.output_zip, "supersu/supersu.zip", supersu)

def FlashSUperSU(info):
    info.script.AppendExtra(('ui_print("Flashing SuperSU...");'))
    info.script.AppendExtra(('package_extract_dir("supersu", "/tmp/supersu");'))
    info.script.AppendExtra(('run_program("/sbin/busybox", "unzip", "/tmp/supersu/supersu.zip", "META-INF/com/google/android/*", "-d", "/tmp/supersu");'))
    info.script.AppendExtra(('run_program("/sbin/busybox", "sh", "/tmp/supersu/META-INF/com/google/android/update-binary", "dummy", "1", "/tmp/supersu/supersu.zip");'))

def MountData(info):
    info.script.AppendExtra(('run_program("/sbin/busybox", "mount", "/data");'))

def FullOTA_InstallEnd(info):
    InstallSuperSU(info)
    FlashSUperSU(info)
    MountData(info)

