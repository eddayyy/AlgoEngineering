Here is the pseudocode for the algorithm:

Dijkstras Algorithm
    INPUT: graph G with vertices V and edges E, and source vertex s
    OUTPUT: minimum spanning tree of G
    
    1. Initialize set S to be empty, and array dist to store the shortest distances from source
     vertex s, with all values set to infinity except for s, which is 0.
    2. Repeat the following steps until all vertices have been processed and added to set S:
        a. Pick the unprocessed vertex v with the smallest value in dist, add it to S, and
        update the values in dist for all its connected vertices.
        b. For each vertex w connected to v and not in S, update the value in 
        dist[w] to be the minimum of the current value and the distance from the source vertex
        v to w through the edge (v, w).
    3. The final result of Prim's algorithm is the set S, which represents the minimum 
    spanning tree of the graph G.
END PROCEDURE