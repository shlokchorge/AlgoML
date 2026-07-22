# Orthogonality, Projections & Least Squares — Full Notes
### (Structured like MIT 18.06, Lectures 15 & 16 — Gilbert Strang)

---

## LECTURE 15 — Projections onto Subspaces

### 15.1 Why we need projections at all

We want to solve `Ax = b`. Most real systems are **overdetermined** — more equations (`m`) than unknowns (`n`), e.g. fitting a line through 100 noisy data points with only 2 unknowns (slope, intercept).

When `m > n`, `b` almost never lies exactly in `Col(A)` (the column space). So `Ax = b` has **no exact solution**.

**The fix:** don't solve for `b`. Solve for the **closest point to `b`** that *is* reachable, i.e. the closest point inside `Col(A)`. That closest point is called the **projection**, `p`.

### 15.2 Projecting onto a single line (the simplest case)

Given a vector `b` and a line through the origin in direction `a`, we want the point `p = x̂·a` on that line closest to `b`.

**Geometric fact:** the closest point makes the error `e = b − p` **perpendicular to `a`**.

```
        b
        |\
        | \  e ⊥ a
        |  \
        o---p----→ a   (line = Col(a))
```

Perpendicularity condition: `aᵀe = 0` → `aᵀ(b − x̂a) = 0` → `aᵀb − x̂ aᵀa = 0`

`x̂ = aᵀb / aᵀa`,  `p = a x̂ = a(aᵀb)/(aᵀa)`

This is the 1-D warm-up. Everything in Lecture 16 is just this idea generalized from "one line" to "a whole subspace."

### 15.3 Projecting onto a subspace (multiple columns)

Now `Col(A)` is a **plane** (or higher-dim subspace) spanned by the columns of `A`, not just one line. We want `p`, the point in that plane closest to `b`.

Same geometric fact, generalized: the error `e = b − p` must be perpendicular to **every column of `A`**, not just one vector.

`Aᵀe = 0`

This single line is the entire idea of Lecture 15. Lecture 16 just turns it into a formula.

---

## LECTURE 16 — Projection Matrices and Least Squares

### 16.1 Setting up the algebra

