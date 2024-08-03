print("Part One:", 
  *[ans[2] * (ans[0] - ans[1]) 
    for ans in 
      [
        [
          sum(i[1] for i in lst if i[0] == condition) 
            for condition in ["down", "up", "forward"]
        ] 
        for lst in 
          [[
              (data.strip().split()[0], int(data.strip().split()[1])) 
                for data in 
                  open("input.txt", "r").readlines()
          ]]
      ]    
  ]
)

print("Part Two:", 
  *[ans[0] * ans[2]
    for ans in
      [[data
        for count, item in enumerate(
          [
              (data.strip().split()[0], int(data.strip().split()[1])) 
                for data in 
                open("input.txt", "r").readlines()
          ])
        for depth in 
          [
            0 
            if count == 0 
            else (
              depth + item[1] * aim if item[0] == "forward"
              else depth
            )
          ]
        for aim in
          [
            (
              item[1] if item[0] == "down"
              else item[1] if item[0] == "up"
              else 0
            ) if count == 0 
            else (
              aim + item[1] if item[0] == "down"
              else aim - item[1] if item[0] == "up"
              else aim
            )
          ]
        for position in
          [
            (
              item[1] if item[0] == "forward"
              else 0
            ) if count == 0 
            else (
              position + item[1] if item[0] == "forward"
              else position
            )
          ]
        for data in [(depth, aim, position)]
    ][-1]]
  ]
)

'''
-Part One-
  I collected all of the same instructions (down, up, forward in that order) and its magnitude (the integer that 
  comes after it) into a list of 3 items, each element representing the sum of the magnitudes of an instruction. 
  The formula for the answer is forward * (down - up).

-Part Two-
  I newly discovered a method to keep a cumulative sum using list comprehension :) Credit goes to Stack 
  Overflow user Kelly Bundy in this thread: https://stackoverflow.com/a/71835053. It is very difficult to explain,
  but it pretty much is just a construction of a cumulative sum list using a for loop disguised as list comprehension.
  A thing to note with this method: Due to the first element of the cumulative sum list being 0, this would mean that
  the size of this list is equal to the size of the data. So, I made modifications to have the first element of the 
  list be the first element in the list. My method introduces repetitive code as the compiler screams at me when I
  try to use a variable without a value (even if it isn't used).

  My solution is very much like the intended solution but converted into a list comprehension. For every instruction,
  update the depth, aim, position accordingly and in the end, multiply the depth and position.
'''