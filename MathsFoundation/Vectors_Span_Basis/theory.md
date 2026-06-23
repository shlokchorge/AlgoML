# Day 1 Theory Notes — UPDATED
## Gilbert Strang — MIT 18.06 Lecture 1 & Lecture 6
### + ML Outcomes + Numericals + mitmath/1806 additions

> **Write these by hand after reading.** Goal is intuition, not memorization.

---

## ⚡ BEFORE YOU WATCH — What to Look For

### Lecture 1 — "The Geometry of Linear Equations"
**Your one question going in:** *How does Strang see Ax as a column combination, not a row dot-product?*

| Watch for | Why it matters for ML |
|---|---|
| Row picture vs Column picture | In ML, weight matrices W act on input vectors — you're always in column-picture land |
| "Do columns fill the space?" | This is literally what full-rank weight layers mean — no dead dimensions |
| Ax as linear combo of columns | Forward pass of a neural net IS this, layer by layer |
| 3D planes failing intuition | Why visualizing high-dim ML spaces always breaks — Strang's warning scales to 10,000D |

**Concrete ML link:** In a linear layer `y = Wx`, the output `y` is a linear combination of columns of `W`, weighted by `x`. Strang's column picture = every forward pass.

---

### Lecture 6 — "Column Space and Nullspace"
**Your one question going in:** *What does it mean for a matrix to "crush" part of the input space to zero?*

| Watch for | Why it matters for ML |
|---|---|
| Column space C(A) | The set of all outputs your model can produce — its "representational capacity" |
| Null space N(A) | Directions in input space the model is blind to — dead features, degenerate weights |
| Subspace closure rules | Why linear layers can't escape their subspace — no matter how deep, if no nonlinearity |
| Rank | Number of "independent directions" a layer uses — low-rank = bottleneck |

**Concrete ML link:** A weight matrix W with rank r < n means your model collapses the input into an r-dimensional subspace. This is exactly what LoRA exploits — you already fine-tune VisionTeX with this! Low-rank ΔW is an intentional null-space manipulation.

---

## ━━ LECTURE 1 ━━  The Geometry of Linear Equations

### The Fundamental Problem

> *"The fundamental problem of linear algebra is to solve a system of linear equations."*
> — Strang, Lecture 1 opening

Everything — every matrix, every subspace, every algorithm — connects back to this.

---

### The Example System

```
2x  −  y  =  0
−x  + 2y  =  3
```

Three ways to see the same system.

---

### WAY 1 — Row Picture

Each equation = a **line** in the xy-plane.

```
2x − y = 0   →  line through origin (slope 2)
−x + 2y = 3  →  another line (slope 0.5, shifted)
```

They intersect at **(x=1, y=2)**. In 3D this becomes planes — almost impossible to visualize. Row picture breaks at high dimension.

---

### WAY 2 — Column Picture ⭐

```
x · [ 2]  +  y · [-1]  =  [0]
    [-1]         [ 2]      [3]
```

"What combination of column vectors hits b?"

**1 × [2,−1] + 2 × [−1,2] = [0, 3] ✓**

Reframe: *"Is b in the span of the columns?"* — this is the right question for all of LA.

---

### WAY 3 — Matrix Form

```
Ax = b   where   A = [ 2 -1]   x = [x]   b = [0]
                     [-1  2]       [y]       [3]
```

Compact notation that scales identically to 200 unknowns.

---

### Ax — The Column Way (Strang's Key Insight)

**Row way:** dot product of each row with x (what you learned in school)

**Column way (better):**
```
Ax = x₁·(col1 of A) + x₂·(col2 of A) + ...
```

Ax is a **linear combination of columns**, with x as coefficients. This unlocks everything.

---

### The Big Question Strang Ends Lecture 1 With

> **"Do the linear combinations of the columns fill the entire space?"**

- YES → Ax = b has a solution for **every** b
- NO → some b's are unreachable → no solution

---

### 3D Extension

```
 2x −  y       = 0
−x  + 2y −  z  = −1
     −3y + 4z  =  4
```

Row picture: 3 planes — very hard to see where they meet.
Column picture: b = 3rd column exactly → z=1, x=0, y=0.

**Strang's warning:** Row picture breaks as dimensions grow. Column picture always asks the same clean question.

---

## ━━ LECTURE 6 ━━  Column Space and Null Space

> *"We're at the start of Chapter 3 — really getting to the center of linear algebra."*

---

### Vector Space (Quick Reminder)

