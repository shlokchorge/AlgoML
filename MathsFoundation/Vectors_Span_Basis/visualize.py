"""
Day 1 Visualizations — Strang MIT 18.06 Lec 1 & Lec 6
=======================================================
8 diagrams covering:
  Lec 1: Row picture, Column picture, 3D planes
  Lec 6: Vector space, Subspaces of R3, Column space,
          Null space, C(A) vs N(A) contrast

Run:  python visualize.py
Requires: pip install numpy matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrow

# ── Global style ─────────────────────────────────
plt.rcParams.update({
    "figure.facecolor": "#0d1117",
    "axes.facecolor":   "#0d1117",
    "text.color":       "white",
    "axes.labelcolor":  "#8b949e",
    "xtick.color":      "#8b949e",
    "ytick.color":      "#8b949e",
})
BG   = "#0d1117"
RED  = "#e05c5c"
BLUE = "#4f9cf9"
GRN  = "#3dd68c"
YLW  = "#f5c542"
GRAY = "#8b949e"
PRP  = "#c792ea"
ORG  = "#ff9d6f"

def savefig(name):
    plt.savefig(name, dpi=130, bbox_inches="tight", facecolor=BG)
    print(f"  ✓ {name}")
    plt.show()

def ax_style(ax, title, xlim=(-4,4), ylim=(-4,4), grid=True):
    ax.set_facecolor(BG)
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.axhline(0, color=GRAY, lw=0.7, alpha=0.4)
    ax.axvline(0, color=GRAY, lw=0.7, alpha=0.4)
    ax.set_title(title, color="white", fontsize=11, fontweight="bold", pad=8)
    for sp in ax.spines.values():
        sp.set_edgecolor(GRAY); sp.set_alpha(0.3)
    ax.tick_params(labelsize=8)
    if grid:
        ax.grid(True, color=GRAY, alpha=0.12, lw=0.5)

def arrow(ax, vec, origin=(0,0), color=RED, label="", lw=2.5, off=(0.12,0.12)):
    ax.annotate("", xy=(origin[0]+vec[0], origin[1]+vec[1]), xytext=origin,
                arrowprops=dict(arrowstyle="-|>", color=color, lw=lw, mutation_scale=18))
    if label:
        tip = (origin[0]+vec[0]+off[0], origin[1]+vec[1]+off[1])
        ax.text(*tip, label, color=color, fontsize=10, fontweight="bold")


# ══════════════════════════════════════════════════════
# DIAGRAM 1 — Lec 1: Row Picture (lines meeting)
# ══════════════════════════════════════════════════════
def diagram1_row_picture():
    print("\n[1] Row Picture — Two Lines Meeting")
    fig, ax = plt.subplots(figsize=(7, 7), facecolor=BG)
    ax_style(ax, "DIAGRAM 1 — Row Picture\n2x − y = 0  and  −x + 2y = 3")

    x = np.linspace(-3.5, 3.5, 300)

    # Line 1: 2x - y = 0  →  y = 2x
    y1 = 2 * x
    ax.plot(x, y1, color=RED, lw=2.5, label="2x − y = 0  (y = 2x)")

    # Line 2: -x + 2y = 3  →  y = (x+3)/2
    y2 = (x + 3) / 2
    ax.plot(x, y2, color=BLUE, lw=2.5, label="−x + 2y = 3  (y = (x+3)/2)")

    # Solution point
    ax.plot(1, 2, 'o', color=GRN, markersize=14, zorder=5)
    ax.annotate("Solution\n(x=1, y=2)", xy=(1, 2), xytext=(1.5, 0.7),
                color=GRN, fontsize=11, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=GRN, lw=1.5))

    ax.legend(fontsize=10, facecolor="#1a1f2e", edgecolor=GRAY, labelcolor="white",
              loc="upper left")

    # Annotation boxes
    ax.text(-3.5, 3.5,
            "Each equation = a line\nWhere they cross = solution\n(Row picture: one eq at a time)",
            color=GRAY, fontsize=9, va="top",
            bbox=dict(facecolor="#1a1f2e", edgecolor=GRAY, alpha=0.8, pad=5))

    savefig("day1_diagram1_row_picture.png")


# ══════════════════════════════════════════════════════
# DIAGRAM 2 — Lec 1: Column Picture (vector combination)
# ══════════════════════════════════════════════════════
def diagram2_column_picture():
    print("\n[2] Column Picture — Combining Column Vectors")
    fig, axes = plt.subplots(1, 2, figsize=(14, 7), facecolor=BG)
    fig.suptitle("DIAGRAM 2 — Column Picture\n"
                 "x·col₁ + y·col₂ = b    →    1·[2,−1] + 2·[−1,2] = [0,3]",
                 color="white", fontsize=12, fontweight="bold")

    # ── Left: Show all three vectors individually ──
    ax = axes[0]
    ax_style(ax, "The Three Vectors")
    arrow(ax, [2, -1], color=RED,  label="col₁=[2,−1]")
    arrow(ax, [-1, 2], color=BLUE, label="col₂=[−1,2]")
    arrow(ax, [0, 3],  color=GRN,  label="b=[0,3]", lw=3)
    ax.text(-3.8, 3.5,
            "Question:\nWhat combo of\ncol₁ and col₂\nmakes b?",
            color=GRAY, fontsize=9,
            bbox=dict(facecolor="#1a1f2e", edgecolor=GRAY, alpha=0.8, pad=4))

    # ── Right: Tip-to-tail combination ──
    ax = axes[1]
    ax_style(ax, "Solution: 1×col₁ + 2×col₂ = b  (tip-to-tail)")
    # Step 1: draw 1×col1 from origin
    arrow(ax, [2, -1], color=RED,  label="1×col₁", off=(0.1, -0.25))
    # Step 2: draw 2×col2 from tip of col1
    arrow(ax, [-2, 4], origin=(2, -1), color=BLUE, label="2×col₂", off=(0.1, 0.1))
    # Result
    arrow(ax, [0, 3], color=GRN, label="b=[0,3] ✓", lw=3.5)

    ax.text(-3.8, 3.5,
            "Walk along 1×col₁\nthen 2×col₂.\nLand on b!\n→ x=1, y=2",
            color=GRN, fontsize=10, fontweight="bold",
            bbox=dict(facecolor="#1a1f2e", edgecolor=GRN, alpha=0.8, pad=4))

    plt.tight_layout()
    savefig("day1_diagram2_column_picture.png")


# ══════════════════════════════════════════════════════
# DIAGRAM 3 — Lec 1: Row vs Column side by side comparison
# ══════════════════════════════════════════════════════
def diagram3_row_vs_column():
    print("\n[3] Row Picture vs Column Picture — Side by Side")
    fig, axes = plt.subplots(1, 2, figsize=(14, 6), facecolor=BG)
    fig.suptitle("DIAGRAM 3 — Same System, Two Views\n"
                 "2x − y = 0,   −x + 2y = 3",
                 color="white", fontsize=12, fontweight="bold")

    # ── Row picture (left) ──
    ax = axes[0]
    ax_style(ax, "ROW PICTURE\n(equations = lines)")
    x = np.linspace(-3.5, 3.5, 300)
    ax.plot(x, 2*x, color=RED,  lw=2.5, label="Eq 1: y=2x")
    ax.plot(x, (x+3)/2, color=BLUE, lw=2.5, label="Eq 2: y=(x+3)/2")
    ax.plot(1, 2, 'o', color=GRN, markersize=12, zorder=5)
    ax.text(1.2, 2.2, "(1,2)\nSOLUTION", color=GRN, fontsize=9, fontweight="bold")
    ax.legend(fontsize=9, facecolor="#1a1f2e", edgecolor=GRAY, labelcolor="white")
    ax.text(-3.5, -3.0, "View: equations\nGeometry: lines cross", color=GRAY, fontsize=9)

    # ── Column picture (right) ──
    ax = axes[1]
    ax_style(ax, "COLUMN PICTURE\n(vectors = arrows)")
    arrow(ax, [2,-1], color=RED,  label="col₁", off=(0.12,-0.3))
    arrow(ax, [-2,4], origin=(2,-1), color=BLUE, label="2×col₂", off=(0.1,0.1))
    arrow(ax, [0, 3], color=GRN,  label="b ✓", lw=3.5)
    ax.text(-3.5, -3.0, "View: columns\nGeometry: arrows combine", color=GRAY, fontsize=9)

    for ax in axes:
        ax.set_xlabel("x axis", color=GRAY, fontsize=8)
        ax.set_ylabel("y axis", color=GRAY, fontsize=8)

    plt.tight_layout()
    savefig("day1_diagram3_row_vs_column.png")


# ══════════════════════════════════════════════════════
# DIAGRAM 4 — Lec 1: 3D Row Picture (three planes)
# ══════════════════════════════════════════════════════
def diagram4_3d_planes():
    print("\n[4] 3D Row Picture — Three Planes Meeting at a Point")
    fig = plt.figure(figsize=(9, 8), facecolor=BG)
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor(BG)

    # Plot three planes: z=1 is the solution (x=0,y=0,z=1)
    u = np.linspace(-1.5, 1.5, 15)
    v = np.linspace(-1.5, 1.5, 15)
    U, V = np.meshgrid(u, v)

    # Plane 1: 2x - y = 0  → y = 2x  (vertical plane)
    X1 = U
    Y1 = 2*U
    Z1 = V
    ax.plot_surface(X1, Y1, Z1, alpha=0.25, color="#e05c5c")

    # Plane 2: -x + 2y - z = -1  → z = -x + 2y + 1
    X2 = U
    Y2 = V
    Z2 = -U + 2*V + 1
    ax.plot_surface(X2, Y2, Z2, alpha=0.25, color="#4f9cf9")

    # Plane 3: -3y + 4z = 4  → z = (4 + 3y)/4
    X3 = V
    Y3 = U
    Z3 = (4 + 3*U) / 4
    ax.plot_surface(X3, Y3, Z3, alpha=0.25, color="#3dd68c")

    # Solution point (0, 0, 1)
    ax.scatter([0], [0], [1], color=YLW, s=120, zorder=5)
    ax.text(0.1, 0.1, 1.1, "Solution\n(0,0,1)", color=YLW, fontsize=9, fontweight="bold")

    ax.set_xlabel("x", color=GRAY)
    ax.set_ylabel("y", color=GRAY)
    ax.set_zlabel("z", color=GRAY)
    ax.set_title("DIAGRAM 4 — 3D Row Picture\nThree planes, one solution point\n"
                 "(Strang: 'almost impossible to spot!')",
                 color="white", fontsize=11, fontweight="bold")
    ax.tick_params(colors=GRAY, labelsize=7)

    # Legend
    patches = [
        mpatches.Patch(color="#e05c5c", alpha=0.6, label="Plane 1: 2x−y=0"),
        mpatches.Patch(color="#4f9cf9", alpha=0.6, label="Plane 2: −x+2y−z=−1"),
        mpatches.Patch(color="#3dd68c", alpha=0.6, label="Plane 3: −3y+4z=4"),
    ]
    ax.legend(handles=patches, loc="upper left", facecolor="#1a1f2e",
              edgecolor=GRAY, labelcolor="white", fontsize=8)

    savefig("day1_diagram4_3d_planes.png")


# ══════════════════════════════════════════════════════
# DIAGRAM 5 — Lec 6: Subspaces of R³ (all four types)
# ══════════════════════════════════════════════════════
def diagram5_subspaces_of_R3():
    print("\n[5] Lec 6 — All Subspace Types of R³")
    fig, axes = plt.subplots(1, 4, figsize=(18, 5), facecolor=BG)
    fig.suptitle("DIAGRAM 5 — Every Type of Subspace in ℝ³  (Strang, Lec 6)",
                 color="white", fontsize=13, fontweight="bold")

    titles  = ["Type 1: Just {0}", "Type 2: A Line", "Type 3: A Plane", "Type 4: All of ℝ³"]
    colors  = [GRN, RED, BLUE, YLW]
    descs   = [
        "dim = 0\nOnly the origin.\nSmallest subspace.",
        "dim = 1\nAll c·v for any scalar c.\ne.g. span of one vector.",
        "dim = 2\nAll a·u + b·v.\ne.g. span of two\nindependent vectors.",
        "dim = 3\nEverything in ℝ³.\nAll vectors reachable."
    ]

    for i, ax in enumerate(axes):
        ax_style(ax, titles[i], xlim=(-3,3), ylim=(-3,3))
        c = colors[i]

        if i == 0:  # Just origin
            ax.plot(0, 0, 'o', color=c, markersize=16)
            ax.text(0.2, 0.2, "{0}", color=c, fontsize=14, fontweight="bold")

        elif i == 1:  # Line
            t = np.linspace(-3, 3, 200)
            ax.plot(t*0.8, t*0.6, color=c, lw=3, label="span{v}")
            arrow(ax, [0.8, 0.6], color=c, label="v")
            ax.text(-2.8, 2.5, "All c·v\nfor c ∈ ℝ", color=c, fontsize=9, fontweight="bold")

        elif i == 2:  # Plane (shaded)
            ax.set_facecolor("#0d1f2e")
            t = np.linspace(-3, 3, 300)
            for s in np.linspace(-3, 3, 12):
                ax.plot(t, s + 0*t, color=c, lw=0.4, alpha=0.3)
                ax.plot(s + 0*t, t, color=c, lw=0.4, alpha=0.3)
            arrow(ax, [2, 0], color=c, label="u")
            arrow(ax, [0, 2], color=PRP, label="v")
            ax.text(-2.8, 2.5, "All a·u+b·v\n(the whole plane)", color=c,
                    fontsize=9, fontweight="bold")

        elif i == 3:  # All of R3
            ax.set_facecolor("#1a1f0d")
            for x_ in np.linspace(-3, 3, 10):
                ax.axvline(x_, color=c, lw=0.3, alpha=0.2)
            for y_ in np.linspace(-3, 3, 10):
                ax.axhline(y_, color=c, lw=0.3, alpha=0.2)
            ax.text(0, 0, "All of ℝ³\n∞ vectors", color=c, fontsize=11,
                    fontweight="bold", ha="center", va="center")

        ax.text(-2.8, -2.7, descs[i], color=GRAY, fontsize=8)

    plt.tight_layout()
    savefig("day1_diagram5_subspace_types.png")


# ══════════════════════════════════════════════════════
# DIAGRAM 6 — Lec 6: Column Space — what Ax reaches
# ══════════════════════════════════════════════════════
def diagram6_column_space():
    print("\n[6] Lec 6 — Column Space: What Does A Reach?")
    fig, axes = plt.subplots(1, 2, figsize=(14, 6), facecolor=BG)
    fig.suptitle("DIAGRAM 6 — Column Space C(A)\n"
                 "Ax = b is solvable  ⟺  b is in C(A)",
                 color="white", fontsize=12, fontweight="bold")

    # ── Full rank case (rank 2) — C(A) = all of R² ──
    ax = axes[0]
    ax_style(ax, "Full Rank: A has 2 independent cols\nC(A) = all of ℝ²  →  every b reachable")
    ax.set_facecolor("#0d1a0d")
    # fill plane
    for x_ in np.linspace(-4, 4, 14):
        ax.axvline(x_, color=GRN, lw=0.3, alpha=0.2)
    for y_ in np.linspace(-4, 4, 14):
        ax.axhline(y_, color=GRN, lw=0.3, alpha=0.2)
    arrow(ax, [2, 1], color=GRN, label="col₁")
    arrow(ax, [0, 2], color=BLUE, label="col₂")
    # Some reachable b's
    for bx, by in [(3,2), (-2,3), (-1,-2), (2,-1)]:
        ax.plot(bx, by, 's', color=YLW, markersize=8, alpha=0.8)
    ax.text(-3.8, 3.5, "★ Any b is reachable!\nAx=b always has a solution",
            color=GRN, fontsize=9, fontweight="bold",
            bbox=dict(facecolor="#0a1a0a", edgecolor=GRN, pad=4, alpha=0.9))
    ax.text(1.5, -3.5, "Yellow squares = some b's\nAll are in C(A)", color=YLW, fontsize=8)

    # ── Rank 1 case — C(A) = a line ──
    ax = axes[1]
    ax_style(ax, "Rank 1: A has dependent cols\nC(A) = a LINE  →  most b's unreachable")
    c1 = np.array([1, 2])
    c2 = np.array([2, 4])   # c2 = 2*c1 !
    t = np.linspace(-2, 2, 200)
    ax.plot(t*c1[0], t*c1[1], color=GRN, lw=3, alpha=0.8, label="C(A) = line")
    arrow(ax, c1, color=GRN, label="col₁=[1,2]")
    arrow(ax, c2, color=BLUE, label="col₂=[2,4]=2·col₁")
    # Reachable b on line
    ax.plot(1.5, 3, 's', color=GRN, markersize=10, zorder=5)
    ax.text(1.6, 3.1, "b=[1.5,3] ✓\n(on the line)", color=GRN, fontsize=8)
    # Unreachable b off line
    ax.plot(2, 1, 'x', color=RED, markersize=12, mew=2.5, zorder=5)
    ax.text(2.1, 1.1, "b=[2,1] ✗\n(off the line)", color=RED, fontsize=8)
    ax.legend(fontsize=8, facecolor="#1a1f2e", edgecolor=GRAY, labelcolor="white")
    ax.text(-3.8, -3.3, "col₂ = 2·col₁ → dependent!\nRank = 1, C(A) is a line",
            color=GRAY, fontsize=8)

    plt.tight_layout()
    savefig("day1_diagram6_column_space.png")


# ══════════════════════════════════════════════════════
# DIAGRAM 7 — Lec 6: Null Space — what maps to zero
# ══════════════════════════════════════════════════════
def diagram7_null_space():
    print("\n[7] Lec 6 — Null Space: What Does A Crush to Zero?")
    fig, axes = plt.subplots(1, 2, figsize=(14, 7), facecolor=BG)
    fig.suptitle("DIAGRAM 7 — Null Space N(A)\n"
                 "All x with Ax = 0   |   A = [[1,2],[2,4]]  (rank 1)",
                 color="white", fontsize=12, fontweight="bold")

    A = np.array([[1, 2], [2, 4]])

    # ── Left: Input space — the null space line ──
    ax = axes[0]
    ax_style(ax, "INPUT SPACE ℝ²\nNull space = line of direction [−2, 1]")
    null_dir = np.array([-2, 1])
    t = np.linspace(-1.8, 1.8, 200)
    ax.plot(t*null_dir[0], t*null_dir[1], color=RED, lw=3, alpha=0.8,
            label="N(A): all t·[−2,1]")
    arrow(ax, null_dir, color=RED, label="[−2,1]")
    arrow(ax, -null_dir, color=RED)
    # A non-null vector
    arrow(ax, [1, 1], color=BLUE, label="[1,1] ← not in N(A)")
    ax.plot(0, 0, 'o', color=GRN, markersize=10)
    ax.text(0.15, 0.15, "origin\nalways in N(A)", color=GRN, fontsize=8)
    ax.legend(fontsize=8, facecolor="#1a1f2e", edgecolor=GRAY, labelcolor="white",
              loc="lower right")
    ax.text(-3.8, 3.5,
            "Solve Ax=0:\nx₁ + 2x₂ = 0\n→ x₁ = −2x₂\nN(A) = line through 0",
            color=GRAY, fontsize=9,
            bbox=dict(facecolor="#1a1f2e", edgecolor=GRAY, alpha=0.8, pad=4))

    # ── Right: Mapping diagram (arrow shows what happens under A) ──
    ax = axes[1]
    ax.set_facecolor(BG)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis("off")
    ax.set_title("What A Does to Each Vector", color="white",
                 fontsize=11, fontweight="bold")

    def draw_box(x, y, w, h, label, body, color):
        rect = mpatches.FancyBboxPatch((x,y), w, h, boxstyle="round,pad=0.1",
                                       facecolor=color+"22", edgecolor=color, lw=2)
        ax.add_patch(rect)
        ax.text(x+w/2, y+h-0.3, label, ha="center", color=color,
                fontsize=9, fontweight="bold")
        ax.text(x+w/2, y+h/2-0.1, body, ha="center", va="center",
                color="white", fontsize=8, linespacing=1.5)

    # Input
    draw_box(0.3, 5.0, 3.5, 2.5, "t·[−2, 1]  ∈ N(A)", "null space inputs\ndim = 1\nany t ∈ ℝ", RED)
    draw_box(0.3, 1.5, 3.5, 2.5, "[1, 1]  ∉ N(A)", "non-null input\nmaps to nonzero", BLUE)

    # Output
    draw_box(6.2, 5.0, 3.5, 2.5, "[0, 0]", "zero vector\nA always sends\nN(A) here", RED)
    draw_box(6.2, 1.5, 3.5, 2.5, "A·[1,1]=[3,6]", "nonzero output\nin C(A)", BLUE)

    # Arrows
    ax.annotate("", xy=(6.1,6.2), xytext=(3.9,6.2),
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=2, mutation_scale=15))
    ax.text(4.9, 6.5, "A maps to 0", ha="center", color=RED, fontsize=9)
    ax.annotate("", xy=(6.1,2.7), xytext=(3.9,2.7),
                arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=2, mutation_scale=15))
    ax.text(4.9, 3.0, "A maps to C(A)", ha="center", color=BLUE, fontsize=9)

    ax.text(5.0, 0.5, "rank + nullity = 1 + 1 = 2 = n  ✓",
            ha="center", color=GRN, fontsize=10, fontweight="bold")

    plt.tight_layout()
    savefig("day1_diagram7_null_space.png")


# ══════════════════════════════════════════════════════
# DIAGRAM 8 — Lec 6: Subspace test — union vs intersection
# ══════════════════════════════════════════════════════
def diagram8_union_vs_intersection():
    print("\n[8] Lec 6 — Union ✗  vs  Intersection ✓  of Subspaces")
    fig, axes = plt.subplots(1, 2, figsize=(14, 6), facecolor=BG)
    fig.suptitle("DIAGRAM 8 — Strang Lec 6: Union vs Intersection of Subspaces\n"
                 "Union is usually NOT a subspace | Intersection ALWAYS is",
                 color="white", fontsize=12, fontweight="bold")

    # ── Left: Union (NOT a subspace) ──
    ax = axes[0]
    ax_style(ax, "P ∪ L  =  NOT a subspace ✗\n(adding one from each lands OUTSIDE both)")
    # Plane P: horizontal (the x-axis line in 2D represents it)
    t = np.linspace(-3.5, 3.5, 300)
    ax.fill_between(t, -0.05, 0.05, color=BLUE, alpha=0.3)
    ax.plot(t, 0*t, color=BLUE, lw=2.5, label="L: x-axis (subspace)")
    # Line L: diagonal
    ax.plot(t, t, color=RED, lw=2.5, label="P: y=x line (subspace)")
    # Pick one from each and add
    v_from_L = np.array([2, 0])
    w_from_P = np.array([1, 1])
    sum_vw   = v_from_L + w_from_P
    arrow(ax, v_from_L, color=BLUE, label="v∈L")
    arrow(ax, w_from_P, color=RED, label="w∈P")
    arrow(ax, sum_vw, color=YLW, label="v+w=?", lw=3)
    ax.plot(*sum_vw, 'x', color=YLW, markersize=14, mew=3)
    ax.text(sum_vw[0]+0.1, sum_vw[1]-0.4, "v+w=[3,1]\n✗ NOT on L or P!",
            color=YLW, fontsize=9, fontweight="bold")
    ax.legend(fontsize=8, facecolor="#1a1f2e", edgecolor=GRAY, labelcolor="white",
              loc="lower right")
    ax.text(-3.5, 3.5,
            "Took v from L (blue)\nTook w from P (red)\nv+w is in NEITHER\n→ Union fails closure!",
            color=GRAY, fontsize=9,
            bbox=dict(facecolor="#1a1f2e", edgecolor=RED, alpha=0.8, pad=4))

    # ── Right: Intersection (IS a subspace) ──
    ax = axes[1]
    ax_style(ax, "P ∩ L  =  always a subspace ✓\n(Strang's example: only the origin {0})")
    ax.plot(t, 0*t, color=BLUE, lw=2.5, label="L: x-axis")
    ax.plot(t, 1.5*t, color=RED, lw=2.5, label="P: y=1.5x")
    # Intersection = origin
    ax.plot(0, 0, 'o', color=GRN, markersize=16, zorder=5)
    ax.text(0.15, 0.3, "P∩L = {0}\nOnly origin\nis in BOTH",
            color=GRN, fontsize=10, fontweight="bold")
    ax.legend(fontsize=8, facecolor="#1a1f2e", edgecolor=GRAY, labelcolor="white",
              loc="lower right")
    ax.text(-3.5, 3.5,
            "Origin is always in both.\nIntersection = {0}\nThis IS a subspace!\n(dim 0 subspace)",
            color=GRN, fontsize=9, fontweight="bold",
            bbox=dict(facecolor="#1a1f2e", edgecolor=GRN, alpha=0.8, pad=4))

    plt.tight_layout()
    savefig("day1_diagram8_union_intersection.png")


# ══════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════
if __name__ == "__main__":
    print("=" * 60)
    print("  Day 1 — 8 Diagrams from Strang MIT 18.06 Lec 1 & Lec 6")
    print("=" * 60)
    print("\nLECTURE 1 — Geometry of Linear Equations")
    diagram1_row_picture()           # Lines crossing
    diagram2_column_picture()        # Column vectors combining
    diagram3_row_vs_column()         # Side-by-side comparison
    diagram4_3d_planes()             # 3D row picture (planes)

    print("\nLECTURE 6 — Column Space and Null Space")
    diagram5_subspaces_of_R3()       # All 4 subspace types
    diagram6_column_space()          # Full rank vs rank-1 C(A)
    diagram7_null_space()            # N(A) + mapping diagram
    diagram8_union_vs_intersection() # Strang's union/intersection lesson

    print("\n" + "="*60)
    print("  All 8 diagrams saved as PNG files.")
    print("  Read theory.md alongside each diagram:")
    print("  - Diagrams 1-4  →  theory.md LECTURE 1 sections")
    print("  - Diagrams 5-8  →  theory.md LECTURE 6 sections")
    print("="*60)