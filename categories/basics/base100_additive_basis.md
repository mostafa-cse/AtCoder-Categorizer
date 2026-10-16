# Constructive Base-100 Representation for Additive Basis

**Domain**: `Basics`  
**Subtopic**: `Constructive Algorithms`  

This workbook contains curated, high-quality competitive programming problems teaching **Constructive Base-100 Representation for Additive Basis**.

---

## Curated Problems

### `[problem:AtCoder-abc251_d]` — At Most 3
- **Rating / Difficulty**: 1463
- **Contest**: `abc251`
- **Analysis**: [`analysis/AtCoder-abc251_d.md`](../../analysis/AtCoder-abc251_d.md)
- **Key Idea**: Decompose numbers in base 100. Any number <= 10^6 can be written as a + b * 100 + c * 10000 with 0 <= a, b, c <= 99.
- **Time Complexity**: `O(1)`
- **Space Complexity**: `O(1)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int w;
    if (!(cin >> w)) return 0;

    vector<int> ans;
    for (int i = 1; i <= 99; ++i) ans.push_back(i);
    for (int i = 1; i <= 99; ++i) ans.push_back(i * 100);
    for (int i = 1; i <= 99; ++i) ans.push_back(i * 10000);

    cout << ans.size() << "\n";
    for (size_t i = 0; i < ans.size(); ++i) {
        cout << ans[i] << (i + 1 == ans.size() ? "\n" : " ");
    }

    return 0;
}
```
