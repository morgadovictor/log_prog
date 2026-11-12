"""
Implemente um jogo onde o usuário disputa uma melhor de 3 rodadas
contra a máquina para adivinhar um número secreto entre 1 e 50.
○ Regras de Negócio:
■ Utilize um loop for para controlar as 3 rodadas fixas do jogo.
■ Em cada rodada, o jogador tem até 5 tentativas para acertar o
número. Utilize um loop while para gerenciar essas tentativas.
■ A cada palpite, use if/elif/else para:
● Alertar se o palpite foi maior que o número secreto.
● Alertar se o palpite foi menor que o número secreto.
● Encerrar a rodada caso o jogador acerte, somando
pontos: 100 pontos na 1a tentativa, 75 na 2a, 50 na 3a, 25
na 4a e 10 na 5a.
● Indicar fim de tentativas na rodada com 0 pontos ganhos
se esgotar as 5 chances.

■ No final das 3 rodadas, avalie a pontuação total com if/elif/else e
imprima a classificação: "Excelente" (acima de 200), "Bom"
(entre 100 e 200) ou "Tente Novamente" (abaixo de 100).
○ Restrição: Sem uso de vetores/listas. O número secreto pode ser
definido com a biblioteca random ou valores inteiros pré-definidos para
cada rodada.
"""
