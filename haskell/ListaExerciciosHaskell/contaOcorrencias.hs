--contaOcorrencias
contaOcorrencias :: [Int] -> Int -> Int
contaOcorrencias [] _ = 0
contaOcorrencias [x] y | x /= y = 0
contaOcorrencias (aHead:aTail) n | aHead == n = (contaOcorrencias aTail n)+1
 | otherwise = contaOcorrencias aTail n