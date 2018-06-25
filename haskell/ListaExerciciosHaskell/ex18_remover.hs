-- remover
remover :: Int -> [Int] -> [Int]

remover _ [] = []
remover n [y] | n == y = []
remover n (aHead:aSecond:aTail) | n == aHead = [aSecond] ++ aTail
 | n == aSecond = [aHead] ++ aTail
 | otherwise = [aHead, aSecond] ++ (remover n aTail)
