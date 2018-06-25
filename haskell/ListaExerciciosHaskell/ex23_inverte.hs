--23 inverte
inverte :: [Int] -> [Int]

inverte [] = []
inverte [x] = [x]
inverte (aHead:aTail) = (inverte aTail) ++ [aHead]
