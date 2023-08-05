cspy
====

A collection of algorithms for the (resource) Constrained Shortest Path problem.

The algorithms implemented include:

 - [X] Monodirectional forward labeling algorithm;
 - [X] Monodirectional backward labeling algorithm;
 - [X] Bidirectional labeling algorithm with static halfway point;
 - [X] Bidirectional labeling algorithm with dynamic halfway point [1];
 - [X] Heuristic Tabu search [2].

Features implemented include: generic resource extension functions (not restricted to additive resources), generic resource consumptions (not restricted to non-negative values), and, increased efficiency (when compared to other implementations of monodirectional algorithms) [3].


TODO
----

 - [ ] Implement generic resource extension functions for bidirectional algorithm
 - [ ] Tabu clean up

Changelog
---------

pre-release v0.0.1: 20/06/2019


- Implemented Heuristic Tabu Search.
- Documentation updates (docstring modifications to include maths)


References
----------


[1] https://www.sciencedirect.com/science/article/pii/S0377221717302035

[2] To appear.

[3] https://www.researchgate.net/publication/227142556_Shortest_Path_Problems_with_Resource_Constraints


