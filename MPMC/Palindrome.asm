data segment
    msg1 db 10,13,"Enter the String:$"
    msg2 db 10,13,"String is Palindrome$"
    msg3 db 10,13,"String is not Palindrome$"
    str db 50 dup(0)
data ends

code segment
    assume CS:code, DS:data

start:
    mov AX, data
    mov DS, AX

    lea dx, msg1
    mov ah, 09h
    int 21h

    lea SI, str
    lea DI, str
    mov ah, 01h

next:
    int 21h
    cmp al, 0Dh
    je terminate
    mov [di], al
    inc di
    jmp next

terminate:
    mov al, '$'
    mov [di], al

logic:
    dec di
    mov al, [si]
    cmp [di], al
    jne notPalindrome
    inc si
    dec di
    cmp si, di
    jl logic

Palindrome:
    mov ah, 09h
    lea dx, msg2
    int 21h
    jmp xx

notPalindrome:
    mov ah, 09h
    lea dx, msg3
    int 21h

xx:
    mov ah, 4Ch
    int 21h

code ends
end start