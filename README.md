## Scheduling Optimization – Heuristic Approach

This project implements a simple Operations Research scheduling problem:
minimizing total weighted lateness under deadline constraints.

### Problem
- Each task has:
  - processing time
  - deadline
  - lateness penalty
- Objective: minimize total penalty due to late completion

### Approach
- Greedy heuristic: Earliest Due Date (EDD)
- Simple cost evaluation
- Emphasis on clarity and correctness over brute force

### Why Heuristics?
Exact optimization becomes computationally expensive as problem size grows.
Heuristics provide fast, explainable, and often near-optimal solutions,
which are widely used in industrial optimization systems.

### Future Improvements
- Local search (swap-based improvement)
- Constraint relaxation
- Integration with exact solvers
