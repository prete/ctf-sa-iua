##include <string.h>
##include <stdio.h>
##include <assert.h>
#int main(int argc, char*argv[]){
#    char buf[256];
#
#    read(0,buf,256);
#    assert( strstr(buf, "WIN!") == NULL);
#
#    printf(buf);
#
#return 0;
#}

#import struct 
import commands

for i in range(256):
	args = i*'%x'
	o = commands.getoutput('./09-challenge '+args)
	if 'fault' in o:
		print(i, o)
		
#with open('./09-challenge.win','wb') as win:
#	win.write("YOU %s")
