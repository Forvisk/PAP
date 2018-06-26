--7 ePrimo
ePrimo :: Int -> Bool
ePrimo 1 = False
ePrimo 2 = True
ePrimo n | (mod n 2) == 0 = False
 | otherwise = testaSePrimo n 3

testaSePrimo :: Int -> Int -> Bool
testaSePrimo n d | d > div n 2 = True
testaSePrimo n d | (mod n d) == 0 = False
 | otherwise = testaSePrimo n (d+2)
