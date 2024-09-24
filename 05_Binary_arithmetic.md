##### _Written in Markdown by Onni Kivinen_ - https://github.com/onnikiv/Hardware1_Digital-Circuits
# Digital Circuits - 5 Binary Arithmetic
Fifth week's assignments

### 1.1 Computation of 8-bit unsigned numbers, if possible or not.

a) ✅ $27 + 55$ __is possible__  
b) ❌ $13 - 19$ __is not possible__, the answer is negative and the 8-bit unsigned range is from 0 to 255, so cant be negative.  
c) ✅ $39 - 16$ __is possible__   
d) ❌ $359 - 219$ __is not possible__, because 359 is out of the 8-bit range (0-255).   
e) ❌ $192 + 71 = 263$ __is not possible__, out of 8-bit range.   
f) ✅ $42 + 33$ __is possible.__

___

### 1.2 Hexadecimal to decimal

a) $0x19 = (1 \cdot 16^1) + (9 \cdot 16^0) =  \textbf{25}$   
b) $0x100 =(1 \cdot 16^2) + (0 \cdot 16^1) + (0 \cdot 16^0) = \textbf{256}$  
c) $0xBEEF = (11 \cdot 16^3) + (14\cdot 16^2) + (14\cdot 16^1) + (15 \cdot 16^0) = \textbf{48679}$   
d) $0xACE = (10 \cdot 16^2) + (12 \cdot 16^1) + (14 \cdot 16^0) = \textbf{2766}$  
e) $0x2022 = (2 \cdot 16^3) + (0 \cdot 16^2) + (2 \cdot 16^1) + (2 \cdot 16^0) = \textbf{8226}$   
f) $0xAC0DE5 = (10 \cdot 16^5) + (12 \cdot 16^4) + (0 \cdot 16^3) + (13 \cdot 16^2) + (14 \cdot 16^1) + (5 \cdot 16^0) = \textbf{11275749}$

___

### 1.3 Base-10 numbers to binary and 2's complement arithmetic.
- Adding bits so there is __no overflow__.


a) $67-5$  
**Numbers to binary**
 - $67_{10} = 01000011_2$ (8 bits)
 - $5_{10} =  00000101_2$ (8 bits)   
```
1. Inversion of 5: 00000101 → 11111010  
2. Adding 1

      11111010
    + 00000001
    ---------
      11111011
```
 **Calculation 67 + (-5):**
 ```
    11000011   
     01000011  (67)
   + 11111011  (-5)
   -----------
     00111110  (62)

8 bits needed for this calculation.
```

---
b) $123 + 998 - 754$   
**Numbers to binary**
 - $123_{10} =  000001111011_2$ (12 bits)
 - $998_{10} =  001111100110_2$ (12 bits) 
 - $754_{10} =  001011110010_2$ (12 bits)

 ```
 1. Inversion of 754: 001011110010 → 110100001101
 2. Adding 1
    
    110100001101
  +  00000000001
  -------------
    110100001110  (-754)
 ```

 **Calculation  123 + 998:**
 ```
      111111111
     000001111011  (123, 12bit)
   + 001111100110  (998, 12bit)
   ---------------
     010001100001  (1121, 12bit)
```
 **Calculation  1121 + (-754):**
```
     11
      010001100001  (1121)
    + 110100001110  (-754)
    ---------------
      000101101111  (367, 12bit)

Atleast 12 bits are needed for this calculation.
```

___

c) $45 - 124$   
**Numbers to binary**  
 - $45_{10} = 00101101_2$ (8 bits)
 - $124_{10} = 01111100_2$ (8 bits)

```
 1. Inversion of 124: 0111 1100 → 10000011
 2. Adding 1 
    
         11
    10000011
  + 00000001
  ----------
    10000100  (-124)
```
 **Calculation  45 + (-124):**
 ```
       11
    00101101  (45)
  + 10000100  (-124)
  ----------
    10110001  (-79, 8bit)

Atleast 8 bits are needed for this calculation.
```

d) $-78 -23$   
**Numbers to binary**  
 - $78_{10} = 01001110_2$ (8 bits)
 - $23_{10} = 00010111_2$ (8 bits)

```
 1. Inversion of 78: 01001110 → 10110001
 2. Adding 1

          1
    10110001
  + 00000001
  ----------
    10110010  (-78)
```
```
 1. Inversion of 23: 00010111 → 11101000
 2. Adding 1
    
    11101000  
  + 00000001
  ----------
    11101001  (-23)
```

 **Calculation  -78 + (-23):**
```
   111
    10110010  (-78)
  + 11101001  (-23)
  ----------
    10011011  (-101, 8bit)

Atleast 8 bits are needed for this calculation.
```

___

### 1.4 Signed 16-bit numbers, and their following calculations.
$A = 0xABBA$   
$B = 0x0ACE$   
$C = 0x1974$   