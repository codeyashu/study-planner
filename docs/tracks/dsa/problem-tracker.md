---
title: NeetCode 250 problem tracker
track: dsa
slug: problem-tracker
priority: P0
complexity: 1
est_hours: 0
phase: 1
tags: [dsa, P0]
last_reviewed: 2026-09-25
---

# NeetCode 250 problem tracker

!!! abstract "At a glance"
    **Priority:** P0 · **Complexity:** 1/5 · **Est. time:** ongoing (about 7-12 problems per week) · **Phase:** 1-6 · **Prereqs:** [Approach & complexity](approach-complexity.md), [Python idioms](python-idioms.md)
    **You're done when:** all 150 NeetCode 150 core problems are ticked and solved within the time-box, every failed problem has been re-solved on days 1, 3, 7 and 21, and you can solve a random unseen Medium in 25 minutes and a Hard in 40.

## Why it matters

Volume with reflection builds pattern recognition, and a tracker keeps you honest. This master list has **265 problems** grouped by pattern: the **150** NeetCode 150 core set (`NC150`) plus **115** extra problems (`NC250+`) chosen for Staff-level FAANG coverage (harder variants, classic follow-ups, and the concurrency/LLD set). Ordering inside each pattern is Easy, then Medium, then Hard. The "Week" column follows the roadmap phases in `topics.yml`.

## How to use this page

### Time-boxing (the 25-35 minute rule)

| Minute | Action |
|---|---|
| 0-5 | Restate the problem, examples, constraints, target complexity |
| 5-10 | Brute force + complexity, then name the pattern |
| 10-25 | Implement and trace one example |
| 25-35 | Still stuck? **Stop.** Read or watch the solution, then close it |
| After | Re-implement from memory without looking, then write a 2-line "key insight" in your notes |

Never grind past 35 minutes on a first attempt: after that you learn little and burn energy. Hards get 40-45 minutes.

### Spaced-repetition rule (re-solve on day 1, 3, 7, 21)

Every problem that needed a hint, took over the time-box, or had a bug gets scheduled for re-solve **from scratch, no notes**:

| Attempt | When | Pass criterion |
|---|---|---|
| R0 | Day 0 | First attempt (with the 35-minute box) |
| R1 | Day 1 | Solve unaided in the time-box |
| R2 | Day 3 | Solve unaided in ≤ 20 min |
| R3 | Day 7 | Solve unaided in ≤ 15 min, and explain the complexity out loud |
| R4 | Day 21 | Solve unaided in ≤ 15 min; retire the problem |

A failed re-solve resets the ladder to R0. Keep a simple sheet (or a `progress` note) with columns: problem, first-solved date, next-due date, ladder step. Aim for 30-40% of each session on re-solves in revision weeks.

### Weekly rhythm (12-15 h/week total, DSA about 3-4 h)

| Slot | Activity |
|---|---|
| Weekdays (about 30-45 min) | 1-2 new problems from this week's list, timed |
| Saturday | 2-3 harder problems + mock-style: talk aloud, no IDE |
| Sunday | Re-solve queue (due R1-R4 items) + update the tracker |
| Checkpoint weeks 4/8/12/16/20 | Mostly revision: re-solve failed problems, one 45-min mock |
| Week 24 | Mock interviews only (no new problems) |
| Weeks 25-26 (buffer) | Catch-up on stretch problems |

Schedule assumptions: no `curriculum.yml` was available when this page was generated, so weeks are computed from each pattern's phase (phase 1 starts week 1, phase 2 week 5, phase 3 week 9, phase 4 week 13, phase 5 week 17, phase 6 week 21). Core problems are scheduled first (max 8 per week, 3 on checkpoint weeks), and stretch problems fill remaining capacity once their pattern has started. If `data/curriculum.yml` moves a phase, shift the week numbers accordingly.

### Week summary

| Week | Core (NC150) | Stretch | Patterns | Note |
|---|---|---|---|---|
| W01 | 8 | 4 | Arrays & hashing |  |
| W02 | 8 | 4 | Arrays & hashing, Two pointers, Sliding window |  |
| W03 | 8 | 4 | Arrays & hashing, Two pointers, Sliding window, Stack |  |
| W04 | 3 | 2 | Two pointers, Stack | Checkpoint / revision week |
| W05 | 8 | 4 | Two pointers, Sliding window, Binary search, Linked list |  |
| W06 | 8 | 4 | Sliding window, Linked list |  |
| W07 | 8 | 4 | Sliding window, Stack, Linked list, Trees |  |
| W08 | 3 | 2 | Stack, Trees | Checkpoint / revision week |
| W09 | 8 | 4 | Stack, Trees, Tries |  |
| W10 | 8 | 4 | Binary search, Tries, Heap |  |
| W11 | 8 | 4 | Binary search, Backtracking |  |
| W12 | 3 | 2 | Linked list, Backtracking, Graphs | Checkpoint / revision week |
| W13 | 8 | 4 | Linked list, Trees, Graphs |  |
| W14 | 8 | 4 | Trees, Tries, Graphs, Advanced graphs |  |
| W15 | 8 | 4 | Tries, Heap, Advanced graphs, DP 1-D |  |
| W16 | 3 | 2 | Heap, DP 1-D | Checkpoint / revision week |
| W17 | 8 | 4 | Heap, Backtracking, DP 1-D, DP 2-D |  |
| W18 | 8 | 4 | Backtracking, DP 2-D, Greedy |  |
| W19 | 8 | 4 | Backtracking, Graphs, Greedy, Intervals |  |
| W20 | 3 | 2 | Graphs, Intervals | Checkpoint / revision week |
| W21 | 8 | 4 | Math & bits, Concurrency & LLD |  |
| W22 | 7 | 5 | Math & bits, Concurrency & LLD |  |
| W23 | 0 | 12 | Graphs, Advanced graphs, Concurrency & LLD |  |
| W24 | 0 | 0 | - | Checkpoint / revision week; Mock interviews only |
| W25 | 0 | 12 | DP 1-D, DP 2-D, Greedy | Buffer |
| W26 | 0 | 12 | Greedy, Intervals, Math & bits | Buffer |

