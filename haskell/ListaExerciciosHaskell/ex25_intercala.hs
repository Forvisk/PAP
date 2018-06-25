--25 intercala
intercala :: [Int] -> [Int] -> [Int]


intercala [] [] = []
intercala aList [] = aList
intercala [] aList = aList
intercala (aHead1:aTail1) (aHead2:aTail2) = [aHead1,aHead2] ++ (intercala aTail1 aTail2)
