#########################################################################
##
## Build Makefile for FRAMETHROWER
##
#########################################################################


 COMPILER = gcc -g -pthread -Wall 
 BIN_PATH = .
 COMP_FLAG =  -D__C_APPL 

 TARGET = FT 
 HDRFILES =  -I./   
 LIBFILES = -L/usr/include

########################################################################
## Define local c/cpp file(s)
########################################################################
COBJECTS = \
file_read.o\
framethrower.o\
ft_lib.o\
ft_socket_utils.o\
ft_thread_utils.o

## Define possible compiler flags
#######################################################################
CFLAGS = $(COMP_FLAG) $(HDRFILES)

CC = $(COMPILER) $(HDRFILES) #$(COMP_FLAG)

#######################################################################
## Define make targets
#######################################################################
RM = rm
RM1 = rm -rf obj
MKDIR = mkdir obj
MV = mv *.o obj/


.PHONY: all
all: $(COBJECTS)
	$(CC)  $(LIBFILES) -o $(TARGET) $(COBJECTS) 
	$(MKDIR) 
	$(MV) 
.PHONY: clean
clean:
	$(RM1) $(COBJECTS) $(TARGET)

.PHONY: debug
debug: $(COBJECTS)
	$(COMPILER) $(LIBFILES) -o $(TARGET) $(COBJECTS)  


