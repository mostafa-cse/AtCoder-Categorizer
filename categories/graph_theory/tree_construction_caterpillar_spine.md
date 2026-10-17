# Tree Construction by Component Size Complementarity (Caterpillar Spine)

**Domain**: `Graph Theory`  
**Subtopic**: `Tree Construction`  

This workbook contains curated, high-quality competitive programming problems teaching **Tree Construction by Component Size Complementarity (Caterpillar Spine)**.

---

## Curated Problems

### `[problem:AtCoder-arc103_c]` — Tr/ee
- **Rating / Difficulty**: 1722
- **Contest**: `arc103`
- **Analysis**: [`analysis/AtCoder-arc103_c.md`](../../analysis/AtCoder-arc103_c.md)
- **Key Idea**: Removing any edge from an n-vertex tree splits it into components of sizes i and n - i. Therefore, s_i MUST equal s_{n - i}. Also, s_1 must be '1' (leaf removal) and s_n must be '0'. If these hold, construct a caterpillar tree whose spine vertices correspond to prefix sizes.
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    int n = s.size();
    if (s[0] != '1' || s[n - 1] != '0') {
        cout << -1 << "\n";
        return 0;
    }

    for (int i = 0; i < n - 1; ++i) {
        if (s[i] != s[n - 2 - i]) {
            cout << -1 << "\n";
            return 0;
        }
    }

    vector<int> spine;
    for (int i = 0; i < n - 1; ++i) {
        if (s[i] == '1') {
            spine.push_back(i + 1);
        }
    }

    vector<pair<int, int>> edges;
    int current_vertex = 1;
    for (int sz : spine) {
        int next_vertex = sz + 1;
        edges.push_back({current_vertex, next_vertex});
        for (int v = current_vertex + 1; v <= sz; ++v) {
            edges.push_back({current_vertex, v});
        }
        current_vertex = next_vertex;
    }

    for (auto& e : edges) {
        cout << e.first << " " << e.second << "\n";
    }

    return 0;
}
```
