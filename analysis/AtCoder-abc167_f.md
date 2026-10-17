# Problem Analysis: AtCoder-abc167_f — Bracket Sequencing

**Problem ID**: `AtCoder-abc167_f`  
**Contest**: `abc167`  
**Rating / Difficulty**: 1961  
**URL**: https://atcoder.jp/contests/abc167/tasks/abc167_f  
**VJudge Tag**: `[problem:AtCoder-abc167_f]`  
**Category File**: [`../categories/basics/bipartite_greedy_bracket_concatenation.md`](../categories/basics/bipartite_greedy_bracket_concatenation.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy / Invariants`  
- **Topic (Skill)**: `Bipartite Greedy Balance Sorting for Bracket Sequence Concatenation`  

---

## 1. Problem Statement & Key Idea
Given N bracket sequences S_1, ..., S_N. Determine whether they can be concatenated in some order to form a single valid bracket sequence.

Reduce each string by canceling matched pairs '()', leaving a string of form ')))((('. Each string is characterized by required prefix balance L_i and net change delta_i = R_i - L_i. Overall balance sum(delta_i) must equal 0. Partition into positive delta (delta >= 0) and negative delta (delta < 0). Positive delta strings are sorted by L_i ascending (process low requirements first). Negative delta strings are viewed in reverse and sorted by R_i descending. Then simulate prefix balance to ensure it never drops below 0.

## 2. Core Observation & Invariant
Reversing the process for net-negative brackets aligns the greedy priority with right-end requirements.

## 3. Step-by-Step Algorithm
1. For each string S_i, compute min_balance L_i and net delta_i.
2. Check if sum(delta_i) == 0; if not, return No.
3. Split into positive (delta >= 0) and negative (delta < 0).
4. Sort positive by L_i ascending.
5. Sort negative by R_i = L_i + delta_i descending.
6. Simulate running balance across concatenated positive then negative strings.
7. If running balance < 0 at any point, output No; else Yes.

## 4. Complexity Analysis
- **Time Complexity**: `O(sum |S_i| + N log N)`
- **Space Complexity**: `O(sum |S_i|)`

## 5. Complete C++ Solution
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

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Bipartite exchange sorting on prefix and suffix bracket balance profiles.
- **Reusable Pattern**: `Bracket Sequencing: delta >= 0 sorted by L asc; delta < 0 sorted by R desc.`
