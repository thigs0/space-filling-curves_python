# space-filling-curves_python

## To product a video about Space-filling curve, i did a code based on Lindenmayer system, with objective animate with python  

It can be used to teach about recursive functions, to product video and teach childrens about the turtle power.

To construct the curve faster, use https://github.com/PrincetonLIPS/numpy-hilbert-curve

**Corrigir:**

- The 3d curves have a error at constants. At both

- The Gosper_Flowsnake_curve have a little erro that make the iteraction >3 colapse in some lines
**Plus**
  - Add proprietis to change colors with make the iteractions
  
  
  **How to use**
  
  - Install the package
  > **pip install L-SpaceCurves**
  
```
from L_SpaceCurves import L_SpaceCurves_animation as ls

l = ls.L_SpaceCurves(leng=10, speed=0, iter=2, origin=(0, 0))
# leng is the size of each line to construct the curve
# speed is the speed to contruct the curve. 0 fast, 10 sloow
# iter is the total of iteractions that you wish (more iteractions is more time)
$ origin is a tuple that set the origin of curve ( nor always the center od curve is the center od figure)
```

 ```
from L_SpaceCurves import L_SpaceCurves as ls

l = ls.L_SpaceCurves(leng=10, speed=0, iter=2, origin=(0, 0))
# leng is the size of each line to construct the curve
# speed is the speed to contruct the curve. 0 fast, 10 sloow
# iter is the total of iteractions that you wish (more iteractions is more time)
$ origin is a tuple that set the origin of curve ( nor always the center od curve is the center od figure)
```
  
  - to plot in 2D, only select the start letter. Choose one below
  
  - to plot in 3D, select the start letter and call the function "plot()"
  
<b>All the operations have reference of vector (1, 0, 0, ....) </b>
## 2D Curves 

#### sierspinski curve
![hilbert_curve](/imagem/sierpins.png)

**Letters**
| P | R | S | Z|
|----------|----------|----------|----------|
| ![Hilbert_A_2](/imagem/sierpinski_P_2.png) | ![Hilbert_B_2](/imagem/sierpinski_R_2.png) | ![Hilbert_C_2](/imagem/sierpinski_S_2.png) | ![Hilbert_H_2](/imagem/sierpinski_Z_2.png)|

**Gramatics**

- First Grammar

<p> <b>S</b> <b>R</b> <b>P</b> <b>S</b> </p>

- Second Grammar
<p> <b>R</b> <b>Z</b> <b>S</b> <b>R</b> </p>

- Third Grammar

<p> <b>P</b> <b>S</b> <b>Z</b> <b>P</b> </p>

- fourth Grammar

<p> <b>Z</b> <b>P</b> <b>R</b> <b>Z</b> </p>



