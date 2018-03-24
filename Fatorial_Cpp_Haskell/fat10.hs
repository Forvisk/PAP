fat 0 = 1
fat n =  n * fat (n-1)

main = do putStr "Resp: "
          print (fat 10)