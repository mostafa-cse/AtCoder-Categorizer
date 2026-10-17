# Problem Analysis: AtCoder-jsc2021_e — Level K Palindrome

**Problem ID**: `AtCoder-jsc2021_e`  
**Contest**: `jsc2021`  
**Rating / Difficulty**: 2213  
**URL**: https://atcoder.jp/contests/jsc2021/tasks/jsc2021_e  
**VJudge Tag**: `[problem:AtCoder-jsc2021_e]`  
**Category File**: [`../categories/data_structures/level_k_palindrome_dsu_recursive_halving_parity_break.md`](../categories/data_structures/level_k_palindrome_dsu_recursive_halving_parity_break.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Disjoint Set Union (DSU)`  
- **Topic (Skill)**: `DSU / Union Find`  

---

## 1. Problem Statement & Key Idea
DSU equivalence class grouping across recursive palindrome halving with optimal majority character assignment and parity breaking.

## 2. Core Observation & Invariant
Being a level K palindrome forces mirror equalities across K recursive halving steps. If at any step length is 0, or final base string length L0 == 1, it is impossible (a length 1 string is always a palindrome, never level 0). If L0 >= 2, the base string t0 must NOT be a palindrome. If the greedy majority character assignment forms a palindrome, change one position to its second-best character at minimum penalty.

## 3. Step-by-Step Algorithm
1. 1. Recursively simulate the K halving steps, uniting mirrored indices in DSU.
2. 2. If any segment becomes empty or L0 == 1, output 'impossible'.
3. 3. For each DSU component, count character frequencies; greedy choice takes majority character.
4. 4. Check if the resulting base string t0 is a palindrome. If not, output sum of base changes.
5. 5. If t0 is a palindrome, find min penalty among all positions 0 <= p < L0/2 to change t0[p] or t0[L0 - 1 - p] to a different character.

## 4. Complexity Analysis
- **Time Complexity**: `O(N * alpha(N) + 26 * N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

struct DSU {
    vector<int> parent;
    DSU(int n) : parent(n) {
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    void unite(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);
        if (root_i != root_j) {
            parent[root_i] = root_j;
        }
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int K;
    string S;
    if (!(cin >> K >> S)) return 0;

    int N = S.size();

    // Check segment lengths at each of the K steps
    // At step 1, segments of length N.
    // At step k, length is len.
    vector<pair<int, int>> segs; // list of [l, r] segments
    segs.push_back({0, N - 1});

    DSU dsu(N);

    for (int step = 1; step <= K; ++step) {
        vector<pair<int, int>> next_segs;
        for (auto seg : segs) {
            int l = seg.first, r = seg.second;
            int len = r - l + 1;
            if (len == 0) {
                cout << "impossible\n";
                return 0;
            }
            int half = len / 2;
            for (int i = 0; i < half; ++i) {
                dsu.unite(l + i, r - i);
            }
            // left half
            next_segs.push_back({l, l + half - 1});
            // right half
            next_segs.push_back({r - half + 1, r});
        }
        segs = next_segs;
    }

    // Now segs contains 2^K segments, each of length L0
    int L0 = segs[0].second - segs[0].first + 1;
    if (L0 == 1) {
        cout << "impossible\n";
        return 0;
    }

    // Count frequencies for each DSU component
    vector<vector<int>> count(N, vector<int>(26, 0));
    vector<int> comp_size(N, 0);

    for (int i = 0; i < N; ++i) {
        int root = dsu.find(i);
        count[root][S[i] - 'a']++;
        comp_size[root]++;
    }

    int base_ans = 0;
    // For each unique component, add (comp_size - max_freq)
    for (int i = 0; i < N; ++i) {
        if (dsu.find(i) == i) {
            int max_f = 0;
            for (int c = 0; c < 26; ++c) {
                max_f = max(max_f, count[i][c]);
            }
            base_ans += comp_size[i] - max_f;
        }
    }

    if (L0 == 0) {
        cout << base_ans << "\n";
        return 0;
    }

    // Check if the chosen base string t0 is a palindrome
    // t0 has length L0. The p-th character of t0 is the majority char in comp of segs[0].first + p
    vector<int> t0(L0);
    vector<int> root_at(L0);
    for (int p = 0; p < L0; ++p) {
        int root = dsu.find(segs[0].first + p);
        root_at[p] = root;
        int best_c = 0;
        for (int c = 1; c < 26; ++c) {
            if (count[root][c] > count[root][best_c]) {
                best_c = c;
            }
        }
        t0[p] = best_c;
    }

    bool is_pal = true;
    for (int p = 0; p < L0 / 2; ++p) {
        if (t0[p] != t0[L0 - 1 - p]) {
            is_pal = false;
            break;
        }
    }

    if (!is_pal) {
        cout << base_ans << "\n";
        return 0;
    }

    // Must break palindrome by altering either p or L0 - 1 - p
    int min_penalty = 1e9;
    for (int p = 0; p < L0 / 2; ++p) {
        int r1 = root_at[p];
        int r2 = root_at[L0 - 1 - p];
        int c_match = t0[p]; // t0[p] == t0[L0 - 1 - p]

        // Penalty to pick c != c_match for r1:
        int best_other1 = -1;
        for (int c = 0; c < 26; ++c) {
            if (c == c_match) continue;
            if (best_other1 == -1 || count[r1][c] > count[r1][best_other1]) {
                best_other1 = c;
            }
        }
        int pen1 = count[r1][c_match] - count[r1][best_other1];

        // Penalty to pick c != c_match for r2:
        int best_other2 = -1;
        for (int c = 0; c < 26; ++c) {
            if (c == c_match) continue;
            if (best_other2 == -1 || count[r2][c] > count[r2][best_other2]) {
                best_other2 = c;
            }
        }
        int pen2 = count[r2][c_match] - count[r2][best_other2];

        min_penalty = min({min_penalty, pen1, pen2});
    }

    cout << base_ans + min_penalty << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
