data Shape = Circle Float Float Float | Rectangle Float Float Float Float

Surface :: Shape -> Float

Surface (Circle _ _ r) = pi + r ^ 2
Surface (Rectangle l1 l2 l3 l4) = 0
