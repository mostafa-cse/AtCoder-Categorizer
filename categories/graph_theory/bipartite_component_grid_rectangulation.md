# Bipartite Component Product Transformation for 2D Grid Point Rectangulation

**Domain**: `Graph Theory`  
**Subtopic**: `Connected Components / Bipartite Graphs`  

This workbook contains curated, high-quality competitive programming problems teaching **Bipartite Component Product Transformation for 2D Grid Point Rectangulation**.

---

## Curated Problems

### `[problem:AtCoder-abc131_f]` — Must Be Rectangular!
- **Rating / Difficulty**: 1937
- **Contest**: `abc131`
- **Analysis**: [`analysis/AtCoder-abc131_f.md`](../../analysis/AtCoder-abc131_f.md)
- **Key Idea**: Model 2D points as edges in a bipartite graph between X coordinates and Y coordinates. The operation states: if edges (x_1, y_1), (x_1, y_2), (x_2, y_1) exist, add (x_2, y_2). This means any X and Y in the same connected component can eventually be connected! Each connected component becomes a complete bipartite graph K_{|X_c|, |Y_c|}. The maximum total points is sum_{c} (|X_c| * |Y_c|), and the number of added points is this sum minus N.
- **Time Complexity**: `O(N * alpha(MAX))`
- **Space Complexity**: `O(MAX)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MAX = 100001;

int parent_arr[2 * MAX];
long long size_x[2 * MAX];
long long size_y[2 * MAX];

int find_set(int v) {
    if (v == parent_arr[v]) return v;
    return parent_arr[v] = find_set(parent_arr[v]);
}

void union_sets(int a, int b) {
    a = find_set(a);
    b = find_set(b);
    if (a != b) {
        parent_arr[b] = a;
        size_x[a] += size_x[b];
        size_y[a] += size_y[b];
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    for (int i = 0; i < 2 * MAX; ++i) {
        parent_arr[i] = i;
        if (i < MAX) size_x[i] = 1;
        else size_y[i] = 1;
    }

    for (int i = 0; i < n; ++i) {
        int x, y;
        cin >> x >> y;
        union_sets(x, y + MAX);
    }

    long long max_points = 0;
    for (int i = 0; i < 2 * MAX; ++i) {
        if (parent_arr[i] == i) {
            max_points += size_x[i] * size_y[i];
        }
    }

    long long added = max_points - n;
    cout << added << "\n";
    return 0;
}
```
