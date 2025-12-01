
# Project 1 — Simulating Relativistic Time Dilation for Satellite Clocks

**Goal:** Reproduce the gravitational redshift + special-relativistic time dilation for a satellite clock, and show the periodic **ns-level modulation** for an eccentric orbit.

## What this code does
- Generates a Keplerian orbit (semi-major axis a = 29600 km; eccentricity e = 0 and e = 0.16).
- Computes fractional proper-time rate relative to a ground clock: Δ = (U_sat - U_ground)/c^2 - (v_sat^2 - v_ground^2)/(2 c^2).
- Integrates Δ over time to get the **clock offset vs. ground**.
- For the eccentric case, detrends the linear drift to reveal the **orbital residual** (hundreds of ns scale).

## How to run
- Open `proj1_sim.py` or replicate the functions in a notebook.
- The plots saved:
  - `proj1_circular_offset.png` – per-day net offset for a circular MEO.
  - `proj1_eccentric_residual.png` – detrended ns-level orbital residual for e=0.16.

## Notes
- The typical GPS/Galileo net offset is on the order of +38 µs/day (gravity makes space clocks run faster; velocity slows them; net is positive). The exact number depends on altitude; the circular plot shows this scale.
- The eccentric case produces a sinusoidal residual per orbit; the exact amplitude depends on eccentricity and orbit geometry, but **hundreds of ns** are typical for noticeable eccentricity.
