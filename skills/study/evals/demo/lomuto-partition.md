---
date: 2026-10-16
mode: concept
concept: Lomuto partition (quicksort)
note: eval run for the stepper-trace template; the trace is produced by running the algorithm in the page
---
# 快速排序的划分（Lomuto）

## 1. 大白话
挑最后一个数当主元，从左往右扫一遍：遇到不比主元大的，就扔进左边的“小数区”；扫完把主元放到两区之间。

## 2. 动机
快速排序的全部工作都在划分里：划分做对了，递归只是在左右两块上重复。

## 3. 分步演示
![图 1：一趟扫描把 [7, 2, 9, 4, 3, 8, 5] 分成 ≤ 5 和 > 5 两块](fig-lomuto-partition-strip.png)

交互版：`fig-lomuto-partition.html`（◀ ▶ 或播放）。每一步的数组由页面里的 `trace()` 实际运行算法得到，`console.assert` 检查最终满足划分性质。

## 4. 不变式（理解的关键）
循环每一步之后：`a[lo..i]` 都 ≤ pivot，`a[i+1..j]` 都 > pivot，`a[j+1..hi-1]` 未处理。图中绿色、橙色、白色三段正好是这三部分，所以“看图”就是在看不变式是否保持。

## 5. 连接
| 已知概念 | 相同 | 不同 | 类比在哪里失效 |
|---|---|---|---|
| Hoare 划分 | 都把数组分成两块 | Hoare 用两个指针从两端相向走，交换次数通常更少 | Hoare 结束时主元不一定在最终位置 |
| 荷兰国旗（三路划分） | 一趟扫描维护区间不变式 | 多一个“= pivot”区 | 大量重复元素时 Lomuto 会退化到 O(n²)，三路划分不会 |

## 6. 常见误解（复述时检查）
- “i 指向下一个要放小数的位置”：差一格，i 指向小数区的**最后一个**元素（初始化为 lo − 1 正是因为小数区一开始是空的）。
- “划分后两边都排好序了”：没有，只保证左边都 ≤、右边都 >（图中最后一步右边是 9, 8, 7）。
