
# Project 3 — GNSS Relativistic Corrections Demonstrator

**Goal:** Show, with simple simulations, how GNSS relies on relativistic time corrections and how navigation would fail if they were ignored.

## Part A: Cumulative navigation error without relativity
GNSS satellite clocks run faster than ground clocks due to gravitational redshift and slower due to velocity time dilation. The **net** is about **+38 µs/day** (GPS-like). If a receiver ignored this:
- Time error after 1 day: ~38 µs ⇒ range error c Δt ≈ 11.4 km
- The plot `proj3_nav_error_growth.png` shows linear growth over a week.

## Part B: Broadcast relativistic correction (eccentricity term)
Receivers apply an additional correction (proportional to e * sin E) to account for periodic relativistic effects in eccentric orbits:

    Δt_rel = F * e * sqrt(a) * sin(E),   with F = -2 sqrt(μ)/c^2

`proj3_broadcast_rel_correction.png` shows a **ns-level** correction over one orbit for e = 0.01.

## How to run
- Open `proj3_demo.py` or adapt in a notebook.
- Extend by parsing real RINEX navigation files to extract the same term from live data.
