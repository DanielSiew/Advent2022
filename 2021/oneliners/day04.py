print(
  *[
    get_score := lambda nums, board, check, prev_num, final_idx:
      (
        prev_num * sum(num for idx, num in enumerate(board) if check[idx] == False),
        final_idx
      )
        if
          any(
          [
            all(line) for line in
            [check[n * 5:n * 5 + 5] for n in range(5)] +
            [[check[n * 5 + m] for n in range(5)] for m in range(5)]
          ]
          )
        else 
      (
        (None, -1) if len(nums) == 1 else 
        [
          get_score(
            nums[1:], 
            board, 
            (check[:n] + [True] + check[n + 1:] if n != -1 else check), 
            nums[0], 
            final_idx + 1
            ) 
          for n in [board.index(nums[0]) if nums[0] in board else -1] 
        ][0]
      ),
    [f"Part One: {ans[0][0]}\nPart Two: {ans[-1][0]}" for ans in
      [
        *[
          [
            (
              
            ),
            [sorted(
              [i 
                for i in
                  [get_score(numbers, board, [False] * 5 * 5, -1, 0) 
                    for board in boards
                  ]
                if i[1] != -1
              ],
              key=lambda x: x[1]
            )][0]
          ][-1]
          for numbers, boards in
            [
              [
                list(map(int, file[0].split(","))),
                [
                [num
                  for line in board
                  for num in line
                ]
                for board in
                  [
                    [
                      list(map(int, line.split()))
                      for line in
                      [
                        line.strip() for line in board
                      ]
                    ]
                    for board in
                      [ 
                        file[n*5 + 2 + n:n * 5 + 2 + 5 + n]
                        for n in range((len(file) - 2) // 5)
                      ]
                  ]
                ]
              ]
              for file in
                [open("input.txt", "r").readlines()]
            ]
        ]        
      ]
    ]
  ][1]
)

'''
-Part One + Part Two-
  Once again, recursion is used here. Since the prompt is asking for the first one to win (Part One), 
  and the last one to win (Part Two), we can use the same algorithm for both parts.

  I started by parsing the input and turned it into a list of 2 elements: the list of numbers and the
  list of all the boards. For the boards, it is stored as a one-dimensional array (started as 2d but
  figured 1d is much easier to index). The lambda function takes in some arguments: the list of numbers,
  the board itself (list of all the numbers in a board), a "checking" list, which is defaulted as a list
  of length 25 (5 * 5) of 'False's, the previous number (used for final calculation for the board, 0 for
  default), and the final index (the position of the number which won this board, defaulted as 0).

  The function works by first constructing a list of all the rows and columns of the "check" list, then
  checking if any of the lists contains all 'True'. If it is true, it will return a tuple of 2 elements,
  containing the product of previous number (winning number) and the sum of all the remaining unchecked 
  numbers, and the second element containing the final index. If false, it will call itself, thelist of 
  numbers will be passed without the first number, the board remains, the previous number is the first 
  number of the numbers list, and the final index increments by 1. If the board never wins, it returns
  (None, -1).

  The fuction is called for every board, returning a list of all the board scores and their final index.
  Sort the list by their final indices, then print the score of the first element (Part One) and the
  last (for Part Two).
'''