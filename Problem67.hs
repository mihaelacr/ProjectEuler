-- http://projecteuler.net/problem=67
-- this solution also works for problem 18

import qualified Data.Vector as V

filename :: String
filename = "Problem67.txt"

filename1 :: String
filename1 = "sample.txt"

filename18 :: String
filename18 = "Problem18.txt"


data TriangleType = LeftT | RightT

type Triangle = V.Vector (V.Vector Int)

-- | Converts a list of lists to a 2D vector
vector2D :: [[a]] -> V.Vector (V.Vector a)
vector2D ll = V.fromList $ map V.fromList ll


getTriangleAt :: TriangleType -> Triangle -> Int -> Triangle
getTriangleAt LeftT xs index  = V.fromList [ V.take (i - index + 1) $ xs V.! i |  i <- [index .. V.length xs - 1]]
getTriangleAt RightT xs index = V.fromList [ V.drop index $ xs V.! i |  i <- [index .. V.length xs - 1]]


getMaxSum :: Triangle -> Int
getMaxSum t = case V.length t of
  0 -> 0
  1 -> V.head $ V.head t
  _ -> if V.null xs then x + max y1 y2
                    else x + max s1 (getMaxSum rest)
  where x  = V.head $ V.head t
        y1 = V.head $ (V.!) t 1
        y2 = (V.!) ((V.!) t 1) 1
        xs = V.drop 2 t
        s1 = if y1 > y2 then y2 + getMaxSum (getTriangleAt RightT t 2)
                        else y1 + getMaxSum (getTriangleAt LeftT  t 2)
        rest = if y1 > y2 then getTriangleAt LeftT t 1
                          else getTriangleAt RightT t 1


sol :: String -> IO()
sol file = do
  triangle <- readFile file
  let values = (map (map read . words) $ lines triangle) :: [[Int]]
  print $ getMaxSum $ vector2D values