## Master checklist

Status legend: `[ ]` not started, `[~]` in progress / needs re-solve, `[x]` done (R4 passed). Edit the status cell by hand as you go. The tracker is a plain table so it renders everywhere.

### Arrays & hashing

Pattern page: [Arrays & hashing](arrays-hashing.md) · Phase 1

| # | Problem | Difficulty | Pattern | Set | Week | Status |
|---|---|---|---|---|---|---|
| 1 | [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Easy | Arrays & hashing | NC150 | W01 | [ ] |
| 2 | [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/) | Easy | Arrays & hashing | NC150 | W01 | [ ] |
| 3 | [1. Two Sum](https://leetcode.com/problems/two-sum/) | Easy | Arrays & hashing | NC150 | W01 | [ ] |
| 4 | [1929. Concatenation of Array](https://leetcode.com/problems/concatenation-of-array/) | Easy | Arrays & hashing | NC250+ | W01 | [ ] |
| 5 | [14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) | Easy | Arrays & hashing | NC250+ | W01 | [ ] |
| 6 | [169. Majority Element](https://leetcode.com/problems/majority-element/) | Easy | Arrays & hashing | NC250+ | W01 | [ ] |
| 7 | [706. Design HashMap](https://leetcode.com/problems/design-hashmap/) | Easy | Arrays & hashing | NC250+ | W01 | [ ] |
| 8 | [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Medium | Arrays & hashing | NC150 | W01 | [ ] |
| 9 | [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Medium | Arrays & hashing | NC150 | W01 | [ ] |
| 10 | [271. Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/) | Medium | Arrays & hashing | NC150 | W01 | [ ] |
| 11 | [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | Medium | Arrays & hashing | NC150 | W01 | [ ] |
| 12 | [36. Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) | Medium | Arrays & hashing | NC150 | W01 | [ ] |
| 13 | [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | Medium | Arrays & hashing | NC150 | W02 | [ ] |
| 14 | [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) | Medium | Arrays & hashing | NC250+ | W02 | [ ] |
| 15 | [75. Sort Colors](https://leetcode.com/problems/sort-colors/) | Medium | Arrays & hashing | NC250+ | W02 | [ ] |
| 16 | [912. Sort an Array](https://leetcode.com/problems/sort-an-array/) | Medium | Arrays & hashing | NC250+ | W02 | [ ] |
| 17 | [229. Majority Element II](https://leetcode.com/problems/majority-element-ii/) | Medium | Arrays & hashing | NC250+ | W02 | [ ] |
| 18 | [41. First Missing Positive](https://leetcode.com/problems/first-missing-positive/) | Hard | Arrays & hashing | NC250+ | W03 | [ ] |

### Two pointers

Pattern page: [Two pointers](two-pointers.md) · Phase 1

| # | Problem | Difficulty | Pattern | Set | Week | Status |
|---|---|---|---|---|---|---|
| 19 | [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | Easy | Two pointers | NC150 | W02 | [ ] |
| 20 | [344. Reverse String](https://leetcode.com/problems/reverse-string/) | Easy | Two pointers | NC250+ | W03 | [ ] |
| 21 | [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) | Easy | Two pointers | NC250+ | W03 | [ ] |
| 22 | [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/) | Easy | Two pointers | NC250+ | W03 | [ ] |
| 23 | [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | Easy | Two pointers | NC250+ | W04 | [ ] |
| 24 | [680. Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/) | Easy | Two pointers | NC250+ | W04 | [ ] |
| 25 | [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | Medium | Two pointers | NC150 | W02 | [ ] |
| 26 | [15. 3Sum](https://leetcode.com/problems/3sum/) | Medium | Two pointers | NC150 | W02 | [ ] |
| 27 | [18. 4Sum](https://leetcode.com/problems/4sum/) | Medium | Two pointers | NC250+ | W05 | [ ] |
| 28 | [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | Medium | Two pointers | NC150 | W02 | [ ] |
| 29 | [881. Boats to Save People](https://leetcode.com/problems/boats-to-save-people/) | Medium | Two pointers | NC250+ | W05 | [ ] |
| 30 | [189. Rotate Array](https://leetcode.com/problems/rotate-array/) | Medium | Two pointers | NC250+ | W05 | [ ] |
| 31 | [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | Hard | Two pointers | NC150 | W02 | [ ] |

### Sliding window

Pattern page: [Sliding window](sliding-window.md) · Phase 1

| # | Problem | Difficulty | Pattern | Set | Week | Status |
|---|---|---|---|---|---|---|
| 32 | [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Easy | Sliding window | NC150 | W02 | [ ] |
| 33 | [219. Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/) | Easy | Sliding window | NC250+ | W05 | [ ] |
| 34 | [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Medium | Sliding window | NC150 | W02 | [ ] |
| 35 | [424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | Medium | Sliding window | NC150 | W03 | [ ] |
| 36 | [567. Permutation in String](https://leetcode.com/problems/permutation-in-string/) | Medium | Sliding window | NC150 | W03 | [ ] |
| 37 | [209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) | Medium | Sliding window | NC250+ | W06 | [ ] |
| 38 | [1004. Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/) | Medium | Sliding window | NC250+ | W06 | [ ] |
| 39 | [438. Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) | Medium | Sliding window | NC250+ | W06 | [ ] |
| 40 | [904. Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/) | Medium | Sliding window | NC250+ | W06 | [ ] |
| 41 | [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | Hard | Sliding window | NC150 | W03 | [ ] |
| 42 | [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | Hard | Sliding window | NC150 | W03 | [ ] |
| 43 | [992. Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/) | Hard | Sliding window | NC250+ | W07 | [ ] |

### Stack

Pattern page: [Stack](stack.md) · Phase 1

| # | Problem | Difficulty | Pattern | Set | Week | Status |
|---|---|---|---|---|---|---|
| 44 | [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Easy | Stack | NC150 | W03 | [ ] |
| 45 | [682. Baseball Game](https://leetcode.com/problems/baseball-game/) | Easy | Stack | NC250+ | W07 | [ ] |
| 46 | [225. Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/) | Easy | Stack | NC250+ | W07 | [ ] |
| 47 | [155. Min Stack](https://leetcode.com/problems/min-stack/) | Medium | Stack | NC150 | W03 | [ ] |
| 48 | [150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | Medium | Stack | NC150 | W03 | [ ] |
| 49 | [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) | Medium | Stack | NC150 | W03 | [ ] |
| 50 | [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | Medium | Stack | NC150 | W04 | [ ] |
| 51 | [853. Car Fleet](https://leetcode.com/problems/car-fleet/) | Medium | Stack | NC150 | W04 | [ ] |
| 52 | [71. Simplify Path](https://leetcode.com/problems/simplify-path/) | Medium | Stack | NC250+ | W07 | [ ] |
| 53 | [394. Decode String](https://leetcode.com/problems/decode-string/) | Medium | Stack | NC250+ | W08 | [ ] |
| 54 | [735. Asteroid Collision](https://leetcode.com/problems/asteroid-collision/) | Medium | Stack | NC250+ | W08 | [ ] |
| 55 | [901. Online Stock Span](https://leetcode.com/problems/online-stock-span/) | Medium | Stack | NC250+ | W09 | [ ] |
| 56 | [402. Remove K Digits](https://leetcode.com/problems/remove-k-digits/) | Medium | Stack | NC250+ | W09 | [ ] |
| 57 | [907. Sum of Subarray Minimums](https://leetcode.com/problems/sum-of-subarray-minimums/) | Medium | Stack | NC250+ | W09 | [ ] |
| 58 | [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | Hard | Stack | NC150 | W04 | [ ] |
| 59 | [85. Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/) | Hard | Stack | NC250+ | W09 | [ ] |

### Binary search

Pattern page: [Binary search](binary-search.md) · Phase 2

| # | Problem | Difficulty | Pattern | Set | Week | Status |
|---|---|---|---|---|---|---|
| 60 | [704. Binary Search](https://leetcode.com/problems/binary-search/) | Easy | Binary search | NC150 | W05 | [ ] |
| 61 | [35. Search Insert Position](https://leetcode.com/problems/search-insert-position/) | Easy | Binary search | NC250+ | W10 | [ ] |
| 62 | [374. Guess Number Higher or Lower](https://leetcode.com/problems/guess-number-higher-or-lower/) | Easy | Binary search | NC250+ | W10 | [ ] |
| 63 | [69. Sqrt(x)](https://leetcode.com/problems/sqrtx/) | Easy | Binary search | NC250+ | W10 | [ ] |
| 64 | [74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) | Medium | Binary search | NC150 | W05 | [ ] |
| 65 | [875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | Medium | Binary search | NC150 | W05 | [ ] |
| 66 | [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | Medium | Binary search | NC150 | W05 | [ ] |
| 67 | [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | Medium | Binary search | NC150 | W05 | [ ] |
| 68 | [981. Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/) | Medium | Binary search | NC150 | W05 | [ ] |
| 69 | [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | Medium | Binary search | NC250+ | W10 | [ ] |
| 70 | [162. Find Peak Element](https://leetcode.com/problems/find-peak-element/) | Medium | Binary search | NC250+ | W11 | [ ] |
| 71 | [1011. Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) | Medium | Binary search | NC250+ | W11 | [ ] |
| 72 | [81. Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/) | Medium | Binary search | NC250+ | W11 | [ ] |
| 73 | [410. Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/) | Hard | Binary search | NC250+ | W11 | [ ] |
| 74 | [4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | Hard | Binary search | NC150 | W05 | [ ] |

### Linked list

Pattern page: [Linked list](linked-list.md) · Phase 2

| # | Problem | Difficulty | Pattern | Set | Week | Status |
|---|---|---|---|---|---|---|
| 75 | [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | Easy | Linked list | NC150 | W05 | [ ] |
| 76 | [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | Easy | Linked list | NC150 | W06 | [ ] |
| 77 | [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | Easy | Linked list | NC150 | W06 | [ ] |
| 78 | [234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) | Easy | Linked list | NC250+ | W12 | [ ] |
| 79 | [143. Reorder List](https://leetcode.com/problems/reorder-list/) | Medium | Linked list | NC150 | W06 | [ ] |
| 80 | [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | Medium | Linked list | NC150 | W06 | [ ] |
| 81 | [138. Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) | Medium | Linked list | NC150 | W06 | [ ] |
| 82 | [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | Medium | Linked list | NC150 | W06 | [ ] |
| 83 | [287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) | Medium | Linked list | NC150 | W06 | [ ] |
| 84 | [142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) | Medium | Linked list | NC250+ | W12 | [ ] |
| 85 | [92. Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/) | Medium | Linked list | NC250+ | W13 | [ ] |
| 86 | [146. LRU Cache](https://leetcode.com/problems/lru-cache/) | Medium | Linked list | NC150 | W06 | [ ] |
| 87 | [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | Hard | Linked list | NC150 | W07 | [ ] |
| 88 | [25. Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) | Hard | Linked list | NC150 | W07 | [ ] |

### Trees

Pattern page: [Trees](trees.md) · Phase 2

| # | Problem | Difficulty | Pattern | Set | Week | Status |
|---|---|---|---|---|---|---|
| 89 | [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) | Easy | Trees | NC250+ | W13 | [ ] |
| 90 | [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | Easy | Trees | NC150 | W07 | [ ] |
| 91 | [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | Easy | Trees | NC150 | W07 | [ ] |
| 92 | [543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) | Easy | Trees | NC150 | W07 | [ ] |
| 93 | [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/) | Easy | Trees | NC150 | W07 | [ ] |
| 94 | [100. Same Tree](https://leetcode.com/problems/same-tree/) | Easy | Trees | NC150 | W07 | [ ] |
| 95 | [572. Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/) | Easy | Trees | NC150 | W07 | [ ] |
| 96 | [235. Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | Medium | Trees | NC150 | W08 | [ ] |
| 97 | [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | Medium | Trees | NC150 | W08 | [ ] |
| 98 | [199. Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) | Medium | Trees | NC150 | W08 | [ ] |
| 99 | [103. Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) | Medium | Trees | NC250+ | W13 | [ ] |
| 100 | [1448. Count Good Nodes in Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) | Medium | Trees | NC150 | W09 | [ ] |
| 101 | [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | Medium | Trees | NC150 | W09 | [ ] |
| 102 | [230. Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | Medium | Trees | NC150 | W09 | [ ] |
| 103 | [105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | Medium | Trees | NC150 | W09 | [ ] |
| 104 | [236. Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | Medium | Trees | NC250+ | W13 | [ ] |
| 105 | [450. Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/) | Medium | Trees | NC250+ | W14 | [ ] |
| 106 | [124. Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | Hard | Trees | NC150 | W09 | [ ] |
| 107 | [297. Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | Hard | Trees | NC150 | W09 | [ ] |

### Tries

Pattern page: [Tries](tries.md) · Phase 3

| # | Problem | Difficulty | Pattern | Set | Week | Status |
|---|---|---|---|---|---|---|
| 108 | [208. Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) | Medium | Tries | NC150 | W09 | [ ] |
| 109 | [211. Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | Medium | Tries | NC150 | W09 | [ ] |
| 110 | [720. Longest Word in Dictionary](https://leetcode.com/problems/longest-word-in-dictionary/) | Medium | Tries | NC250+ | W14 | [ ] |
| 111 | [648. Replace Words](https://leetcode.com/problems/replace-words/) | Medium | Tries | NC250+ | W14 | [ ] |
| 112 | [1268. Search Suggestions System](https://leetcode.com/problems/search-suggestions-system/) | Medium | Tries | NC250+ | W14 | [ ] |
| 113 | [421. Maximum XOR of Two Numbers in an Array](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/) | Medium | Tries | NC250+ | W15 | [ ] |
| 114 | [212. Word Search II](https://leetcode.com/problems/word-search-ii/) | Hard | Tries | NC150 | W10 | [ ] |
| 115 | [336. Palindrome Pairs](https://leetcode.com/problems/palindrome-pairs/) | Hard | Tries | NC250+ | W15 | [ ] |

### Heap

Pattern page: [Heap](heap.md) · Phase 3

| # | Problem | Difficulty | Pattern | Set | Week | Status |
|---|---|---|---|---|---|---|
| 116 | [703. Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | Easy | Heap | NC150 | W10 | [ ] |
| 117 | [1046. Last Stone Weight](https://leetcode.com/problems/last-stone-weight/) | Easy | Heap | NC150 | W10 | [ ] |
| 118 | [973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) | Medium | Heap | NC150 | W10 | [ ] |
| 119 | [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | Medium | Heap | NC150 | W10 | [ ] |
| 120 | [621. Task Scheduler](https://leetcode.com/problems/task-scheduler/) | Medium | Heap | NC150 | W10 | [ ] |
| 121 | [355. Design Twitter](https://leetcode.com/problems/design-twitter/) | Medium | Heap | NC150 | W10 | [ ] |
| 122 | [767. Reorganize String](https://leetcode.com/problems/reorganize-string/) | Medium | Heap | NC250+ | W15 | [ ] |
| 123 | [1405. Longest Happy String](https://leetcode.com/problems/longest-happy-string/) | Medium | Heap | NC250+ | W15 | [ ] |
| 124 | [1834. Single-Threaded CPU](https://leetcode.com/problems/single-threaded-cpu/) | Medium | Heap | NC250+ | W16 | [ ] |
| 125 | [373. Find K Pairs with Smallest Sums](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/) | Medium | Heap | NC250+ | W16 | [ ] |
| 126 | [295. Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) | Hard | Heap | NC150 | W10 | [ ] |
| 127 | [502. IPO](https://leetcode.com/problems/ipo/) | Hard | Heap | NC250+ | W17 | [ ] |
| 128 | [480. Sliding Window Median](https://leetcode.com/problems/sliding-window-median/) | Hard | Heap | NC250+ | W17 | [ ] |

### Backtracking

Pattern page: [Backtracking](backtracking.md) · Phase 3

| # | Problem | Difficulty | Pattern | Set | Week | Status |
|---|---|---|---|---|---|---|
| 129 | [1863. Sum of All Subset XOR Totals](https://leetcode.com/problems/sum-of-all-subset-xor-totals/) | Easy | Backtracking | NC250+ | W17 | [ ] |
| 130 | [78. Subsets](https://leetcode.com/problems/subsets/) | Medium | Backtracking | NC150 | W11 | [ ] |
| 131 | [39. Combination Sum](https://leetcode.com/problems/combination-sum/) | Medium | Backtracking | NC150 | W11 | [ ] |
| 132 | [40. Combination Sum II](https://leetcode.com/problems/combination-sum-ii/) | Medium | Backtracking | NC150 | W11 | [ ] |
| 133 | [77. Combinations](https://leetcode.com/problems/combinations/) | Medium | Backtracking | NC250+ | W17 | [ ] |
| 134 | [46. Permutations](https://leetcode.com/problems/permutations/) | Medium | Backtracking | NC150 | W11 | [ ] |
| 135 | [90. Subsets II](https://leetcode.com/problems/subsets-ii/) | Medium | Backtracking | NC150 | W11 | [ ] |
| 136 | [47. Permutations II](https://leetcode.com/problems/permutations-ii/) | Medium | Backtracking | NC250+ | W18 | [ ] |
| 137 | [79. Word Search](https://leetcode.com/problems/word-search/) | Medium | Backtracking | NC150 | W11 | [ ] |
| 138 | [131. Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/) | Medium | Backtracking | NC150 | W11 | [ ] |
| 139 | [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | Medium | Backtracking | NC150 | W11 | [ ] |
| 140 | [473. Matchsticks to Square](https://leetcode.com/problems/matchsticks-to-square/) | Medium | Backtracking | NC250+ | W18 | [ ] |
| 141 | [698. Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/) | Medium | Backtracking | NC250+ | W18 | [ ] |
| 142 | [51. N-Queens](https://leetcode.com/problems/n-queens/) | Hard | Backtracking | NC150 | W12 | [ ] |
| 143 | [52. N-Queens II](https://leetcode.com/problems/n-queens-ii/) | Hard | Backtracking | NC250+ | W18 | [ ] |
| 144 | [37. Sudoku Solver](https://leetcode.com/problems/sudoku-solver/) | Hard | Backtracking | NC250+ | W19 | [ ] |

### Graphs

Pattern page: [Graphs](graphs.md) · Phase 3

| # | Problem | Difficulty | Pattern | Set | Week | Status |
|---|---|---|---|---|---|---|
| 145 | [733. Flood Fill](https://leetcode.com/problems/flood-fill/) | Easy | Graphs | NC250+ | W19 | [ ] |
| 146 | [463. Island Perimeter](https://leetcode.com/problems/island-perimeter/) | Easy | Graphs | NC250+ | W19 | [ ] |
| 147 | [200. Number of Islands](https://leetcode.com/problems/number-of-islands/) | Medium | Graphs | NC150 | W12 | [ ] |
| 148 | [695. Max Area of Island](https://leetcode.com/problems/max-area-of-island/) | Medium | Graphs | NC150 | W12 | [ ] |
| 149 | [133. Clone Graph](https://leetcode.com/problems/clone-graph/) | Medium | Graphs | NC150 | W13 | [ ] |
| 150 | [286. Walls and Gates](https://leetcode.com/problems/walls-and-gates/) | Medium | Graphs | NC150 | W13 | [ ] |
| 151 | [994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) | Medium | Graphs | NC150 | W13 | [ ] |
| 152 | [417. Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) | Medium | Graphs | NC150 | W13 | [ ] |
| 153 | [130. Surrounded Regions](https://leetcode.com/problems/surrounded-regions/) | Medium | Graphs | NC150 | W13 | [ ] |
| 154 | [207. Course Schedule](https://leetcode.com/problems/course-schedule/) | Medium | Graphs | NC150 | W13 | [ ] |
| 155 | [210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | Medium | Graphs | NC150 | W13 | [ ] |
| 156 | [684. Redundant Connection](https://leetcode.com/problems/redundant-connection/) | Medium | Graphs | NC150 | W13 | [ ] |
| 157 | [323. Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) | Medium | Graphs | NC150 | W14 | [ ] |
| 158 | [261. Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/) | Medium | Graphs | NC150 | W14 | [ ] |
| 159 | [1091. Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/) | Medium | Graphs | NC250+ | W19 | [ ] |
| 160 | [1466. Reorder Routes to Make All Paths Lead to the City Zero](https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/) | Medium | Graphs | NC250+ | W20 | [ ] |
| 161 | [399. Evaluate Division](https://leetcode.com/problems/evaluate-division/) | Medium | Graphs | NC250+ | W20 | [ ] |
| 162 | [721. Accounts Merge](https://leetcode.com/problems/accounts-merge/) | Medium | Graphs | NC250+ | W23 | [ ] |
| 163 | [909. Snakes and Ladders](https://leetcode.com/problems/snakes-and-ladders/) | Medium | Graphs | NC250+ | W23 | [ ] |
| 164 | [752. Open the Lock](https://leetcode.com/problems/open-the-lock/) | Medium | Graphs | NC250+ | W23 | [ ] |
| 165 | [127. Word Ladder](https://leetcode.com/problems/word-ladder/) | Hard | Graphs | NC150 | W14 | [ ] |

### Advanced graphs

Pattern page: [Advanced graphs](advanced-graphs.md) · Phase 4

| # | Problem | Difficulty | Pattern | Set | Week | Status |
|---|---|---|---|---|---|---|
| 166 | [743. Network Delay Time](https://leetcode.com/problems/network-delay-time/) | Medium | Advanced graphs | NC150 | W14 | [ ] |
| 167 | [1584. Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) | Medium | Advanced graphs | NC150 | W14 | [ ] |
| 168 | [787. Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | Medium | Advanced graphs | NC150 | W14 | [ ] |
| 169 | [1514. Path with Maximum Probability](https://leetcode.com/problems/path-with-maximum-probability/) | Medium | Advanced graphs | NC250+ | W23 | [ ] |
| 170 | [1631. Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/) | Medium | Advanced graphs | NC250+ | W23 | [ ] |
| 171 | [332. Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/) | Hard | Advanced graphs | NC150 | W14 | [ ] |
| 172 | [778. Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/) | Hard | Advanced graphs | NC150 | W14 | [ ] |
| 173 | [269. Alien Dictionary](https://leetcode.com/problems/alien-dictionary/) | Hard | Advanced graphs | NC150 | W15 | [ ] |
| 174 | [2392. Build a Matrix With Conditions](https://leetcode.com/problems/build-a-matrix-with-conditions/) | Hard | Advanced graphs | NC250+ | W23 | [ ] |
| 175 | [1192. Critical Connections in a Network](https://leetcode.com/problems/critical-connections-in-a-network/) | Hard | Advanced graphs | NC250+ | W23 | [ ] |
| 176 | [1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree](https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/) | Hard | Advanced graphs | NC250+ | W23 | [ ] |

### DP 1-D

Pattern page: [DP 1-D](dp-1d.md) · Phase 4

| # | Problem | Difficulty | Pattern | Set | Week | Status |
|---|---|---|---|---|---|---|
| 177 | [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | Easy | DP 1-D | NC150 | W15 | [ ] |
| 178 | [746. Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) | Easy | DP 1-D | NC150 | W15 | [ ] |
| 179 | [1137. N-th Tribonacci Number](https://leetcode.com/problems/n-th-tribonacci-number/) | Easy | DP 1-D | NC250+ | W25 | [ ] |
| 180 | [198. House Robber](https://leetcode.com/problems/house-robber/) | Medium | DP 1-D | NC150 | W15 | [ ] |
| 181 | [213. House Robber II](https://leetcode.com/problems/house-robber-ii/) | Medium | DP 1-D | NC150 | W15 | [ ] |
| 182 | [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | Medium | DP 1-D | NC150 | W15 | [ ] |
| 183 | [647. Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) | Medium | DP 1-D | NC150 | W15 | [ ] |
| 184 | [91. Decode Ways](https://leetcode.com/problems/decode-ways/) | Medium | DP 1-D | NC150 | W15 | [ ] |
| 185 | [322. Coin Change](https://leetcode.com/problems/coin-change/) | Medium | DP 1-D | NC150 | W16 | [ ] |
| 186 | [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) | Medium | DP 1-D | NC150 | W16 | [ ] |
| 187 | [139. Word Break](https://leetcode.com/problems/word-break/) | Medium | DP 1-D | NC150 | W16 | [ ] |
| 188 | [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | Medium | DP 1-D | NC150 | W17 | [ ] |
| 189 | [416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) | Medium | DP 1-D | NC150 | W17 | [ ] |
| 190 | [279. Perfect Squares](https://leetcode.com/problems/perfect-squares/) | Medium | DP 1-D | NC250+ | W25 | [ ] |
| 191 | [377. Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/) | Medium | DP 1-D | NC250+ | W25 | [ ] |
| 192 | [740. Delete and Earn](https://leetcode.com/problems/delete-and-earn/) | Medium | DP 1-D | NC250+ | W25 | [ ] |
| 193 | [368. Largest Divisible Subset](https://leetcode.com/problems/largest-divisible-subset/) | Medium | DP 1-D | NC250+ | W25 | [ ] |
| 194 | [354. Russian Doll Envelopes](https://leetcode.com/problems/russian-doll-envelopes/) | Hard | DP 1-D | NC250+ | W25 | [ ] |

### DP 2-D

Pattern page: [DP 2-D](dp-2d.md) · Phase 5

| # | Problem | Difficulty | Pattern | Set | Week | Status |
|---|---|---|---|---|---|---|
| 195 | [62. Unique Paths](https://leetcode.com/problems/unique-paths/) | Medium | DP 2-D | NC150 | W17 | [ ] |
| 196 | [63. Unique Paths II](https://leetcode.com/problems/unique-paths-ii/) | Medium | DP 2-D | NC250+ | W25 | [ ] |
| 197 | [64. Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/) | Medium | DP 2-D | NC250+ | W25 | [ ] |
| 198 | [1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | Medium | DP 2-D | NC150 | W17 | [ ] |
| 199 | [309. Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) | Medium | DP 2-D | NC150 | W17 | [ ] |
| 200 | [518. Coin Change II](https://leetcode.com/problems/coin-change-ii/) | Medium | DP 2-D | NC150 | W17 | [ ] |
| 201 | [494. Target Sum](https://leetcode.com/problems/target-sum/) | Medium | DP 2-D | NC150 | W17 | [ ] |
| 202 | [97. Interleaving String](https://leetcode.com/problems/interleaving-string/) | Medium | DP 2-D | NC150 | W17 | [ ] |
| 203 | [72. Edit Distance](https://leetcode.com/problems/edit-distance/) | Medium | DP 2-D | NC150 | W18 | [ ] |
| 204 | [221. Maximal Square](https://leetcode.com/problems/maximal-square/) | Medium | DP 2-D | NC250+ | W25 | [ ] |
| 205 | [474. Ones and Zeroes](https://leetcode.com/problems/ones-and-zeroes/) | Medium | DP 2-D | NC250+ | W25 | [ ] |
| 206 | [329. Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) | Hard | DP 2-D | NC150 | W18 | [ ] |
| 207 | [115. Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/) | Hard | DP 2-D | NC150 | W18 | [ ] |
| 208 | [188. Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/) | Hard | DP 2-D | NC250+ | W25 | [ ] |
| 209 | [312. Burst Balloons](https://leetcode.com/problems/burst-balloons/) | Hard | DP 2-D | NC150 | W18 | [ ] |
| 210 | [10. Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) | Hard | DP 2-D | NC150 | W18 | [ ] |

### Greedy

Pattern page: [Greedy](greedy.md) · Phase 5

| # | Problem | Difficulty | Pattern | Set | Week | Status |
|---|---|---|---|---|---|---|
| 211 | [860. Lemonade Change](https://leetcode.com/problems/lemonade-change/) | Easy | Greedy | NC250+ | W25 | [ ] |
| 212 | [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | Medium | Greedy | NC150 | W18 | [ ] |
| 213 | [122. Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) | Medium | Greedy | NC250+ | W26 | [ ] |
| 214 | [918. Maximum Sum Circular Subarray](https://leetcode.com/problems/maximum-sum-circular-subarray/) | Medium | Greedy | NC250+ | W26 | [ ] |
| 215 | [978. Longest Turbulent Subarray](https://leetcode.com/problems/longest-turbulent-subarray/) | Medium | Greedy | NC250+ | W26 | [ ] |
| 216 | [55. Jump Game](https://leetcode.com/problems/jump-game/) | Medium | Greedy | NC150 | W18 | [ ] |
| 217 | [45. Jump Game II](https://leetcode.com/problems/jump-game-ii/) | Medium | Greedy | NC150 | W18 | [ ] |
| 218 | [134. Gas Station](https://leetcode.com/problems/gas-station/) | Medium | Greedy | NC150 | W19 | [ ] |
| 219 | [846. Hand of Straights](https://leetcode.com/problems/hand-of-straights/) | Medium | Greedy | NC150 | W19 | [ ] |
| 220 | [1899. Merge Triplets to Form Target Triplet](https://leetcode.com/problems/merge-triplets-to-form-target-triplet/) | Medium | Greedy | NC150 | W19 | [ ] |
| 221 | [763. Partition Labels](https://leetcode.com/problems/partition-labels/) | Medium | Greedy | NC150 | W19 | [ ] |
| 222 | [678. Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/) | Medium | Greedy | NC150 | W19 | [ ] |
| 223 | [1029. Two City Scheduling](https://leetcode.com/problems/two-city-scheduling/) | Medium | Greedy | NC250+ | W26 | [ ] |
| 224 | [135. Candy](https://leetcode.com/problems/candy/) | Hard | Greedy | NC250+ | W26 | [ ] |

### Intervals

Pattern page: [Intervals](intervals.md) · Phase 5

| # | Problem | Difficulty | Pattern | Set | Week | Status |
|---|---|---|---|---|---|---|
| 225 | [252. Meeting Rooms](https://leetcode.com/problems/meeting-rooms/) | Easy | Intervals | NC150 | W19 | [ ] |
| 226 | [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/) | Medium | Intervals | NC150 | W19 | [ ] |
| 227 | [57. Insert Interval](https://leetcode.com/problems/insert-interval/) | Medium | Intervals | NC150 | W19 | [ ] |
| 228 | [435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) | Medium | Intervals | NC150 | W20 | [ ] |
| 229 | [452. Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) | Medium | Intervals | NC250+ | W26 | [ ] |
| 230 | [253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) | Medium | Intervals | NC150 | W20 | [ ] |
| 231 | [986. Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/) | Medium | Intervals | NC250+ | W26 | [ ] |
| 232 | [1288. Remove Covered Intervals](https://leetcode.com/problems/remove-covered-intervals/) | Medium | Intervals | NC250+ | W26 | [ ] |
| 233 | [729. My Calendar I](https://leetcode.com/problems/my-calendar-i/) | Medium | Intervals | NC250+ | W26 | [ ] |
| 234 | [1851. Minimum Interval to Include Each Query](https://leetcode.com/problems/minimum-interval-to-include-each-query/) | Hard | Intervals | NC150 | W20 | [ ] |
| 235 | [759. Employee Free Time](https://leetcode.com/problems/employee-free-time/) | Hard | Intervals | NC250+ | W26 | [ ] |

### Math & bits

Pattern page: [Math & bits](math-bits.md) · Phase 5

| # | Problem | Difficulty | Pattern | Set | Week | Status |
|---|---|---|---|---|---|---|
| 236 | [136. Single Number](https://leetcode.com/problems/single-number/) | Easy | Math & bits | NC150 | W21 | [ ] |
| 237 | [191. Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) | Easy | Math & bits | NC150 | W21 | [ ] |
| 238 | [338. Counting Bits](https://leetcode.com/problems/counting-bits/) | Easy | Math & bits | NC150 | W21 | [ ] |
| 239 | [190. Reverse Bits](https://leetcode.com/problems/reverse-bits/) | Easy | Math & bits | NC150 | W21 | [ ] |
| 240 | [268. Missing Number](https://leetcode.com/problems/missing-number/) | Easy | Math & bits | NC150 | W21 | [ ] |
| 241 | [202. Happy Number](https://leetcode.com/problems/happy-number/) | Easy | Math & bits | NC150 | W21 | [ ] |
| 242 | [66. Plus One](https://leetcode.com/problems/plus-one/) | Easy | Math & bits | NC150 | W21 | [ ] |
| 243 | [371. Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/) | Medium | Math & bits | NC150 | W21 | [ ] |
| 244 | [7. Reverse Integer](https://leetcode.com/problems/reverse-integer/) | Medium | Math & bits | NC150 | W22 | [ ] |
| 245 | [48. Rotate Image](https://leetcode.com/problems/rotate-image/) | Medium | Math & bits | NC150 | W22 | [ ] |
| 246 | [54. Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) | Medium | Math & bits | NC150 | W22 | [ ] |
| 247 | [73. Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/) | Medium | Math & bits | NC150 | W22 | [ ] |
| 248 | [50. Pow(x, n)](https://leetcode.com/problems/powx-n/) | Medium | Math & bits | NC150 | W22 | [ ] |
| 249 | [43. Multiply Strings](https://leetcode.com/problems/multiply-strings/) | Medium | Math & bits | NC150 | W22 | [ ] |
| 250 | [2013. Detect Squares](https://leetcode.com/problems/detect-squares/) | Medium | Math & bits | NC150 | W22 | [ ] |
| 251 | [201. Bitwise AND of Numbers Range](https://leetcode.com/problems/bitwise-and-of-numbers-range/) | Medium | Math & bits | NC250+ | W26 | [ ] |
| 252 | [149. Max Points on a Line](https://leetcode.com/problems/max-points-on-a-line/) | Hard | Math & bits | NC250+ | W26 | [ ] |

### Concurrency & LLD

Pattern page: [Concurrency & LLD](concurrency-lld.md) · Phase 6

| # | Problem | Difficulty | Pattern | Set | Week | Status |
|---|---|---|---|---|---|---|
| 253 | [1114. Print in Order](https://leetcode.com/problems/print-in-order/) | Easy | Concurrency & LLD | NC250+ | W21 | [ ] |
| 254 | [359. Logger Rate Limiter](https://leetcode.com/problems/logger-rate-limiter/) | Easy | Concurrency & LLD | NC250+ | W21 | [ ] |
| 255 | [1115. Print FooBar Alternately](https://leetcode.com/problems/print-foobar-alternately/) | Medium | Concurrency & LLD | NC250+ | W21 | [ ] |
| 256 | [1116. Print Zero Even Odd](https://leetcode.com/problems/print-zero-even-odd/) | Medium | Concurrency & LLD | NC250+ | W21 | [ ] |
| 257 | [1117. Building H2O](https://leetcode.com/problems/building-h2o/) | Medium | Concurrency & LLD | NC250+ | W22 | [ ] |
| 258 | [1195. Fizz Buzz Multithreaded](https://leetcode.com/problems/fizz-buzz-multithreaded/) | Medium | Concurrency & LLD | NC250+ | W22 | [ ] |
| 259 | [1226. The Dining Philosophers](https://leetcode.com/problems/the-dining-philosophers/) | Medium | Concurrency & LLD | NC250+ | W22 | [ ] |
| 260 | [1188. Design Bounded Blocking Queue](https://leetcode.com/problems/design-bounded-blocking-queue/) | Medium | Concurrency & LLD | NC250+ | W22 | [ ] |
| 261 | [1242. Web Crawler Multithreaded](https://leetcode.com/problems/web-crawler-multithreaded/) | Medium | Concurrency & LLD | NC250+ | W22 | [ ] |
| 262 | [362. Design Hit Counter](https://leetcode.com/problems/design-hit-counter/) | Medium | Concurrency & LLD | NC250+ | W23 | [ ] |
| 263 | [380. Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/) | Medium | Concurrency & LLD | NC250+ | W23 | [ ] |
| 264 | [1472. Design Browser History](https://leetcode.com/problems/design-browser-history/) | Medium | Concurrency & LLD | NC250+ | W23 | [ ] |
| 265 | [460. LFU Cache](https://leetcode.com/problems/lfu-cache/) | Hard | Concurrency & LLD | NC250+ | W23 | [ ] |

## Notes

- Premium LeetCode problems are marked "(Premium)" in each pattern page's insight column. NeetCode.io offers free access to the same problem statements (see the [resources](index.md#resources-summary)). If you do not have access, skip them: none is required for the core set except 271, 286, 323, 261 and 269 (substitute the NeetCode versions).
- LeetCode returns `403` to scripted link checks (bot protection), so the problem URLs here were built from the official title slugs, not machine-verified. If a link 404s, search the number on leetcode.com.
- Problem 146 (LRU Cache) appears once, under Linked list, and is repeated in the [concurrency & LLD](concurrency-lld.md) lab as an extension exercise.

## Questions

### L1 — Recall

??? question "Q1. State the spaced-repetition ladder and the pass criterion for retiring a problem."
    ??? success "Answer"
        Re-solve on day 1, 3, 7, 21 without notes. Retire it after the day-21 solve is done in ≤ 15 minutes with the complexity explained. A failure resets to day 0.

??? question "Q2. What is the time-box, and what do you do at its end?"
    ??? success "Answer"
        25-35 minutes (40-45 for Hards). At the end, stop, read or watch one solution, close it, re-implement from memory, then write the key insight. Schedule R1.

??? question "Q3. What is the NC150 vs NC250+ distinction in this tracker?"
    ??? success "Answer"
        NC150 is the NeetCode core interview set and is mandatory. NC250+ adds harder variants, Staff-level classics and concurrency/LLD problems, and is done as time allows (buffer weeks absorb overflow).

### L2 — Apply

??? question "Q4. You are 3 days behind at the end of week 6. Re-plan."
    ??? success "Answer"
        Never drop NC150. Move that week's NC250+ problems into the next buffer or revision week, keep the re-solve queue (it is the highest-value activity), and cut the week's new problems to the ones in patterns due for the next checkpoint. If two weeks behind, push the P1 patterns (tries, advanced graphs, math and bits) into the buffer weeks 25-26.

??? question "Q5. Design your personal spreadsheet columns for the spaced-repetition queue."
    ??? success "Answer"
        Problem id, pattern, first-solved date, ladder step (R0-R4), next-due date (= first-solved + 1/3/7/21 days according to the step), last time (minutes), needed hint (y/n), failure reason (pattern-miss, bug, edge case, complexity). A filter on next-due ≤ today gives the daily queue.

??? question "Q6. After a mock you notice most failures are 'edge case bugs', not pattern misses. What do you change?"
    ??? success "Answer"
        Add a mandatory 3-minute test phase to your loop (empty, single, duplicates, max size, negative), keep a personal bug log by category, practise tracing your code line by line instead of re-reading it, and add "edge cases" to the pass criterion of each re-solve.

### L3 — Design & trade-offs

??? question "Q7. Breadth-first (all patterns once) vs depth-first (one pattern to mastery) for 24 weeks?"
    ??? success "Answer"
        Use pattern-by-pattern progression for learning (this plan's phases), and interleave old patterns through the re-solve queue and checkpoint-week mixed sets, because interleaving improves discrimination ("which pattern is this?") and retention. Pure blocking makes every problem look like the current pattern's problem, which does not match real interviews.

??? question "Q8. How many problems are enough? Defend a number."
    ??? success "Answer"
        Around 150-250 well-reviewed problems is a common threshold for pattern fluency, but the number matters less than the quality of review. 150 with proper re-solving beats 500 solved once. Track the leading indicators instead: percent of unseen Mediums solved in 25 minutes without hints, and the failure-cause distribution from mocks.

??? question "Q9. How do you use company-tagged problem lists responsibly?"
    ??? success "Answer"
        Use them for the last 2-3 weeks to calibrate difficulty and style, not as a shortcut. Prioritise pattern coverage first. Treat frequency data as weak evidence, since interviewers rotate questions and the tags are self-reported.

### L4 — Staff-level ambiguity

??? question "Q10. You have a Staff loop in 4 weeks and are only at week 12 of this plan. What do you cut and keep?"
    ??? success "Answer"
        Keep: all NC150 in trees, graphs, heap, DP 1-D, intervals and binary search (highest frequency), daily re-solves, and 2-3 mocks per week. Compress: DP 2-D and advanced graphs to the 6-8 most common problems (LCS, edit distance, coin change II, Dijkstra, topological sort, union-find). Drop: math/bit trivia, tries beyond the basic implementation, NC250+ entirely. Add: LLD/concurrency and one system-design mock per week, since Staff loops weigh these heavily. Communicate that trade-off to your recruiter if you need more time, because moving the date is often possible.

??? question "Q11. A colleague preparing with you memorises solutions. How do you help them shift?"
    ??? success "Answer"
        Introduce the "explain to a rubber duck without code" exercise, ask them to derive the brute force and identify the inefficiency before reading hints, run mocks with a twist (change a constraint, for example negative numbers or streaming) so memorised solutions fail visibly, and give the re-solve ladder with a strict no-notes rule. The goal is derivation ability, so make that the measured outcome.

## Real-world use cases

- **Personal learning ops:** the same tracker-plus-spaced-repetition mechanic works for on-call runbook drills and incident-response practice.
- **Team interview prep groups:** shared tracker for a peer study cohort (mock rotation).
- **Interviewer calibration:** if you interview others, the tracker's difficulty ladder helps pick fair problems.

## Pitfalls & anti-patterns

- Solving a problem once and marking it done.
- Watching solutions first ("passive learning").
- Grinding past the time-box.
- Only practising your strongest patterns.
- No mock interviews (talking aloud is a separate skill).

## Checklist

- [ ] I created my spaced-repetition sheet with due dates
- [ ] I use the 25-35 minute time-box on every first attempt
- [ ] I completed at least one mock interview every checkpoint week
- [ ] I answered all L3 questions out loud in < 3 min each
