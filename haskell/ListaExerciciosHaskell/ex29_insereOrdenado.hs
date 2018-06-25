--29 insereOrdenado
insereOrdenado :: [Int] -> Int -> [Int]

insereOrdenado [] n = [n]

insereOrdenado (aHead:aTail) n | n < aHead = [n,aHead] ++ aTail
 | otherwise = [aHead] ++ insereOrdenado aTail n
