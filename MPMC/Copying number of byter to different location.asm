org 00H
sjmp start
org 30H

start: mov R0, #40H
       mov R1, #50H
       mov R7, #0AH

back:  mov A, @R0
       mov @R1, A
       INC R0
       INC R1
       DJNZ R7, back

Here:  sjmp Here
end
