# Mandatory Task Identification via Leftmost vs Rightmost Greedy Schedules

**Domain**: `Basics`  
**Subtopic**: `Greedy`  

This workbook contains curated, high-quality competitive programming problems teaching **Mandatory Task Identification via Leftmost vs Rightmost Greedy Schedules**.

---

## Curated Problems

### `[problem:AtCoder-abc161_e]` — Yutori
- **Rating / Difficulty**: 1760
- **Contest**: `abc161`
- **Analysis**: [`analysis/AtCoder-abc161_e.md`](../../analysis/AtCoder-abc161_e.md)
- **Key Idea**: Compute the greedy earliest schedule L[1..K] from left to right, and the greedy latest schedule R[1..K] from right to left. Day d is mandatory iff for some task index i, L[i] == R[i] == d.
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N + K)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k, c;
    if (!(cin >> n >> k >> c)) return 0;

    string s;
    cin >> s;

    vector<int> L(k + 1);
    int cur_day = 0;
    for (int i = 1; i <= k; ++i) {
        while (cur_day < n && s[cur_day] != 'o') cur_day++;
        L[i] = cur_day + 1;
        cur_day += c + 1;
    }

    vector<int> R(k + 1);
    cur_day = n - 1;
    for (int i = k; i >= 1; --i) {
        while (cur_day >= 0 && s[cur_day] != 'o') cur_day--;
        R[i] = cur_day + 1;
        cur_day -= (c + 1);
    }

    for (int i = 1; i <= k; ++i) {
        if (L[i] == R[i]) {
            cout << L[i] << "\n";
        }
    }

    return 0;
}
```
