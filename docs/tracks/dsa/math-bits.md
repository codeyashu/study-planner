---
title: "Math, geometry & bit manipulation"
track: dsa
slug: math-bits
priority: P1
complexity: 2
est_hours: 2
phase: 5
tags: [dsa, P1]
last_reviewed: 2026-09-25
---

# Math, geometry & bit manipulation

!!! abstract "At a glance"
    **Priority:** P1 · **Complexity:** 2/5 · **Est. time:** 2 h · **Phase:** 5 · **Prereqs:** [Arrays & hashing](arrays-hashing.md)
    **You're done when:** you can do the classic bit tricks (`n & (n-1)`, XOR cancellation, masks), matrix rotation/spiral/zeroing in place, fast exponentiation, and gcd-normalised geometry without floats.

## Why it matters

This is the "grab bag" NeetCode category: matrix manipulation, number handling and bit tricks. These problems are short but unforgiving of off-by-one and overflow mistakes, and they appear as warm-ups or as sub-steps in harder problems (bitmask DP, hashing of slopes, XOR tries). Python's arbitrary-precision ints remove overflow worries but introduce a different trap: negative numbers have infinite sign extension, so 32-bit emulation needs explicit masks.

## Core concepts

### Pattern recognition signals

| When you see… | Think… |
|---|---|
| "every element appears twice except one" | XOR |
| "count set bits", "power of two" | `n & (n-1)`, `bit_count()` |
| "add/multiply without operators" | Bitwise loops (carry = `(a & b) << 1`) |
| "rotate/spiral/zero a matrix in place" | Layer/boundary loops, transpose + reverse, marker row/col |
| "x^n", modular power | Exponentiation by squaring |
| "digits", "reverse integer", "happy number" | `divmod` loops, cycle detection |
| Points on a line / slopes | gcd-reduced `(dy, dx)` with sign normalisation |
| Subsets of ≤ 20 items as state | Bitmask |

### Bit-trick reference

