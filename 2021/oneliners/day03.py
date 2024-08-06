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

print("Part Two:",
  [
    solve := lambda lst, condition, n :
      int(lst[0], 2) if n >= len(lst[0]) or len(lst) <= 1 else 
      solve(
          sorted([
            [num
              for num in lst
              if num[n] == digit
            ]
            for digit in '01'
          ],
          key=lambda x: (len(x), x[0][n] == "1"))[condition]
        , condition, n+1),
    *[
      solve(all_numbers, 0, 0) * solve(all_numbers, 1, 0)
        for all_numbers in
          [[
            i.strip()
              for i in
                open("input.txt", "r")
          ]]
    ]
  ][1]
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
  Recursion in a "single line"!!!!!!
  With the help of lambda functions, recursion is possible in a single line, and is actually
  straightforward and relatively simple.

  *Walrus operator (:=) is used here, and therefore this solution does not work before Python 3.8.

  For every iteration of the loop, split the list of numbers into two lists, one being numbers
  with '1' in the nth position, and the other being numbers with '0' in the same nth position. This
  list will be sorted by number of elements in each list (number of occurrences of the digit in the
  nth position), then by the nth digit being '1' (this is to resolve same number of occurences). If
  the condition is 1 (oxygen generator rating), it will take the 2nd item of the array (most number
  of occurences in the nth position or nth digit being '1' if both numbers of occurence is
  identical). After there is only 1 item left in the list, return that number which is converted
  into decimal. The solution calls the function for condition 0 and 1, multiplying them together.
'''