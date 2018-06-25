--nroElementos
nroElementos :: [Int] -> Int
nroElementos [] = 0
nroElementos (aHead:aTail) = nroElementos(aTail) + 1