| Goal | Expression |
|---|---|
| Test bit i | `(x >> i) & 1` |
| Set / clear / toggle bit i | `x \| (1 << i)`, `x & ~(1 << i)`, `x ^ (1 << i)` |
| Lowest set bit | `x & -x` |
| Drop lowest set bit | `x & (x - 1)` |
| Power of two | `x > 0 and x & (x - 1) == 0` |
| Count bits | `x.bit_count()` (3.10+) or the loop with `x &= x - 1` |
| Swap without temp | `a ^= b; b ^= a; a ^= b` (know it, don't use it) |
| Iterate submasks of m | `s = m; while s: ...; s = (s - 1) & m` |
| 32-bit wrap in Python | `x & 0xFFFFFFFF`, then sign: `x if x < 2**31 else x - 2**32` |

### Template 1: XOR and counting bits

```python
def single_number(nums):
    r = 0
    for x in nums: r ^= x
    return r

def counting_bits(n):
    bits = [0] * (n + 1)
    for i in range(1, n + 1):
        bits[i] = bits[i >> 1] + (i & 1)
    return bits

def sum_two(a, b):                          # LC 371, 32-bit emulation
    MASK, MAX = 0xFFFFFFFF, 0x7FFFFFFF
    while b:
        a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK
    return a if a <= MAX else ~(a ^ MASK)
```

### Template 2: matrix in place

```python
def rotate(m):                              # 90 degrees clockwise
    n = len(m)
    for i in range(n):
        for j in range(i + 1, n):
            m[i][j], m[j][i] = m[j][i], m[i][j]      # transpose
    for row in m:
        row.reverse()

def spiral_order(m):
    res = []
    top, bot, left, right = 0, len(m) - 1, 0, len(m[0]) - 1
    while top <= bot and left <= right:
        res += m[top][left:right + 1]; top += 1
        for r in range(top, bot + 1): res.append(m[r][right])
        right -= 1
        if top <= bot:
            res += m[bot][left:right + 1][::-1]; bot -= 1
        if left <= right:
            for r in range(bot, top - 1, -1): res.append(m[r][left])
            left += 1
    return res

def set_zeroes(m):                          # O(1) extra space via first row/col markers
    R, C = len(m), len(m[0])
    row0 = any(m[0][c] == 0 for c in range(C))
    col0 = any(m[r][0] == 0 for r in range(R))
    for r in range(1, R):
        for c in range(1, C):
            if m[r][c] == 0: m[r][0] = m[0][c] = 0
    for r in range(1, R):
        for c in range(1, C):
            if m[r][0] == 0 or m[0][c] == 0: m[r][c] = 0
    if row0: m[0] = [0] * C
    if col0:
        for r in range(R): m[r][0] = 0
```

### Template 3: fast power, gcd, multiply strings

```python
def my_pow(x, n):
    if n < 0: x, n = 1 / x, -n
    res = 1.0
    while n:
        if n & 1: res *= x
        x *= x; n >>= 1
    return res                              # O(log n)

def multiply(a, b):                         # LC 43 without int() conversion
    res = [0] * (len(a) + len(b))
    for i in range(len(a) - 1, -1, -1):
        for j in range(len(b) - 1, -1, -1):
            p = (ord(a[i]) - 48) * (ord(b[j]) - 48) + res[i + j + 1]
            res[i + j + 1] = p % 10
            res[i + j] += p // 10
    s = "".join(map(str, res)).lstrip("0")
    return s or "0"
```

### Template 4: geometry with exact arithmetic (Max Points on a Line)

```python
from math import gcd
from collections import defaultdict

def max_points(points):
    best = 1
    for i, (x1, y1) in enumerate(points):
        slopes = defaultdict(int)
        for x2, y2 in points[i + 1:]:
            dx, dy = x2 - x1, y2 - y1
            g = gcd(dx, dy)
            dx, dy = dx // g, dy // g
            if dx < 0 or (dx == 0 and dy < 0):       # canonical sign
                dx, dy = -dx, -dy
            slopes[(dx, dy)] += 1
            best = max(best, slopes[(dx, dy)] + 1)
    return best                                       # O(n^2)
```

Use cross products for orientation tests (`(b-a) x (c-a)`), never float slopes.

### Common bugs

- Python `>>` on negatives is arithmetic (sign-extending), and `~x == -x-1`. Mask to emulate 32 bits.
- `//` floors toward −∞, and `%` result takes the sign of the divisor, which differs from C/Java.
- Reverse Integer: check the 32-bit range *after* reversing (Python doesn't overflow).
- Rotate Image: transposing the whole matrix (not just the upper triangle) undoes itself.
- Set Matrix Zeroes: not saving the first row/col flags separately.
- Float slopes: 1e-9 collisions. Use gcd-reduced integer pairs.
- Detect Squares: counting the same-point pairs incorrectly (needs the count map and diagonal check with `abs(dx) == abs(dy) != 0`).

## Resources

| Resource | Type | Why this one | Level | Cost |
|---|---|---|---|---|
| [NeetCode roadmap: Math & Geometry, Bit Manipulation](https://neetcode.io/roadmap) | video | Clear walk-throughs of rotation, spiral and bit adders | intermediate | freemium |
| [Bit Twiddling Hacks (Sean Anderson)](https://graphics.stanford.edu/~seander/bithacks.html) :gem: | article | The canonical catalogue of bit tricks with explanations | advanced | free |
| [cp-algorithms: Bit manipulation](https://cp-algorithms.com/algebra/bit-manipulation.html) | article | Modern reference with submask iteration | advanced | free |
| [cp-algorithms: Binary exponentiation](https://cp-algorithms.com/algebra/binary-exp.html) | article | Modular power and applications | advanced | free |
| [cp-algorithms: Euclidean algorithm](https://cp-algorithms.com/algebra/euclid-algorithm.html) | article | gcd, extended gcd, proofs | advanced | free |
| [Tech Interview Handbook: Math / Matrix / Binary](https://www.techinterviewhandbook.org/algorithms/math/) | article | Corner cases checklist | intermediate | free |
| [VisuAlgo: Bitmask](https://visualgo.net/en/bitmask) :gem: | interactive | See bit operations on integers | intermediate | free |

## Hands-on lab

| # | LC | Problem | Difficulty | Set | Key insight |
|---|---|---|---|---|---|
| 1 | 136 | [Single Number](https://leetcode.com/problems/single-number/) | Easy | NC150 | XOR cancels pairs. |
| 2 | 191 | [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) | Easy | NC150 | n &= n - 1 drops the lowest set bit. |
| 3 | 338 | [Counting Bits](https://leetcode.com/problems/counting-bits/) | Easy | NC150 | bits[i] = bits[i >> 1] + (i & 1). |
| 4 | 190 | [Reverse Bits](https://leetcode.com/problems/reverse-bits/) | Easy | NC150 | Shift out LSB into result 32 times; mask to 32 bits. |
| 5 | 268 | [Missing Number](https://leetcode.com/problems/missing-number/) | Easy | NC150 | XOR of indices and values, or Gauss sum. |
| 6 | 202 | [Happy Number](https://leetcode.com/problems/happy-number/) | Easy | NC150 | Cycle detection on the digit-square function. |
| 7 | 66 | [Plus One](https://leetcode.com/problems/plus-one/) | Easy | NC150 | Carry from the right; all 9s grows the array. |
| 8 | 371 | [Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/) | Medium | NC150 | XOR = sum w/o carry, AND<<1 = carry; mask 32 bits in Python. |
| 9 | 7 | [Reverse Integer](https://leetcode.com/problems/reverse-integer/) | Medium | NC150 | Check 32-bit overflow before it happens. |
| 10 | 48 | [Rotate Image](https://leetcode.com/problems/rotate-image/) | Medium | NC150 | Transpose, then reverse each row. |
| 11 | 54 | [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) | Medium | NC150 | Shrinking boundaries top/bottom/left/right. |
| 12 | 73 | [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/) | Medium | NC150 | Use first row/col as markers; separate flag for row 0. |
| 13 | 50 | [Pow(x, n)](https://leetcode.com/problems/powx-n/) | Medium | NC150 | Fast exponentiation by squaring; negative n. |
| 14 | 43 | [Multiply Strings](https://leetcode.com/problems/multiply-strings/) | Medium | NC150 | Digit i*j lands at positions i+j and i+j+1. |
| 15 | 2013 | [Detect Squares](https://leetcode.com/problems/detect-squares/) | Medium | NC150 | Count map; iterate diagonal partners of the query. |
| 16 | 201 | [Bitwise AND of Numbers Range](https://leetcode.com/problems/bitwise-and-of-numbers-range/) | Medium | NC250+ | Common binary prefix of left and right. |
| 17 | 149 | [Max Points on a Line](https://leetcode.com/problems/max-points-on-a-line/) | Hard | NC250+ | Slope as reduced (dy, dx) via gcd; avoid floats. |

**Stretch exercise:** implement subset-sum DP over bitmasks for n=20 (`dp[mask]`), and use submask iteration to solve "partition into k equal-sum subsets". Time it against the backtracking version from [Backtracking](backtracking.md).

## Questions

### L1 — Recall

??? question "Q1. What does `n & (n - 1)` do and where is it used?"
    ??? success "Answer"
        It clears the lowest set bit. Uses: count set bits in O(popcount), power-of-two test (result is 0), and Fenwick tree / bitmask iteration logic.

??? question "Q2. Why does XOR find the single non-duplicated number?"
    ??? success "Answer"
        XOR is commutative and associative, `x ^ x = 0`, and `x ^ 0 = x`. All paired values cancel, leaving the singleton, in O(n) time and O(1) space.

??? question "Q3. How does exponentiation by squaring achieve O(log n)?"
    ??? success "Answer"
        It uses x^n = (x²)^(n/2) for even n and x · x^(n-1) for odd n, so each step halves the exponent. Iteratively, process the bits of n, multiplying the result by the current square when the bit is set.

### L2 — Apply

??? question "Q4. Implement Missing Number three ways."
    ??? success "Answer"
        ```python
        def missing_gauss(a): n = len(a); return n * (n + 1) // 2 - sum(a)
        def missing_xor(a):
            r = len(a)
            for i, x in enumerate(a): r ^= i ^ x
            return r
        def missing_swap_sort(a):             # cyclic placement, O(1) extra, mutates
            i = 0
            while i < len(a):
                if a[i] < len(a) and a[a[i]] != a[i]:
                    a[a[i]], a[i] = a[i], a[a[i]]
                else:
                    i += 1
            for i, x in enumerate(a):
                if i != x: return i
            return len(a)
        ```
        All O(n). Gauss is simplest but can overflow in fixed-width languages, so XOR avoids that.

??? question "Q5. Trace `sum_two(5, 3)`."
    ??? success "Answer"
        a=101, b=011. Iteration 1: a^b=110 (6), carry (a&b)<<1 = 001<<1 = 010 (2). Iteration 2: a=110^010=100 (4), b=(110&010)<<1=100 (4). Iteration 3: a=100^100=000, b=(100&100)<<1=1000 (8). Iteration 4: a=1000 (8), b=0. Result 8.

??? question "Q6. Implement Happy Number using cycle detection."
    ??? success "Answer"
        ```python
        def is_happy(n):
            def step(x):
                s = 0
                while x:
                    x, d = divmod(x, 10); s += d * d
                return s
            slow, fast = n, step(n)
            while fast != 1 and slow != fast:
                slow, fast = step(slow), step(step(fast))
            return fast == 1
        ```
        Floyd's algorithm, O(1) space. A set of seen values also works, in O(k) space.

### L3 — Design & trade-offs

??? question "Q7. Rotate Image: transpose+reverse vs four-way cycle swap vs new matrix?"
    ??? success "Answer"
        Transpose + reverse rows: two simple passes, in place, O(n²), easiest to get right. Four-way swap by layers: single pass, in place, but trickier index math. New matrix: O(n²) space, simplest, and fine unless the interviewer says in place. Pick transpose + reverse and know the formula `new[j][n-1-i] = old[i][j]`.

??? question "Q8. Max Points on a Line: float slope vs gcd-normalised vs cross-product. Compare."
    ??? success "Answer"
        Float slopes have precision collisions and vertical-line special cases. gcd-normalised `(dy, dx)` pairs are exact hashable keys (with sign normalisation). Cross-product checks (`(b-a) × (c-a) == 0`) give O(n³) without hashing, exact but slower. Use gcd for O(n²).

??? question "Q9. Bitmask DP vs backtracking for subset problems with n = 20?"
    ??? success "Answer"
        Bitmask DP visits each of the 2^n masks once with O(n) transitions: O(n · 2^n) guaranteed, and memory 2^n (1M entries is fine). Backtracking can be faster with strong pruning but has no worst-case guarantee. Choose bitmask DP when overlapping states exist (TSP, k-partition), and backtracking when solutions must be enumerated or pruning is strong.

### L4 — Staff-level ambiguity

??? question "Q10. Feature flags for 10M users are stored as 64 booleans per user. Design the storage and evaluation."
    ??? success "Answer"
        Pack the 64 flags into a `uint64` per user (8 bytes: 80 MB for 10M users), evaluate with mask tests `(flags & MASK) == MASK`, and support atomic updates with compare-and-swap or DB bit operations (`flags | mask`). Trade-offs: readability and schema evolution (adding flag 65 needs a second word, so version the bitset layout), auditability (bit positions need a registry, and never reuse retired bits), and analytics (bit ops in SQL are awkward, so expose a view). Alternatives: Roaring bitmaps per flag (a set of user ids) for fast audience counting and set algebra, which scale better when flags are numerous and sparse.

??? question "Q11. Review: a teammate replaced clear code with bit-twiddling to 'save memory' in a hot path. How do you respond?"
    ??? success "Answer"
        Ask for evidence: a profile showing the memory or CPU is the bottleneck, and a benchmark of before and after. If it's justified, require named constants and helper functions (`has_flag(flags, F_X)`), unit tests for boundaries, and a comment explaining the layout. If not, prefer readability. The principle: bit-packing trades maintainability for density, so it should be a measured decision with an owner, not a default.

## Real-world use cases

- **Permissions and feature flags:** bitsets (Unix file modes, capability masks, Roaring bitmaps in analytics).
- **Networking:** subnet masks, CIDR checks (`(ip & mask) == net`), checksum computation.
- **Graphics/GIS:** matrix rotations, cross-product orientation tests for geofence polygons around ports.
- **Hashing and crypto primitives:** XOR/shift mixing, Bloom filters (bit arrays with multiple hashes).

## Pitfalls & anti-patterns

- Assuming fixed-width overflow semantics in Python (or vice versa in Java/C++).
- Using floats for geometric equality.
- In-place matrix operations without documenting mutation.
- Clever bit tricks without named constants.

## Checklist

- [ ] I can list the ten bit tricks in the reference table without notes
- [ ] I can rotate, spiral and zero a matrix without index bugs
- [ ] I know Python's negative-number and floor-division semantics and their traps
- [ ] I answered all L3 questions out loud in < 3 min each
