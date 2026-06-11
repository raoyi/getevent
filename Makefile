.DELETE_ON_ERROR:

CC := $(CROSS_COMPILE)gcc
TARGET := $(shell $(CC) -dumpmachine)
INPUT_H := $(firstword $(wildcard \
    /usr/$(TARGET)/include/linux/input.h \
    /usr/$(TARGET)/usr/include/linux/input.h \
    /usr/include/linux/input.h))

getevent: getevent.c input.h-labels.h
	$(CC) -o $@ $<

input.h-labels.h:
	python3 ./generate-input.h-labels.py $(INPUT_H) > $@

clean:
	-rm -f getevent input.h-labels.h
