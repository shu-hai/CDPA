# CDPA: Common and Distinctive Pattern Analysis between High-dimensional Datasets
This python package implements the CDPA method proposed in the paper [1]. See [example.py](https://github.com/shu-hai/CDPA/blob/master/example.py) for details, with Python 3.6.3 (or above) and the lapjv package (pip install lapjv).

Let <img src="/tex/73582d21b52f64e8f6cfec7e236f6cf1.svg?invert_in_darkmode&sanitize=true" align=middle width=144.82236944999997pt height=26.17730939999998pt/>
be two datasets measured on a common set of <img src="/tex/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode&sanitize=true" align=middle width=9.86687624999999pt height=14.15524440000002pt/> objects, where <img src="/tex/a28020cb9b58a3a875adec3adf5d824a.svg?invert_in_darkmode&sanitize=true" align=middle width=15.536596349999991pt height=14.15524440000002pt/> is the number of variables in the <img src="/tex/63bb9849783d01d91403bc9a5fea12a2.svg?invert_in_darkmode&sanitize=true" align=middle width=9.075367949999992pt height=22.831056599999986pt/>-th dataset. The CDPA method conducts the following decomposition:

<p align="center"><img src="/tex/99f9f8beaf6d6d050e9831935856422a.svg?invert_in_darkmode&sanitize=true" align=middle width=116.54325375pt height=19.481243099999997pt/></p>

where <img src="/tex/2f67330d681e9f37f73e79472330b18c.svg?invert_in_darkmode&sanitize=true" align=middle width=184.29076709999998pt height=22.465723500000017pt/> is obtained from the D-CCA method. Specifically,

<img src="/tex/1a35cf75b6c416e1e4a2b594e79040e6.svg?invert_in_darkmode&sanitize=true" align=middle width=20.88478094999999pt height=22.465723500000017pt/>: the signal matrix,

<img src="/tex/1a567506286617473a9c0d9b2172f951.svg?invert_in_darkmode&sanitize=true" align=middle width=19.014878849999988pt height=22.465723500000017pt/>: the common-source matrix,

<img src="/tex/8daec2445e7b537498820d34172b49d0.svg?invert_in_darkmode&sanitize=true" align=middle width=20.87562509999999pt height=22.465723500000017pt/>: the distinctive-source matrix,

<img src="/tex/05bf2b668cae2b5ab9a4c170036b069b.svg?invert_in_darkmode&sanitize=true" align=middle width=19.40074949999999pt height=22.465723500000017pt/>: the noise matrix,

<img src="/tex/c224988d43a0e45defa4f81ea2ce9c06.svg?invert_in_darkmode&sanitize=true" align=middle width=21.461213399999988pt height=26.76175259999998pt/>: the <img src="/tex/1a35cf75b6c416e1e4a2b594e79040e6.svg?invert_in_darkmode&sanitize=true" align=middle width=20.88478094999999pt height=22.465723500000017pt/> matrix with zero padding and permutation matrix <img src="/tex/df5a289587a2f0247a5b97c1e8ac58ca.svg?invert_in_darkmode&sanitize=true" align=middle width=12.83677559999999pt height=22.465723500000017pt/> if necessary,

<img src="/tex/091ad638c3450d381237a949a1d2bd7a.svg?invert_in_darkmode&sanitize=true" align=middle width=30.46469909999999pt height=29.190975000000005pt/>: the common-pattern matrix <img src="/tex/9b325b9e31e85137d1de765f43c0f8bc.svg?invert_in_darkmode&sanitize=true" align=middle width=12.92464304999999pt height=22.465723500000017pt/> rescaled with the magnitude of <img src="/tex/1a35cf75b6c416e1e4a2b594e79040e6.svg?invert_in_darkmode&sanitize=true" align=middle width=20.88478094999999pt height=22.465723500000017pt/>, 

<img src="/tex/06ce646ed4f5c14cd540fc9284ccf083.svg?invert_in_darkmode&sanitize=true" align=middle width=20.96470199999999pt height=22.465723500000017pt/>: the distinctive-pattern matrix.


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

- r_1, r_2: the ranks of <img src="/tex/bec03c6ce0f92e410b62b5c2e75bc903.svg?invert_in_darkmode&sanitize=true" align=middle width=73.77680804999999pt height=34.337843099999986pt/> and <img src="/tex/2fce69ef438a7627b9261e76d1388cd2.svg?invert_in_darkmode&sanitize=true" align=middle width=73.77680804999999pt height=34.337843099999986pt/>. 

- method: If r_1 and r_2 are None, then for the selection of r_1 and r_2, method='ED' and method=None use the ED method [3], and method='GR' uses the GR method [4].

- r_12: the rank of <img src="/tex/a380f440f8cad2e20eaf960a5f888343.svg?invert_in_darkmode&sanitize=true" align=middle width=118.43436989999998pt height=34.337843099999986pt/>. If r_12=None, then r_12 is automatically selected by the MDL-IC method [5].

- P_set, P_mat, assignment: If P_set=0, no row matching of <img src="/tex/4a0dab614eaf1e6dc58146666d67ace8.svg?invert_in_darkmode&sanitize=true" align=middle width=20.17129784999999pt height=22.465723500000017pt/> and <img src="/tex/f6fac43e354f1b2ca85658091df26df1.svg?invert_in_darkmode&sanitize=true" align=middle width=20.17129784999999pt height=22.465723500000017pt/>. If P_set=1, then the row matching is implemented by permuting <img src="/tex/f6fac43e354f1b2ca85658091df26df1.svg?invert_in_darkmode&sanitize=true" align=middle width=20.17129784999999pt height=22.465723500000017pt/> to be <img src="/tex/72934103d5f2cec40878bbf9eb8a36f5.svg?invert_in_darkmode&sanitize=true" align=middle width=33.00807014999999pt height=22.465723500000017pt/>: in particular, if P_mat=None, then assignment=1 and assignment=0 respectively use a greedy algorithm [6] (fast but less accurate) and the Jonker-Volgenant algorithm [7] for the DSPFP method [6] for the row matching, and otherwise P_mat can be assigned to be a given permutation matrix.

**with output:**

- X_1_hat, X_2_hat, C_1_hat, C_2_hat, D_1_hat, D_2_hat: the D-CCA matrix estimates [2] for <img src="/tex/c140d20471e781769f4542e9b091c21a.svg?invert_in_darkmode&sanitize=true" align=middle width=104.42793735pt height=22.465723500000017pt/>.

- r_1_hat, r_2_hat, r_12_hat: estimates of r_1, r_2, r_12.

- ccor_hat, ctheta_hat: the estimated canonical correlations and associated angles between the respective latent-factor spaces of <img src="/tex/4a0dab614eaf1e6dc58146666d67ace8.svg?invert_in_darkmode&sanitize=true" align=middle width=20.17129784999999pt height=22.465723500000017pt/> and <img src="/tex/f6fac43e354f1b2ca85658091df26df1.svg?invert_in_darkmode&sanitize=true" align=middle width=20.17129784999999pt height=22.465723500000017pt/>.

- C_mat_hat: the estimate for the unscaled common-pattern matrix <img src="/tex/9b325b9e31e85137d1de765f43c0f8bc.svg?invert_in_darkmode&sanitize=true" align=middle width=12.92464304999999pt height=22.465723500000017pt/> of <img src="/tex/4a0dab614eaf1e6dc58146666d67ace8.svg?invert_in_darkmode&sanitize=true" align=middle width=20.17129784999999pt height=22.465723500000017pt/> and <img src="/tex/f6fac43e354f1b2ca85658091df26df1.svg?invert_in_darkmode&sanitize=true" align=middle width=20.17129784999999pt height=22.465723500000017pt/>.

- C_mat_neg_hat: the estimate for the unscaled common-pattern matrix <img src="/tex/9b325b9e31e85137d1de765f43c0f8bc.svg?invert_in_darkmode&sanitize=true" align=middle width=12.92464304999999pt height=22.465723500000017pt/> of <img src="/tex/4a0dab614eaf1e6dc58146666d67ace8.svg?invert_in_darkmode&sanitize=true" align=middle width=20.17129784999999pt height=22.465723500000017pt/> and <img src="/tex/f6fac43e354f1b2ca85658091df26df1.svg?invert_in_darkmode&sanitize=true" align=middle width=20.17129784999999pt height=22.465723500000017pt/>.

- ptheta_hat, pcor_hat: the estimated principal angles and their cosines between the respective column spaces of <img src="/tex/fe468915e44d9e34d437fbf99b371809.svg?invert_in_darkmode&sanitize=true" align=middle width=19.021198349999988pt height=22.465723500000017pt/> and <img src="/tex/2b7de9b9b655b068f97484efba8812fb.svg?invert_in_darkmode&sanitize=true" align=middle width=19.021198349999988pt height=22.465723500000017pt/> that are coefficient matrices of 
<img src="/tex/d81a84099e7856ffa4484e1572ceadff.svg?invert_in_darkmode&sanitize=true" align=middle width=18.30139574999999pt height=22.465723500000017pt/> and <img src="/tex/85f3e1190907b9a8e94ce25bec4ec435.svg?invert_in_darkmode&sanitize=true" align=middle width=18.30139574999999pt height=22.465723500000017pt/> on the common latent factors of <img src="/tex/4a0dab614eaf1e6dc58146666d67ace8.svg?invert_in_darkmode&sanitize=true" align=middle width=20.17129784999999pt height=22.465723500000017pt/> and <img src="/tex/f6fac43e354f1b2ca85658091df26df1.svg?invert_in_darkmode&sanitize=true" align=middle width=20.17129784999999pt height=22.465723500000017pt/>.

- P_mat_hat: the estimate fo the permutation matrix <img src="/tex/df5a289587a2f0247a5b97c1e8ac58ca.svg?invert_in_darkmode&sanitize=true" align=middle width=12.83677559999999pt height=22.465723500000017pt/> for <img src="/tex/72934103d5f2cec40878bbf9eb8a36f5.svg?invert_in_darkmode&sanitize=true" align=middle width=33.00807014999999pt height=22.465723500000017pt/>.




[1] Shu, H., & Qu, Z. (2022). [CDPA: Common and Distinctive Pattern Analysis between High-dimensional Datasets.](https://doi.org/10.1214/22-EJS2008) Electronic Journal of Statistics, 16(1), 2475–2517.

[2] Shu, H., Wang, X., & Zhu, H. (2020) [D-CCA: A Decomposition-based Canonical Correlation Analysis for High-dimensional Datasets.](https://doi.org/10.1080/01621459.2018.1543599) Journal of the American Statistical Association, 115(529), 292-306. 
 
[3] Onatski, A. (2010). Determining the number of factors from empirical distribution of eigenvalues. The Review of Economics and Statistics, 92(4), 1004-1016.

[4] Ahn, S. C., & Horenstein, A. R. (2013). Eigenvalue ratio test for the number of factors. Econometrica, 81(3), 1203-1227.

[5] Song, Y., Schreier, P. J., Ramírez, D., & Hasija, T. (2016). Canonical correlation analysis of high-dimensional data with very small sample support. Signal Processing, 128, 449-458.

[6] Lu, Y., Huang, K., & Liu, C. L. (2016). A fast projected fixed-point algorithm for large graph matching. Pattern Recognition, 60, 971-982.

[7] Jonker, R., & Volgenant, A. (1987). A shortest augmenting path algorithm for dense and sparse linear assignment problems. Computing, 38(4), 325-340.
