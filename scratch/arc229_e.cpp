#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
#include <map>

using namespace std;

struct DSU {
    int n;
    vector<int> parent;
    DSU(int n) : n(n), parent(n + 1) {
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int i) {
        if (parent[i] == i)
            return i;
        return parent[i] = find(parent[i]);
    }
    void unite(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);
        if (root_i != root_j) {
            parent[root_i] = root_j;
        }
    }
};

void solve() {
    int n, m;
    if (!(cin >> n >> m)) return;

    struct Edge {
        int u, v, l;
    };
    vector<Edge> edges(m);
    for (int i = 0; i < m; ++i) {
        cin >> edges[i].u >> edges[i].v >> edges[i].l;
    }

    DSU dsu2(n), dsu3(n);
    for (const auto& e : edges) {
        if (e.l == 2) dsu2.unite(e.u, e.v);
        if (e.l == 3) dsu3.unite(e.u, e.v);
    }

    map<pair<int, int>, int> head;
    DSU dsu_all(n);

    for (int i = 1; i <= n; ++i) {
        pair<int, int> key = {dsu2.find(i), dsu3.find(i)};
        if (head.find(key) == head.end()) {
            head[key] = i;
        } else {
            dsu_all.unite(head[key], i);
        }
    }

    for (const auto& e : edges) {
        if (e.l == 1) {
            dsu_all.unite(e.u, e.v);
        }
    }

    int root1 = dsu_all.find(1);
    vector<int> ans;
    for (int i = 1; i <= n; ++i) {
        if (dsu_all.find(i) == root1) {
            ans.push_back(i);
        }
    }

    cout << ans.size() << "\n";
    for (size_t i = 0; i < ans.size(); ++i) {
        cout << ans[i] << (i + 1 == ans.size() ? "" : " ");
    }
    cout << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (cin >> t) {
        while (t--) {
            solve();
        }
    }
    return 0;
}