Two closure rules:
1. **Add** any two vectors → stay inside
2. **Scale** any vector by any scalar → stay inside

Standard: ℝ², ℝ³, {0}.

---

### Subspace

A vector space living inside a bigger one. Three requirements:

1. **0 ∈ S** (zero vector test — if it fails, stop here, NOT a subspace)
2. **u + v ∈ S** whenever u, v ∈ S (closed under addition)
3. **cu ∈ S** whenever u ∈ S (closed under scaling)

**Quick check:** A line through the origin in ℝ² = subspace ✓. A line NOT through origin = NOT a subspace ✗.

---

### All Subspaces of ℝ³ (Strang's Complete List)

```
{0}          — just the origin
Line thru 0  — one direction, all scalings
Plane thru 0 — two directions, all combinations
All of ℝ³   — the whole space
```

A plane NOT through the origin is **not** a subspace.

---

### Union vs Intersection

**Union (P ∪ L):** NOT a subspace (in general). Pick one vector from P, one from L — their sum can land outside both.

**Intersection (P ∩ L):** ALWAYS a subspace. If Strang's plane and a line (not in plane) intersect, result = {0} — still valid.

---

### Column Space C(A)

```
C(A) = { Ax : x ∈ ℝⁿ } = span of columns of A
```

> *"The column space of A tells us when Ax = b has a solution."*

**Ax = b has a solution ⟺ b ∈ C(A)**

---

### Column Space Example

```
A = [1  1  2]
    [2  1  3]
    [3  1  4]
    [4  1  5]
```

Column 3 = Col 1 + Col 2 → dependent. C(A) = a **plane** in ℝ⁴, not all of ℝ⁴. Only b's in that plane have a solution.

**Strang's trick:** Want a b that works? Pick any x, compute b = Ax. Guaranteed to be in C(A).

---

### Null Space N(A)

```
N(A) = { x ∈ ℝⁿ : Ax = 0 }
```

> *"The null space tells us which x solve Ax = 0."*

**Proof it's a subspace:**
- If Ax = 0 and Ay = 0 → A(x+y) = 0 ✓
- If Ax = 0 → A(cx) = c(Ax) = 0 ✓

Always a subspace. Guaranteed by linearity of A.

---

### Null Space Example

```
A = [1  2]
    [2  4]   ← row 2 = 2 × row 1
```

Solve Ax = 0: only one real equation → x₁ = −2x₂

```
x = x₂ · [-2]    for any x₂
           [ 1]
```

**N(A) = a line in ℝ² through origin, direction [-2, 1].** A is rank 1, crushes this entire line to zero.

---

### The Key Contrast

| | Column Space C(A) | Null Space N(A) |
|---|---|---|
| **Lives in** | ℝᵐ (output space) | ℝⁿ (input space) |
| **Answers** | When does Ax = b have a solution? | What inputs does A map to zero? |
| **Always has** | At least **0** | Always at least **{0}** |

---

### Strang's Subspace Check (always ask these 3)

1. Is **0** in S?
2. If u, v ∈ S → is u+v ∈ S?
3. If u ∈ S and c ∈ ℝ → is cu ∈ S?

All three YES = subspace. Fail one = not a subspace.

---

## ━━ NUMERICALS — Solve These ━━

> From Strang's 18.06 problem sets + mitmath/1806 exercises. Do on paper first.

---

### Block 1 — Lec 1 (Row/Column Picture, Ax = b)

**N1.** Solve by column picture — find x, y as scalings of column vectors:
```
3x + y  = 7
x  + 2y = 4
```
Sketch: draw col1=[3,1], col2=[1,2], target b=[7,4]. What combo works?

**N2.** For A = [[2,1],[6,3]], and b = [4, 12]:
- Write Ax = b.
- Does a solution exist? Infinitely many?
- Find the null space of A (what x satisfies Ax = 0?).

**N3.** Compute Ax using the **column picture** (linear combination of columns):
```
A = [1  2  3]    x = [2]
    [4  5  6]        [0]
                     [1]
```
Don't use row dot-products. Compute: 2·col1 + 0·col2 + 1·col3.

---

### Block 2 — Lec 6 (Subspace, C(A), N(A))

**N4.** Which of these are subspaces of ℝ²?
- a) All vectors [x, y] with x + y = 0
- b) All vectors [x, y] with x + y = 1
- c) All vectors [x, y] with x ≥ 0
- d) All vectors [x, 2x] (the line y = 2x)

