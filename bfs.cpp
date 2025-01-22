#include <bits/stdc++.h>
using namespace std;


void bfs(int startingNode, vector<int> adj[], int n) {
    vector<int> visited(n + 1, 0);
    queue<int> q;
    q.push(startingNode);
    visited[startingNode] = 1;

    cout << "BFS Traversal: ";
    while (!q.empty()) {
        int node = q.front();
        q.pop();
        cout << node << " ";

        for (auto &i : adj[node]) {
            if (!visited[i]) {
                q.push(i);
                visited[i] = 1;
            }
        }
    }
    cout << endl;
}

int main() {
    int n, m;
    cin >> n >> m;
    vector<int> adj[n + 1];

    
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    bfs(1, adj, n);

    return 0;
}
