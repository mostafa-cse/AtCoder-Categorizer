# Problem Analysis: AtCoder-abc210_f — F - Coprime Solitaire

**Problem ID**: `AtCoder-abc210_f`  
**Contest**: `abc210`  
**Rating / Difficulty**: 2632  
**URL**: https://atcoder.jp/contests/abc210/tasks/abc210_f  
**VJudge Tag**: `[problem:AtCoder-abc210_f]`  
**Category File**: [`../categories/graph_theory/coprime_solitaire_2sat.md`](../categories/graph_theory/coprime_solitaire_2sat.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Satisfiability`  
- **Topic (Skill)**: `2 SAT`  

---

## 1. Problem Statement & Key Idea
Given N cards with numbers A_i and B_i, choose one side for each card such that all chosen numbers are pairwise coprime.

## 2. Core Observation & Invariant
Two numbers are coprime iff they share no prime factor. Each number <= 2 * 10^6 has at most 7 distinct prime factors. For each prime p, at most one card can select a side divisible by p. This "at most one" constraint across multiple choices is mapped to 2-SAT using prefix implication chains, keeping total 2-SAT vertices and edges O(N).

## 3. Step-by-Step Algorithm
1. Factorize each A_i and B_i into prime factors using linear sieve.
2. Assign boolean variable x_i for card i (True for A_i, False for B_i).
3. For each prime p, group all choices (i, side) that are multiples of p.
4. Construct prefix implication variables pref_k to enforce at most one choice.
5. Run Tarjan's SCC on the resulting 2-SAT graph.
6. If x_i and not x_i belong to the same SCC, output No, else Yes.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + \sum \omega(A_i) + \sum \omega(B_i))`
- **Space Complexity**: `O(N + \sum \omega(A_i) + \sum \omega(B_i))`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MAXV = 2000000;
int spf[MAXV + 1];

void sieve() {
    for (int i = 0; i <= MAXV; ++i) spf[i] = i;
    for (int i = 2; i * i <= MAXV; ++i) {
        if (spf[i] == i) {
            for (int j = i * i; j <= MAXV; j += i) {
                if (spf[j] == j) spf[j] = i;
            }
        }
    }
}

vector<int> get_primes(int val) {
    vector<int> ps;
    while (val > 1) {
        int p = spf[val];
        ps.push_back(p);
        while (val % p == 0) val /= p;
    }
    return ps;
}

struct TwoSAT {
    int n_vars;
    vector<vector<int>> adj;
    vector<int> dfn, low, scc;
    vector<bool> in_st;
    vector<int> st;
    int timer, scc_cnt;

    TwoSAT(int vars) : n_vars(vars), adj(2 * vars + 2), dfn(2 * vars + 2, 0),
                       low(2 * vars + 2, 0), scc(2 * vars + 2, 0), in_st(2 * vars + 2, false),
                       timer(0), scc_cnt(0) {}

    void add_clause(int lit1, int lit2) {
        adj[lit1 ^ 1].push_back(lit2);
        adj[lit2 ^ 1].push_back(lit1);
    }

    void dfs(int u) {
        dfn[u] = low[u] = ++timer;
        st.push_back(u);
        in_st[u] = true;
        for (int v : adj[u]) {
            if (!dfn[v]) {
                dfs(v);
                low[u] = min(low[u], low[v]);
            } else if (in_st[v]) {
                low[u] = min(low[u], dfn[v]);
            }
        }
        if (low[u] == dfn[u]) {
            scc_cnt++;
            while (true) {
                int v = st.back();
                st.pop_back();
                in_st[v] = false;
                scc[v] = scc_cnt;
                if (v == u) break;
            }
        }
    }

    bool solve(int n_orig) {
        for (int u = 2; u <= 2 * n_vars + 1; ++u) {
            if (!dfn[u]) dfs(u);
        }
        for (int i = 1; i <= n_orig; ++i) {
            if (scc[2 * i] == scc[2 * i + 1]) return false;
        }
        return true;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    sieve();

    int N;
    if (!(cin >> N)) return 0;

    vector<pair<int, int>> cards(N + 1);
    vector<vector<int>> prime_lits(MAXV + 1);

    for (int i = 1; i <= N; ++i) {
        cin >> cards[i].first >> cards[i].second;
        for (int p : get_primes(cards[i].first)) {
            prime_lits[p].push_back(2 * i);
        }
        for (int p : get_primes(cards[i].second)) {
            prime_lits[p].push_back(2 * i + 1);
        }
    }

    int extra_vars = 0;
    for (int p = 2; p <= MAXV; ++p) {
        int k = (int)prime_lits[p].size();
        if (k > 1) extra_vars += k;
    }

    TwoSAT sat(N + extra_vars);
    int cur_var = N;

    for (int p = 2; p <= MAXV; ++p) {
        int k = (int)prime_lits[p].size();
        if (k <= 1) continue;

        vector<int> prefix_vars(k);
        for (int j = 0; j < k; ++j) {
            prefix_vars[j] = ++cur_var;
        }

        for (int j = 0; j < k; ++j) {
            int l = prime_lits[p][j];
            int P = 2 * prefix_vars[j];
            sat.add_clause(l ^ 1, P);

            if (j > 0) {
                int P_prev = 2 * prefix_vars[j - 1];
                sat.add_clause(P_prev ^ 1, P);
                sat.add_clause(P_prev ^ 1, l ^ 1);
            }
        }
    }

    if (sat.solve(N)) {
        cout << "Yes\n";
    } else {
        cout << "No\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
