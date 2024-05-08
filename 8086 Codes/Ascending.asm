data segment
string1 db 99h,12h,56h,45h,36h
data ends

code segment
assume cs:code ds:data
start:
mov ax,data
mov ds,ax

mov ch,04h

UP2: mov cl,04h
lea si,string1

UP1: mov al,[si]
mov bl,[si+1]  
cmp al,bl
jc down
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