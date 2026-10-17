#include <iostream>
#include <vector>
#include <cmath>
#include <numeric>
#include <iomanip>

using namespace std;

struct DSU {
    vector<int> parent;
    DSU(int n) : parent(n) {
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    void unite(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);
        if (root_i != root_j) parent[root_i] = root_j;
    }
    bool same(int i, int j) {
        return find(i) == find(j);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<pair<double, double>> pts(n);
    for (int i = 0; i < n; ++i) {
        cin >> pts[i].first >> pts[i].second;
    }

    int top_node = n, bot_node = n + 1;

    auto check = [&](double r) {
        DSU dsu(n + 2);
        double d2 = 2.0 * r;

        for (int i = 0; i < n; ++i) {
            if (100.0 - pts[i].second < d2) {
                dsu.unite(i, top_node);
            }
            if (pts[i].second - (-100.0) < d2) {
                dsu.unite(i, bot_node);
            }
        }

        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                double dist = hypot(pts[i].first - pts[j].first, pts[i].second - pts[j].second);
                if (dist < d2) {
                    dsu.unite(i, j);
                }
            }
        }

        return !dsu.same(top_node, bot_node);
    };

    double low = 0.0, high = 100.0;
    for (int iter = 0; iter < 80; ++iter) {
        double mid = (low + high) / 2.0;
        if (check(mid)) {
            low = mid;
        } else {
            high = mid;
        }
    }

    cout << fixed << setprecision(10) << low << "\n";
    return 0;
}
