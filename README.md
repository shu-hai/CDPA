# CDPA
This python package implements the CDPA method proposed in the paper [1]. See [example.py](https://github.com/shu-hai/D-CCA/blob/master/example.py) for details, with Python 3.6.3 (or above) and the lapjv package (pip install lapjv).

Let <img src="https://render.githubusercontent.com/render/math?math=Y_k\in \mathbb{R}^{p_k\times n}, k=1,2">
be two datasets measured on a common set of <img src="https://render.githubusercontent.com/render/math?math=n"> objects, where <img src="https://render.githubusercontent.com/render/math?math=p_k"> is the number of variables in the <img src="https://render.githubusercontent.com/render/math?math=k">-th dataset. The CDPA method conducts the following decomposition


<img src="https://latex.codecogs.com/svg.latex?\Large&space;X_k^0=C^{(k)}+\Delta_k">

where <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_k=C_k+D_k=Y_k-E_k"> is obtained from the D-CCA method. Specifically,

<img src="https://latex.codecogs.com/svg.latex?\Large&space;X_k">: the signal matrix,

<img src="https://latex.codecogs.com/svg.latex?\Large&space;C_k">: the common-source matrix,

<img src="https://latex.codecogs.com/svg.latex?\Large&space;D_k">: the distinctive-source matrix,

<img src="https://latex.codecogs.com/svg.latex?\Large&space;E_k">: the distinctive-source matrix,

<img src="https://latex.codecogs.com/svg.latex?\Large&space;X_k^0">: the <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_k"> matrix with zero padding and permutation matrix <img src="https://latex.codecogs.com/svg.latex?\Large&space;P"> if necessary,

<img src="https://latex.codecogs.com/svg.latex?\Large&space;C^{(k)}">: the common-pattern matrix <img src="https://latex.codecogs.com/svg.latex?\Large&space;C"> rescaled to the magnitude of <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_k">, 

<img src="https://latex.codecogs.com/svg.latex?\Large&space;\Delta_k">: the distinctive-pattern matrix.


<br/>

Use the CDPA function:
```
X_1_hat, X_2_hat, C_1_hat, C_2_hat, D_1_hat, D_2_hat, r_1_hat, r_2_hat, r_12_hat, \
ccor_hat, ctheta_hat, C_mat_hat, C_mat_neg_hat, pcor_hat, ptheta_hat, P_mat_hat \
= dcca.CDPA(Y_1, Y_2, r_1=None, r_2=None, r_12=None, method=None, P_set = 1, P_mat=None, assignment=1)   
```
or 
```
X_1_hat, X_2_hat, C_1_hat, C_2_hat, D_1_hat, D_2_hat, r_1_hat, r_2_hat, r_12_hat, \
ccor_hat, ctheta_hat, C_mat_hat, C_mat_neg_hat, pcor_hat, ptheta_hat \
= dcca.CDPA(Y_1, Y_2, r_1=None, r_2=None, r_12=None, method=None, P_set = 0)   
```

with the function parameters

r_1, r_2: the ranks of <img src="https://latex.codecogs.com/svg.latex?\Large&space;cov(X_1^{[:,1]})"> and <img src="https://latex.codecogs.com/svg.latex?\Large&space;cov(X_2^{[:,1]})">

r_12: the rank of <img src="https://latex.codecogs.com/svg.latex?\Large&space;cov(X_1^{[:,1]},X_2^{[:,1]})">

method: if method='ED, t


[1] Qu, Z., & Shu, H. (2019). CDPA: Common and Distinctive Pattern Analysis between High-dimensional Datasets. arXiv preprint [arXiv:1912.09989](https://arxiv.org/abs/1912.09989).

[2] Shu, H., Wang, X., & Zhu, H. (2019) D-CCA: A Decomposition-based Canonical Correlation Analysis for High-dimensional Datasets. Journal of the American Statistical Association, [DOI: 10.1080/01621459.2018.1543599](https://doi.org/10.1080/01621459.2018.1543599) 
