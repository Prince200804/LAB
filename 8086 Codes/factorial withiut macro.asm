data segment 
a db 5
fact db ?
ends

code segment
assume cs:code ds:data
start:
mov ax,data
mov ds,ax
mov ah,00h
mov al,a
LI:
dec a
mul a
mov cl,a
cmp cl,01
jnz li    
mov fact,al
code ends 
end start