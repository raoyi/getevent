.DELETE_ON_ERROR:

getevent: getevent.c input.h-labels.h
	$(CROSS_COMPILE)gcc -o $@ $<

input.h-labels.h:
	python3 ./generate-input.h-labels.py > $@

clean:
	-rm -f getevent input.h-labels.h
