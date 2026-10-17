# Prefix Sum

**Taxonomy Path**: `Basics` > `Range Queries Without Updates` > `Prefix Sum`

## Description
This topic focuses on prefix sum techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Instead of updating timelines naively on every tweet, store a snapshot of (T_u, T_v) whenever u and v follow each other. When they unfollow (or at the end of the simulation), add T_v - snap_v to u and T_u - snap_u to v. Since there are at most M follow events, an adjacency map tracks all active friendships in O(M log M) time.
- Common Reductions: Track an SNS timeline network with N users, M events (tweet, mutual follow, mutual unfollow). Determine the K-th largest timeline tweet count. Tweets of user v during an active mutual follow period [start, end] contribute T_v(end) - T_v(start) to user u timeline.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-digitalarts_3`](../../analysis/AtCoder-digitalarts_3.md) | C. Chokutter | 2179 | Track an SNS timeline network with N users, M events (tweet, mutual follow, mutual unfollow). Determine the K-th largest... |
