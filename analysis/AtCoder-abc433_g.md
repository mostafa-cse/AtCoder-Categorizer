# Problem Analysis: AtCoder-abc433_g — Substring Game

**Problem ID**: `AtCoder-abc433_g`  
**Contest**: `abc433`  
**Rating / Difficulty**: 2060  
**URL**: https://atcoder.jp/contests/abc433/tasks/abc433_g  
**VJudge Tag**: `[problem:AtCoder-abc433_g]`  
**Category File**: [`../categories/strings/suffix_automaton_game_evaluation.md`](../categories/strings/suffix_automaton_game_evaluation.md)  

- **Tag (Domain)**: `Strings`  
- **Subtopic**: `Suffix Automaton / Suffix Tree`  
- **Topic (Skill)**: `Suffix Automaton DAG Impartial Game Evaluation`  

---

## 1. Problem Statement & Key Idea
Starting with an empty string T, Alice and Bob take turns appending a character to T such that T remains a substring of S. The first player unable to make a move loses. Determine the winner under optimal play.

**Key Idea**: The set of all substrings of S forms a DAG under character append operations. Substrings belonging to the same state in the Suffix Automaton (SAM) share the exact same outgoing character transitions. Therefore, game states naturally project onto the O(|S|) states of the Suffix Automaton. A state is a winning state (N-state) if it has a transition to a losing state (P-state), and losing otherwise. We evaluate the DAG in topological order from sink states to the initial state (empty string).

## 2. Core Observation & Invariant
The impartial substring game state collapses onto the Suffix Automaton DAG, reducing an O(|S|^2) trie to an O(|S|) DAG.

## 3. Step-by-Step Algorithm
1. Construct the Suffix Automaton of S in O(|S| * Sigma) time.
2. Topologically sort the SAM states by length in descending order using counting sort.
3. Initialize win[u] = false for all states.
4. Process states in reverse topological order: for each state u, if any transition (u, c) leads to a state v with !win[v], set win[u] = true.
5. If win[0] is true, Alice wins; otherwise Bob wins.

## 4. Complexity Analysis
- **Time Complexity**: `O(|S| * Sigma)`
- **Space Complexity**: `O(|S| * Sigma)`

## 5. Core Algorithmic Skill & Learning Takeaway
Recognizing that substring game state transitions are equivalent to transitions on the Suffix Automaton DAG.

**Reusable Pattern**: Impartial games played by extending substrings of a fixed string are solved via Win/Loss DP on the Suffix Automaton.

## 6. Comparison with Alternative Approaches
Matches official editorial.

## 7. Verified Clean C++ Source Code
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
