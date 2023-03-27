#!../../bin/linux-x86_64/dummy

#- You may have to change dummy to something else
#- everywhere it appears in this file

< envPaths

cd "${TOP}"

## Register all support components
dbLoadDatabase "dbd/dummy.dbd"
dummy_registerRecordDeviceDriver pdbbase

## Load record instances
# dbLoadTemplate "db/wf.substitutions"
dbLoadTemplate "db/scalars1.substitutions"
dbLoadTemplate "db/waveforms1.substitutions"

cd "${TOP}/iocBoot/${IOC}"
iocInit
