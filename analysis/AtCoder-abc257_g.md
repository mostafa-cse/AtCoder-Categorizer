# Problem Analysis: AtCoder-abc257_g — Prefix Concatenation

**Problem ID**: `AtCoder-abc257_g`  
**Contest**: `abc257`  
**Rating / Difficulty**: 2075  
**URL**: https://atcoder.jp/contests/abc257/tasks/abc257_g  
**VJudge Tag**: `[problem:AtCoder-abc257_g]`  
**Category File**: [`../categories/strings/greedy_prefix_extension_kmp.md`](../categories/strings/greedy_prefix_extension_kmp.md)  

- **Tag (Domain)**: `Strings`  
- **Subtopic**: `String Matching`  
- **Topic (Skill)**: `Knuth Morris Pratt (KMP) and Prefix Automaton`  

---

## 1. Problem Statement & Key Idea
You are given two strings S and T. Find the minimum number of prefixes of S needed to concatenate together to form T. If impossible, output -1.

**Key Insight**: To minimize the number of prefixes used, we greedily take the longest possible prefix of S matching the remaining prefix of T at each step. By concatenating S + '#' + T and computing the KMP prefix function (pi array), pi[|S| + 1 + i] gives the length of the longest prefix of S that matches a suffix of T[1..i]. Then, starting from index |T|, we can greedily jump backward: if we are at position curr and the longest prefix of S ending at curr is L = pi[|S| + 1 + curr], we jump to curr - L. If L == 0, it is impossible to cover position curr, so output -1.

## 2. Core Observation & Invariant
The greedy strategy of extending each prefix as far right as possible is always optimal because prefix subsets are strictly nested.

## 3. Step-by-Step Algorithm
1. Construct combined string U = S + '#' + T.
2. Compute KMP pi array of U in O(|S| + |T|).
3. Set curr = |T| and steps = 0.
4. While curr > 0:
5.   Let L = pi[|S| + 1 + curr].
6.   If L <= 0, return -1.
7.   curr -= L, steps++.
8. Output steps.

## 4. Complexity Analysis
- **Time Complexity**: `O(|S| + |T|)`
- **Space Complexity**: `O(|S| + |T|)`

## 5. Core Skill & Reusable Pattern
- **Core Skill**: KMP prefix function on concatenated strings for longest prefix matching and greedy reverse jumping.
- **Reusable Pattern**: Finding longest prefix of S ending at each position of T using KMP on S + '#' + T in linear time.

## 6. Editorial Comparison & Alternative Approaches
Matches official editorial.

## 7. Verified C++17 Implementation
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