We write `p = Ax̂` (the projection is *some* combination of the columns of `A` — that's what "in `Col(A)`" means). Substitute into the perpendicularity condition from 15.3:

`Aᵀ(b − Ax̂) = 0`

This one substitution is the entire derivation — see Section 3 below for it worked out in full.

### 16.2 What comes out: the Normal Equations

`AᵀA x̂ = Aᵀb`

Solvable whenever `A` has independent columns (so `AᵀA` is invertible):

`x̂ = (AᵀA)⁻¹ Aᵀb`

### 16.3 What comes out: the Projection Matrix

Since `p = Ax̂`, substitute:

`p = A(AᵀA)⁻¹Aᵀ b = Pb`,  where  **`P = A(AᵀA)⁻¹Aᵀ`**

`P` is the machine that takes *any* `b` and instantly returns its shadow on `Col(A)` — no need to resolve `x̂` first if you only want `p`.

### 16.4 Properties of `P` (check these with a small numeric example)

| Property | Statement | Why it matters |
|---|---|---|
| Symmetric | `Pᵀ = P` | projections are self-adjoint |
| Idempotent | `P² = P` | projecting a projection changes nothing |
| Eigenvalues | only `0` or `1` | `1` on `Col(A)`, `0` on its perpendicular complement |
| Complement | `I − P` projects onto `N(Aᵀ)` | `(I−P)b = e`, the leftover error |

**Try it:** `A = [[1,0],[0,1],[1,1]]`. Compute `AᵀA`, invert, multiply out `P`, confirm `P² = P` numerically. Doing this once by hand is what makes the formula stick.

### 16.5 Classic application: fitting a line

Data `(t₁,b₁)...(tₘ,bₘ)`, model `b = C + Dt`:

`A = [[1,t₁],[1,t₂],...,[1,tₘ]]`,  `x = [C, D]ᵀ`

Expanding `AᵀA x̂ = Aᵀb` for this specific `A` reproduces the regression formulas:

`D = Σ(tᵢ−t̄)(bᵢ−b̄) / Σ(tᵢ−t̄)²`,  `C = b̄ − Dt̄`

This is the bridge between the abstract matrix formula and the "slope/intercept" formula from any intro stats class.

---

## LECTURE 14 (needed background) — The Four Fundamental Subspaces

For `A` sized `m × n`, rank `r`:

| Subspace | Lives in | Dimension |
|---|---|---|
| Column space `Col(A)` | `ℝᵐ` | `r` |
| Row space `Row(A) = Col(Aᵀ)` | `ℝⁿ` | `r` |
| Null space `N(A)` | `ℝⁿ` | `n − r` |
| Left null space `N(Aᵀ)` | `ℝᵐ` | `m − r` |

**Two perpendicularity facts:**
1. `Row(A) ⊥ N(A)`, together filling `ℝⁿ`. If `Ax=0`, every row dotted with `x` gives 0 → `x` ⊥ every row → `x` ⊥ whole row space.
2. `Col(A) ⊥ N(Aᵀ)`, together filling `ℝᵐ`. Same argument applied to `Aᵀ`.

**Why this matters:** fact (2) guarantees that *any* `b ∈ ℝᵐ` splits uniquely as

`b = p + e`,  `p ∈ Col(A)`,  `e ∈ N(Aᵀ)`

Least squares isn't a trick bolted onto linear algebra — it's the *forced consequence* of `ℝᵐ` splitting cleanly into `Col(A)` and its perpendicular complement. This is the "why" underneath everything in Lecture 16.

---

## THE FULL DERIVATION, Start to Finish

*(consolidated in one place — this is what you should be able to reproduce on paper from memory)*

**Given:** `A` is `m×n` with independent columns. `Ax = b` has no exact solution. Find `x̂` minimizing `‖b − Ax‖`.

```
Step 1 (geometry → algebra):
   The closest point p = Ax̂ has error e = b − Ax̂ perpendicular
   to the whole column space of A, i.e. perpendicular to every column:
        Aᵀe = 0

Step 2 (substitute e):
        Aᵀ(b − Ax̂) = 0

Step 3 (expand):
        Aᵀb − AᵀAx̂ = 0

Step 4 (Normal Equations):
        AᵀA x̂ = Aᵀb

Step 5 (solve, AᵀA invertible since A has independent columns):
        x̂ = (AᵀA)⁻¹ Aᵀ b

Step 6 (recover the projection point):
        p = A x̂ = A(AᵀA)⁻¹Aᵀ b

Step 7 (name the matrix multiplying b):
        P = A(AᵀA)⁻¹Aᵀ        ← THE PROJECTION MATRIX
```

That's the whole thing — 7 lines, and every line follows necessarily from the one before it. Nothing here is arbitrary: Step 1 is the *only* geometric fact used, and everything else is algebra.

---

## What This Means for Machine Learning

- **Linear regression *is* this formula.** `θ̂ = (XᵀX)⁻¹Xᵀy` (`X`=features, `y`=targets) is `x̂ = (AᵀA)⁻¹Aᵀb` with relabeled letters. There is no separate "ML version" — it's the identical derivation.
- **`ŷ = Xθ̂` is literally `p = Pb`.** Your model's predictions are the projection of the true labels onto the space your features can reach. This is why linear regression *cannot* fit patterns outside `Col(X)` — no amount of "trying harder" gets it there; it's geometrically blocked.
- **`P` is called the "hat matrix" `H` in regression diagnostics** (`ŷ = Hy`). Leverage and influence statistics used to detect outliers are literally reading off entries of `P`.
- **Residuals being "uncorrelated with features" is the same perpendicularity fact.** `Aᵀe = 0` means the residual has zero correlation with every feature column at the optimum — this is *the* textbook regression diagnostic, and it's not a separate rule, it's Step 1 of the derivation.
- **Ridge regression is a direct patch on Step 5.** If `AᵀA` is singular or near-singular (correlated features, or more features than rows), Step 5 breaks. Ridge fixes it by using `(AᵀA + λI)⁻¹` instead — same derivation, one added term.
- **PCA is the same projection geometry**, just projecting onto an eigenvector-spanned subspace instead of `Col(A)`.
- **Libraries never actually compute `(AᵀA)⁻¹` directly.** `sklearn.linear_model.LinearRegression` and `np.linalg.lstsq` use QR or SVD internally, because explicitly inverting `AᵀA` is numerically unstable (squares the condition number). Know the formula for understanding; use the library's solver in practice.

**Do this exercise once:** implement `x̂ = (AᵀA)⁻¹Aᵀb` by hand in NumPy on toy data, compare against `sklearn.linear_model.LinearRegression`, then compare both against `np.linalg.lstsq`. All three should agree on `x̂`; only the numerical method differs.

---

## Things to Keep in Mind (common trip-ups)

1. **Don't drop the extra `A`.** It's `AᵀA x̂ = Aᵀb`, not `Aᵀx̂ = Aᵀb`. Easy typo, wrong equation, unsolvable dimensions.
2. **`P = A(AᵀA)⁻¹Aᵀ` requires `A` to have independent columns.** If columns are dependent (or you have more features than data points), `AᵀA` is singular and this formula breaks — that's exactly when you reach for Ridge regression or SVD-based pseudoinverse.
3. **`P` projects `b`, not `x`.** `P` lives in `ℝᵐ → ℝᵐ` (maps data-space vectors to data-space vectors). `x̂` lives in `ℝⁿ` (the coefficient/weight space). Don't confuse the two spaces.
4. **`(AᵀA)⁻¹Aᵀ` alone is called the Moore–Penrose pseudoinverse of `A`, `A⁺`.** So `x̂ = A⁺b`, and `P = AA⁺`. Worth knowing this name — it's how the concept reappears in more advanced texts and in `numpy.linalg.pinv`.
5. **Least squares minimizes squared error because of the geometry, not by definition.** People sometimes memorize "least squares minimizes `‖Ax-b‖²`" as an arbitrary choice of loss. It's not arbitrary here — it falls straight out of "closest point = perpendicular error," which is why the closed form exists at all (most other loss functions don't have one).
6. **In practice, never explicitly invert `AᵀA` in code** for anything beyond toy examples — numerical instability. Use `np.linalg.lstsq`, QR, or SVD.

---

## Self-Check

Without notes, can you:
1. Draw the `b, p, e` triangle and say which pair is perpendicular?
2. Reproduce all 7 derivation steps from `Aᵀe=0` to `P=A(AᵀA)⁻¹Aᵀ`?
3. Name which two of the four subspaces are perpendicular complements in `ℝᵐ`, and which two in `ℝⁿ`?
4. Explain in one sentence why Ridge regression adds `λI`?
5. State what `P` is called in a regression textbook, and what equation it appears in?

All five → this topic is solid.
