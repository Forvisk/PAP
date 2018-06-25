--19 removerUltimo
removerUltimo :: [Int] -> [Int]

removerUltimo [] = []
removerUltimo [x] = []
removerUltimo (aHead:aTail) = [aHead] ++ removerUltimo aTail
