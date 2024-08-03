print("Part One:",
  *[ans[0]*ans[1]
    for ans in
      [
        [
          int("".join(
            [
              j[k] for j in i[n]
            ][0] 
              for n in range(len(i))
          ), 2)
            for k in range(2)
        ]
        for i in
          [[
          [(str(count.index(max(count))), str(1 - count.index(max(count))))
            for count in
              [[digit.count("0"), digit.count("1")]]
          ]
          for digit in
            [
              [
                item[j][i] 
                  for j in range(len(item))
              ]
                for item in
                  [[
                    i.strip() 
                      for i in 
                        open("input.txt", "r").readlines()
                  ]]
                for i in range(len(item[0]))
            ]
          ]]
      ]
  ]
)

'''
-Part One-
  Amazingly long and convoluted as a result of being tired.
  I started off with separating each line of input into a list of the bits, which I then took 
  the first bit of each line, then the second, and so on into a list as elements. Then, count 
  the number of occurence and put them in its respective index (count of '0' bits in 0 and 
  same for '1' bits). Get the index of the highest occurence, which also translates to the bit
  corresponding to it, along with 1 - that and put them together as tuples. Now, we have a list
  of tuples, where each tuple has the nth digit of the gamma/epsilon rate, n being the nth
  element of the list. For example, [('0', '1'), ('0', '1'), ('1', '0')] means '001' for gamma
  rate and '110' as epsilon rate. The only step left is to put them together and convert to
  decimal, which is very simple, then multiplying the two together.

-Part Two-
  This requires a lot more logic, and therefore has been put on hold for a moment.
'''