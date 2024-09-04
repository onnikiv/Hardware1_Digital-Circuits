##### _Written in Markdown by Onni Kivinen_ - https://github.com/onnikiv/Hardware1_Digital-Circuits
# Digital circuits - 2 Expressions and truth table
Second week's assignments

### 1.1 Truth table
| A | B | F |
|:--|---|--:|
| 0 | 0 | 1 |
| 1 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 1 | 1 |

| A | B | G |
|:--|---|--:|
| 0 | 0 | 1 |
| 1 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 1 | 0 |

___
### 1.2 Truth table and expression from verbal description

| Button 1 | Button 2 | Alarm | Vault door |
|:--------:|:--------:|:-----:|:----------:|
|    1     |    0     |   0   |     0      |
|    1     |    1     |   0   |     1      |
|    1     |    1     |   1   |     0      |
|    1     |    0     |   1   |     0      |
|    0     |    1     |   0   |     0      |
|    0     |    1     |   1   |     0      |
|    0     |    0     |   1   |     0      |
|    0     |    0     |   0   |     0      |
___
### 1.3 Evaluate expression

>#### Basic logical operations:
>| Operation | Symbol |
>|:---------:|:------:|
>| $$AND$$   | $$\cdot$$|
>| $$OR$$    | $$+$$  |
>| $$NOT$$   | $$ \overline{A} $$|


Functions F and G:

$$F = \overline{A}\cdot{C}+B\cdot\overline{C}$$
$$G = (A + B) \cdot (\overline{B} + \overline{C})$$

Values of both functions when:

**A = 0**

**B = 1**

**C = 1**

|Function F                                       |
|:------------------------------------------------|
|$$F = \overline{A}\cdot{C}+B\cdot\overline{C}$$  |                              
|$$F = \overline{0} \cdot{1}+1 \cdot\overline{1}$$|
|$$F = 1 \cdot{1}+1 \cdot{0}$$                    |
|$$F = 1 +1 \cdot{0}$$                            |
|$$F = 1 + 0 $$                                   |
|$$F = 1$$                                        |

|Function G                                         |
|:--------------------------------------------------|
|$$G = (A + B) \cdot (\overline{B} + \overline{C})$$|                              
|$$G =(0+1) \cdot {(\overline{1} + \overline{1})} $$|
|$$G =(0+1) \cdot {({0} + {0})} $$                  |
|$$G = 1 \cdot 0$$                                  |
|$$G = 0$$                                          |
___
### 1.4 Expression from circuit diagram
Construct an expression defining function L(A, B, C, D) represented in the following circuit
diagram:
![alt text](images/02_Expressions-1.4.png)
