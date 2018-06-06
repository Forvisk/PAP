type Nome = String
type Idade = Int
type Pais = String
type Pessoa = (Nome, Idade, Pais)

pessoa :: Pessoa
pessoa = ("Joao", 20, "Brasil")

retornaNome :: Pessoa -> Nome
retornaNome(n, i, p) = n
