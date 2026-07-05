"""
dCas12f/p53 Epigenetic Circuit — ODE Model
--------------------------------------------
Simulates the autoregulatory dynamics of the feedback-controlled dCas12f
epigenetic circuit described in the SynBio Registry model writeup.

State variables:
    M : active circuit mRNA concentration
    C : intracellular epigenetic scaffold concentration
    P : total intracellular p53 concentration

This is a theoretical / hypothesis-generating model, not experimentally
validated. See docs/model_writeup.md for full derivation and assumptions.
"""

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


def circuit_odes(t, y, params):
    M, C, P = y
    p = params

    dM_dt = (
        p["alpha_m"] * (1 / (1 + (P / p["K_beta"]) ** p["m"])) * p["theta_L"]
        - p["gamma_m"] * M
    )
    dC_dt = p["alpha_c"] * M - p["gamma_c"] * C
    dP_dt = (
        p["Vmax"] * (C ** p["n"]) / (p["K"] ** p["n"] + C ** p["n"])
        - p["gamma_p"] * P
    )

    return [dM_dt, dC_dt, dP_dt]


PARAMS = {
    "alpha_m": 1.0,
    "gamma_m": 0.2,
    "alpha_c": 0.8,
    "gamma_c": 0.15,
    "Vmax": 5.0,
    "K": 2.0,
    "n": 2,
    "K_beta": 3.0,
    "m": 2,
    "gamma_p": 0.25,
    "theta_L": 1.0,
}


def run_simulation(params=PARAMS, y0=(0, 0, 0), t_span=(0, 100), n_points=500):
    t_eval = np.linspace(*t_span, n_points)
    sol = solve_ivp(
        circuit_odes, t_span, y0, t_eval=t_eval, args=(params,), method="RK45"
    )
    return sol


def plot_simulation(sol, title="dCas12f/p53 Circuit Dynamics"):
    plt.figure(figsize=(8, 5))
    plt.plot(sol.t, sol.y[0], label="[M] mRNA")
    plt.plot(sol.t, sol.y[1], label="[C] Scaffold")
    plt.plot(sol.t, sol.y[2], label="[P] p53")
    plt.xlabel("Time")
    plt.ylabel("Concentration (a.u.)")
    plt.title(title)
    plt.legend()
    plt.tight_layout()
    plt.savefig("figures/simulation_output.png", dpi=200)
    plt.show()


if __name__ == "__main__":
    sol = run_simulation()
    plot_simulation(sol, title="State 2 -> 3 Transition (Ligand Present)")
