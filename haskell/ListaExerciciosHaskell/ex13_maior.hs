--maior
maior :: [Int] -> Int
maior [x] = x
maior (aHead:aTail) | aHead < (maior aTail) = maior aTail
 | otherwise = aHead