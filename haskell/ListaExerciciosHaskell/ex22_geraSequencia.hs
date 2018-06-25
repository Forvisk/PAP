--22 geraSequencia
geraSequencia :: Int -> [Int]

geraSequencia 0 = []
geraSequencia n =  geraSequencia (n-1) ++ [n, -n]
