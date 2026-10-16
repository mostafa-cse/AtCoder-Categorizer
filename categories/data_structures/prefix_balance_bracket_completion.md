# Prefix Balance Minimization for Valid Bracket Completion

**Domain**: `Data Structures`  
**Subtopic**: `Stacks & Parentheses`  

This workbook contains curated, high-quality competitive programming problems teaching **Prefix Balance Minimization for Valid Bracket Completion**.

---

## Curated Problems

### [problem:AtCoder-abc064_d] — Insertion
- **Contest**: `abc064`
- **Rating / Difficulty**: 969
- **Specific Skill**: Prefix Balance Minimization for Valid Bracket Completion
- **Individual Analysis**: [`../../analysis/AtCoder-abc064_d.md`](../../analysis/AtCoder-abc064_d.md)
- **Problem Statement Summary**: Given a bracket string S of length N containing '(' and ')'. Find the shortest valid bracket sequence that contains S as a contiguous substring and is lexicographically smallest.
- **Core Insight**: Track running balance: +1 for '(', -1 for ')'. Let min_bal be the minimum balance reached across all prefixes. If min_bal < 0, we must prepend -min_bal '(' characters at the beginning. After prepending, if the final balance is rem > 0, we must append rem ')' characters at the end. Since '(' < ')', prepending '(' and appending ')' also guarantees lexicographical minimality.
- **Complexity**: Time: `O(N)` | Space: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    string s;
    if (!(cin >> n >> s)) return 0;

    int bal = 0;
    int min_bal = 0;

    for (char c : s) {
        if (c == '(') bal++;
        else bal--;
        min_bal = min(min_bal, bal);
    }

    int need_open = (min_bal < 0 ? -min_bal : 0);
    int final_bal = bal + need_open;
    int need_close = final_bal;

    string res = string(need_open, '(') + s + string(need_close, ')');
    cout << res << "\n";
    return 0;
}
```
