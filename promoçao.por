programa 
{
  funcao inicio()
  {
   real produto, promocao, preco

   escreva("digite o valor do produto: ")
   leia(produto)

   promocao = produto * 0.05
   escreva("\no desconto será de: ", promocao)

   preco = produto - promocao
   escreva("\no valor promocionalé de: ", preco)
 }
}
