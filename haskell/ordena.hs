-- PAP - BCC - UDESC
-- Adriano Zanella Junior
-- Ordenador em haskell

-- função primária para detectar se precisa ordenar
ordena :: [Int] -> [Int]
ordena [] = []
ordena [i] = [i]
ordena [i,j] | i > j = [j, i]
 | otherwise = [i, j]
ordena l = ordena ( remove l (maximum l)) ++ [maximum l]

-- função que percorre a lista de inteiros buscando o numero e removendo ele
remove :: [Int] -> Int -> [Int]
remove (j:i:atail) x | j == x = i:atail
 | i == x = j:atail
 | length atail == 1 && atail == [x] = [i,j]
 | otherwise = [i,j] ++ (remove atail x)

-- pior caso -- com n inteiros, os n-1 primeiros elementos em ordem crescente, e no n-esimo elemento, o menor numero de todos
