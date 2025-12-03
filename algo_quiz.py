import click
import random
import getopt
import sys

MAP = {
    'a': 1,
    'b': 2,
    'c': 3,
}

PROBLEM_TO_CATEGORY = {
    # arrays & hashing
    'Contains Duplicate': {
        'category': 'arrays_hashing',
        'solution_summary': 'Store each number in hash set. If number already exists in set, return False. If you make to to the end, return True',
        'problem_statement': 'Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.',
        'level': 'easy',
    },
    'Valid Anagram': {
        'category': 'arrays_hashing',
        'solution_summary': 'Make hash maps to count char frequencies for each string. Return true if sets are equal',
        'problem_statement': 'Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.\n\nAn anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.',
        'level': 'easy',
    },
    'Two Sum': {
        'category': 'arrays_hashing',
        'solution_summary': 'Create hash map with number -> list index. Iterate over nums. If diff between target and nums[i] is in the hashmap i != indices[i], then solution is [i, indices[i]]',
        'problem_statement': 'Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.\n\nYou may assume that every input has exactly one pair of indices i and j that satisfy the condition.\n\nReturn the answer with the smaller index first. ',
        'level': 'easy',
    },
    'Group Anagrams': {
        'category': 'arrays_hashing',
        'problem_statement': 'Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.\n\nAn anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.',
        'solution_summary': 'Create hasmap tuple -> list. One entry per anagram. For each string, create a length 26 array of counts of letters. Convert to tuple. If tuple already exists in hashmap, add to list. Otherwise, add to hashamp with list containing current word.',
        'level': 'medium',
    },
    'Top K Frequent Elements': {
        'category': 'arrays_hashing',
        'problem_statement': 'Given an integer array nums and an integer k, return the k most frequent elements within the array.\n\nThe test cases are generated such that the answer is always unique.\n\nYou may return the output in any order.',
        'solution_summary': 'Group numbers into buckets based on frequency, using 2D array. Iterate backwards through array to start with highest freq bucket. Add numbers in order until the length of result equals k',
        'level': 'medium',
    },
    'Encode and Decode Strings': {
        'category': 'arrays_hashing',
        'problem_statement': 'Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.\n\nPlease implement encode and decode',
        'solution_summary': 'We can use an encoding approach where we start with a number representing the length of the string, followed by a separator character (let\'s use # for simplicity), and then the string itself. To decode, we read the number until we reach a #, then use that number to read the specified number of characters as the string.',
        'level': 'medium',
    },
    'Product of Array Except Self': {
        'category': 'arrays_hashing',
        'problem_statement': 'Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].\n\nEach product is guaranteed to fit in a 32-bit integer.\n\nFollow-up: Could you solve it in O(n)O(n) time without using the division operation?',
        'solution_summary': 'Use prefix/suffix arrays. Prefix[i] is the product of all nums to left, suffix[i] is the product of all nums to right. Result is element-wise multiplication of prefix and suffix.',
        'level': 'medium',
    },
    'Valid Sudoku': {
        'category': 'arrays_hashing',
        'problem_statement': 'You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:\n\n    Each row must contain the digits 1-9 without duplicates.\n    Each column must contain the digits 1-9 without duplicates.\n    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.\n\nReturn true if the Sudoku board is valid, otherwise return false.\n\nNote: A board does not need to be full or be solvable to be valid.',
        'solution_summary': 'Scan every element in matrix. Use hashmaps of sets to track the values in each row, col, and square.',
        'level': 'medium',
    },
    'Longest Consecutive Sequence': {
        'category': 'arrays_hashing',
        'problem_statement': 'Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.\n\nA consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.\n\nYou must write an algorithm that runs in O(n) time.',
        'solution_summary': 'Put all nums in a hash set. For each number in set, if num - 1 is in the hashset, continue. Otherwise, check for streak by incrementing curNum by 1 and checking if it\'s in the hash set.',
        'level': 'medium',
    },

    # two pointers
    'Valid Palindrome': {
        'category': 'two_pointers',
        'problem_statement': 'Given a string s, return true if it is a palindrome, otherwise return false.\n\nA palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.\n\nNote: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).',
        'solution_summary': 'Create left and right pointers. Shift each pointer to next alphanumeric character. If there is a mismatch, return false. If you make it all the way through the string, return true.',
        'level': 'easy',
    },
    'Two Sum II Input Array Is Sorted': {
        'category': 'two_pointers',
        'problem_statement': 'Given an array of integers numbers that is sorted in non-decreasing order.\n\nReturn the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.\n\nThere will always be exactly one valid solution.\n\nYour solution must use O(1)O(1) additional space.',
        'solution_summary': 'Start with left = 0, right = len(nums) - 1. While loop on left < right. Each iteration, get current sum. If sum > target, decrement right. Is sum < target, increment left. If sum == target, return [left, right]. If loop exits without match, return []',
        'level': 'medium',
    },
    '3Sum': {
        'category': 'two_pointers',
        'problem_statement': 'Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.\n\nThe output should not contain any duplicate triplets. You may return the output and the triplets in any order.',
        'solution_summary': 'Sort nums. Loop over nums. If a > 0, break loop, because we won\'t encounter any more negative numbers to add to zero. If current number is same as previous number, continue loop, because we are not supposed to have duplicates. Then problem basically becomes 2Sum II for each (i, a) pair, and target is always 0. Also need to update left & right after match is found, because there can be multiple solutions, unlike 2Sum.',
        'level': 'medium',
    },
    'Container With Most Water': {
        'category': 'two_pointers',
        'problem_statement': 'You are given an integer array heights where heights[i] represents the height of the ithith bar.\n\nYou may choose any two bars to form a container. Return the maximum amount of water a container can store.',
        'solution_summary': 'Start with l/r pointers at each end of array. While l < r, calculate area as min(h[l], h[r]) * (r - l). Store as max if greater than current result. Move whichever pointer has the smaller height.',
        'level': 'medium',
    },
    'Trapping Rain Water': {
        'category': 'two_pointers',
        'problem_statement': 'You are given an array of non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.\n\nReturn the maximum area of water that can be trapped between the bars.',
        'solution_summary': 'Start with l/r pointers at each end of array. leftMax and rightMax track highest values seen from l/r, initialize with end values. While l < r, if leftMax < rightMax - move l += 1, update leftMax, result += leftMax - current height. Otherwise, do same for right.',
        'level': 'hard',
    },

    # sliding window
    'Best Time to Buy And Sell Stock': {
        'category': 'sliding_window',
        'problem_statement': 'You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.\n\nYou may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.\n\nReturn the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.',
        'solution_summary': 'Start with l = 0, r = 1. Move r forward every iteration until the end of array. At every iteration, if there is a profit from prices[l] to prices[r], update maxProfit. Otherwise, move l up to r position.',
        'level': 'easy',
    },
    'Longest Substring Without Repeating Characters': {
        'category': 'sliding_window',
        'problem_statement': 'Given a string s, find the length of the longest substring without duplicate characters.\n\nA substring is a contiguous sequence of characters within a string.',
        'solution_summary': 'Start with l = 0, r = 0. Increment r once per iteration. Use hashset to keep track of characters in current window. If s[r] is already in set, move l forward until character is removed from set. Then add s[r] and update maxLen with r - l + 1.',
        'level': 'medium',
    },
    'Longest Repeating Character Replacement': {
        'category': 'sliding_window',
        'problem_statement': 'You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.\n\nAfter performing at most k replacements, return the length of the longest substring which contains only one distinct character.',
        'solution_summary': '',
        'level': 'medium',
    },
    'Permutation In String': {
        'category': 'sliding_window',
    },
    'Minimum Window Substring': {
        'category': 'sliding_window',
    },
    'Sliding Window Maximum': {
        'category': 'sliding_window',
    },

    # stack
    'Valid Parentheses': {
        'category': 'stack',
    },
    'Min Stack': {
        'category': 'stack',
    },
    'Evaluate Reverse Polish Notation': {
        'category': 'stack',
    },
    'Daily Temperatures': {
        'category': 'stack',
    },
    'Car Fleet': {
        'category': 'stack',
    },
    'Largest Rectangle In Histogram': {
        'category': 'stack',
        'problem_statement': 'You are given an array of integers heights where heights[i] represents the height of a bar. The width of each bar is 1.\n\nReturn the area of the largest rectangle that can be formed among the bars.\n\nNote: This chart is known as a histogram.',
        'solution_summary': '',
        'level': 'hard',
    },

    # binary search
    'Binary Search': {
        'category': 'binary_search',
    },
    'Search a 2D Matrix': {
        'category': 'binary_search',
    },
    'Koko Eating Bananas': {
        'category': 'binary_search',
    },
    'Find Minimum In Rotated Sorted Array': {
        'category': 'binary_search',
    },
    'Search In Rotated Sorted Array': {
        'category': 'binary_search',
    },
    'Time Based Key Value Store': {
        'category': 'binary_search',
    },
    'Median of Two Sorted Arrays': {
        'category': 'binary_search',
    },

    # linked list
    'Reverse Linked List': {
        'category': 'linked_list',
        'problem_statement': 'Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.',
        'solution_summary': 'Start with cur = head, prev = None. While cur, nxt = cur.next; cur.next = prev; prev = cur; cur = nxt. Return prev.',
        'level': 'easy',
    },
    'Merge Two Sorted Lists': {
        'category': 'linked_list',
    },
    'Linked List Cycle': {
        'category': 'linked_list',
    },
    'Reorder List': {
        'category': 'linked_list',
    },
    'Remove Nth Node From End of List': {
        'category': 'linked_list',
    },
    'Copy List With Random Pointer': {
        'category': 'linked_list',
    },
    'Add Two Numbers': {
        'category': 'linked_list',
    },
    'Find The Duplicate Number': {
        'category': 'linked_list',
    },
    'LRU Cache': {
        'category': 'linked_list',
    },
    'Merge K Sorted Lists': {
        'category': 'linked_list',
    },
    'Reverse Nodes In K Group': {
        'category': 'linked_list',
    },

    # trees
    'Invert Binary Tree': {
        'category': 'trees',
    },
    'Maximum Depth of Binary Tree': {
        'category': 'trees',
    },
    'Diameter of Binary Tree': {
        'category': 'trees',
    },
    'Balanced Binary Tree': {
        'category': 'trees',
    },
    'Same Tree': {
        'category': 'trees',
    },
    'Subtree of Another Tree': {
        'category': 'trees',
    },
    'Lowest Common Ancestor of a Binary Search Tree': {
        'category': 'trees',
        'problem_statement': 'Given a binary search tree (BST) where all node values are unique, and two nodes from the tree p and q, return the lowest common ancestor (LCA) of the two nodes.\n\nThe lowest common ancestor between two nodes p and q is the lowest node in a tree T such that both p and q as descendants. The ancestor is allowed to be a descendant of itself.',
        'solution_summary': 'DFS(root, p, q). If root, p, or q are null, return null. If p and q are both less than root, search left. If p and q are both greater than root, search right. Otherwise, root must be common ancestor',
        'level': 'medium',
    },
    'Binary Tree Level Order Traversal': {
        'category': 'trees',
    },
    'Binary Tree Right Side View': {
        'category': 'trees',
    },
    'Count Good Nodes In Binary Tree': {
        'category': 'trees',
    },
    'Validate Binary Search Tree': {
        'category': 'trees',
    },
    'Kth Smallest Element In a Bst': {
        'category': 'trees',
    },
    'Construct Binary Tree From Preorder And Inorder Traversal': {
        'category': 'trees',
    },
    'Binary Tree Maximum Path Sum': {
        'category': 'trees',
    },
    'Serialize And Deserialize Binary Tree': {
        'category': 'trees',
    },

    # heap
    'Kth Largest Element In a Stream': {
        'category': 'heap',
    },
    'Last Stone Weight': {
        'category': 'heap',
    },
    'K Closest Points to Origin': {
        'category': 'heap',
    },
    'Kth Largest Element In An Array': {
        'category': 'heap',
    },
    'Task Scheduler': {
        'category': 'heap',
    },
    'Design Twitter': {
        'category': 'heap',
    },
    'Find Median From Data Stream': {
        'category': 'heap',
    },
    
    # backtracking
    'Subsets': {
        'category': 'backtracking',
        'problem_statement': 'Given an array nums of unique integers, return all possible subsets of nums.\n\nThe solution set must not contain duplicate subsets. You may return the solution in any order.',
        'solution_summary': 'DFS(curIndex). If curIndex >= len(nums), add copy of current subset list to result. Otherwise, add nums[curIndex] to subset and call DFS(curIndex + 1), then pop from nums and call DFS(curIndex + 1) again.',
        'level': 'medium',
    },
    'Combination Sum': {
        'category': 'backtracking',
        'problem_statement': 'You are given an array of distinct integers nums and a target integer target. Your task is to return a list of all unique combinations of nums where the chosen numbers sum to target.\n\nThe same number may be chosen from nums an unlimited number of times. Two combinations are the same if the frequency of each of the chosen numbers is the same, otherwise they are different.\n\nYou may return the combinations in any order and the order of the numbers in each combination can be in any order.',
        'solution_summary': 'DFS(idx, cur, total). Use list for result set. Base case - If total == target, add copy of cur to result set and return. If idx >= len(nums) or total > target, return. Add nums[idx] to cur and call DFS(idx, cur, total + nums[idx]) (include current index). Then cur.pop() and call DFS(idx + 1, cur, total) (exclude current index)',
        'level': 'medium',
    },
    'Combination Sum II': {
        'category': 'backtracking',
        'problem_statement': 'You are given an array of integers candidates, which may contain duplicates, and a target integer target. Your task is to return a list of all unique combinations of candidates where the chosen numbers sum to target.\n\nEach element from candidates may be chosen at most once within a combination. The solution set must not contain duplicate combinations.\n\nYou may return the combinations in any order and the order of the numbers in each combination can be in any order.',
        'solution_summary': 'DFS(idx, cur, total). Use hashset for result set. Base case - If total == target, add copy of cur to result set and return. If total > target or idx >= len(candidates), return. Add nums[idx] to cur and call DFS(idx, cur, total + candidates[idx]) (include current candidate). Then cur.pop() and can to next candidate that is not equal to the following candidate. Then call DFS(idx + 1, cur, total) (exlcude current candidate).',
        'level': 'medium',
    },
    'Permutations': {
        'category': 'backtracking',
        'problem_statement': 'Given an array nums of unique integers, return all the possible permutations. You may return the answer in any order.',
        'solution_summary': 'DFS(perm, pick). Base case - If len(perm) == len(nums), we have constructed a permutation; add perm.copy() to result set and return. Otherwise, for each index in nums: if picks[i] is False, then perm.append(nums[i]), picks[i] = True, and backtrack(perm, pick). After backtrack, perm.pop and set pick[i] = False again. Return result set',
        'level': 'medium',
    },
    'Subsets II': {
        'category': 'backtracking',
        'problem_statement': 'You are given an array nums of integers, which may contain duplicates. Return all possible subsets.\n\nThe solution must not contain duplicate subsets. You may return the solution in any order.',
        'solution_summary': 'DFS(i, subset). Base case - If i == len(nums), we have reached end of nums; add subset.copy() to result set and return. Otherwise, backtrack including current element: subset.append(nums[i]) -> backtrack(i, subset). Then backtrack excluding current element: subset.pop; iterate to next unique value, call backtrack(i + 1, subset). Return result set',
        'level': 'medium',
    },
    'Generate Parentheses': {
        'category': 'backtracking',
        'problem_statement': 'You are given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.',
        'solution_summary': 'DFS(openN, closedN). Base case - If openN == closedN == n, we have found a solution; append to result list and return. If openN < n, then we try another ( -> push ( onto stack, call backtrack(openN + 1, closedN), and pop stack. If closedN < openN, then we try another ) -> push ) onto stack, call backtrack(openN, closedN + 1), and pop stack. Return result list',
        'level': 'medium',
    },
    'Word Search': {
        'category': 'backtracking',
        'problem_statement': 'Given a 2-D grid of characters board and a string word, return true if the word is present in the grid, otherwise return false.\n\nFor the word to be present it must be possible to form it with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.',
        'solution_summary': 'DFS(idx, row, col). Base case -  if idx reaches end of word, return true. Use visited array. Check neighboring cells. Make sure to unset visited[row][col] after recursive calls.',
        'level': 'medium',
    },
    'Palindrome Partitioning': {
        'category': 'backtracking',
        'problem_statement': 'Given a string s, split s into substrings where every substring is a palindrome. Return all possible lists of palindromic substrings.\n\nYou may return the solution in any order.',
        'solution_summary': 'DFS(i), where i is index in string. Base case - when i >= len(s), append current part to result. Otherwise, loop over j in range(i, len(s)) and at each iteration if isPali, append s[i : j + 1] to part, dfs(j + 1), and s.pop()',
        'level': 'medium',
    },
    'Letter Combinations of a Phone Number': {
        'category': 'backtracking',
        'problem_statement': 'You are given a string digits made up of digits from 2 through 9 inclusive.\n\nEach digit (not including 1) is mapped to a set of characters as shown below:\n\nA digit could represent any one of the characters it maps to.\n\nReturn all possible letter combinations that digits could represent. You may return the answer in any order.',
        'solution_summary': 'DFS(word), where word is a char array. Base case - if len(word) == len(digits), add word to results and return. Otherwise, get letters for current digit. For each letter, add letter to char array, dfs, and pop char array',
        'level': 'medium',
    },
    'N Queens': {
        'category': 'backtracking',
        'problem_statement': 'The n-queens puzzle is the problem of placing n queens on an n x n chessboard so that no two queens can attack each other.\n\nA queen in a chessboard can attack horizontally, vertically, and diagonally.\n\nGiven an integer n, return all distinct solutions to the n-queens puzzle.\n\nEach solution contains a unique board layout where the queen pieces are placed. 'Q' indicates a queen and '.' indicates an empty space.\n\nYou may return the answer in any order.',
        'solution_summary': 'DFS(row). Base case - if row == n, it means we\'ve place a queen in each row and have found a solution. Otherwise, iterate throuch each column. If we have already blocked the current column, the positive diagonal (row + col) or the negative diagonal (row - col), then skip. Otherwise, mark col, pos diagonal, and neg diagonal as blocked, and DFS(row + 1)',
        'level': 'hard',
    },

    # tries
    'Implement Trie Prefix Tree': {
        'category': 'tries',
    },
    'Design Add And Search Words Data Structure': {
        'category': 'tries',
    },
    'Word Search II': {
        'category': 'tries',
    },

    # graphs
    'Number of Islands': {
        'category': 'graphs',
    },
    'Max Area of Island': {
        'category': 'graphs',
    },
    'Clone Graph': {
        'category': 'graphs',
    },
    'Walls And Gates': {
        'category': 'graphs',
    },
    'Rotting Oranges': {
        'category': 'graphs',
    },
    'Pacific Atlantic Water Flow': {
        'category': 'graphs',
    },
    'Surrounded Regions': {
        'category': 'graphs',
    },
    'Course Schedule': {
        'category': 'graphs',
    },
    'Course Schedule II': {
        'category': 'graphs',
    },
    'Graph Valid Tree': {
        'category': 'graphs',
    },
    'Number of Connected Components In An Undirected Graph': {
        'category': 'graphs',
    },
    'Redundant Connection': {
        'category': 'graphs',
    },
    'Word Ladder': {
        'category': 'graphs',
    },

    # advanced graphs
    'Network Delay Time': {
        'category': 'graphs',
    },
    'Reconstruct Itinerary': {
        'category': 'graphs',
    },
    'Min Cost to Connect All Points': {
        'category': 'graphs',
    },
    'Swim In Rising Water': {
        'category': 'graphs',
    },
    'Alien Dictionary': {
        'category': 'graphs',
    },
    'Cheapest Flights Within K Stops': {
        'category': 'graphs',
    },

    # 1D dynamic programming
    'Climbing Stairs': {
        'category': 'dynamic_programming',
        'problem_statement': 'You are given an integer n representing the number of steps to reach the top of a staircase. You can climb with either 1 or 2 steps at a time.\n\nReturn the number of distinct ways to climb to the top of the staircase.',
        'solution_summary': 'Base case - If 0 stairs remain, return 1. If less than 0 stairs remain, return 0. Otherwise, dfs(rem - 1) + dfs(rem - 2). Cache with rem as key',
        'level': 'easy',
    },
    'Min Cost Climbing Stairs': {
        'category': 'dynamic_programming',
        'problem_statement': 'You are given an array of integers cost where cost[i] is the cost of taking a step from the ith floor of a staircase. After paying the cost, you can step to either the (i + 1)th floor or the (i + 2)th floor.\n\nYou may choose to start at the index 0 or the index 1 floor.\n\nReturn the minimum cost to reach the top of the staircase, i.e. just past the last index in cost.',
        'solution_summary': 'DFS(stair). Base case - If 0 or fewer stairs remain, return 0 (i.e. if we are past the end of the array). Otherwise, return cost[stair] + min(dfs(stair + 1), dfs(stair + 2)). Cache result for each value of stair. Initialize with min(dfs(0), dfs(1))',
        'level': 'easy',
    },
    'House Robber': {
        'category': 'dynamic_programming',
        'problem_statement': 'You are given an integer array nums where nums[i] represents the amount of money the ith house has. The houses are arranged in a straight line, i.e. the ith house is the neighbor of the (i-1)th and (i+1)th house.\n\nYou are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system will automatically alert the police if two adjacent houses were both broken into.\n\nReturn the maximum amount of money you can rob without alerting the police.',
        'solution_summary': 'DFS(house). Base case - If 0 or fewer houses remain, return 0 (i.e. if we are past the end of the array). Otherwise, return nums[house] + max(dfs(house + 2), dfs(house + 3)). Cache result for each house. Initialize with max(dfs(0), dfs(1))',
        'level': 'medium',
    },
    'House Robber II': {
        'category': 'dynamic_programming',
        'problem_statement': 'You are given an integer array nums where nums[i] represents the amount of money the ith house has. The houses are arranged in a circle, i.e. the first house and the last house are neighbors.\n\nYou are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system will automatically alert the police if two adjacent houses were both broken into.\n\nReturn the maximum amount of money you can rob without alerting the police.',
    },
    'Longest Palindromic Substring': {
        'category': 'dynamic_programming',
    },
    'Palindromic Substrings': {
        'category': 'dynamic_programming',
    },
    'Decode Ways': {
        'category': 'dynamic_programming',
        'problem_statement': 'A string consisting of uppercase english characters can be encoded to a number using the following mapping:\n\n\t'A' -> "1"\n\t'B' -> "2"\n\t...\n\t'Z' -> "26"\n\nTo decode a message, digits must be grouped and then mapped back into letters using the reverse of the mapping above. There may be multiple ways to decode a message. For example, "1012" can be mapped into:\n\n\t"JAB" with the grouping (10 1 2)\n\t"JL" with the grouping (10 12)\n\nThe grouping (1 01 2) is invalid because 01 cannot be mapped into a letter since it contains a leading zero.\n\nGiven a string s containing only digits, return the number of ways to decode it. You can assume that the answer fits in a 32-bit integer.',
        'solution_summary': 'DFS(i). Base case - if i == len(s) (reached end of string), return 1. If s[i] == \'0\', then string is invalid -> return 0. Otherwise, dfs(i + 1). If not at end of array and s[i] == 1 or s[i] == 2 and s[i + 1] < 7, then dfs(i + 2). Cache on i',
        'level': 'medium',
    },
    'Coin Change': {
        'category': 'dynamic_programming',
        'problem_statement': 'You are given an integer array coins representing coins of different denominations (e.g. 1 dollar, 5 dollars, etc) and an integer amount representing a target amount of money.\n\nReturn the fewest number of coins that you need to make up the exact target amount. If it is impossible to make up the amount, return -1.\n\nYou may assume that you have an unlimited number of each coin.',
        'solution_summary': 'DFS(remaining). Base case - if remaining == 0 return 0. For each coin, if remaining - coin_value > 0, result = min(result, 1 + dfs(remaining - coin_value)',
        'level': 'medium',
    },
    'Maximum Product Subarray': {
        'category': 'dynamic_programming',
    },
    'Word Break': {
        'category': 'dynamic_programming',
    },
    'Longest Increasing Subsequence': {
        'category': 'dynamic_programming',
    },
    'Partition Equal Subset Sum': {
        'category': 'dynamic_programming',
    },

    # 2D dynamic programming
    'Unique Paths': {
        'category': 'dynamic_programming',
    },
    'Longest Common Subsequence': {
        'category': 'dynamic_programming',
    },
    'Best Time to Buy And Sell Stock With Cooldown': {
        'category': 'dynamic_programming',
    },
    'Coin Change II': {
        'category': 'dynamic_programming',
    },
    'Target Sum': {
        'category': 'dynamic_programming',
    },
    'Interleaving String': {
        'category': 'dynamic_programming',
    },
    'Longest Increasing Path In a Matrix': {
        'category': 'dynamic_programming',
    },
    'Distinct Subsequences': {
        'category': 'dynamic_programming',
    },
    'Edit Distance': {
        'category': 'dynamic_programming',
    },
    'Burst Balloons': {
        'category': 'dynamic_programming',
    },
    'Regular Expression Matching': {
        'category': 'dynamic_programming',
    },

    # greedy
    'Maximum Subarray': {
        'category': 'greedy',
    },
    'Jump Game': {
        'category': 'greedy',
    },
    'Jump Game II': {
        'category': 'greedy',
    },
    'Gas Station': {
        'category': 'greedy',
    },
    'Hand of Straights': {
        'category': 'greedy',
    },
    'Merge Triplets to Form Target Triplet': {
        'category': 'greedy',
    },
    'Partition Labels': {
        'category': 'greedy',
    },
    'Valid Parenthesis String': {
        'category': 'greedy',
    },

    # intervals
    'Insert Interval': {
        'category': 'intervals',
    },
    'Merge Intervals': {
        'category': 'intervals',
    },
    'Non Overlapping Intervals': {
        'category': 'intervals',
    },
    'Meeting Rooms': {
        'category': 'intervals',
    },
    'Meeting Rooms II': {
        'category': 'intervals',
    },
    'Minimum Interval to Include Each Query': {
        'category': 'intervals',
    },

    # math & geometry
    'Rotate Image': {
        'category': 'math',
    },
    'Spiral Matrix': {
        'category': 'math',
    },
    'Set Matrix Zeroes': {
        'category': 'math',
    },
    'Happy Number': {
        'category': 'math',
    },
    'Plus One': {
        'category': 'math',
    },
    'Pow(x, n)': {
        'category': 'math',
    },
    'Multiply Strings': {
        'category': 'math',
    },
    'Detect Squares': {
        'category': 'math',
    },

    # bit manipulation
    'Single Number': {
        'category': 'bits',
        'problem_statement': 'You are given a non-empty array of integers nums. Every integer appears twice except for one.\n\nReturn the integer that appears only once.\n\nYou must implement a solution with O(n)O(n) runtime complexity and use only O(1)O(1) extra space.',
        'solution_summary': 'Iterate through list and bitwise XOR all the numbers together. The result will be the single number.',
        'level': 'easy',
    },
    'Number of 1 Bits': {
        'category': 'bits',
        'problem_statement': 'You are given an unsigned integer n. Return the number of 1 bits in its binary representation.\n\nYou may assume n is a non-negative integer which fits within 32-bits.',
        'solution_summary': '',
        'level': 'easy',
    },
    'Counting Bits': {
        'category': 'bits',
    },
    'Reverse Bits': {
        'category': 'bits',
    },
    'Missing Number': {
        'category': 'bits',
    },
    'Sum of Two Integers': {
        'category': 'bits',
    },
    'Reverse Integer': {
        'category': 'bits',
    },
}

