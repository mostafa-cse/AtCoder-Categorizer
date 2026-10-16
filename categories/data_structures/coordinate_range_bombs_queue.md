# Coordinate Range Bombs with Queue / Difference Array Greedy

**Domain**: `Data Structures`  
**Subtopic**: `Greedy & Queue`  

This workbook contains curated, high-quality competitive programming problems teaching **Coordinate Range Bombs with Queue / Difference Array Greedy**.

---

## Curated Problems

### [problem:AtCoder-abc153_f] — Silver Fox vs Monster
- **Contest**: `abc153`
- **Rating / Difficulty**: 1393
- **Specific Skill**: Coordinate Range Bombs with Queue / Difference Array Greedy
- **Individual Analysis**: [`../../analysis/AtCoder-abc153_f.md`](../../analysis/AtCoder-abc153_f.md)
- **Problem Statement Summary**: N monsters at coordinates X_i with health H_i. A bomb dropped at x damages all monsters in [x, x + 2D] by A. Find the minimum bombs to kill all monsters.
- **Core Insight**: Maintain active bomb damage using a queue of expiry events: queue stores (expiry_coord, total_damage). Before processing monster i at X_i, pop all expired bombs with expiry_coord < X_i. Subtract current active damage from H_i; if health remains, drop ceil(rem_H / A) bombs covering up to X_i + 2D, and push into queue.
- **Complexity**: Time: `O(N log N)` | Space: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

struct Monster {
    long long x, h;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long d, a;
    if (!(cin >> n >> d >> a)) return 0;

    vector<Monster> m(n);
    for (int i = 0; i < n; ++i) {
        cin >> m[i].x >> m[i].h;
    }

    sort(m.begin(), m.end(), [](const Monster& m1, const Monster& m2) {
        return m1.x < m2.x;
    });

    long long total_bombs = 0;
    long long current_damage = 0;
    queue<pair<long long, long long>> q; // {max_reach_x, damage}

    for (int i = 0; i < n; ++i) {
        while (!q.empty() && q.front().first < m[i].x) {
            current_damage -= q.front().second;
            q.pop();
        }

        m[i].h -= current_damage;
        if (m[i].h > 0) {
            long long needed = (m[i].h + a - 1) / a;
            long long dmg = needed * a;
            total_bombs += needed;
            current_damage += dmg;
            q.push({m[i].x + 2 * d, dmg});
        }
    }

    cout << total_bombs << "\n";
    return 0;
}
```
