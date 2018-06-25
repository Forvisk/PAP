--elemento
elemento :: [Int] -> Int -> Int
elemento [] _ = 0
elemento aList n | length aList < n = last aList
 | otherwise = getItem aList n

getItem :: [Int] -> Int -> Int
getItem [] _ = 0
getItem (aHead:aTail) n | n == 1 = aHead
 | otherwise = getItem aTail (n-1)
