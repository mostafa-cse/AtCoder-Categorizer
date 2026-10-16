# Bounded-Length Substring Generation for Small K-th Ranking

**Domain**: `Strings`  
**Subtopic**: `Substring Ranking`  

This workbook contains curated, high-quality competitive programming problems teaching **Bounded-Length Substring Generation for Small K-th Ranking**.

---

## Curated Problems

### [problem:AtCoder-arc097_a] — K-th Substring
- **Contest**: `abc097`
- **Rating / Difficulty**: 1108
- **Specific Skill**: Bounded-Length Substring Generation for Small K-th Ranking
- **Individual Analysis**: [`../../analysis/AtCoder-arc097_a.md`](../../analysis/AtCoder-arc097_a.md)
- **Problem Statement Summary**: Given string S and integer K (K <= 5). Find the K-th lexicographically smallest distinct substring of S.
- **Core Insight**: Since K <= 5, we only need to extract all substrings of length 1, 2, ..., K. Insert them into a std::set<string> to automatically deduplicate and sort them in O(|S| * K^2), then retrieve the K-th element.
- **Complexity**: Time: `O(|S| * K^2)` | Space: `O(|S| * K)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <string>
#include <set>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    int k;
    if (!(cin >> s >> k)) return 0;

    set<string> subs;
    int n = s.size();

    for (int i = 0; i < n; ++i) {
        for (int len = 1; len <= k && i + len <= n; ++len) {
            subs.insert(s.substr(i, len));
        }
    }

    auto it = subs.begin();
    for (int i = 0; i < k - 1; ++i) {
        it++;
    }

    cout << *it << "\n";
    return 0;
}
```
