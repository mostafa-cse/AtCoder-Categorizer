# Circular Truth-Telling Consistency 4-Case Brute Force

**Domain**: `Basics`  
**Subtopic**: `Circular Invariants`  

This workbook contains curated, high-quality competitive programming problems teaching **Circular Truth-Telling Consistency 4-Case Brute Force**.

---

## Curated Problems

### [problem:AtCoder-arc069_b] — Menagerie
- **Contest**: `abc055`
- **Rating / Difficulty**: 1344
- **Specific Skill**: Circular Truth-Telling Consistency 4-Case Brute Force
- **Individual Analysis**: [`../../analysis/AtCoder-arc069_b.md`](../../analysis/AtCoder-arc069_b.md)
- **Problem Statement Summary**: N animals in a circle: Sheep 'S' (always tell truth), Wolves 'W' (always lie). Animal i says animal i-1 and i+1 are of the same type ('o') or different ('x'). Find a valid assignment or output -1.
- **Core Insight**: There are only 2 x 2 = 4 choices for (animal 0, animal 1): (S, S), (S, W), (W, S), (W, W). For each choice, deduce animal 2, 3, ..., N-1 sequentially. Finally, verify that animal N-1 and animal 0's statements are consistent with the circular wrap-around to animal 0 and animal 1.
- **Complexity**: Time: `O(N)` | Space: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    string s;
    if (!(cin >> n >> s)) return 0;

    char roles[2] = {'S', 'W'};

    for (char c0 : roles) {
        for (char c1 : roles) {
            string ans(n, ' ');
            ans[0] = c0;
            ans[1] = c1;

            for (int i = 1; i < n - 1; ++i) {
                bool is_same = (s[i] == 'o');
                if (ans[i] == 'W') is_same = !is_same;

                if (is_same) {
                    ans[i + 1] = ans[i - 1];
                } else {
                    ans[i + 1] = (ans[i - 1] == 'S' ? 'W' : 'S');
                }
            }

            // Check wrap-around consistency for n - 1
            bool same_last = (s[n - 1] == 'o');
            if (ans[n - 1] == 'W') same_last = !same_last;
            bool check_last = (same_last ? (ans[n - 2] == ans[0]) : (ans[n - 2] != ans[0]));

            // Check wrap-around consistency for 0
            bool same_zero = (s[0] == 'o');
            if (ans[0] == 'W') same_zero = !same_zero;
            bool check_zero = (same_zero ? (ans[n - 1] == ans[1]) : (ans[n - 1] != ans[1]));

            if (check_last && check_zero) {
                cout << ans << "\n";
                return 0;
            }
        }
    }

    cout << -1 << "\n";
    return 0;
}
```
