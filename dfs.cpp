#include <bits/stdc++.h>
using namespace std;

// Result vector to store DFS traversal order
vector<int> res;

// Function for DFS traversal
void dfs(int node, vector<int>& visited, vector<int> adj[]) {
    visited[node] = 1;
    res.push_back(node);

    for (auto &i : adj[node]) {
        if (!visited[i]) {
            dfs(i, visited, adj);
        }
    }
}

int main() {
    int n, m;
    cin >> n >> m;
    vector<int> adj[n + 1];

    // Input for edges
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    // Vector to mark visited nodes
    vector<int> visited(n + 1, 0);

    // Perform DFS starting from node 1
    dfs(1, visited, adj);

    // Print DFS result
    cout << "DFS Traversal: ";
    for (auto &i : res) {
        cout << i << " ";
    }
    cout << endl;

    return 0;
}
