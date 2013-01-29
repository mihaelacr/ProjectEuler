-- http://projecteuler.net/problem=67
-- this solution also works for problem 18


filename :: String
filename = "Problem67.txt"

filename1 :: String
filename1 = "sample.txt"

 -- replace s1 with something like this
-- maximum getMaxSum ( [[l !! i !! j | j <- [i .. length l !! i]] |  i <- [ 2 .. length l])


-- precondition:: the lengths of the lists are consecutive numvers
getMaxSum :: [[Int]] -> Int
getMaxSum [] = 0
getMaxSum [x] = head x
getMaxSum (x:y:xs) = head x + max s1 (getMaxSum rest)
  where y1:y2: _ = y
      -- it is not as easy as finding out s1, but the maximum of
      -- all triangles which start in the left most or right most corner of the respectively
      -- chosen edge
        s1 = if y1 > y2  then sum $ map last (y:xs)
                         else sum $ map head (y:xs)

        rest = if y1 > y2 then map init (y:xs)
                          else map tail (y:xs)

sol :: String -> IO()
sol file = do
  triangle <- readFile file
  let values = (map (map read . words) $ lines triangle) :: [[Int]]
  -- print values
  print $ getMaxSum values

