# Day 1 Theory Notes
## Based on Gilbert Strang — MIT 18.06 Lecture 1 & Lecture 6

> **Write these by hand after reading.** The goal is intuition, not memorization.

---

## ━━ LECTURE 1 ━━  The Geometry of Linear Equations

### What is the fundamental problem of Linear Algebra?

Strang opens Lecture 1 with a direct statement:

> *"The fundamental problem of linear algebra is to solve a system of linear equations."*

Everything — every matrix, every subspace, every algorithm — connects back to this one goal.

---

### The Example System (2 equations, 2 unknowns)

```
2x  −  y  =  0
−x  + 2y  =  3
```

Strang shows **three completely different ways** to look at this same system. Each way gives you a different picture — and a different insight.

---

### WAY 1 — The Row Picture (one equation at a time)

Each equation is a **line** in the xy-plane.

```
2x − y = 0   →  a line through the origin (slope 2)
−x + 2y = 3  →  another line (slope 0.5, shifted)
```

**Plot them. They intersect at exactly one point: (x=1, y=2).**

```
    y
  3 |        ●  ← solution (1, 2)
  2 |      /  \
  1 |    /      \
  0 +---/--------\--→ x
       line 1   line 2
```

**Strang's key insight:** The row picture shows lines (in 2D) or planes (in 3D) meeting at a point. Works well in 2D, becomes *very hard* to see in 3D because three planes meeting at a point is almost impossible to visualize.

---

### WAY 2 — The Column Picture ⭐ (Strang puts a star on this)

Instead of rows, look at the **columns** of the coefficient matrix:

```
x · [2]  +  y · [-1]  =  [0]
    [-1]         [2]      [3]
```

This says: **"What combination of the column vectors gives us the right-hand side?"**

Column 1 = [2, -1] (call it the green vector)
Column 2 = [-1, 2] (call it the blue vector)
Target b = [0, 3]   (the gray vector we want to reach)

**Answer: 1 × [2,-1] + 2 × [-1,2] = [0, 3] ✓**

So x=1, y=2. Same answer, completely different picture.

```
     ↑
  3  |   . b=[0,3]
  2  |  /
  1  | /  col2=[-1,2] added twice
  0  +-------→
     |
    col1=[2,-1] added once
```

**Strang's key insight:** The column picture reframes the problem as: *"Can I find the right linear combination of columns to hit b?"* This is the heart of linear algebra.

---

### WAY 3 — The Matrix Form

Write it compactly as **Ax = b**:

```
A  =  [ 2  -1 ]    x = [ x ]    b = [ 0 ]
      [-1   2 ]        [ y ]        [ 3 ]
```

This is just a shorthand for the same system. The power of matrix notation is that it works identically whether you have 2 unknowns or 200.

---

### Extending to 3D (3 equations, 3 unknowns)

```
 2x −  y       =  0
−x  + 2y −  z  = −1
      −3y + 4z  =  4
```

**Row picture:** Three planes in 3D space. They should all meet at one point. But Strang notes this becomes *very difficult* to visualize — "almost impossible to spot the intersection."

**Column picture:** Still the same idea — find coefficients x, y, z to combine three 3D column vectors and hit b. In this example, b = the third column exactly, so z=1, x=0, y=0 is the solution.

**Strang's warning:** As dimensions grow, the row picture becomes useless for intuition. The column picture scales better — it always asks the same question: *"Is b in the span of the columns?"*

---

### The Big Question Strang Ends Lecture 1 With

> **"Do the linear combinations of the columns fill the entire space?"**

- If YES → Ax = b has a solution for **every** b
- If NO → some b's are unreachable; the system has no solution

This question about "filling the space" is exactly what column space captures — which is what Lecture 6 answers.

---

### How to Multiply Ax — Strang's Column Way

Strang shows two ways to think about Ax:

**Row way (usual):** Take dot products of each row with x.

**Column way (better for intuition):**
```
Ax  =  x₁ · (col 1 of A)  +  x₂ · (col 2 of A)  + ...
```

Ax is a **linear combination of columns of A**, with x providing the coefficients. This single insight unlocks everything that follows.

---

## ━━ LECTURE 6 ━━  Column Space and Null Space

> *"We're at the start of Chapter 3 — really getting to the center of linear algebra."*
> — Strang, opening of Lecture 6

---

### First: What is a Vector Space?

Before column space and null space, Strang reminds us what a **vector space** is:

A collection of vectors where:
1. You can **add** any two vectors and stay inside the space
2. You can **multiply** any vector by any scalar and stay inside the space

Both operations must keep you inside. These are the two closure rules.

**Standard examples:**
- ℝ² — all 2D vectors (the whole xy-plane)
- ℝ³ — all 3D vectors
- Just the zero vector {0} — the smallest possible vector space

---

### What is a Subspace?

A **subspace** is a vector space that lives *inside* a bigger vector space.

**Three requirements for S to be a subspace of ℝⁿ:**
1. The **zero vector** is in S
2. S is **closed under addition**: u + v ∈ S whenever u, v ∈ S
3. S is **closed under scalar multiplication**: cu ∈ S whenever u ∈ S

**Quick test — the zero vector rule:** If your set doesn't contain **0**, it's NOT a subspace. Period.

