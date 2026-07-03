# Day 02 — Matrix Multiplication, Linear Transformations, Determinants
> **Source:** 3B1B Essence of LA Ch.4–7 + Ch.13 
> **Phase 1 · Days 1–8 · Linear Algebra — Vectors to SVD**  
> **Target:** matrix multiplication as composing transformations · det = 0 means squish to lower dimension · what A⁻¹MA means geometrically

---

## 1. Matrix Multiplication

### Why matmul is defined the way it is

Elementwise multiply (A .* B) requires n² ops. Matmul requires ~2n³. The definition seems arbitrary until you understand: **a matrix is a linear transformation, and matmul is the composition of two transformations.**

The matmul rule is fully determined by one requirement — associativity:

```
A(Bx) = (AB)x    for all A, B, x
```

Apply B first, then A. The product AB is the single matrix that does both in one shot.

---

### The 5 Perspectives (from MIT notebook)

All 5 produce the same C = AB. They differ in *how you think* about what's happening.

#### Perspective 1 — Rows × Columns (high school)

Entry (i, j) of C = dot product of row i of A with column j of B:

```
c_ij = Σₖ aᵢₖ bₖⱼ
```

Example (row 2 of A · col 1 of B):
```
A = [ 2  -1  5 ]      B = [ 1   0  -2 ]
    [ 3   4  4 ]          [ 1  -5   1 ]
    [-4  -2  0 ]          [-3   0   3 ]

c₂₁ = 3·1 + 4·1 + 4·(-3) = 3 + 4 - 12 = -5   ✓
```

Cost: n² dot products, each of length n → O(n³) total.

#### Perspective 2 — Matrix × Columns

Each **column** of C = A multiplied by the corresponding **column** of B:

```
C = [ A·b₁ | A·b₂ | ... | A·bₚ ]
```

Each column of C is a linear combination of columns of A, with coefficients given by the column of B. This is the column space view — C(AB) ⊆ C(A).

#### Perspective 3 — Rows × Matrix

Each **row** of C = the corresponding **row** of A multiplied by B:

```
C[i, :] = A[i, :] · B
```

Each row of A tells you how to combine rows of B. This is why left-multiplying rearranges rows — the key mechanic behind Gaussian elimination (E·A = upper triangular).

Elimination step as matrix multiplication:
```
[ 1  0  0 ]       adds 3×row1 to row3,
[-1  1  0 ] · B = subtracts row1 from row2,
[ 3  0  1 ]       leaves row1 untouched
```

#### Perspective 4 — Columns × Rows (Outer Products)

Each column of A times the corresponding row of B gives a **rank-1 matrix**. AB = sum of n rank-1 matrices:

```
AB = Σₖ A[:, k] · B[k, :]ᵀ
```

Example (k=1):
```
A[:,1] = [2, 3, -4]ᵀ    B[1,:] = [1, 0, -2]

A[:,1]·B[1,:]ᵀ = [ 2   0  -4 ]
                 [ 3   0  -6 ]
                 [-4   0   8 ]
```

Sum all three k=1,2,3 outer products → C. This is the decomposition view used in SVD and low-rank approximation.

#### Perspective 5 — Block × Block

Partition A and B into submatrix blocks. Multiply blocks as if they were scalars (valid when dimensions align). All previous perspectives are special cases with different block shapes.

---

### Key Non-Properties of Matmul

| Property | Status |
|---|---|
| Associativity: A(BC) = (AB)C | ✓ Always |
| Left distributivity: A(B+C) = AB+AC | ✓ Always |
| Commutativity: AB = BA | ✗ Generally false |
| AB = 0 ⟹ A=0 or B=0 | ✗ Not always |
| AB = AC ⟹ B=C | ✗ Not always (unless A invertible) |

AB = A(A² + 2A + A⁻¹·10) commutes with A because all terms are polynomials of A — a matrix always commutes with functions of itself.

---

## 2. Linear Transformations

### What a matrix actually is

A matrix A is not a grid of numbers. It is a **function** T: ℝⁿ → ℝᵐ that satisfies two rules:

```
T(u + v) = T(u) + T(v)       (additivity)
T(cu)    = c·T(u)             (scaling)
```

Together: T(cu + dv) = cT(u) + dT(v). The transformation is completely defined by where it sends the basis vectors.

### How to read the columns of a matrix

