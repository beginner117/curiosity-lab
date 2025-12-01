
This repository contains simple, intuitive Python toy models to build intuition for **hybrid quantum–mechanical systems**.  

---

## Contents

### 1. Levitated Particle in an Optical / Magnetic Trap
**Goal:** Simulate the center-of-mass dynamics of a levitated particle inside either:
- a stiffer optical trap, or  
- a softer, low-dissipation magnetic trap  

using the damped harmonic oscillator equation:

\[
m \ddot{x} + \gamma \dot{x} + kx = 0
\]
---

### 2. Qubit–Oscillator Coupling (Jaynes–Cummings Toy Model)
**Goal:** Demonstrate excitation exchange between:
- a two-level system (qubit), and  
- a single mechanical mode (harmonic oscillator)  

via a simplified Jaynes–Cummings Hamiltonian:


\[
H = \hbar \omega_m a^\dagger a + \frac{\hbar \Omega}{2} \sigma_z + \hbar g (\sigma^+ a + \sigma^- a^\dagger)
\]

---

### 3. Gravity-Mediated Interaction Between Two Masses (Classical Toy Model)
**Goal:** Simulate two harmonically trapped masses interacting via a weak Newtonian gravitational potential:

\[
V_g = - \frac{G m^2}{d^3} x_1 x_2
\]

leading to coupled oscillator equations. 

---


