--3 menorDeTres
menorDeTres :: Int -> Int -> Int -> Int
menorDeTres x y z | x > y = menorDeDois y z
 | y > x = menorDeDois x z
