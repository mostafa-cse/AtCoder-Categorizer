# 4-State Quaternary Choice Backtracking (4^N)

**Domain**: `Basics`  
**Subtopic**: `Backtracking`  

This workbook contains curated, high-quality competitive programming problems teaching **4-State Quaternary Choice Backtracking (4^N)**.

---

## Curated Problems

### [problem:AtCoder-abc119_c] — Synthetic Kadomatsu
- **Contest**: `abc119`
- **Rating / Difficulty**: 1346
- **Specific Skill**: 4-State Quaternary Choice Backtracking (4^N)
- **Individual Analysis**: [`../../analysis/AtCoder-abc119_c.md`](../../analysis/AtCoder-abc119_c.md)
- **Problem Statement Summary**: N bamboos of lengths l_1..l_N. You want to craft three bamboos of lengths A, B, C. Magic 1 (10 MP): combine two bamboos into one. Magic 2 (1 MP): lengthen or shorten by 1. Find the minimum MP needed (N <= 8).
- **Core Insight**: Because N <= 8, there are 4^N <= 4^8 = 65,536 possible assignments. For any assignment where at least one bamboo is assigned to A, B, and C: if k bamboos are assigned to A with total length L_A, combining them costs 10 * (k - 1) MP, and adjusting to length A costs |L_A - A| MP. We test all 4^N assignments.
- **Complexity**: Time: `O(4^N)` | Space: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

const int INF = 1e9;
int n, A, B, C;
vector<int> l;

int dfs(int idx, int sumA, int sumB, int sumC, int cntA, int cntB, int cntC) {
    if (idx == n) {
        if (cntA == 0 || cntB == 0 || cntC == 0) return INF;
        int mp = 10 * (cntA + cntB + cntC - 3);
        mp += abs(sumA - A) + abs(sumB - B) + abs(sumC - C);
        return mp;
    }

    int res = dfs(idx + 1, sumA, sumB, sumC, cntA, cntB, cntC);
    res = min(res, dfs(idx + 1, sumA + l[idx], sumB, sumC, cntA + 1, cntB, cntC));
    res = min(res, dfs(idx + 1, sumA, sumB + l[idx], sumC, cntA, cntB + 1, cntC));
    res = min(res, dfs(idx + 1, sumA, sumB, sumC + l[idx], cntA, cntB, cntC + 1));

    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n >> A >> B >> C)) return 0;

    l.resize(n);
    for (int i = 0; i < n; ++i) {
        cin >> l[i];
    }

    cout << dfs(0, 0, 0, 0, 0, 0, 0) << "\n";
    return 0;
}
```
