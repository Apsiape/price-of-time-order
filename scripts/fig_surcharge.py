"""Figure 3: the time-order surcharge of amplitude damping is a difference of two maxima.

Amplitude damping with p = 1/2 on a qubit with gap E, at beta*E = ln 2, so that one unit
of k_B T ln 2 is one unit of E. For an input with excited population x (diagonal inputs are optimal):
    c(x)     = h(x) - h(x/2) - x/2        batch integrand; its maximum is the capacity
    c(x)+m(x) = h(x/2) - x/2              real-time integrand; its maximum is kappa_beta
    m(x)     = 2 h(x/2) - h(x)            least output-device mutual information
in bits, that is, in units of E per use.
Usage: python scripts/fig_surcharge.py   (run from the repository root)
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "serif", "font.serif": ["DejaVu Serif"], "mathtext.fontset": "cm"})

def h(x):
    x = np.clip(x, 1e-300, 1.0)
    y = np.clip(1.0 - x, 1e-300, 1.0)
    return -(x * np.log2(x) + y * np.log2(y)) * ((x > 0) & (x < 1))

x = np.linspace(0.0, 1.0, 200001)
c = h(x) - h(x / 2) - x / 2
cm = h(x / 2) - x / 2
m = 2 * h(x / 2) - h(x)

ib, ir = np.argmax(c), np.argmax(cm)
xb, cap = x[ib], c[ib]
xr, kap = x[ir], cm[ir]
assert abs(xr - 2 / 3) < 1e-4 and abs(kap - 0.585) < 5e-4
assert abs(cap - 0.154) < 5e-4 and abs(m[ir] - 0.918) < 5e-4
assert abs((kap - cap) - 0.431) < 5e-4

if __name__ == "__main__":
    fig, ax = plt.subplots(figsize=(4.8, 3.3))
    ax.plot(x, m, color="0.55", lw=1.3, ls=":", label=r"$m_\rho$ (correlation term)")
    ax.plot(x, cm, color="C0", lw=1.8, label=r"$c_\rho+m_\rho$ (real time)")
    ax.plot(x, c, color="C1", lw=1.6, ls="--", label=r"$c_\rho$ (batch)")
    ax.plot([xr], [kap], "o", color="C0", ms=4.5)
    ax.plot([xb], [cap], "o", color="C1", ms=4.5)
    ax.plot([xr], [m[ir]], "o", color="0.55", ms=3.5)
    ax.annotate(r"$\kappa_\beta=%.3f$" % kap, (xr, kap), xytext=(xr + 0.04, kap + 0.09), fontsize=8)
    ax.annotate(r"capacity $%.3f$" % cap, (xb, cap), xytext=(xb - 0.05, cap - 0.17), fontsize=8,
                arrowprops=dict(arrowstyle="-", color="0.4", lw=0.6))
    ax.annotate(r"$m_\rho=%.3f$" % m[ir], (xr, m[ir]), xytext=(xr + 0.06, m[ir] + 0.04), fontsize=8)
    ax.axhline(kap, color="C0", lw=0.5, alpha=0.5)
    ax.axhline(cap, color="C1", lw=0.5, alpha=0.5)
    ax.annotate("", xy=(0.97, kap), xytext=(0.97, cap),
                arrowprops=dict(arrowstyle="<->", color="k", lw=0.8))
    ax.text(0.955, (kap + cap) / 2, "surcharge\n$%.3f$" % (kap - cap), ha="right", va="center", fontsize=8)
    ax.set_xlabel(r"excited population $x$ of the input")
    ax.set_ylabel(r"bits per use (units of $E$)")
    ax.set_xlim(0, 1)
    ax.set_ylim(-0.6, 2.1)
    ax.axhline(0, color="0.75", lw=0.5)
    ax.legend(fontsize=7.5, frameon=False, loc="upper left", handlelength=2.2)
    fig.tight_layout()
    fig.savefig("paper/fig-surcharge.pdf")
    print("batch optimum x=%.4f, capacity %.4f; real-time optimum x=%.4f, kappa %.4f, m there %.4f, m at batch optimum %.4f; surcharge %.4f"
          % (xb, cap, xr, kap, m[ir], m[ib], kap - cap))