**Example:** A line through the origin in ℝ² IS a subspace. A line that doesn't pass through the origin is NOT (it fails the zero vector test).

---

### Strang's Subspace Examples (from Lecture 6)

Subspaces of ℝ³ — there are only these types:

```
Type 1: Just {0}          — a single point (the origin)
Type 2: A LINE through 0  — one direction, all scalings
Type 3: A PLANE through 0 — two directions, all combinations
Type 4: All of ℝ³         — the whole space
```

**Key point from Strang:** A plane in ℝ³ that doesn't go through the origin is NOT a subspace. It might look flat and nice, but it fails closure — add two vectors in it and you can land outside it.

---

### Union vs Intersection of Subspaces

Strang discusses this in Lecture 6 carefully.

**Union (P ∪ L):** Take all vectors in P (a plane) OR in L (a line). Is this a subspace?

**NO.** You can pick one vector from P and one from L, add them, and land somewhere outside both. Union almost never gives a subspace.

**Intersection (P ∩ L):** Take all vectors that are in BOTH P and L. Is this a subspace?

**YES — always.** The intersection of any two subspaces is still a subspace.

**Strang's example:** If P is a plane through origin and L is a line through origin (not in the plane), their intersection is just {0} — the zero vector. Still a valid (tiny) subspace.

---

### Column Space C(A)

**Definition:** The column space of A is the set of all linear combinations of the columns of A.

```
C(A)  =  { Ax : x ∈ ℝⁿ }
       =  span of all columns of A
```

**Why does this matter?** Strang states it clearly:

> *"The column space of A tells us when the equation Ax = b will have a solution x."*

**Ax = b has a solution ⟺ b is in C(A)**

Because Ax is always a linear combination of columns, b must be reachable from those columns.

---

### Column Space Example

```
A  =  [ 1  1  2 ]
      [ 2  1  3 ]
      [ 3  1  4 ]
      [ 4  1  5 ]
```

The third column = column 1 + column 2. So it's dependent. C(A) is a **plane** in ℝ⁴, not all of ℝ⁴.

**Only b's that lie in this plane have a solution Ax = b.**

Strang's classroom moment: He asks students to find b's that work. The trick: think of a solution x first, then compute b = Ax. That guarantees b is in C(A).

---

### Null Space N(A)

**Definition:** The null space of A is the set of all solutions to Ax = 0.

```
N(A)  =  { x ∈ ℝⁿ : Ax = 0 }
```

**Strang says:**

> *"The null space tells us which values of x solve the equation Ax = 0."*

**Is the null space really a subspace?** Strang verifies the two rules:

1. **Closure under addition:** If Ax = 0 and Ay = 0, then A(x+y) = Ax + Ay = 0 + 0 = 0 ✓
2. **Closure under scalar multiplication:** If Ax = 0, then A(cx) = c(Ax) = c·0 = 0 ✓

**Yes — the null space is always a subspace.** This is guaranteed by the linearity of A.

---

### Null Space Example

```
A  =  [ 1  2 ]
      [ 2  4 ]
```

Solve Ax = 0:
```
x₁ + 2x₂ = 0
2x₁ + 4x₂ = 0   ← same equation! (row 2 = 2 × row 1)
```

Solution: x₁ = −2x₂, so x₂ is free.

```
x = x₂ · [-2]    for any x₂ ∈ ℝ
           [ 1]
```

**N(A) = a line in ℝ² through the origin, pointing in direction [-2, 1].**

The matrix A is rank 1. It crushes an entire line down to zero.

---

### The Key Contrast: Column Space vs Null Space

| | Column Space C(A) | Null Space N(A) |
|---|---|---|
| **Lives in** | ℝᵐ (output space) | ℝⁿ (input space) |
| **Answers** | When does Ax = b have a solution? | What inputs x does A map to zero? |
| **Contains** | All possible outputs Ax | All x that A "ignores" |
| **Always has** | At least the zero vector | Always at least {0} |

---

### Strang's Subspace Check — 3 Questions to Always Ask

Whenever someone hands you a set S and asks "is it a subspace?", check:
1. Is **0** in S?
2. If u and v are in S, is **u + v** in S?
3. If u is in S and c is any scalar, is **cu** in S?

If all three: YES, subspace. Fail any one: NOT a subspace.

---

## Quick Reference — Both Lectures Together

```
LECTURE 1 CORE IDEAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Row picture    → equations as lines/planes
Column picture → Ax as linear combo of columns ⭐
Matrix form   → Ax = b (compact notation)

Key question: Do column combinations fill all of ℝⁿ?

LECTURE 6 CORE IDEAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Vector space  → closed under + and scalar ×
Subspace      → vector space inside a bigger one;
                must contain 0
Column space  → C(A) = span of columns = all Ax
               Ax = b solvable ⟺ b ∈ C(A)
Null space    → N(A) = all x with Ax = 0
               always a subspace (by linearity)
```

---

## Hand-Note Task (Do This Right Now)

> Without looking at this file, write answers to:
> 1. What are the three pictures of a linear system? Sketch each for 2×2.
> 2. What does Ax mean as a column combination?
> 3. Define column space and null space in one sentence each.
> 4. Why is C(A) relevant to solving Ax = b?
> 5. Prove that N(A) is closed under addition (2 lines).
> 6. Is the union of two subspaces always a subspace? Give a counterexample.