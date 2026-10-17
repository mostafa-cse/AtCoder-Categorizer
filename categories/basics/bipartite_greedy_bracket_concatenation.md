# Bipartite Greedy Balance Sorting for Bracket Sequence Concatenation

**Domain**: `Basics`  
**Subtopic**: `Greedy / Invariants`  

This workbook contains curated, high-quality competitive programming problems teaching **Bipartite Greedy Balance Sorting for Bracket Sequence Concatenation**.

---

## Curated Problems

### `[problem:AtCoder-abc167_f]` — Bracket Sequencing
- **Rating / Difficulty**: 1961
- **Contest**: `abc167`
- **Analysis**: [`analysis/AtCoder-abc167_f.md`](../../analysis/AtCoder-abc167_f.md)
- **Key Idea**: Reduce each string by canceling matched pairs '()', leaving a string of form ')))((('. Each string is characterized by required prefix balance L_i and net change delta_i = R_i - L_i. Overall balance sum(delta_i) must equal 0. Partition into positive delta (delta >= 0) and negative delta (delta < 0). Positive delta strings are sorted by L_i ascending (process low requirements first). Negative delta strings are viewed in reverse and sorted by R_i descending. Then simulate prefix balance to ensure it never drops below 0.
- **Time Complexity**: `O(sum |S_i| + N log N)`
- **Space Complexity**: `O(sum |S_i|)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

struct BracketString {
    int req;   // min prefix balance required
    int delta; // net change
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<BracketString> pos, neg;
    long long total_delta = 0;

    for (int i = 0; i < n; ++i) {
        string s;
        cin >> s;

        int bal = 0;
        int min_bal = 0;
        for (char c : s) {
            if (c == '(') bal++;
            else bal--;
            min_bal = min(min_bal, bal);
        }

        int req = -min_bal;
        int delta = bal;
        total_delta += delta;

        if (delta >= 0) {
            pos.push_back({req, delta});
        } else {
            neg.push_back({req, delta});
        }
    }

    if (total_delta != 0) {
        cout << "No\n";
        return 0;
    }

    sort(pos.begin(), pos.end(), [](const BracketString& a, const BracketString& b) {
        return a.req < b.req;
    });

    sort(neg.begin(), neg.end(), [](const BracketString& a, const BracketString& b) {
        int ra = a.req + a.delta;
        int rb = b.req + b.delta;
        return ra > rb;
    });

    long long cur_bal = 0;
    for (const auto& bs : pos) {
        if (cur_bal < bs.req) {
            cout << "No\n";
            return 0;
        }
        cur_bal += bs.delta;
    }

    for (const auto& bs : neg) {
        if (cur_bal < bs.req) {
            cout << "No\n";
            return 0;
        }
        cur_bal += bs.delta;
    }

    cout << (cur_bal == 0 ? "Yes" : "No") << "\n";
    return 0;
}
```
