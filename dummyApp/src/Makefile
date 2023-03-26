TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# Use typed rset structure (see 3.16.1 release notes)
USR_CPPFLAGS += -DUSE_TYPED_RSET

# Build an IOC support library
LIBRARY_IOC += dummySupport

dummySupport_LIBS += $(EPICS_BASE_IOC_LIBS)

# Build the IOC application
PROD_IOC = dummy

# dummy.dbd will be created and installed
DBD += dummy.dbd

# dummy.dbd will include these files:
dummy_DBD += base.dbd
# use our menu scan definition with 0.05 and 0.07 s
dummy_DBD += menuScan.dbd

# dummy_registerRecordDeviceDriver.cpp derives from dummy.dbd
dummy_SRCS += dummy_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
dummy_SRCS_DEFAULT += dummyMain.cpp
dummy_SRCS_vxWorks += -nil-

# Finally link IOC to the EPICS Base libraries
dummy_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

# Explicit dependency needed for generated header file
devdummyVersion$(DEP): $(COMMON_DIR)/$(GENVERSION)
