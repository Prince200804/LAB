code:
mov ax,[1000h]
mov bx,[1002h]
mov cl,00h
add ax,bx
mov [1004h],ax
jnc jump
inc cl
jump:
mov [1006h],cl
hlt