The standard basis in ℝ²:
```
e₁ = [1, 0]ᵀ    e₂ = [0, 1]ᵀ
```

Where A sends them:
```
A = [a  b]   →   A·e₁ = [a, c]ᵀ    A·e₂ = [b, d]ᵀ
    [c  d]
```

The **columns of A are the images of the basis vectors**. Any vector x = x₁e₁ + x₂e₂ maps to:
```
Ax = x₁·(col 1 of A) + x₂·(col 2 of A)
```

This is why matrix × vector is a linear combination of columns.

### Common 2D transformations

| Transformation | Matrix |
|---|---|
| Rotation by θ | [[cos θ, -sin θ], [sin θ, cos θ]] |
| Shear (x-axis) | [[1, k], [0, 1]] |
| Reflection (y-axis) | [[-1, 0], [0, 1]] |
| Scaling by s | [[s, 0], [0, s]] |
| Projection onto x-axis | [[1, 0], [0, 0]] |

### Composition = Multiplication

Applying B first, then A:

```
y = A(Bx) = (AB)x
```

Order matters: AB ≠ BA because rotating then shearing ≠ shearing then rotating. The rightmost matrix acts first.

---

## 3. Determinants

### Geometric meaning

The determinant of A = **signed volume scaling factor** of the transformation.

- det(A) = 2 → the transformation doubles area (in 2D) or volume (in 3D)
- det(A) = -1 → preserves area, flips orientation
- det(A) = 0 → **squishes to a lower dimension** (maps ℝ² into a line, ℝ³ into a plane, etc.)

For a 2×2 matrix:
```
A = [a  b]      det(A) = ad - bc
    [c  d]
```

Geometrically: the parallelogram formed by [a,c]ᵀ and [b,d]ᵀ has signed area = ad - bc.

### det = 0 means singular

```
det(A) = 0   ⟺   columns are linearly dependent
             ⟺   A is not invertible
             ⟺   Ax = b has no unique solution
             ⟺   the transformation collapses dimension
```

This is the most important single fact about determinants. When det = 0, the output lives in a lower-dimensional subspace (the column space has rank < n).

### Properties

```
det(AB)  = det(A) · det(B)      (product rule)
det(Aᵀ)  = det(A)               (transpose preserves det)
det(A⁻¹) = 1 / det(A)
det(cA)  = cⁿ · det(A)          (n = matrix dimension)
```

Row operations and determinants:
- Swap two rows → det changes sign
- Multiply a row by c → det multiplied by c
- Add multiple of one row to another → det unchanged (this is why elimination preserves det up to sign/pivots)

For triangular matrices:
```
det = product of diagonal entries (pivots)
```

### 3×3 formula (Sarrus / cofactor expansion)

```
det [a  b  c]  =  a(ei - fh) - b(di - fg) + c(dh - eg)
    [d  e  f]
    [g  h  i]
```

Pattern: alternating signs along the first row, each multiplied by the 2×2 minor obtained by deleting that row and column.

---

## 4. Change of Basis + A⁻¹MA Conjugation

### The core idea

Every vector is a geometric object. **Coordinates are just labels** — they depend on which basis you use. Two different people using different bases will describe the same vector with different numbers.

Standard basis (our language): e₁ = [1,0]ᵀ, e₂ = [0,1]ᵀ  
Jenny's basis: b₁ = [2,1]ᵀ, b₂ = [-1,1]ᵀ

Jenny says a vector is [3, -1] (in her coordinates). In our coordinates:
```
3·b₁ + (-1)·b₂ = 3[2,1]ᵀ - 1[-1,1]ᵀ = [7, 2]ᵀ
```

### The change-of-basis matrix P

Construct P with the new basis vectors as columns:
```
P = [b₁ | b₂ | ... | bₙ]
```

| Operation | Formula | Meaning |
|---|---|---|
| Jenny → Standard | x = P · [x]_B | Decode Jenny's coordinates |
| Standard → Jenny | [x]_B = P⁻¹ · x | Encode in Jenny's language |

P is invertible iff the basis vectors are linearly independent (which they must be for a valid basis).

### The sandwich formula: M = P⁻¹AP

You have transformation A in standard coords. What's the equivalent matrix M in Jenny's language?

