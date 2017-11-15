$$
\begin{equation*}
 B = [b_{ij}] = 
 \begin{bmatrix}
  0 &-1 &-1 & 0 \\
  3 & 0 & 0 &-1 \\
  1 & 0 & 0 & 0 \\
  0 & 1 & 0 & 0 \\
 \end{bmatrix},
 \quad
 C = [c_{ij}] = DB = 
 \begin{bmatrix}
  0 &-3 &-3 & 0 \\
  3 & 0 & 0 &-1 \\
  3 & 0 & 0 & 0 \\
  0 & 1 & 0 & 0 \\
 \end{bmatrix}
\end{equation*}
$$

$$
\begin{equation*}
 \begin{array}{ccccc}
  y_1,y_2          &\overset2\rightarrow& y_1y_2^3, y_2^{-1} &\overset1\rightarrow&y_1^{-1}y_2^{-3}, y_1y_2^2 \\
  \scriptsize1\downarrow    &                    &                    &                    &\downarrow\scriptsize2 \\
  y_1^{-1},y_2     &                    &                    &                    &y_1^2y_2^3, y_1^{-1}y_2^{-2}\\
  \scriptsize2\downarrow    &                    &                    &                    &\downarrow\scriptsize1 \\
  y_1^{-1},y_2^{-1}&\overset1\leftarrow &y_1,y_1^{-1}y_2^{-1}&\overset2\leftarrow &y_1^{-2}y_2^{-3}, y_1y_2 \\
 \end{array}
\end{equation*}
$$

$$ \begin{pmatrix}- B \left(k_{x}^{2} + k_{y}^{2}\right) + C - D \left(k_{x}^{2} + k_{y}^{2}\right) + M & A \left(k_{x} + i k_{y}\right) & 0 & 0\\A \left(k_{x} - i k_{y}\right) & B \left(k_{x}^{2} + k_{y}^{2}\right) + C - D \left(k_{x}^{2} + k_{y}^{2}\right) - M & 0 & 0\\0 & 0 & - B \left(k_{x}^{2} + k_{y}^{2}\right) + C - D \left(k_{x}^{2} + k_{y}^{2}\right) + M & A \left(- k_{x} + i k_{y}\right)\\0 & 0 & - A \left(k_{x} + i k_{y}\right) & B \left(k_{x}^{2} + k_{y}^{2}\right) + C - D \left(k_{x}^{2} + k_{y}^{2}\right) - M\end{pmatrix} $$

$$ \exp x = 1 + x + x^2/2 + x^3/6 + \cdots $$


```bash
$ npm install gitbook-api
```
