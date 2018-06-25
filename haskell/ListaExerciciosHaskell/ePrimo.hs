--7 ePrimo
ePrimo :: Int -> Bool
ePrimo 1 = False
ePrimo 2 = True
ePrimo n | (n mod 2) == 0 = False
 | otherwise = True
