# BFS and DFS Traversal Algorithms

## Overview

This repository contains implementations of two common graph traversal algorithms:
- **BFS (Breadth-First Search)**
- **DFS (Depth-First Search)**

These algorithms are used to explore the nodes and edges of a graph. They differ in the order in which they explore the graph:
- **BFS** explores nodes level by level, using a queue.
- **DFS** explores as deep as possible along a branch, using recursion or a stack.

---

## Files

- `bfs.cpp`: Implementation of the Breadth-First Search algorithm.
- `dfs.cpp`: Implementation of the Depth-First Search algorithm.

---

## BFS: Breadth-First Search

### How BFS Works
- BFS starts from a source node and explores all of its neighbors before moving on to the neighbors' neighbors.
- It uses a **queue** to keep track of the nodes that need to be explored.
- The traversal ensures that nodes are visited in the order of their proximity to the starting node.

### Input Format
- The input consists of two integers, `n` (the number of nodes) and `m` (the number of edges).
- The next `m` lines each contain two integers, `u` and `v`, representing an undirected edge between nodes `u` and `v`.

### Output Format
- The output is the BFS traversal of the graph starting from node `1`.

### Example

#### Input
```
9 8
1 2
1 6
2 3
2 4
4 5
5 8
6 7
6 9
7 8
```

#### Output
```
BFS Traversal: 1 2 6 3 4 7 9 5 8
```

---

## DFS: Depth-First Search

### How DFS Works
- DFS starts from a source node and explores as far as possible along a branch before backtracking.
- It uses **recursion** to explore each branch deeply before moving to the next.
- The traversal ensures that nodes are visited in the depth-first order, i.e., as far down one branch as possible before backtracking.

### Input Format
- The input consists of two integers, `n` (the number of nodes) and `m` (the number of edges).
- The next `m` lines each contain two integers, `u` and `v`, representing an undirected edge between nodes `u` and `v`.

### Output Format
- The output is the DFS traversal of the graph starting from node `1`.

### Example

#### Input
```
9 8
1 2
1 6
2 3
2 4
4 5
5 8
6 7
6 9
7 8
```

#### Output
```
DFS Traversal: 1 2 3 4 5 8 6 7 9
```

---

## How to Run

1. **Compile the Code:**
    You can compile the code using a C++ compiler like `g++`.

    For `bfs.cpp`:
    ```
    g++ bfs.cpp -o bfs
    ```

    For `dfs.cpp`:
    ```
    g++ dfs.cpp -o dfs
    ```

2. **Run the Executable:**
    After compilation, you can run the executable for both BFS and DFS.

    For BFS:
    ```
    ./bfs
    ```

    For DFS:
    ```
    ./dfs
    ```

3. **Input:**
    - Provide the input for the number of nodes and edges, followed by the edges themselves as shown in the example input.

4. **Output:**
    - The program will display the traversal order for BFS or DFS.

---

## Notes

- Both implementations assume the graph is **undirected**.
- These algorithms can be modified to handle directed graphs by adjusting the edge input or the adjacency list construction.