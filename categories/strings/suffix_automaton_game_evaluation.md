# Suffix Automaton DAG Impartial Game Evaluation

**Domain**: `Strings`  
**Subtopic**: `Suffix Automaton / Suffix Tree`  

This workbook contains curated, high-quality competitive programming problems teaching **Suffix Automaton DAG Impartial Game Evaluation**.

---

## Curated Problems

### `[problem:AtCoder-abc433_g]` — Substring Game
- **Rating / Difficulty**: 2060
- **Contest**: `abc433`
- **Analysis**: [`analysis/AtCoder-abc433_g.md`](../../analysis/AtCoder-abc433_g.md)
- **Key Idea**: The set of all substrings of S forms a DAG under character append operations. Substrings belonging to the same state in the Suffix Automaton (SAM) share the exact same outgoing character transitions. Therefore, game states naturally project onto the O(|S|) states of the Suffix Automaton. A state is a winning state (N-state) if it has a transition to a losing state (P-state), and losing otherwise. We evaluate the DAG in topological order from sink states to the initial state (empty string).
- **Time Complexity**: `O(|S| * Sigma)`
- **Space Complexity**: `O(|S| * Sigma)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

struct State {
    int len, link;
    int next[26];
};

void solve() {
    string s;
    cin >> s;
    int n = s.size();

    vector<State> st(2 * n + 5);
    st[0].len = 0;
    st[0].link = -1;
    for (int c = 0; c < 26; ++c) st[0].next[c] = -1;
    int sz = 1, last = 0;

    auto extend = [&](char ch) {
        int c = ch - 'a';
        int cur = sz++;
        st[cur].len = st[last].len + 1;
        for (int i = 0; i < 26; ++i) st[cur].next[i] = -1;
        int p = last;
        while (p != -1 && st[p].next[c] == -1) {
            st[p].next[c] = cur;
            p = st[p].link;
        }
        if (p == -1) {
            st[cur].link = 0;
        } else {
            int q = st[p].next[c];
            if (st[p].len + 1 == st[q].len) {
                st[cur].link = q;
            } else {
                int clone = sz++;
                st[clone].len = st[p].len + 1;
                for (int i = 0; i < 26; ++i) st[clone].next[i] = st[q].next[i];
                st[clone].link = st[q].link;
                while (p != -1 && st[p].next[c] == q) {
                    st[p].next[c] = clone;
                    p = st[p].link;
                }
                st[q].link = clone;
                st[cur].link = clone;
            }
        }
        last = cur;
    };

    for (char ch : s) extend(ch);

    vector<int> cnt(n + 1, 0);
    for (int i = 0; i < sz; ++i) cnt[st[i].len]++;
    for (int i = 1; i <= n; ++i) cnt[i] += cnt[i - 1];
    vector<int> order(sz);
    for (int i = sz - 1; i >= 0; --i) {
        order[--cnt[st[i].len]] = i;
    }

    vector<bool> win(sz, false);
    for (int i = sz - 1; i >= 0; --i) {
        int u = order[i];
        for (int c = 0; c < 26; ++c) {
            int v = st[u].next[c];
            if (v != -1 && !win[v]) {
                win[u] = true;
                break;
            }
        }
    }

    if (win[0]) {
        cout << "Alice\n";
    } else {
        cout << "Bob\n";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (cin >> t) {
        while (t--) solve();
    }
    return 0;
}
```
