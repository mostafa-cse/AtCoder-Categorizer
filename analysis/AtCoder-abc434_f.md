# Problem Analysis: AtCoder-abc434_f — I. Concat (2nd)

**Problem ID**: `AtCoder-abc434_f`  
**Contest**: `abc434`  
**Rating / Difficulty**: 2600  
**URL**: https://atcoder.jp/contests/abc434/tasks/abc434_f  
**VJudge Tag**: `[problem:AtCoder-abc434_f]`  
**Category File**: [`../categories/strings/concat_2nd_z_algorithm.md`](../categories/strings/concat_2nd_z_algorithm.md)  

- **Tag (Domain)**: `Strings`  
- **Subtopic**: `String Matching`  
- **Topic (Skill)**: `Z Algorithm`  

---

## 1. Problem Statement & Key Idea
Given N strings S_i with total length sum(|S_i|) <= 10^6, consider all N! concatenations S_{P_1} S_{P_2} ... S_{P_N} sorted in lexicographical order. Output the second lexicographically smallest string A_2.

## 2. Core Observation & Invariant
The first lexicographical concatenation A_1 is obtained by sorting the strings according to the comparator X + Y < Y + X. Comparing X + Y and Y + X naively takes O(|X| + |Y|), which can TLE (O(N * |S_i|)). However, using the Z-algorithm array Z_X of each string X, we can compare X + Y and Y + X in O(min(|X|, |Y|)), allowing the full sort in O(sum(|S_i|) log N). Once sorted as S'_1, ..., S'_N: if any adjacent pair has S'_i + S'_{i+1} == S'_{i+1} + S'_i, swapping them yields the identical minimal string, so A_2 = A_1. Otherwise, no adjacent pairs are identical, so A_2 must be the smaller of swapping the last two strings (S'_N, S'_{N-1}) or swapping the last three (S'_{N-1}, S'_{N-2}, S'_N).

## 3. Step-by-Step Algorithm
1. For each string S_i, precompute its Z-array Z_{S_i} using standard linear-time Z-algorithm.
2. Sort strings using the O(min(|X|, |Y|)) Z-algorithm comparator: if |X| >= |Y|, compare X[0..|Y|-1] with Y; if equal, use Z_X[|Y|] to compare the middle segment in O(1); if equal, compare Y with the suffix of X.
3. If N == 2: output S'_2 + S'_1.
4. Check if any adjacent pair satisfies S'_i + S'_{i+1} == S'_{i+1} + S'_i. If so, output the primary concatenation concat(S').
5. Otherwise, compare the two candidates: candidate 1 = swap(S'_{N-1}, S'_N); candidate 2 = swap(S'_{N-2}, S'_{N-3}) on the prefix; output min(candidate 1, candidate 2).

## 4. Complexity Analysis
- **Time Complexity**: `O(sum(|S_i|) log N)`
- **Space Complexity**: `O(sum(|S_i|))`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

using psv = pair<string, vector<int>>;

vector<int> z_algorithm(const string& s) {
    int n = s.size();
    vector<int> z(n, 0);
    z[0] = 0;
    int l = 0, r = 0;
    for (int i = 1; i < n; i++) {
        if (i < r) z[i] = min(r - i, z[i - l]);
        while (i + z[i] < n && s[z[i]] == s[i + z[i]]) z[i]++;
        if (i + z[i] > r) {
            l = i;
            r = i + z[i];
        }
    }
    return z;
}

bool comp(const psv& x, const psv& y) {
    int xl = x.first.size(), yl = y.first.size();
    if (xl >= yl) {
        for (int i = 0; i < yl; i++) {
            if (x.first[i] != y.first[i]) {
                return (x.first[i] < y.first[i]);
            }
        }
        if (xl != yl && x.second[yl] < (xl - yl)) {
            return (x.first[yl + x.second[yl]] < x.first[x.second[yl]]);
        }
        for (int i = 0; i < yl; i++) {
            if (y.first[i] != x.first[i + (xl - yl)]) {
                return (y.first[i] < x.first[i + (xl - yl)]);
            }
        }
    } else {
        for (int i = 0; i < xl; i++) {
            if (x.first[i] != y.first[i]) {
                return (x.first[i] < y.first[i]);
            }
        }
        if (y.second[xl] < (yl - xl)) {
            return (y.first[y.second[xl]] < y.first[xl + y.second[xl]]);
        }
        for (int i = 0; i < xl; i++) {
            if (y.first[i + (yl - xl)] != x.first[i]) {
                return (y.first[i + (yl - xl)] < x.first[i]);
            }
        }
    }
    return false;
}

string concat(const vector<psv>& s) {
    string res = "";
    for (const auto& nx : s) {
        res += nx.first;
    }
    return res;
}

void solve() {
    int n;
    if (!(cin >> n)) return;
    vector<psv> s(n);
    for (auto& nx : s) {
        cin >> nx.first;
        nx.second = z_algorithm(nx.first);
    }
    sort(s.begin(), s.end(), comp);
    if (n == 2) {
        cout << s[1].first + s[0].first << "\n";
        return;
    }
    bool ok = false;
    for (int i = 1; i < n; i++) {
        if (s[i - 1].first + s[i].first == s[i].first + s[i - 1].first) {
            ok = true;
            break;
        }
    }
    if (ok) {
        cout << concat(s) << "\n";
        return;
    }
    swap(s[n - 1], s[n - 2]);
    string c1 = concat(s);
    swap(s[n - 1], s[n - 2]);
    swap(s[n - 2], s[n - 3]);
    cout << min(c1, concat(s)) << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (cin >> t) {
        while (t--) {
            solve();
        }
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
