comp_string :: [Char] -> [Char] -> Bool
comp_string [] [] = True
comp_string [] _ = False
comp_string _ [] = False
comp_string (aHead:aTail) (bHead:bTail) | ( aHead == bHead ) = comp_string aTail bTail
 | otherwise = False

(#) :: [Char] -> [Char] -> [Char]
(#) [] [] = []
(#) aList1 aList2 | comp_string aList1 aList2 = aList1
 | otherwise = aList1 ++ aList2