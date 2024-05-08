data segment
string1 db 99h,12h,22h,45h,10h
ends

code segment
assume cs:code ds:data
start:
mov ax,data
mov ds,ax 

mov ch,05h

UP2:
mov cl,05h
lea si,string1

UP1:
mov al,[si]
mov bl,[si+1]
cmp al,bl
jnc down
mov dl,[si+1]
xchg [si],dl
mov [si+1],dl

down: 
inc si
dec cl
jnz UP1
dec ch 
jnz UP2

code ends
end start
 
