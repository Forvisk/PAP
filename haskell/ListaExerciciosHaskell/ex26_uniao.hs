--26 uniao
uniao :: [Int] -> [Int] -> [Int]

uniao [] [] = []
uniao aList [] = aList
uniao [] aList = aList

uniao aL1 aL2 = removerRepetidos (aL1 ++ aL2)

--20 removerRepetidos
removerRepetidos :: [Int] -> [Int]

removerRepetidos [] = []
removerRepetidos [x] = [x]
removerRepetidos (aHead:aTail) = [aHead] ++ (removerRepetidos (removerDaLista aHead aTail))

removerDaLista :: Int -> [Int] -> [Int]

removerDaLista _ [] = []
removerDaLista n [x] | n == x = []
 | otherwise = [x]
removerDaLista n (aHead:aTail) | n == aHead = removerDaLista n aTail
 | otherwise = [aHead] ++ (removerDaLista n aTail)
