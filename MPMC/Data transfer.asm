DATA SEGMENT
    SOURCE DB 10H
    DEST DB ?
DATA ENDS

CODE SEGMENT
ASSUME CS:CODE, DS:DATA

START:
    MOV AX, DATA
    MOV DS, AX

    MOV AL, [SOURCE]
    MOV [DEST], AL

    MOV AH, 4Ch
    INT 21h

CODE ENDS
END START