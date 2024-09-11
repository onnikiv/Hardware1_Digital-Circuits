##### _Written in Markdown by Onni Kivinen_ - https://github.com/onnikiv/Hardware1_Digital-Circuits
# Digital circuits - 3 Boolean Algebra
Third week's assignments


### 1.1 De Morgan's theorem

$\overline{\overline A + B} → \overline{\overline A} \cdot \overline B = A \cdot \overline B$

$\overline{A \cdot \overline B \cdot \overline C} → \overline A + \overline{\overline B} + \overline{\overline C} = \overline A + B + C$

$\overline{(\overline A + B) \cdot (A + \overline B)} → (\overline{\overline A} \cdot \overline B) + (\overline A \cdot \overline{\overline B}) = (A \cdot \overline B) + (\overline A \cdot B)$

___

### 1.2 Canonical SOP and POS

Truth table
| | A | B | F |       |
|-|:-:|--:|--:|------:|
|$_o$| 0 | 0 | 1 | ← SOP |
|$_1$| 0 | 1 | 0 | ← POS |
|$_2$| 1 | 0 | 1 | ← SOP |
|$_3$| 1 | 1 | 0 | ← POS |

In the Sum of Products (SOP) we need to find where the function F has a value 1.

$F(A,B) = \overline A \cdot \overline B + A \cdot \overline B$

$F(A,B) = m0 + m2$

$F(A,B) = Σm(0,2)$


In the Product of Sums (POS) we need to find where function F has a value 0.

$F(A,B) = (A + \overline B) \cdot (\overline A + \overline B)$

$F(A,B) = M1 \cdot M3$

$F(A,B) = ΠM(1,3)$

___

### 1.3 Truth table from a standard expression

Truth table for F

$F(A,B) = A \overline B + B$

| A | B | F | Calculation  |
|:--|---|--:|:-------------|
| 0 | 0 | 0 | ← $F(0,0) = 0 \cdot \overline 0 + 0 = 0 \cdot 1 + 0 = 0$|
| 0 | 1 | 1 | ← $F(0,1) = 0 \cdot \overline 1 + 1 = 0 \cdot 0 + 1 = 1$|
| 1 | 0 | 1 | ← $F(1,0) = 1 \cdot \overline 1 + 1 = 1 \cdot 0 + 1 = 1$|
| 1 | 1 | 1 | ← $F(1,1) = 1 \cdot \overline 0 + 1 = 1 \cdot 1 + 1 = 1$|

Truth table for G

$G(A,B) = (A+B) \cdot (\overline A + \overline B)$

| A | B | G | Calculation  |
|:--|---|--:|:--|
| 0 | 0 | 0 | ← $G(0,0) = (0+0) \cdot (\overline 0 + \overline 0) = 0 \cdot (1+1) = 0$ |
| 0 | 1 | 1 | ← $G(0,1) = (0+1) \cdot (\overline 0 + \overline 1) = 1 \cdot (1+0) = 1$ |
| 1 | 0 | 1 | ← $G(1,0) = (1+0) \cdot (\overline 1 + \overline 0) = 1 \cdot (0+1) = 1$ |
| 1 | 1 | 0 | ← $G(1,1) = (1+1) \cdot (\overline 1 + \overline 1) = 1 \cdot (0+0) = 0$ |

___

### 1.4 De Morgan’s theorem in programming

