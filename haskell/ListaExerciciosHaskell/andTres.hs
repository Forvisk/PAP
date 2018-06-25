-- andTres
andTres :: Bool -> Bool -> Bool -> Bool
andTres True True True = True
andTres False _ _ = False
andTres _ False _ = False
andTres _ _ False = False 