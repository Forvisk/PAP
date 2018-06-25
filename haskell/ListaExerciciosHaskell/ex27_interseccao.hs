--27 intersecccao
interseccao :: [Int] -> [Int] -> [Int]

interseccao [] [] = []
interseccao aList [] = []
interseccao [] aList = []
interseccao [x] [y] | x == y = [x]
interseccao [x] (aHead:aTail) | x == aHead = [x]
 | otherwise = interseccao [x] aTail

interseccao (aHead:aTail) aList2 = interseccao [aHead] aList2 ++ interseccao aTail aList2
