print("Part One:", *[
  sum(
    sum([
      # check if any 2 nums have diff of 0 (same number)
      all(diff)
      # check if diffs are all ascending or descending
      and any(
        [
          # ascending, check if 1 >= x >= 3
          all(
            1 <= x <= 3 for x in diff
          ),
          # descending, check if -3 <= x <= -1
          all(
            -3 <= x <= -1 for x in diff
          )
        ]
      )
      for diff in
        [[lst[i] - lst[i - 1] for i in range(1, len(lst))]]
    ])
    for lst in
      [
        list(map(int, line.strip().split())) 
        for line in open("input.txt", "r").readlines()
      ]
  )
])

print("Part Two:", *[
  sum(
    any([
      all(diff)
      and any(
        [
          all(
            1 <= x <= 3 for x in diff
          ),
          all(
            -3 <= x <= -1 for x in diff
          )
        ]
      )
      for diff in
        [[__lst[i] - __lst[i - 1] for i in range(1, len(__lst))]]
      ][0] 
      for __lst in lst
    )
    for lst in
    [
      # create copies of the list, where every copy removes an element from the original list
      [_lst] +
      [
        _lst[:i] + _lst[i+1:]
        for i in range(len(_lst))
      ]
      for _lst in
        [
          list(map(int, line.strip().split())) 
          for line in open("input.txt", "r").readlines()
        ]
    ]
  
)
])

'''
explanations later
'''