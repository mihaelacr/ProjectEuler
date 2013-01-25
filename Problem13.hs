import Data.List

filename :: String
filename = "Problem13.txt"
chunkSize :: Int
chunkSize = 10

-- Divides a list into a list of lists, each of size n
chunksOf :: Int -> [a] -> [[a]]
chunksOf n xs = [ [xs !! i | i <- [j .. j + n - 1], i < len]  | j <- [0, n.. len - 1] ]
  where len = length xs


-- Addition on big numbers
-- each element of xs is a number, represented as a list of numbers of c digits
bigAdd :: Int -> [[Int]] -> Int
bigAdd c xs = case xsT of
  [] -> 0
  (first: rest) -> sum first + foldr (s c) 0 rest
  where xsT = transpose xs

s :: Int -> [Int] -> Int -> Int
s c xs a = (sum xs + a) `div` pow
  where pow = 10 ^ c

test :: Int
test = bigAdd chunkSize (replicate 3 $ replicate 10 $ 10 ^ (9::Int))

-- Simulate addition on big numbers by dividing each of the numbers into smaller
-- bits and use carrier addition
sol :: IO ()
sol = do
     str <- readFile filename
     let numbers = lines str
         smallerNumbers = [ [ read n :: Int | n <- chunksOf chunkSize nr ] | nr <- numbers]
     print $ take 10 $ show $ bigAdd chunkSize smallerNumbers


-- Use arbitrary precision integers, Integer
sol2 :: IO()
sol2 = do
  str <- readFile filename
  let numbers = lines str
  print $ sum [read n :: Integer | n <- numbers]
