# Knuth Morris Pratt (KMP) and Prefix Automaton

**Domain**: `Strings`  
**Subtopic**: `String Matching`  

This workbook contains curated, high-quality competitive programming problems teaching **Knuth Morris Pratt (KMP) and Prefix Automaton**.

---

## Curated Problems

### `[problem:AtCoder-abc257_g]` — Prefix Concatenation
- **Rating / Difficulty**: 2075
- **Contest**: `abc257`
- **Analysis**: [`analysis/AtCoder-abc257_g.md`](../../analysis/AtCoder-abc257_g.md)
- **Key Idea**: To minimize the number of prefixes used, we greedily take the longest possible prefix of S matching the remaining prefix of T at each step. By concatenating S + '#' + T and computing the KMP prefix function (pi array), pi[|S| + 1 + i] gives the length of the longest prefix of S that matches a suffix of T[1..i]. Then, starting from index |T|, we can greedily jump backward: if we are at position curr and the longest prefix of S ending at curr is L = pi[|S| + 1 + curr], we jump to curr - L. If L == 0, it is impossible to cover position curr, so output -1.
- **Time Complexity**: `O(|S| + |T|)`
- **Space Complexity**: `O(|S| + |T|)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<int> prefix_function(const string& s) {
    int n = s.size();
    vector<int> pi(n, 0);
    for (int i = 1; i < n; ++i) {
        int j = pi[i - 1];
        while (j > 0 && s[i] != s[j])
            j = pi[j - 1];
        if (s[i] == s[j])
            j++;
        pi[i] = j;
    }
    return pi;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s, t;
    if (!(cin >> s >> t)) return 0;

    string combined = s + '#' + t;
    vector<int> pi = prefix_function(combined);

    int cur = t.size();
    int s_len = s.size();
    int ans = 0;

    while (cur > 0) {
        int match_len = pi[s_len + 1 + cur - 1];
        if (match_len == 0) {
            cout << -1 << "\n";
            return 0;
        }
        ans++;
        cur -= match_len;
    }

    cout << ans << "\n";
    return 0;
}
```
