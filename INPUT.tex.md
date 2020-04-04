# CDPA: Common and Distinctive Pattern Analysis between High-dimensional Datasets
This python package implements the CDPA method proposed in the paper [1]. See [example.py](https://github.com/shu-hai/CDPA/blob/master/example.py) for details, with Python 3.6.3 (or above) and the lapjv package (pip install lapjv).

Let $Y_k\in \mathbb{R}^{p_k\times n}, k=1,2$
be two datasets measured on a common set of $n$ objects, where $p_k$ is the number of variables in the $k$-th dataset. The CDPA method conducts the following decomposition:

$$
X_k^0=C^{(k)}+\Delta_k
$$

where $X_k=C_k+D_k=Y_k-E_k$ is obtained from the D-CCA method. Specifically,

$X_k$: the signal matrix,

$C_k$: the common-source matrix,

$D_k$: the distinctive-source matrix,

$E_k$: the noise matrix,

$X_k^0$: the $X_k$ matrix with zero padding and permutation matrix $P$ if necessary,

$C^{(k)}$: the common-pattern matrix $C$ rescaled with the magnitude of $X_k$, 

$\Delta_k$: the distinctive-pattern matrix.


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

- r_1, r_2: the ranks of $cov(X_1^{[:,1]})$ and $cov(X_2^{[:,1]})$. 

- method: If r_1 and r_2 are None, then for the selection of r_1 and r_2, method='ED' and method=None use the ED method [3], and method='GR' uses the GR method [4].

- r_12: the rank of $cov(X_1^{[:,1]},X_2^{[:,1]})$. If r_12=None, then r_12 is automatically selected by the MDL-IC method [5].

- P_set, P_mat, assignment: If P_set=0, no row matching of $X_1$ and $X_2$. If P_set=1, then the row matching is implemented by permuting $X_2$ to be $PX_2$: in particular, if P_mat=None, then assignment=1 and assignment=0 respectively use a greedy algorithm [6] (fast but less accurate) and the Jonker-Volgenant algorithm [7] for the DSPFP method [6] for the row matching, and otherwise P_mat can be assigned to be a given permutation matrix.

**with output:**

- X_1_hat, X_2_hat, C_1_hat, C_2_hat, D_1_hat, D_2_hat: the D-CCA matrix estimates [2] for $X_k=C_k+D_k$.

- r_1_hat, r_2_hat, r_12_hat: estimates of r_1, r_2, r_12.

- ccor_hat, ctheta_hat: the estimated canonical correlations and associated angles between the respective latent-factor spaces of $X_1$ and $X_2$.

- C_mat_hat: the estimate for the unscaled common-pattern matrix $C$ of $X_1$ and $X_2$.

- C_mat_neg_hat: the estimate for the unscaled common-pattern matrix $C$ of $X_1$ and $X_2$.

- ptheta_hat, pcor_hat: the estimated principal angles and their cosines between the respective column spaces of $B_1$ and $B_2$ that are coefficient matrices of 
$C_1$ and $C_2$ on the common latent factors of $X_1$ and $X_2$.

- P_mat_hat: the estimate fo the permutation matrix $P$ for $PX_2$.




[1] Shu, H., & Qu, Z. (2019). CDPA: Common and Distinctive Pattern Analysis between High-dimensional Datasets. arXiv preprint [arXiv:1912.09989](https://arxiv.org/abs/1912.09989).

[2] Shu, H., Wang, X., & Zhu, H. (2019) D-CCA: A Decomposition-based Canonical Correlation Analysis for High-dimensional Datasets. Journal of the American Statistical Association, [DOI: 10.1080/01621459.2018.1543599](https://doi.org/10.1080/01621459.2018.1543599) 
 
[3] Onatski, A. (2010). Determining the number of factors from empirical distribution of eigenvalues. The Review of Economics and Statistics, 92(4), 1004-1016.

[4] Ahn, S. C., & Horenstein, A. R. (2013). Eigenvalue ratio test for the number of factors. Econometrica, 81(3), 1203-1227.

[5] Song, Y., Schreier, P. J., Ramírez, D., & Hasija, T. (2016). Canonical correlation analysis of high-dimensional data with very small sample support. Signal Processing, 128, 449-458.

[6] Lu, Y., Huang, K., & Liu, C. L. (2016). A fast projected fixed-point algorithm for large graph matching. Pattern Recognition, 60, 971-982.

[7] Jonker, R., & Volgenant, A. (1987). A shortest augmenting path algorithm for dense and sparse linear assignment problems. Computing, 38(4), 325-340.