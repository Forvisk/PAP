--unicaOcorrencia
unicaOcorrencia :: Int -> [Int] -> Bool
unicaOcorrencia _ [] = False
unicaOcorrencia n [x] | n == x = True
 | x /= n = False
unicaOcorrencia n [x,y] | ((n == x) && (n /= y)) || ((n /= x) && (n == y)) = True
 | otherwise = False
unicaOcorrencia n (aHead:aSecond:aTail) | n == aHead && n == aSecond = False
 | (n == aHead && n /= aSecond) = unicaOcorrencia n (aTail ++ [aHead])
 | (n /= aHead && n == aSecond) = unicaOcorrencia n (aTail ++ [aSecond])
 | otherwise = unicaOcorrencia n aTail