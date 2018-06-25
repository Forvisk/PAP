inverte :: [Int] -> [Int]

inverte [] = []
inverte [i] = [i]
inverte (x:aTail) = inverte aTail ++ [x]
