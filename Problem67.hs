-- http://projecteuler.net/problem=67
-- this solution also works for problem 18


-- naive solution for problem 18 would not work in this case

filename :: String
filename = "Problem67.txt"


-- precondition:: the lengths of the lists are consecutive numvers
getMaxSum :: [[Int]] -> Int
getMaxSum [] = 0
getMaxSum [x] = head x
getMaxSum l@(x:y:xs) = max s1 (head x + getMaxSum rest)
  where y1:y2: _ = y
        s1 = if y1 > y2 then sum $ map head l
                        else sum $ map last l
        rest = if y1 > y2 then map tail (y:xs)
                          else map init (y:xs)
sol :: IO()
sol = do
  triangle <- readFile filename
  let values = (map (map read . words) $ lines triangle) :: [[Int]]
  -- print $ map length values
  print $ getMaxSum values

