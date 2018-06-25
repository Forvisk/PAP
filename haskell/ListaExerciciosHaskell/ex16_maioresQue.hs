--maioresQue
maioresQue :: Int -> [Int] -> [Int]
maioresQue _ [] = []
maioresQue n [x] | x > n = [x]
 | otherwise = []
maioresQue n (aHead:aTail) | aHead > n = (maioresQue n aTail) ++ [aHead]
 | otherwise = maioresQue n aTail