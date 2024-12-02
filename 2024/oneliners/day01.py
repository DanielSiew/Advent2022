print("Part One:",
  sum(abs(lst1[0] - lst2[0])
  for lsts in
    [[sorted(
      [(row[i], idx)
        for idx, row in
          enumerate([list(map(int, line.strip().split()))
            for line in
              open("input.txt", "r").readlines()
          ])
      ], key=lambda x: x[0])
      for i in range(2)]
    ]
  for lst1, lst2 in zip(lsts[0], lsts[1])
  )
)

print("Part Two:",
  sum([num * lsts[1].count(num)
  for lsts in
    [[[row[i]
      for row in
        [list(map(int, line.strip().split()))
          for line in
            open("input.txt", "r").readlines()
        ]
    ]
      for i in range(2)]
  ]
  for num in lsts[0]
  ])
)

'''
explanation to be added, just wanted to get this done
'''