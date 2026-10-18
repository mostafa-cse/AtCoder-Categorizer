# Problem Analysis: AtCoder-agc077_a — A - Reverse A…B

**Problem ID**: `AtCoder-agc077_a`  
**Contest**: `agc077`  
**Rating / Difficulty**: 2512  
**URL**: https://atcoder.jp/contests/agc077/tasks/agc077_a  
**VJudge Tag**: `[problem:AtCoder-agc077_a]`  
**Category File**: [`../categories/basics/reverse_a_b_constructive_three_phase_inversion.md`](../categories/basics/reverse_a_b_constructive_three_phase_inversion.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy and Constructive`  
- **Topic (Skill)**: `Basic Constructive Algorithms`  

---

## 1. Problem Statement & Key Idea
Determine if binary string $X$ can be transformed into $Y$ using at most $\lfloor N/2 \rfloor$ reversals of substrings starting with 'A' and ending with 'B', and construct the operations.

## 2. Core Observation & Invariant
Substrings reversed must start with 'A' and end with 'B'. Reversing such a substring changes its first character to 'B' and its last character to 'A', strictly increasing the string lexicographically while preserving 'A' counts and decreasing the reversed string. Thus, necessary and sufficient conditions are: equal 'A' counts, $X \le Y$, and $\text{rev}(X) \ge \text{rev}(Y)$. Stripping matching prefixes and suffixes leaves $X[l]='A', X[r]='B', Y[l]='B', Y[r]='A'$. By matching minority characters between inner substrings, at most $\lfloor N/2 \rfloor$ operations suffice.

## 3. Step-by-Step Algorithm
1. 1. Check feasibility: count of 'A' matches, $X \le Y$, and $\text{rev}(X) \ge \text{rev}(Y)$. If any fails, output `No`.
2. 2. If $X = Y$, output `Yes\n0`.
3. 3. Find the first mismatch $l$ and last mismatch $r$.
4. 4. Identify positions of the minority character in the inner substring and match them greedily from right to left using front and back operations.
5. 5. Combine front operations, central reversal $[l+1, r+1]$, and reversed back operations.
6. 6. Output `Yes`, count of operations, and each operation's 1-based bounds.

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

void solve() {
    int N;
    if (!(cin >> N)) return;
    string X, Y;
    cin >> X >> Y;

    int cntAX = 0, cntAY = 0;
    for (char c : X) if (c == 'A') cntAX++;
    for (char c : Y) if (c == 'A') cntAY++;

    if (cntAX != cntAY) {
        cout << "No\n";
        return;
    }

    if (X > Y) {
        cout << "No\n";
        return;
    }

    string revX = X, revY = Y;
    reverse(revX.begin(), revX.end());
    reverse(revY.begin(), revY.end());
    if (revX < revY) {
        cout << "No\n";
        return;
    }

    if (X == Y) {
        cout << "Yes\n0\n";
        return;
    }

    int l = 0;
    while (l < N && X[l] == Y[l]) l++;
    int r = N - 1;
    while (r >= 0 && X[r] == Y[r]) r--;

    if (l + 1 > r - 1) {
        cout << "Yes\n1\n" << (l + 1) << " " << (r + 1) << "\n";
        return;
    }

    string S = X.substr(l + 1, r - 1 - (l + 1) + 1);
    string subY = Y.substr(l + 1, r - 1 - (l + 1) + 1);
    string T = subY;
    reverse(T.begin(), T.end());

    vector<pair<int, int>> op_front;
    vector<pair<int, int>> op_back;

    int count_A = 0;
    for (char c : S) if (c == 'A') count_A++;
    int count_B = S.length() - count_A;

    char target_char = (count_A <= count_B ? 'A' : 'B');

    vector<int> p, q;
    for (int i = 0; i < (int)S.length(); ++i) {
        if (S[i] == target_char) p.push_back(i);
    }
    for (int i = 0; i < (int)T.length(); ++i) {
        if (T[i] == target_char) q.push_back(i);
    }

    for (int i = (int)p.size() - 1; i >= 0; --i) {
        if (p[i] < q[i]) {
            op_front.push_back({(l + 1) + p[i] + 1, (l + 1) + q[i] + 1});
        } else if (p[i] > q[i]) {
            op_back.push_back({(r - 1 - p[i]) + 1, (r - 1 - q[i]) + 1});
        }
    }

    vector<pair<int, int>> ops = op_front;
    ops.push_back({l + 1, r + 1});
    reverse(op_back.begin(), op_back.end());
    ops.insert(ops.end(), op_back.begin(), op_back.end());

    cout << "Yes\n" << ops.size() << "\n";
    for (auto& op : ops) {
        cout << op.first << " " << op.second << "\n";
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    if (cin >> T) {
        while (T--) solve();
    }
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
