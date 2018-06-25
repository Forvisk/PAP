--28 sequencia
sequencia :: Int -> Int -> [Int]

sequencia 0 _ = []
sequencia n m = [m] ++ sequencia (n-1) (m+1)
