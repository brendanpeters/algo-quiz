import click
import random

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
    },
    'Valid Anagram': {
        'category': 'arrays_hashing',
        'solution_summary': 'Make hash maps to count char frequencies for each string. Return true if sets are equal',
        'problem_statement': 'Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.\n\nAn anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.',
    },
    'Two Sum': {
        'category': 'arrays_hashing',
        'solution_summary': 'Create hash map with number -> list index. Iterate over nums. If diff between target and nums[i] is in the hashmap i != indices[i], then solution is [i, indices[i]]',
        'problem_statement': 'Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.\n\nYou may assume that every input has exactly one pair of indices i and j that satisfy the condition.\n\nReturn the answer with the smaller index first. ',
    },
    'Group Anagrams': {
        'category': 'arrays_hashing',
    },
    'Top K Frequent Elements': {
        'category': 'arrays_hashing',
    },
    'Encode and Decode Strings': {
        'category': 'arrays_hashing',
    },
    'Product of Array Except Self': {
        'category': 'arrays_hashing',
    },
    'Valid Sudoku': {
        'category': 'arrays_hashing',
    },
    'Longest Consecutive Sequence': {
        'category': 'arrays_hashing',
    },

    # two pointers
    'Valid Palindrome': {
        'category': 'two_pointers',
    },
    'Two Sum II Input Array Is Sorted': {
        'category': 'two_pointers',
    },
    '3Sum': {
        'category': 'two_pointers',
    },
    'Container With Most Water': {
        'category': 'two_pointers',
    },
    'Trapping Rain Water': {
        'category': 'two_pointers',
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
    quiz()