#### Hilbert curve
 ![hilbert_curve](https://user-images.githubusercontent.com/99839465/196053916-4f20a51f-f35f-4242-988a-19b46be8510a.GIF)

**Letters**
| A | B | C | D|
|----------|----------|----------|----------|
| ![Hilbert_A_2](/imagem/Hilber_A_2.png) | ![Hilbert_B_2](/imagem/Hilbert_B_2.png) | ![Hilbert_C_2](/imagem/Hilbert_C_2.png) | ![Hilbert_H_2](/imagem/Hilbert_H_2.png)|


**Gramatics**
- First Grammar
<p> <b>A</b> &uarr; <b>H</b> &rarr; <b>H</b> &darr; <b>B</b> </p>

- Second Grammar
<p> <b>H</b> &rarr; <b>A</b> &uarr; <b>A</b> &larr; <b>C</b> 
</p>

- Third Grammar
<p> <b>C</b> &larr; <b>B</b> &darr; <b>B</b> &rarr; <b>H</b> 
</p>

- fourth Grammar
<p> <b>B</b> &darr; <b>C</b> &larr; <b>C</b> &uarr; <b>A</b>  
</p>

#### Peano curve 
![Peano_curve](https://user-images.githubusercontent.com/99839465/196053748-82ab6283-ed5d-4b40-b444-6f5ea853b144.GIF)

**Letters**
| P | Q | R | S|
|----------|----------|----------|----------|
| ![Peano_P_2](/imagem/Peano_P_2.png) | ![Peano_Q_2](/imagem/Peano_Q_2.png) | ![Peano_R_2](/imagem/Peano_R_2.png) | ![Peano_S_2](/imagem/Peano_S_2.png)|
|<p>&larr; &rarr; &rarr; &larr; &larr; </p>|<p>&larr; &larr; &larr; &rarr; &rarr; </p>|<p>&rarr; &rarr;&rarr; &larr; &larr;</p>|<p>&rarr; &larr;&larr;&rarr; &rarr;</p>|

**Gramatics**
- First Grammar
<p> <b>P</b> &uarr; <b>Q</b> &uarr; <b>P</b> &rarr; <b>S</b> &darr; <b>R</b> &darr; <b>S</b> &darr; <b>P</b> &uarr; <b>Q</b> &uarr; <b>P</b></p>

- Second Grammar
<p> <b>Q</b> &uarr; <b>P</b> &uarr; <b>Q</b> &larr; <b>R</b> &darr; <b>S</b> &darr; <b>R</b> &larr; <b>Q</b> &uarr; <b>P</b> &uarr; <b>Q</b></p>

- Third Grammar
<p> <b>R</b> &darr; <b>S</b> &darr; <b>R</b> &larr; <b>Q</b> &uarr; <b>C</b> &uarr; <b>Q</b> &larr; <b>R</b> &darr; <b>S</b> &darr; <b>R</b></p>

- fourth Grammar
<p> <b>S</b> &darr; <b>R</b> &darr; <b>S</b> &darr; <b>P</b> &uarr; <b>Q</b> &uarr; <b>P</b> &darr; <b>S</b> &darr; <b>R</b> &darr; <b>S</b></p>

#### Gosper Flowsnake curve
 ![Gosper_curve](https://user-images.githubusercontent.com/99839465/196053969-04ad53a4-6cda-4266-b820-bd317225cd01.GIF)

**Letters**
| G | R |
|----------|----------|
| ![Peano_P_2](/imagem/gosper_G_2.png) | ![Peano_Q_2](/imagem/gosper_R_2.png) |

**Gramatics**
(arrow show the direction, but tha intensity is 60°)
- First Grammar
<p> <b>G</b> &larr; &uarr; <b>R</b> &larr; &uarr; <b>R</b> &uarr; &rarr; <b>G</b> &uarr; &rarr; <b>G</b> &larr; &uarr;  <b>G</b> &uarr; &rarr; <b>R</b> </p>

- Second Grammar
<p> <b>G</b> &larr; &uarr; <b>R</b> &uarr; &rarr; <b>R</b> &larr; &uarr; <b>R</b> &larr; &uarr; <b>G</b> &uarr; &rarr;  <b>G</b> &uarr; &rarr; <b>R</b> </p>


#### Dragon curve
- Being construct
#### Sorcha curve
(that a create to a friend)

![Peano_P_2](/imagem/Sorcha.png)

| A | B | C | D |
|----------|----------|----------|----------|
| ![Peano_P_2](/imagem/Sorcha_A_2.png) | ![Peano_Q_2](/imagem/Sorcha_B_2.png) | ![Peano_R_2](/imagem/Sorcha_C_2.png) | ![Peano_S_2](/imagem/Sorcha_D_2.png)|

**Gramatics**
(arrow show the direction, but tha intensity is 60°)
- First Grammar
<p> <b> B A C D A  C A B C A B A C D A</b> </p>

- Second Grammar
<p> <b> D B A C B A B D C B B D C A B </b> </p>


- Third Grammar
<p> <b> D C A B C A C D B C D C A B C  </b> </p>

- Four Grammar
<p> <b> C D B A D B D C A D C D B A D </b> </p>

## 3D Curves

#### Hilbert curve 
![hilbert_3d](https://user-images.githubusercontent.com/99839465/196054029-03ccf116-b378-4f91-89ca-a65fc8b26a08.png)

| A | B | C | D |
|----------|----------|----------|----------|
| ![Peano_P_2](/imagem/Hilbert_A_3.png) | ![Peano_Q_2](/imagem/Hilbert_B_3.png) | ![Peano_R_2](/imagem/Hilbert_C_3.png) | ![Peano_S_2](/imagem/Hilbert_D_3.png)|

| E | F | G | H |
|----------|----------|----------|----------|
| ![Peano_P_2](/imagem/Hilbert_E_3.png) | ![Peano_Q_2](/imagem/Hilbert_F_3.png) | ![Peano_R_2](/imagem/Hilbert_G_3.png) | ![Peano_S_2](/imagem/Hilbert_H_3.png)|

| I | J | K | L |
|----------|----------|----------|----------|
| ![Peano_P_2](/imagem/Hilbert_I_3.png) | ![Peano_Q_2](/imagem/Hilbert_J_3.png) | ![Peano_R_2](/imagem/Hilbert_K_3.png) | ![Peano_S_2](/imagem/Hilbert_L_3.png)|

**Grammar**

- Being construct

####  Peano curve
 ![peano_3d](https://user-images.githubusercontent.com/99839465/196054031-6739a95e-c115-4c55-a5ea-cc8398997a32.png)

| P | Q | R | S |
|----------|----------|----------|----------|
| ![Peano_P_2](/imagem/Peano_P_3.png) | ![Peano_Q_2](/imagem/Peano_Q_3.png) | ![Peano_R_2](/imagem/Peano_R_3.png) | ![Peano_S_2](/imagem/Peano_S_3.png)|



