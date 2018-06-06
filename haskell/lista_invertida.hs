-- [t] lista generica
-- ++ é um operador de concatenação entre duas listas
inv_list :: [t] -> [t]
inv_list [] = []
inv_list (aHead:aTail) = inv_list aTail ++ [aHead]
