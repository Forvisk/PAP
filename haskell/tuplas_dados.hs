nomes :: (String, Int, String)
nomes = ("Wesley", 30, "brasileiro")

select_name(x, _, _) = x
select_age(_,y,_) = y
select_country(_,_,z) = z
