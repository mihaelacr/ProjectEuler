-- http://projecteuler.net/problem=67
-- this solution also works for problem 18


filename :: String
filename = "Problem67.txt"

filename1 :: String
filename1 = "sample.txt"

-- TODO replace with one function and one
getLeftTriangleAt :: [[Int]] -> Int -> [[Int]]
getLeftTriangleAt xs index = [ take (i - index + 1)  $ xs !! i |  i <- [index .. length xs - 1]]

getRightTriangleAt :: [[Int]] -> Int -> [[Int]]
getRightTriangleAt xs index = [ drop (i - 1)  $ xs !! i |  i <- [index .. length xs - 1]]


-- precondition:: the lengths of the lists are consecutive numvers
getMaxSum :: [[Int]] -> Int
getMaxSum [] = 0
getMaxSum [x] = head x
getMaxSum l@(x:y:xs) = head x + max s1 (getMaxSum rest)
  where y1:y2: _ = y
        size = length l
        s1 = if y1 > y2  then maximum $ map (getMaxSum . getLeftTriangleAt l)  [2.. size - 1]
                         else maximum $ map (getMaxSum . getRightTriangleAt l) [2.. size - 1]

        rest = if y1 > y2 then map init (y:xs)
                          else map tail (y:xs)

sol :: String -> IO()
sol file = do
  triangle <- readFile file
  let values = (map (map read . words) $ lines triangle) :: [[Int]]
  -- print values
  print $ getMaxSum values

