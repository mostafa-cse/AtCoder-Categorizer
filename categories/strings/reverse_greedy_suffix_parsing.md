# Reverse Greedy Suffix Parsing / Ambiguity Inversion

**Domain**: `Strings`  
**Subtopic**: `Greedy Parsing`  

This workbook contains curated, high-quality competitive programming problems teaching **Reverse Greedy Suffix Parsing / Ambiguity Inversion**.

---

## Curated Problems

### [problem:AtCoder-arc065_a] — Daydream
- **Contest**: `abc049`
- **Rating / Difficulty**: 930
- **Specific Skill**: Reverse Greedy Suffix Parsing / Ambiguity Inversion
- **Individual Analysis**: [`../../analysis/AtCoder-arc065_a.md`](../../analysis/AtCoder-arc065_a.md)
- **Problem Statement Summary**: Determine whether string S can be formed by concatenating copies of 'dream', 'dreamer', 'erase', and 'eraser'.
- **Core Insight**: Reversing S and the words ('maerd', 'remaerd', 'esare', 'resare'), or simply matching from the back: check if S ends with 'eraser' (6), 'erase' (5), 'dreamer' (7), or 'dream' (5). Suffixes never conflict when matched greedily.
- **Complexity**: Time: `O(|S|)` | Space: `O(|S|)`
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

    vector<string> words = {"dream", "dreamer", "erase", "eraser"};
    int pos = s.size();

    while (pos > 0) {
        bool matched = false;
        for (const string& w : words) {
            int len = w.size();
            if (pos >= len && s.substr(pos - len, len) == w) {
                pos -= len;
                matched = true;
                break;
            }
        }
        if (!matched) {
            cout << "NO\n";
            return 0;
        }
    }

    cout << "YES\n";
    return 0;
}
```
