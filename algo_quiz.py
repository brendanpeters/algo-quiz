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
    },
    'Longest Substring Without Repeating Characters': {
        'category': 'sliding_window',
    },
    'Longest Repeating Character Replacement': {
        'category': 'sliding_window',
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
    },
    'Combination Sum': {
        'category': 'backtracking',
    },
    'Combination Sum II': {
        'category': 'backtracking',
    },
    'Permutations': {
        'category': 'backtracking',
    },
    'Subsets II': {
        'category': 'backtracking',
    },
    'Generate Parentheses': {
        'category': 'backtracking',
    },
    'Word Search': {
        'category': 'backtracking',
    },
    'Palindrome Partitioning': {
        'category': 'backtracking',
    },
    'Letter Combinations of a Phone Number': {
        'category': 'backtracking',
    },
    'N Queens': {
        'category': 'backtracking',
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
    },
    'Min Cost Climbing Stairs': {
        'category': 'dynamic_programming',
    },
    'House Robber': {
        'category': 'dynamic_programming',
    },
    'House Robber II': {
        'category': 'dynamic_programming',
    },
    'Longest Palindromic Substring': {
        'category': 'dynamic_programming',
    },
    'Palindromic Substrings': {
        'category': 'dynamic_programming',
    },
    'Decode Ways': {
        'category': 'dynamic_programming',
    },
    'Coin Change': {
        'category': 'dynamic_programming',
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
    },
    'Number of 1 Bits': {
        'category': 'bits',
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
