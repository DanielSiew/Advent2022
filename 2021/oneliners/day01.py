print("Part One:", 
  sum(
    (data[n] > data[n-1] 
      for data in 
        [list(map(int, open("input.txt", "r").readlines()))] 
      for n in range(1, len(data))
    )
  )
)

print("Part Two:", 
  sum(
    sum(data[n:n+3]) > sum(data[n-1:n+2]) 
      for data in 
        [list(map(int, open("input.txt", "r").readlines()))]
      for n in range(1, len(data)-2)
    )
  )

'''
-Part One-
  Python is able to treat a "True" boolean value as a 1, which is what I used here to count the total amount of 
  increases. This is pretty straightforward: all it does is comparing every element in the list to the previous.

-Part Two-
  Same as part one, however checks for the sum of groups of 3s instead of individual elements.
'''