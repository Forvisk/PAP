--24 divide
divide :: Int -> [Int] -> ([Int],[Int])

divide _ [] = ([],[])
divide 0 aList = ([],aList)
