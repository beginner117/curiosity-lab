
# Project 2 — Gravitomagnetic (Frame-Dragging) Clock Effect

**Goal:** Estimate the tiny proper-time difference accumulated by **prograde** vs **retrograde** satellite clocks due to Earth's rotation dragging spacetime (Lense–Thirring / gravitomagnetic effect).

## Key estimate
Using Earth's angular momentum **J = I ω**, a first-order estimate for the per-orbit time separation is:

    Δτ_per_orbit ≈ 4π J / (M c^2) × cos(i)

With:
- I ≈ 0.3307 M R^2
- ω ≈ 0.0000729 rad/s
- → **Δτ_base ≈ 0.137 µs per orbit** at i=0° (equatorial).

At inclination i = 56° (Galileo-like), the cosine factor gives:
- **Δτ_per_orbit ≈ 0.077 µs per orbit**

Although extremely small, this provides a quantitative target for future **clock-based tests** of frame-dragging. Long data spans and ultra-stable clocks could, in principle, integrate this signal.

## Plots
- `proj2_gm_effect_vs_inclination.png` — Δτ per orbit vs inclination.
- `proj2_cumulative_divergence.png` — cumulative separation over many orbits for i = 56°.

## Next steps
- Refine with full post-Newtonian expressions and real orbit parameters.
- Assess detectability with current atomic clock stabilities and realistic noise.
