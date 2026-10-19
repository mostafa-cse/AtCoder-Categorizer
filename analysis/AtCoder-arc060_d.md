# Problem Analysis: AtCoder-arc060_d — F - Best Representation

**Problem ID**: `AtCoder-arc060_d`  
**Contest**: `arc060`  
**Rating / Difficulty**: 2804  
**URL**: https://atcoder.jp/contests/arc060/tasks/arc060_d  
**VJudge Tag**: `[problem:AtCoder-arc060_d]`  
**Category File**: [`../categories/strings/non_periodic_partition_kmp_border_array.md`](../categories/strings/non_periodic_partition_kmp_border_array.md)  

- **Tag (Domain)**: `Strings`  
- **Subtopic**: `String Matching`  
- **Topic (Skill)**: `Knuth Morris Pratt (KMP) and Prefix Automaton`  

---

## 1. Problem Statement & Key Idea
Given a string w, find the minimum integer k such that w can be partitioned into k non-periodic strings, and count the number of such partitions of minimum size.

## 2. Core Observation & Invariant
If all characters are identical, k = |w| and the answer is 1. If w itself is non-periodic, k = 1 and the answer is 1. Otherwise, k = 2 is always achievable! A partition into 2 non-periodic strings exists at cut i iff both prefix w[1..i] and suffix w[i+1..|w|] are non-periodic. By the KMP border array, string s of length L is periodic iff L % (L - pi[L]) == 0 and pi[L] > 0. We compute pi on w and on reversed w^R to classify all prefixes and suffixes in O(N) time.

## 3. Step-by-Step Algorithm
1. 1. If all characters of w are identical, output |w| and 1.
2. 2. Compute KMP prefix function pi on w. Check if w is non-periodic; if so, output 1 and 1.
3. 3. Compute KMP prefix function pi_rev on reversed string w^R.
4. 4. Prefix of length i is non-periodic iff not (i % (i - pi[i]) == 0 and pi[i] > 0).
5. 5. Suffix of length N - i is non-periodic iff not ((N - i) % ((N - i) - pi_rev[N - i]) == 0 and pi_rev[N - i] > 0).
6. 6. Count cuts i in 1..N-1 where both prefix and suffix are non-periodic.
7. 7. Output 2 and the count.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

vector<int> compute_kmp(const string& s) {
    int n = s.size();
    vector<int> pi(n + 1, 0);
    int j = 0;
    for (int i = 1; i < n; ++i) {
        while (j > 0 && s[i] != s[j]) {
            j = pi[j];
        }
        if (s[i] == s[j]) {
            j++;
        }
        pi[i + 1] = j;
    }
    return pi;
}

inline bool is_primitive(int len, int border) {
    if (border == 0) return true;
    int per = len - border;
    return (len % per != 0);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string w;
    if (!(cin >> w)) return 0;

    int L = w.size();

    // Check if monochromatic
    bool mono = true;
    for (int i = 1; i < L; ++i) {
        if (w[i] != w[0]) {
            mono = false;
            break;
        }
    }

    if (mono) {
        cout << L << "\n" << 1 << "\n";
        return 0;
    }

    auto pi = compute_kmp(w);

    if (is_primitive(L, pi[L])) {
        cout << 1 << "\n" << 1 << "\n";
        return 0;
    }

    string rev_w = w;
    reverse(rev_w.begin(), rev_w.end());
    auto rev_pi = compute_kmp(rev_w);

    long long ways = 0;
    for (int i = 1; i < L; ++i) {
        if (is_primitive(i, pi[i]) && is_primitive(L - i, rev_pi[L - i])) {
            ways++;
        }
    }

    cout << 2 << "\n" << ways << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