CATEGORIES = {
    'a': 'Arrays & Hashing',
    'b': 'Two Pointers',
    'c': 'Sliding Window',
}

def quiz(incorrect_questions=set()):
    click.echo("Welcome to Algo Quiz")
    print('incorrect_questions=' + str(incorrect_questions))
    num_questions = 0
    num_correct = 0
    questions = list(incorrect_questions if incorrect_questions else PROBLEM_TO_CATEGORY.keys())
    random.shuffle(questions)
    # print('questions ===')
    # print(questions)
    click.secho('Ready to answer ' + str(len(questions)) + ' questions')
    incorrect = set()
    for question in questions:
        category = PROBLEM_TO_CATEGORY[question]['category']
        problem_statement = PROBLEM_TO_CATEGORY[question]['problem_statement'] if 'problem_statement' in PROBLEM_TO_CATEGORY[question] else None
        click.secho('\n=============================================\n', fg='cyan')
        click.echo('Question: ' + question)
        if problem_statement:
            click.secho('\n' + problem_statement + '\n', fg='magenta')
        num_questions += 1
        # click.echo('Choose a problem category:')
        # choices = []
        # for k in CATEGORIES:
            # choices.append('(' + k + ') ' + CATEGORIES[k])
        # click.echo('\t'.join(choices))
        user_choice = click.prompt('Your choice')
        # user_choice = None
        # while user_choice not in CATEGORIES:
        #     user_choice = click.prompt('Your choice')
        #     if user_choice in CATEGORIES:
        #         break
        #     click.secho('ERROR: invalid choice ' + user_choice, fg='red')
            
        # if CATEGORIES[user_choice] == category:
        if user_choice == category:
            num_correct += 1
            click.secho('Correct!', fg='green', bold=True)
        else:
            incorrect.add(question)
            click.secho('Incorrect - correct answer was ' + category, fg='red')
        click.prompt('\nGuess solution')
        solution_summary = PROBLEM_TO_CATEGORY[question]['solution_summary'] if 'solution_summary' in PROBLEM_TO_CATEGORY[question] else 'No solution summary provided'
        click.secho('Solution summary: ' + solution_summary)

    click.secho('\n\nQuiz Complete!')
    click.secho('Correct answers: ' + str(num_correct) + ' / ' + str(num_questions) + ' (' + str(round(float(num_correct) / num_questions * 100.0)) + '%)')
    click.secho('Try again?')
    click.secho('(a) No (b) Incorrect questions (c) All questions')
    try_again_choice = click.prompt('Your choice')
    if try_again_choice == 'b':
        print('trying again with incorrect: ' + str(incorrect))
        quiz(incorrect)
        return
    elif try_again_choice == 'c':
        quiz()
        return
    else:
        click.secho('Bye!')
        return


            


if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], "t:", ["problem_types="])
    problem_types = []
    for o, v in opts:
        if o == '--problem_types':
            problem_types = v.split(',')
    problems = set()
    for k in PROBLEM_TO_CATEGORY:
        problem = PROBLEM_TO_CATEGORY[k]
        if 'category' in problem and problem['category'] in problem_types:
            problems.add(k)
    
    quiz(problems)
