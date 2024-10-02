##### _Written in Markdown by Onni Kivinen_ - https://github.com/onnikiv/Hardware1_Digital-Circuits
# Digital Circuits - 6 Sequential Circuits
Sixth week's assignments

### 1.1 Sequential circuits and ASM method 

![alt text](/images/06_Sequential-1.1.png)   
#### Since there is (_14_) stateboxes or states, we can calculate how many flip-flops (FF) we need:

__k__ = number of __flip-flops__ and __s__ = number of __states__   
$2^k \geq s$ _or_ $k \geq log_2(s)$

- $k \geq log_2(14)$
- $k \geq 3.8073$
- $k ≈ 4$
- So atleast __4__ flip-flops are needed.   

The ASM chart shows that the system has (__3 unique__) output signals:
 - sis
 - ssis
 - ul

The system is a __Mealy__ state machine, because on some of the branches the outputs depend on the current state and the input values.

___

### 1.2 ASM-chart clock cycle

