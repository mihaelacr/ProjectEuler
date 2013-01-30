-- http://projecteuler.net/problem=67
-- this solution also works for problem 18


filename :: String
filename = "Problem67.txt"

filename1 :: String
filename1 = "sample.txt"

data TriangleType = LeftT | RightT


getTriangleAt :: TriangleType -> [[Int]] -> Int -> [[Int]]
getTriangleAt LeftT xs index  = [ take (i - index + 1) $ xs !! i |  i <- [index .. length xs - 1]]
getTriangleAt RightT xs index = [ drop index  $ xs !! i |  i <- [index .. length xs - 1]]


-- precondition:: the lengths of the lists are consecutive numvers
getMaxSum :: [[Int]] -> Int
getMaxSum [] = 0
getMaxSum [x] = head x
getMaxSum l@(x:y:xs) = if null xs then head x + max y1 y2
                                  else head x + max s1 (getMaxSum rest)
  where y1:y2: _ = y
        s1 = if y1 > y2  then getMaxSum $ getTriangleAt LeftT l 2
                         else getMaxSum $ getTriangleAt RightT l 2
        rest = if y1 > y2 then map init (y:xs)
                          else map tail (y:xs)

sol :: String -> IO()
sol file = do
  triangle <- readFile file
  let values = (map (map read . words) $ lines triangle) :: [[Int]]
  -- print values
  print $ getMaxSum values

