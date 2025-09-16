# Spectral Clustering

# Overview

A hands-on implementation of spectral clustering built from first principles.
This project constructs similarity graphs, Laplacian matrices, and computes eigenpairs using custom numerical methods (shifting and deflation). It then clusters the embedded data with K-Means and visualizes the results, side-by-side with baseline methods (plain K-Means, DBSCAN, and scikit-learn’s SpectralClustering).

Ideal for showcasing algorithmic skills (linear algebra, numerical methods) and practical ML engineering (pipelines, visualization).

---

## Features

- k-NN similarity graph with Gaussian kernel \(RBF\) and σ configurable.
- Unnormalized Laplacian \(L=D-W\) and normalized Laplacian \(L_{\mathrm{sym}}=I-D^{-1/2}WD^{-1/2}\).
- Custom eigen-solvers:
  - **Shifting small method** to fetch the smallest eigenpairs.
  - **Deflation + inverse power** with Householder deflation.
- Automatic or manual choice of cluster count \(M\).
- Clean visualizations: original data, Laplacian eigenvalues, embedding \(U\), clustered assignments.
- Optional baselines: K-Means on raw data, DBSCAN with k-th neighbor distance helper, sklearn SpectralClustering.

---
## Structure

```
.
├── main.py                    # Entry point: selects dataset, toggles interactive & baselines
├── Laplacian.py               # Similarity W, degree D, and Laplacian construction
├── EigenMethods.py            # Shifting + deflation eigen-solvers (inverse power + Householder)
├── SpectralClustering.py      # Eigenvector selection (U) and KMeans on embedding
├── Visualize.py               # Orchestration, plotting, DBSCAN helpers, sklearn baselines
├── Datasets/
│   ├── Circle.csv             # 2D, unlabeled
│   ├── Spiral.csv             # 2D, third column contains labels
│   └── 3D_Dataset.csv         # 3D with header and label column
├── Spectral_Clustering.pdf    # Project report / paper
└── README.md

```

---

# Implementation

## 1. Quick Start
In the ***main.py*** you can set:
```bash
interactive = False           # True for guided run with prompts
k = 10                        # k for k-NN graph
dataset = "Circle.csv"        # "Circle.csv" | "Spiral.csv" | "3D_Dataset.csv"

other_kmeans = True           # Baseline on raw data
other_dbscan = True           # DBSCAN baseline (with helper plot if interactive)
other_sklearn = True          # sklearn's SpectralClustering baseline
```
Then, run:
```bash
python main.py
```

## 2. Run Modes

### Set ***interactive = True*** in main.py.

Flow:
1.	Load dataset and plot Original Data.
2.	Build (L) with k-NN and RBF similarity; show Laplacian Eigenvalues.
3.	Prompt to pick eigenvalue/eigenvector methods: shifting or deflation.
4.	Prompt for the number of clusters (M).
5.	Compute embedding (U) from the (M) smallest eigenvectors; show Projected Data.
6.	Run K-Means in (U); show Clustered Data.
7.	Repeat the same with Normalized Laplacian (L_{\mathrm{sym}}).
8.	Optional baselines:
   -	K-Means on raw data.
   -	DBSCAN: optional k-th neighbor distance plot to pick ε; then run and visualize.
   -	sklearn SpectralClustering using affinity='nearest_neighbors'.

Reproducible (default) mode

### Set ***interactive = False**:
- The pipeline runs end-to-end without prompts.
- The cluster count (M) is chosen by simple heuristics based on dataset and k.
- Plots: Original Data → Eigenvalues → Projected Data → Clustered Data.
- If baselines are enabled, they run after the main pipeline.

### Baselines
Controlled by other_kmeans, other_dbscan, other_sklearn in main.py.
- K-Means: KMeans(n_clusters=self.n_clusters) on raw features.
- DBSCAN:
- If interactive, a k-th neighbor distance curve helps select ε.
- Defaults (non-interactive):
- Circle.csv: min_samples=10, eps=0.75
- Spiral.csv: min_samples=5, eps=2.0
- 3D_Dataset.csv: min_samples=3, eps=2.25
- sklearn SpectralClustering: SpectralClustering(n_clusters=M, affinity='nearest_neighbors').

### Eigenvalue / eigenvector solvers

EigenMethods provides two strategies:
- Shifting small method: iterative shifting to target smallest eigenpairs of a symmetric (L).
- Deflation + inverse power: compute smallest eigenpair with inverse power; apply Householder deflation and repeat to get the next ones.

eigencompute(L, K) returns the (K) smallest eigenvalues and associated eigenvectors according to the selected methods. In the pipeline K=5, then the first (M) are used.

---

# Results and Plots
The run produces these figures in sequence:
- Original Data.
- Laplacian Eigenvalues (optionally also for normalized Laplacian).
- Projected Data (U) scatter.
- Clustered Data on original coordinates.
- Optional k-th neighbor distance curve for DBSCAN.
- 
Plots are shown with matplotlib and are not saved by default.


## Documentation

- [Spectral_Clustering.pdf](Spectral_Clustering.pdf) — Project report with theory, implementation, and results.
