# Problem Analysis: AtCoder-arc005_4 — D - 連射王高橋君

**Problem ID**: `AtCoder-arc005_4`  
**Contest**: `arc005`  
**Rating / Difficulty**: 2487  
**URL**: https://atcoder.jp/contests/arc005/tasks/arc005_4  
**VJudge Tag**: `[problem:AtCoder-arc005_4]`  
**Category File**: [`../categories/dynamic_programming_dp/rensha_king_digit_dp_expression_reconstruction.md`](../categories/dynamic_programming_dp/rensha_king_digit_dp_expression_reconstruction.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Digit DP`  
- **Topic (Skill)**: `Digit DP`  

---

## 1. Problem Statement & Key Idea
Represent price as a sum of valid numbers using only allowed digits, '+' and '=', minimizing the total button presses.

## 2. Core Observation & Invariant
If price contains only allowed digits, the answer is directly the number of digits. Otherwise, we must write an expression $X_1 + \dots + X_K =$. The total keystrokes equals the sum of lengths of $X_i$ plus $K$ (for $K-1$ '+' signs and one '=' sign). We iterate over the number of summands $K \in [1, 9]$. Moving from least significant to most significant digits, we maintain the active count of non-zero summands and carry $c$. Transitioning each column uses subsets of allowed digits of size equal to the active count. Dynamic programming over $(carry, active)$ finds the minimal keystroke count and reconstructs the optimal summands.

## 3. Step-by-Step Algorithm
1. 1. If all digits of price are allowed, output price directly.
2. 2. Precompute all possible sums and digit tuples for multisets of size $k \in [0, 9]$ chosen from allowed digits.
3. 3. For each $K \in [1, 9]$, run Digit DP from least significant digit to higher digits: state $(carry, active)$ stores the minimum keystroke cost and backtrack pointers.
4. 4. Transition by choosing new active count $act' \le active$ and a digit multiset of size $act'$ whose sum $+ carry$ matches the target price digit modulo 10.
5. 5. Reconstruct the optimal expression $X_1 + \dots + X_K =$ from the best DP path across all $K$.

## 4. Complexity Analysis
- **Time Complexity**: `O(\text{len}(\text{price}) \cdot K^2 \cdot \binom{18}{9})`
- **Space Complexity**: `O(\text{len}(\text{price}) \cdot K^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>

using namespace std;

struct Combo {
    int sum_val;
    vector<int> digits;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string digits_str;
    long long price;
    if (!(cin >> digits_str >> price)) return 0;

    vector<int> digits;
    vector<bool> has_digit(10, false);
    for (char c : digits_str) {
        digits.push_back(c - '0');
        has_digit[c - '0'] = true;
    }

    string s_price = to_string(price);
    bool all_ok = true;
    for (char c : s_price) {
        if (!has_digit[c - '0']) {
            all_ok = false;
            break;
        }
    }
    if (all_ok) {
        cout << s_price << "\n";
        return 0;
    }

    vector<int> D;
    long long temp = price;
    while (temp > 0) {
        D.push_back(temp % 10);
        temp /= 10;
    }

    // Combos for each k in 0..9
    vector<vector<Combo>> comb_by_k(10);
    comb_by_k[0].push_back({0, {}});

    for (int k = 1; k <= 9; ++k) {
        map<int, vector<int>> best_c;
        auto gen = [&](auto& self, int depth, int start_idx, int cur_sum, vector<int>& cur_digits) -> void {
            if (depth == k) {
                if (best_c.find(cur_sum) == best_c.end()) {
                    best_c[cur_sum] = cur_digits;
                }
                return;
            }
            for (size_t i = start_idx; i < digits.size(); ++i) {
                cur_digits.push_back(digits[i]);
                self(self, depth + 1, i, cur_sum + digits[i], cur_digits);
                cur_digits.pop_back();
            }
        };
        vector<int> cur_digits;
        gen(gen, 0, 0, 0, cur_digits);
        for (auto& p : best_c) {
            comb_by_k[k].push_back({p.first, p.second});
        }
    }

    int best_cost = 1e9;
    vector<string> best_summands;

    for (int K = 1; K <= 9; ++K) {
        // dp: map (carry, active) -> (cost, prev_state, choice_digits)
        struct StateVal {
            int cost;
            pair<int, int> prev_st;
            vector<int> combo;
        };

        map<pair<int, int>, StateVal> dp;
        dp[{0, K}] = {K, {-1, -1}, {}};

        vector<map<pair<int, int>, StateVal>> history;
        int max_len = D.size() + 5;

        for (int idx = 0; idx < max_len; ++idx) {
            int t_digit = (idx < (int)D.size() ? D[idx] : 0);
            bool is_beyond = (idx >= (int)D.size());
            map<pair<int, int>, StateVal> new_dp;

            for (auto& entry : dp) {
                int c = entry.first.first;
                int active = entry.first.second;
                int cost = entry.second.cost;

                if (is_beyond && c == 0 && active == 0) continue;

                for (int new_act = 0; new_act <= active; ++new_act) {
                    for (auto& combo_info : comb_by_k[new_act]) {
                        int s_val = combo_info.sum_val;
                        int tot = s_val + c;
                        if (tot % 10 == t_digit) {
                            int c_next = tot / 10;
                            int next_cost = cost + new_act;
                            pair<int, int> next_key = {c_next, new_act};
                            if (new_dp.find(next_key) == new_dp.end() || next_cost < new_dp[next_key].cost) {
                                new_dp[next_key] = {next_cost, {c, active}, combo_info.digits};
                            }
                        }
                    }
                }
            }
            history.push_back(new_dp);
            dp = move(new_dp);

            if (dp.find({0, 0}) != dp.end() && idx >= (int)D.size() - 1) {
                int cost = dp[{0, 0}].cost;
                if (cost < best_cost) {
                    best_cost = cost;
                    pair<int, int> cur_state = {0, 0};
                    vector<vector<int>> col_digits;
                    for (int h_idx = idx; h_idx >= 0; --h_idx) {
                        auto& s_val = history[h_idx][cur_state];
                        col_digits.push_back(s_val.combo);
                        cur_state = s_val.prev_st;
                    }
                    reverse(col_digits.begin(), col_digits.end());

                    vector<string> summands(K, "");
                    for (auto& combo : col_digits) {
                        for (size_t i = 0; i < combo.size(); ++i) {
                            summands[i] += to_string(combo[i]);
                        }
                    }

                    vector<string> res_strings;
                    for (auto& s : summands) {
                        if (!s.empty()) {
                            reverse(s.begin(), s.end());
                            size_t p = s.find_first_not_of('0');
                            if (p == string::npos) s = "0";
                            else s = s.substr(p);
                            res_strings.push_back(s);
                        }
                    }
                    best_summands = res_strings;
                }
            }
        }
    }

    string ans = "";
    for (size_t i = 0; i < best_summands.size(); ++i) {
        ans += best_summands[i];
        if (i + 1 < best_summands.size()) ans += "+";
    }
    ans += "=";
    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