**N5.** For A = [[1,1,2],[2,1,3],[3,1,4],[4,1,5]]:
- Find a b = [b1,b2,b3,b4] that IS in C(A) (use Strang's trick: pick x, compute b)
- Find a b that is NOT in C(A)

**N6.** Solve Ax = 0 and describe N(A) geometrically:
```
A = [1  2  3]
    [2  4  6]
```
(Hint: row 2 = 2 × row 1. Two free variables.)

**N7.** (Harder) Prove or disprove: if S₁ and S₂ are subspaces of ℝⁿ, then S₁ ∪ S₂ is a subspace. Give a concrete counterexample in ℝ².

---

### Block 3 — ML-Flavored Applications

**N8.** A weight matrix in a neural net layer:
```
W = [1  0  1]
    [0  1  1]
```
(2 output dims, 3 input dims)
- What is C(W)? What dimension is it? (= how many independent output directions)
- What is N(W)? (= which input directions the layer ignores)

**N9.** LoRA insight: Suppose W = AB where A is 4×2 and B is 2×3.
- What is the maximum rank of W?
- What does this say about C(W) — can it span all of ℝ⁴?

---

## SOLUTIONS (check after attempting)

**N1.** Set up x[3,1] + y[1,2] = [7,4] → 3x+y=7, x+2y=4 → x=2, y=1.

**N2.** Row 2 = 3×row 1. The system has infinitely many solutions. N(A): 2x+y=0 → y=-2x → N(A) = span{[1,-2]}.

**N3.** 2·[1,4] + 0·[2,5] + 1·[3,6] = [2,8] + [0,0] + [3,6] = **[5, 14]**.

**N4.** a) ✓ (line through origin), b) ✗ (doesn't contain 0), c) ✗ (not closed under scaling by -1), d) ✓ (line through origin).

**N5.** Pick x=[1,0,0] → b=[1,2,3,4] ∈ C(A). Pick b=[1,1,1,1] → does NOT satisfy the plane constraints (you can verify after row reduction).

**N6.** Only one equation: x₁+2x₂+3x₃=0. Two free variables (x₂, x₃). N(A) = span{[-2,1,0], [-3,0,1]} — a **plane** in ℝ³.

**N7.** Not a subspace. Counterexample: S₁ = x-axis, S₂ = y-axis in ℝ². Take [1,0] ∈ S₁ and [0,1] ∈ S₂. Sum [1,1] ∉ S₁ ∪ S₂.

**N8.** C(W) = span{[1,0],[0,1],[1,1]} — but col3=col1+col2, so C(W) = all of ℝ² (rank 2). N(W): x₁+x₃=0, x₂+x₃=0 → N(W) = span{[1,1,-1]}.

**N9.** Rank(W) ≤ min(rank(A), rank(B)) ≤ 2. W cannot span ℝ⁴ — C(W) is at most 2D inside ℝ⁴. This is why LoRA is a low-rank approximation — the update lives in a tiny subspace.

---

## Quick Reference — Both Lectures

```
LECTURE 1
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Row picture    → equations as lines/planes
Column picture → Ax as linear combo of columns ⭐
Matrix form    → Ax = b (compact notation)
Key question   → Do column combos fill all of ℝⁿ?

LECTURE 6
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Vector space   → closed under + and scalar ×
Subspace       → must contain 0; closed under both ops
Column space   → C(A) = span of columns = all Ax
                 Ax = b solvable ⟺ b ∈ C(A)
Null space     → N(A) = all x with Ax = 0
                 always a subspace (by linearity)
Rank           → dim(C(A)) = number of pivot columns

ML CONNECTIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Forward pass   → Ax in column picture
C(W)           → representational capacity of a layer
N(W)           → blind directions (dead features)
Low rank W     → bottleneck / LoRA territory
Full rank W    → layer can represent any output in ℝᵐ
```

---

## Hand-Note Task (Do This Right Now — No Peeking)

1. Sketch row picture and column picture for: 2x+y=5, x+3y=7
2. Write Ax for x=[1,2] using column picture for A=[[3,1],[2,4]]
3. One sentence each: define C(A) and N(A)
4. Why does Ax=b solvable ⟺ b ∈ C(A)?
5. Prove N(A) closed under addition (2 lines)
6. Counterexample: union of two subspaces is NOT a subspace
7. **New (ML):** A layer W: ℝ⁵ → ℝ³ has rank 2. What's the dimension of C(W)? Of N(W)?