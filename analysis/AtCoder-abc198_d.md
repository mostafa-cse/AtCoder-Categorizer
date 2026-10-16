# Problem Analysis: AtCoder-abc198_d — Send More Money

**Problem ID**: `AtCoder-abc198_d`  
**Contest**: `abc198`  
**Rating / Difficulty**: 1224  
**URL**: https://atcoder.jp/contests/abc198/tasks/abc198_d  
**VJudge Tag**: `[problem:AtCoder-abc198_d]`  
**Category File**: [`../categories/basics/cryptarithmetic_permutation_search.md`](../categories/basics/cryptarithmetic_permutation_search.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Permutations`  
- **Topic (Skill)**: `Cryptarithmetic Permutation Search via std::next_permutation`  

---

## 1. Problem Statement & Key Idea
Given three strings S_1, S_2, S_3 representing words. Assign distinct digits 0..9 to each distinct letter such that S_1 + S_2 = S_3, with no leading zeros. If possible, output the numbers, else UNRESOLVABLE.

**Key Idea**: There are at most 10 distinct letters. If there are > 10 distinct letters, no injection into digits 0..9 exists (UNRESOLVABLE).

## 2. Core Observation & Invariant
With <= 10 letters, we can test all permutations of 10 digits assigned to the letters using std::next_permutation: P(10, k) <= 10! = 3,628,800. For each assignment, check if leading letters are non-zero and N_1 + N_2 == N_3.

## 3. Step-by-Step Algorithm
1. Collect unique letters in S1, S2, S3. If count > 10, print UNRESOLVABLE.
2. Initialize permutation array digits = {0, 1, 2, ..., 9}.
3. Iterate permutations: assign digits to the unique letters.
4. Check leading digit != 0 for all three words.
5. Evaluate numerical values N1, N2, N3; if N1 + N2 == N3, print and terminate.
6. If all permutations exhausted, print UNRESOLVABLE.

## 4. Complexity Analysis
- **Time Complexity**: `O(10! / (10 - K)!)`
- **Space Complexity**: `O(1)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>
#include <numeric>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s1, s2, s3;
    if (!(cin >> s1 >> s2 >> s3)) return 0;

    set<char> letters_set;
    for (char c : s1) letters_set.insert(c);
    for (char c : s2) letters_set.insert(c);
    for (char c : s3) letters_set.insert(c);

    if (letters_set.size() > 10) {
        cout << "UNRESOLVABLE\n";
        return 0;
    }

    vector<char> letters(letters_set.begin(), letters_set.end());
    int k = letters.size();

    vector<int> p(10);
    iota(p.begin(), p.end(), 0);

    do {
        vector<int> char_to_digit(256, -1);
        for (int i = 0; i < k; ++i) {
            char_to_digit[(unsigned char)letters[i]] = p[i];
        }

        if (char_to_digit[(unsigned char)s1[0]] == 0 ||
            char_to_digit[(unsigned char)s2[0]] == 0 ||
            char_to_digit[(unsigned char)s3[0]] == 0) {
            continue;
        }

        long long n1 = 0, n2 = 0, n3 = 0;
        for (char c : s1) n1 = n1 * 10 + char_to_digit[(unsigned char)c];
        for (char c : s2) n2 = n2 * 10 + char_to_digit[(unsigned char)c];
        for (char c : s3) n3 = n3 * 10 + char_to_digit[(unsigned char)c];

        if (n1 + n2 == n3) {
            cout << n1 << "\n" << n2 << "\n" << n3 << "\n";
            return 0;
        }
    } while (next_permutation(p.begin(), p.end()));

    cout << "UNRESOLVABLE\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Full permutation search over cryptarithmetic letter-to-digit bindings.
- **Reusable Pattern**: `Verbal arithmetic solver: next_permutation over digits {0..9}.`