```
Jenny's vector  →(P)→  standard  →(A)→  transformed  →(P⁻¹)→  Jenny's result
[x]_B                    x               Ax                       [Ax]_B
```

So:
```
M = P⁻¹ A P
```

M and A describe **the same geometric transformation** — just written in different languages.

### What this means geometrically (3B1B's framing)

- P: "translate from Jenny's language to ours"
- A: "apply the transformation in our language"
- P⁻¹: "translate the result back to Jenny's language"

The sandwich P⁻¹AP is a change of perspective, not a change of the underlying geometry.

### Similar matrices

A and M = P⁻¹AP are called **similar**. They share:

```
det(M) = det(A)          (same volume scaling)
trace(M) = trace(A)      (same sum of eigenvalues)
eigenvalues of M = eigenvalues of A   (same characteristic polynomial)
rank(M) = rank(A)
```

### Why this matters: diagonalisation preview

Choose P = eigenvector matrix of A, columns = eigenvectors v₁,...,vₙ:
```
Avᵢ = λᵢvᵢ
```

Then:
```
P⁻¹AP = Λ = diag(λ₁, λ₂, ..., λₙ)
```

In the eigenbasis, A is just scaling. No rotation, no shear — purely diagonal. This is *why* the eigenbasis is the "natural" language for a transformation.

### Orthonormal bases — special case

When P = Q with orthonormal columns (Qᵀ = Q⁻¹):
```
[x]_Q = Qᵀ x       (no matrix inverse needed)
M = QᵀAQ
```

Computationally cheap. This is the structure of QR decomposition, PCA, and the spectral theorem.

---

## Connections Across Today's Topics

```
Matrix multiplication   =   composition of linear transformations
det = 0                 =   transformation collapses dimension (rank drops)
det(AB) = det(A)det(B)  =   composed scalings multiply
P⁻¹AP                  =   same transformation, different basis language
Eigenbasis              =   the basis where A becomes diagonal (det = product of λᵢ)
```

---

## ML Connections

| ML Concept | Today's Mechanism |
|---|---|
| Neural net forward pass | Chain of matrix multiplications = composed linear transformations |
| Backprop (chain rule) | (AB)ᵀ = BᵀAᵀ — reverse order for gradients |
| PCA | Change to eigenbasis of covariance matrix (P⁻¹ΣP = Λ) |
| Attention QKV | Three different linear projections of same input |
| GAN training | Jacobian det tracks how generator distorts latent space volume |
| Whitening | Transform to basis where covariance = I |

---

## Quick Reference

```
C = AB,  c_ij = Σₖ aᵢₖ bₖⱼ              rows × columns
AB = Σₖ A[:,k] · B[k,:]ᵀ                 columns × rows (outer product sum)
T(cu + dv) = cT(u) + dT(v)              linearity
det([a b; c d]) = ad - bc
det(AB) = det(A)·det(B)
det = 0  ⟺  singular  ⟺  rank drop
P = [b₁|b₂|...|bₙ],   [x]_B = P⁻¹x
M = P⁻¹AP                               same transform, Jenny's language
Qᵀ = Q⁻¹  →  [x]_Q = Qᵀx  (orthonormal)
```

---

## Day 02 Tasks

- [ ] `theory.md` — write in own words: why AB ≠ BA with a geometric example
- [ ] `visualize.py` — plot the unit square under a shear, then a rotation; then compose them both ways and show the difference
- [ ] Verify det(AB) = det(A)·det(B) numerically for 3×3
- [ ] Implement Perspective 4 (outer product sum) in Python, verify equals `A @ B`
- [ ] Draw P, P⁻¹, and the sandwich P⁻¹AP for a 2×2 example by hand
- [ ] Write: "det = 0 means ___" in 2 sentences, geometric only, no formulas

---

## Common Mistakes

**Matmul:** Forgetting AB ≠ BA. Always check which transformation acts first (rightmost).  
**Det:** Treating det = 0 as just "the formula gives zero" — it means the space collapses, which is the real insight.  
**Sandwich:** Writing PAP⁻¹ instead of P⁻¹AP — the inverse goes on the left.  
**Change of basis direction:** P converts *from* Jenny's coords *to* standard, so P⁻¹ goes the other way.

---

> *A matrix is a transformation. Multiplying matrices is composing transformations. The determinant measures how much the transformation stretches space — and zero means it destroys a dimension entirely.*