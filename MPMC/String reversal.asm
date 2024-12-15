DATA SEGMENT
    MAX_LEN DB 100
    INPUT_STRING DB MAX_LEN DUP(?)
    OUTPUT_STRING DB MAX_LEN DUP(?)
    LENGTH DB ?
DATA ENDS

CODE SEGMENT
START:
    MOV AX, @DATA
    MOV DS, AX

    MOV AH, 0Ah
    LEA DX, INPUT_STRING
    INT 21h

    MOV SI, OFFSET INPUT_STRING
    MOV CL, [SI + 1]
    MOV LENGTH, CL

    LEA SI, INPUT_STRING + 2
    LEA DI, OUTPUT_STRING + 2
    MOV CX, LENGTH
    ADD DI, CX
    DEC DI

REVERSE_LOOP:
    LODSB
    STOSB
    DEC DI
    LOOP REVERSE_LOOP

    ADD DI, CX
    MOV BYTE PTR [DI], '$'

    MOV AH, 09h
    LEA DX, OUTPUT_STRING + 2
    INT 21h

    MOV AH, 4Ch
    INT 21h
CODE ENDS
END START