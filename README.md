# Spectral Clustering

## Overview

A hands-on implementation of spectral clustering built from first principles.
This project constructs similarity graphs, Laplacian matrices, and computes eigenpairs using custom numerical methods (shifting and deflation). It then clusters the embedded data with K-Means and visualizes the results, side-by-side with baseline methods (plain K-Means, DBSCAN, and scikit-learn’s SpectralClustering).

Ideal for showcasing algorithmic skills (linear algebra, numerical methods) and practical ML engineering (pipelines, visualization).

---

## Features
- From-scratch spectral pipeline
- Similarity graph via Gaussian (RBF) kernel with configurable σ.
- Degree and (normalized) Laplacian construction.
- Custom eigen-solvers:
- Shifting (inverse power with shift) for smallest eigenvalues/eigenvectors.
- Deflation strategy to extract successive eigenpairs.
- Clustering back-end
- Row-space embedding with the first M Laplacian eigenvectors (“rotation matrix U”), then K-Means in the embedded space.
- Comparisons included
- K-Means (original space)
- DBSCAN (with interactive ε helper)
- scikit-learn SpectralClustering for reference
- Interactive or batch mode
- Interactive prompts to pick eigenvalue/eigenvector methods, #clusters, and DBSCAN ε.
- Or run in default, fully reproducible mode.
- Clean visualizations
- Scatter plots of raw data vs. clustered assignments.
- Optional “k-th neighbor distance” plot to help choose DBSCAN ε.
---

# Structure

```
.
├─ main.py                      # Entry point: selects dataset, toggles interactive & baselines
├─ Laplacian.py                 # Similarity W, degree D, and Laplacian construction
├─ EigenMethods.py              # Shifting + deflation eigen-solvers (inverse power + Householder-style steps)
├─ SpectralClustering.py        # Eigenvector selection (U) and KMeans on embedding
├─ Visualize.py                 # Orchestration, plotting, DBSCAN helpers, sklearn baselines
├─ Datasets/
│  ├─ Circle.csv                # 2D, unlabeled
│  ├─ Spiral.csv                # 2D, third column contains labels
│  └─ 3D_Dataset.csv            # 3D with header and label column
└─ README.md

```
