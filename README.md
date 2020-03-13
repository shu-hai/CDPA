# CDPA: Common and Distinctive Pattern Analysis between High-dimensional Datasets
This python package implements the CDPA method proposed in the paper [1]. See [example.py](https://github.com/shu-hai/D-CCA/blob/master/example.py) for details, with Python 3.6.3 (or above) and the lapjv package (pip install lapjv).

Let <img src="https://render.githubusercontent.com/render/math?math=Y_k\in \mathbb{R}^{p_k\times n}, k=1,2">
be two datasets measured on a common set of <img src="https://render.githubusercontent.com/render/math?math=n"> objects, where <img src="https://render.githubusercontent.com/render/math?math=p_k"> is the number of variables in the <img src="https://render.githubusercontent.com/render/math?math=k">-th dataset. The CDPA method conducts the following decomposition:

<p align="center">
<img src="https://latex.codecogs.com/svg.latex?\Large&space;X_k^0=C^{(k)}+\Delta_k">
</p>

where <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_k=C_k+D_k=Y_k-E_k"> is obtained from the D-CCA method. Specifically,

<img src="https://latex.codecogs.com/svg.latex?\Large&space;X_k">: the signal matrix,

<img src="https://latex.codecogs.com/svg.latex?\Large&space;C_k">: the common-source matrix,

<img src="https://latex.codecogs.com/svg.latex?\Large&space;D_k">: the distinctive-source matrix,

<img src="https://latex.codecogs.com/svg.latex?\Large&space;E_k">: the noise matrix,

<img src="https://latex.codecogs.com/svg.latex?\Large&space;X_k^0">: the <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_k"> matrix with zero padding and permutation matrix <img src="https://latex.codecogs.com/svg.latex?\Large&space;P"> if necessary,

<img src="https://latex.codecogs.com/svg.latex?\Large&space;C^{(k)}">: the common-pattern matrix <img src="https://latex.codecogs.com/svg.latex?\Large&space;C"> rescaled to the magnitude of <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_k">, 

<img src="https://latex.codecogs.com/svg.latex?\Large&space;\Delta_k">: the distinctive-pattern matrix.


<br/>

**Use the CDPA function:**
```
X_1_hat, X_2_hat, C_1_hat, C_2_hat, D_1_hat, D_2_hat, r_1_hat, r_2_hat, r_12_hat, \
ccor_hat, ctheta_hat, C_mat_hat, C_mat_neg_hat, pcor_hat, ptheta_hat, P_mat_hat \
= dcca.CDPA(Y_1, Y_2, r_1=None, r_2=None, r_12=None, method=None, P_set = 1, P_mat=None, assignment=1)   
```
**or**
```
X_1_hat, X_2_hat, C_1_hat, C_2_hat, D_1_hat, D_2_hat, r_1_hat, r_2_hat, r_12_hat, \
ccor_hat, ctheta_hat, C_mat_hat, C_mat_neg_hat, pcor_hat, ptheta_hat \
= dcca.CDPA(Y_1, Y_2, r_1=None, r_2=None, r_12=None, method=None, P_set = 0)   
```

**with the function parameters:**

- r_1, r_2: the ranks of <img src="https://latex.codecogs.com/svg.latex?\Large&space;cov(X_1^{[:,1]})"> and <img src="https://latex.codecogs.com/svg.latex?\Large&space;cov(X_2^{[:,1]})">. 

- method: If r_1 and r_2 are None, then for the selection of r_1 and r_2, method='ED' and method=None use the ED method [3], and method='GR' uses the GR method [4].

- r_12: the rank of <img src="https://latex.codecogs.com/svg.latex?\Large&space;cov(X_1^{[:,1]},X_2^{[:,1]})">. If r_12=None, then r_12 is automatically selected by the MDL-IC method [5].

- P_set, P_mat, assignment: If P_set=0, no row matching of <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_1"> and <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_2">. If P_set=1, then the row matching is implemented by permutating <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_2"> to be <img src="https://latex.codecogs.com/svg.latex?\Large&space;PX_2">: in particular, if P_mat=None, then assignment=1 and assignment=0 respectively use a greedy algorithm [6] (fast but less accurate) and the Jonker-Volgenant algorithm [7] for the DSPFP method [6] for the row matching, and otherwise P_mat can be assigned to be a given permutation matrix.

**with output:**

- X_1_hat, X_2_hat, C_1_hat, C_2_hat, D_1_hat, D_2_hat: the D-CCA matrix estimates [2] for <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_k=C_k+D_k">.

- r_1_hat, r_2_hat, r_12_hat: estimates of r_1, r_2, r_12.

- ccor_hat, ctheta_hat: the estimated canonical correlations and associated angles between the respective latent-factor spaces of <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_1"> and <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_2">.

- C_mat_hat: the estimate for the unscaled common-pattern matrix <img src="https://latex.codecogs.com/svg.latex?\Large&space;C"> of <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_1"> and <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_2">.

- C_mat_neg_hat: the estimate for the unscaled common-pattern matrix <img src="https://latex.codecogs.com/svg.latex?\Large&space;C"> of <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_1"> and <img src="https://latex.codecogs.com/svg.latex?\Large&space;-X_2">.

- ptheta_hat, pcor_hat: the estimated principal angles and their cosines between the respective column spaces of <img src="https://latex.codecogs.com/svg.latex?\Large&space;B_1"> and <img src="https://latex.codecogs.com/svg.latex?\Large&space;B_2"> that are coefficient matrices of 
<img src="https://latex.codecogs.com/svg.latex?\Large&space;C_1"> and <img src="https://latex.codecogs.com/svg.latex?\Large&space;C_2"> on the common latent factors of <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_1"> and <img src="https://latex.codecogs.com/svg.latex?\Large&space;X_2">.

- P_mat_hat: the estimate fo the permutation matrix <img src="https://latex.codecogs.com/svg.latex?\Large&space;P"> for <img src="https://latex.codecogs.com/svg.latex?\Large&space;PX_2">.




[1] Qu, Z., & Shu, H. (2019). CDPA: Common and Distinctive Pattern Analysis between High-dimensional Datasets. arXiv preprint [arXiv:1912.09989](https://arxiv.org/abs/1912.09989).

[2] Shu, H., Wang, X., & Zhu, H. (2019) D-CCA: A Decomposition-based Canonical Correlation Analysis for High-dimensional Datasets. Journal of the American Statistical Association, [DOI: 10.1080/01621459.2018.1543599](https://doi.org/10.1080/01621459.2018.1543599) 
 
[3] Onatski, A. (2010). Determining the number of factors from empirical distribution of eigenvalues. The Review of Economics and Statistics, 92(4), 1004-1016.

[4] Ahn, S. C., & Horenstein, A. R. (2013). Eigenvalue ratio test for the number of factors. Econometrica, 81(3), 1203-1227.

[5] Song, Y., Schreier, P. J., Ramírez, D., & Hasija, T. (2016). Canonical correlation analysis of high-dimensional data with very small sample support. Signal Processing, 128, 449-458.

[6] Lu, Y., Huang, K., & Liu, C. L. (2016). A fast projected fixed-point algorithm for large graph matching. Pattern Recognition, 60, 971-982.

[7] Carpaneto, G., Martello, S., & Toth, P. (1988). Algorithms and codes for the assignment problem. Annals of operations research, 13(1), 191-223.
