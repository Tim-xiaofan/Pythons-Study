APP = call
# all source are stored in SRCS-y
SRCS-y := call.c

PKGCONF?= pkg-config
CFLAGS += -g -Wall -fPIE $(shell $(PKGCONF) --cflags python3-embed)
LIBS += $(shell $(PKGCONF) --libs python3-embed)

$(APP): $(SRCS-y)
	$(CC) $(SRCS-y) -o $@ $(CFLAGS) $(LIBS)
