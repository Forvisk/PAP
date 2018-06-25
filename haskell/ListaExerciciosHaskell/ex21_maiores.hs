--21 maiores
maiores :: Int -> [Int] -> [Int]

maiores _ [] = []
maiores n aList | n > lenght aList = aList
maiores 1 [x,y] | x > y = x
 | otherwise = y
