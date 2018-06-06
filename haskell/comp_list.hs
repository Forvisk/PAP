comp_listas :: [Int] -> [Int] -> Bool
comp_listas [] [] = True
comp_listas [] _ = False
comp_listas _ [] = False
comp_listas (aHead:aTail) (bHead:bTail) | ( aHead == bHead ) = comp_listas aTail bTail
                                        | otherwise = False
