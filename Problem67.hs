module Problem67 where
-- http://projecteuler.net/problem=67
-- this solution also works for problem 18

filename :: String
filename = "Problem67.txt"

filename1 :: String
filename1 = "sample.txt"

-- precondition is that the argument is a triangular list
getMaxSum :: [[Int]] -> Int
getMaxSum [] = 0
getMaxSum xs = head $ foldr1 f xs
  where f l acc = zipWith (+) l $ zipWith max acc (0:acc)


sol :: String -> IO()
sol file = do
  triangle <- readFile file
  let values = (map (map read . words) $ lines triangle) :: [[Int]]
  print $ getMaxSum values

