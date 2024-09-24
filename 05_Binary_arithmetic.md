##### _Written in Markdown by Onni Kivinen_ - https://github.com/onnikiv/Hardware1_Digital-Circuits
# Digital Circuits - 5 Binary Arithmetic
Fifth week's assignments

### 1.1 Computation of 8-bit unsigned numbers, if possible or not.

a) $27 + 55$ __is possible__  
b) $13 - 19$ __is not possible__, the answer is negative and the 8-bit unsigned range is from 0 to 255, so cant be negative.  
c) $39 - 16$ __is possible__   
d) $359 - 219$ __is not possible__, because 359 is out of the 8-bit range (0-255).   
e) $192 + 71 = 263$ __is not possible__, out of 8-bit range.   
f) $42 + 33$ __is possible.__

___

### 1.2 Hexadecimal to decimal

a) $0x19 = (1 \cdot 16^1) + (9 \cdot 16^0) =  25$   
b) $0x100 =(1 \cdot 16^2) + \sout{(0 \cdot 16^1)} + \sout{(0 \cdot 16^0)} = 256$  
c) $0xBEEF = (11 \cdot 16^3) + (14\cdot 16^2) + (14\cdot 16^1) + (15 \cdot 16^0) = 48679$   
d) $0xACE = (10 \cdot 16^2) + (12 \cdot 16^1) + (14 \cdot 16^0) = 2766$  
e) $0x2022 = (2 \cdot 16^3) + \sout{(0 \cdot 16^2)} + (2 \cdot 16^1) + (2 \cdot 16^0) = 8226$   
f) $0xAC0DE5 = (10 \cdot 16^5) + (12 \cdot 16^4) + \sout{(0 \cdot 16^3)} + (13 \cdot 16^2) + (14 \cdot 16^1) + (5 \cdot 16^0) = 11275749$

___

### 1.3 Base-10 numbers to binary and 2's complement arithmetic.

a)  **Numbers to binary**
 - $67_{10} = 1000011_2$ (7 bits)
 - $5_{10} =  0000101_2$ (7 bits)   
 - Inversion: `0000101` → `1111010`
   - Add 1:
     - ```
         1111010
       + 0000001
       ---------
         1111011
       ```
 **Calculation 67 + (-5):**
 ```
     1000011  (67)
   + 1111011  (-5)
   -----------
     1101110  (62)
```