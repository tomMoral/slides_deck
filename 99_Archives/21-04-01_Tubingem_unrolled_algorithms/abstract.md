Title: Learning to optimize with unrolled algorithms

Abstract: When solving multiple optimization problems sharing the same underlying structure, using iterative algorithms designed for worst case scenario can be considered as inefficient. When one aim at having good solution in average, it is possible to improve the performances by learning the weights of a neural networked designed to mimic an unfolded optimization algorithm. However, the reason why learning the weights of such a network would accelerate the problem resolution is not always clear.
In this talk, I will first review how one can design unrolled algorithms to solve the linear regression with l1 or TV regularization, with a particular focus on the choice of parametrization and loss. Then, I will discuss the reasons why such procedure can lead to better results compared to classical optimization, with a particular focus on the choice of step sizes.


Linked papers:
1. Moreau & Bruna. Understanding Neural Sparse Coding with Matrix Factorization. ICLR 2017. https://openreview.net/forum?id=SJGPL9Dex
2. Ablin, Moreau, Massias & Gramfort. Learning step sizes for unfolded sparse coding. NeurIPS 2019. http://arxiv.org/abs/1905.11071
3. Cherkaoui, Sulam & Moreau. Learning to solve TV regularised problems with unrolled algorithms. NeurIPS 2020. https://hal.archives-ouvertes.fr/hal-02954181
