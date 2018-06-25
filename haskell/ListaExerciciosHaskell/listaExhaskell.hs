-- Lista de exercicio de PAP - Haskell

--1 soma
soma :: (Int, Int) -> Int
soma (x,y) = x + y

--2 menorDeDois
menorDeDois :: Int -> Int -> Int
menorDeDois x y | x > y = y
 | otherwise = x

--3 menorDeTres
menorDeTres :: Int -> Int -> Int -> Int
menorDeTres x y z | x > y = menorDeDois y z
 | y > x = menorDeDois x z