import click
import random

MAP = {
    'a': 1,
    'b': 2,
    'c': 3,
}

PROBLEM_TO_CATEGORY = {
    # arrays & hashing
    'Contains Duplicate': 'arrays_hashing',
    'Valid Anagram': 'arrays_hashing',
    'Two Sum': 'arrays_hashing',
    'Group Anagrams': 'arrays_hashing',
    'Top K Frequent Elements': 'arrays_hashing',
    'Encode and Decode Strings': 'arrays_hashing',
    'Product of Array Except Self': 'arrays_hashing',
    'Valid Sudoku': 'arrays_hashing',
    'Longest Consecutive Sequence': 'arrays_hashing',

    # two pointers
    'Valid Palindrome': 'two_pointers',
    'Two Sum II Input Array Is Sorted': 'two_pointers',
    '3Sum': 'two_pointers',
    'Container With Most Water': 'two_pointers',
    'Trapping Rain Water': 'two_pointers',

    # sliding window
    'Best Time to Buy And Sell Stock': 'sliding_window',
    'Longest Substring Without Repeating Characters': 'sliding_window',
    'Longest Repeating Character Replacement': 'sliding_window',
    'Permutation In String': 'sliding_window',
    'Minimum Window Substring': 'sliding_window',
    'Sliding Window Maximum': 'sliding_window',

    # stack
    'Valid Parentheses': 'stack',
    'Min Stack': 'stack',
    'Evaluate Reverse Polish Notation': 'stack',
    'Daily Temperatures': 'stack',
    'Car Fleet': 'stack',
    'Largest Rectangle In Histogram': 'stack',

    # binary search
    'Binary Search': 'binary_search',
    'Search a 2D Matrix': 'binary_search',
    'Koko Eating Bananas': 'binary_search',
    'Find Minimum In Rotated Sorted Array': 'binary_search',
    'Search In Rotated Sorted Array': 'binary_search',
    'Time Based Key Value Store': 'binary_search',
    'Median of Two Sorted Arrays': 'binary_search',

    # linked list
    'Reverse Linked List': 'linked_list',
    'Merge Two Sorted Lists': 'linked_list',
    'Linked List Cycle': 'linked_list',
    'Reorder List': 'linked_list',
    'Remove Nth Node From End of List': 'linked_list',
    'Copy List With Random Pointer': 'linked_list',
    'Add Two Numbers': 'linked_list',
    'Find The Duplicate Number': 'linked_list',
    'LRU Cache': 'linked_list',
    'Merge K Sorted Lists': 'linked_list',
    'Reverse Nodes In K Group': 'linked_list',

    # trees
    'Invert Binary Tree': 'trees',
    'Maximum Depth of Binary Tree': 'trees',
    'Diameter of Binary Tree': 'trees',
    'Balanced Binary Tree': 'trees',
    'Same Tree': 'trees',
    'Subtree of Another Tree': 'trees',
    'Lowest Common Ancestor of a Binary Search Tree': 'trees',
    'Binary Tree Level Order Traversal': 'trees',
    'Binary Tree Right Side View': 'trees',
    'Count Good Nodes In Binary Tree': 'trees',
    'Validate Binary Search Tree': 'trees',
    'Kth Smallest Element In a Bst': 'trees',
    'Construct Binary Tree From Preorder And Inorder Traversal': 'trees',
    'Binary Tree Maximum Path Sum': 'trees',
    'Serialize And Deserialize Binary Tree': 'trees',

    # heap
    'Kth Largest Element In a Stream': 'heap',
    'Last Stone Weight': 'heap',
    'K Closest Points to Origin': 'heap',
    'Kth Largest Element In An Array': 'heap',
    'Task Scheduler': 'heap',
    'Design Twitter': 'heap',
    'Find Median From Data Stream': 'heap',
    
    # backtracking
    'Subsets': 'backtracking',
    'Combination Sum': 'backtracking',
    'Combination Sum II': 'backtracking',
    'Permutations': 'backtracking',
    'Subsets II': 'backtracking',
    'Generate Parentheses': 'backtracking',
    'Word Search': 'backtracking',
    'Palindrome Partitioning': 'backtracking',
    'Letter Combinations of a Phone Number': 'backtracking',
    'N Queens': 'backtracking',

    # tries
    'Implement Trie Prefix Tree': 'tries',
    'Design Add And Search Words Data Structure': 'tries',
    'Word Search II': 'tries',

    # graphs
    'Number of Islands': 'graphs',
    'Max Area of Island': 'graphs',
    'Clone Graph': 'graphs',
    'Walls And Gates': 'graphs',
    'Rotting Oranges': 'graphs',
    'Pacific Atlantic Water Flow': 'graphs',
    'Surrounded Regions': 'graphs',
    'Course Schedule': 'graphs',
    'Course Schedule II': 'graphs',
    'Graph Valid Tree': 'graphs',
    'Number of Connected Components In An Undirected Graph': 'graphs',
    'Redundant Connection': 'graphs',
    'Word Ladder': 'graphs',

    # advanced graphs
    'Network Delay Time': 'graphs',
    'Reconstruct Itinerary': 'graphs',
    'Min Cost to Connect All Points': 'graphs',
    'Swim In Rising Water': 'graphs',
    'Alien Dictionary': 'graphs',
    'Cheapest Flights Within K Stops': 'graphs',

    # 1D dynamic programming
    'Climbing Stairs': 'dynamic_programming',
    'Min Cost Climbing Stairs': 'dynamic_programming',
    'House Robber': 'dynamic_programming',
    'House Robber II': 'dynamic_programming',
    'Longest Palindromic Substring': 'dynamic_programming',
    'Palindromic Substrings': 'dynamic_programming',
    'Decode Ways': 'dynamic_programming',
    'Coin Change': 'dynamic_programming',
    'Maximum Product Subarray': 'dynamic_programming',
    'Word Break': 'dynamic_programming',
    'Longest Increasing Subsequence': 'dynamic_programming',
    'Partition Equal Subset Sum': 'dynamic_programming',

    # 2D dynamic programming
    'Unique Paths': 'dynamic_programming',
    'Longest Common Subsequence': 'dynamic_programming',
    'Best Time to Buy And Sell Stock With Cooldown': 'dynamic_programming',
    'Coin Change II': 'dynamic_programming',
    'Target Sum': 'dynamic_programming',
    'Interleaving String': 'dynamic_programming',
    'Longest Increasing Path In a Matrix': 'dynamic_programming',
    'Distinct Subsequences': 'dynamic_programming',
    'Edit Distance': 'dynamic_programming',
    'Burst Balloons': 'dynamic_programming',
    'Regular Expression Matching': 'dynamic_programming',

    # greedy
    'Maximum Subarray': 'greedy',
    'Jump Game': 'greedy',
    'Jump Game II': 'greedy',
    'Gas Station': 'greedy',
    'Hand of Straights': 'greedy',
    'Merge Triplets to Form Target Triplet': 'greedy',
    'Partition Labels': 'greedy',
    'Valid Parenthesis String': 'greedy',

    # intervals
    'Insert Interval': 'intervals',
    'Merge Intervals': 'intervals',
    'Non Overlapping Intervals': 'intervals',
    'Meeting Rooms': 'intervals',
    'Meeting Rooms II': 'intervals',
    'Minimum Interval to Include Each Query': 'intervals',

    # math & geometry
    'Rotate Image': 'math',
    'Spiral Matrix': 'math',
    'Set Matrix Zeroes': 'math',
    'Happy Number': 'math',
    'Plus One': 'math',
    'Pow(x, n)': 'math',
    'Multiply Strings': 'math',
    'Detect Squares': 'math',

    # bit manipulation
    'Single Number': 'bits',
    'Number of 1 Bits': 'bits',
    'Counting Bits': 'bits',
    'Reverse Bits': 'bits',
    'Missing Number': 'bits',
    'Sum of Two Integers': 'bits',
    'Reverse Integ': 'bits',
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
        category = PROBLEM_TO_CATEGORY[question]
        click.echo('Question: ' + question)
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
    click.secho('Quiz Complete!')
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
