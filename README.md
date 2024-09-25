# Desafio Target - Estagio Target Ribeirão Preto

Este repositório contém soluções para as questões do desafio Target, voltado para candidatos ao estágio em Sistemas. As questões abordam conceitos fundamentais de programação e lógica, proporcionando uma oportunidade para demonstrar habilidades de resolução de problemas.

## Questões Incluídas

1. **Sequência de Fibonacci**: 
   - Dado a sequência de Fibonacci, onde se inicia por 0 e 1, escreva um programa que, informado um número, calcule a sequência e retorne uma mensagem avisando se o número pertence ou não à sequência. O número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código.
   - [Solução aqui](https://github.com/GeorgeAlexsander/Estagio_Target_Ribeirao_Preto/blob/main/Questao_1_fibonacci_check/fibonacci_check.py)

2. **Contagem de Letras**: 
   - Escreva um programa que verifique, em uma string, a existência da letra ‘a’ (maiúscula ou minúscula) e informe quantas vezes ela ocorre. A string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código.
   - [Solução aqui](https://github.com/GeorgeAlexsander/Estagio_Target_Ribeirao_Preto/blob/main/Questao_2_contar_letra_a/Questao_2_contar_letra_a.py)

3. **Cálculo da Soma**: 
   - Observe o trecho de código abaixo:
     ```plaintext
     int INDICE = 12, SOMA = 0, K = 1;
     Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
     Imprimir(SOMA);
     ```
     Ao final do processamento, qual será o valor da variável SOMA?
   - [Solução aqui](https://github.com/GeorgeAlexsander/Estagio_Target_Ribeirao_Preto/blob/main/Questao_3_sum_calculation/sum_calculation.py)

4. **Sequências e Lógica**: 
   - Descubra a lógica e complete o próximo elemento:
     - a) 1, 3, 5, 7, <u>**9**</u>
     - b) 2, 4, 8, 16, 32, 64, <u>**128**</u>
     - c) 0, 1, 4, 9, 16, 25, 36, <u>**49**</u>
     - d) 4, 16, 36, 64, <u>**100**</u>
     - e) 1, 1, 2, 3, 5, 8, <u>**13**</u>
     - f) 2, 10, 12, 16, 17, 18, 19, <u>**200**</u>
    Temos respectivamente as seguintes lógicas:
     - a) temos números impares consecutivos;
     - b) temos potências de base 2;
     - c) temos números inteiros em ordem e ao quadrado (ex: 0², 1², 2²,...,7²);
     - d) similar a anterior, porém apenas números pares não nulos ao quadrado (ex: 2², 4², 6²,...,10²);
     - e) consiste na sequência de Fibonacci;
     - f) consiste em números naturais iniciados pela letra D (Dois, Dez, Doze, .... Duzentos).

5. **Interruptores e Lâmpadas**: 
   - Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. Seu objetivo é descobrir qual interruptor controla qual lâmpada, usando apenas duas idas até uma das salas. Como você faria isso?
   
   Para resolver, podemos:
   - Ligar um interruptor e deixar o mesmo ligado por alguns minutos. Em seguida, desligar e ligar um segundo interruptor.
   Assim, quando irmos na sala com as lâmpadas, teremos três casos:
   - a) Lâmpada desligada e quente, referente ao primeiro interruptor ligado.
   - b) Lâmpada ligada e fria, referente ao ultimo interruptor ligado.
   - c) Lâmpada desligada e fria, referente ao interruptor não acionado.
   
   Esta primeira solução, tem como pré-requisito que as lâmpadas sejam suscetíveis ao efeito Joule, ou seja, aqueçam durante seu acionamento. Para uma análise ainda mais precisa, considerando que não haja contato direto com a lâmpada, poder-se-ia fazer a seguinte solução:
   - a) Ligar o primeiro interruptor: ligue o primeiro interruptor e deixe-o ligado.
   - b) Ligar o segundo interruptor: ligue o segundo interruptor e deixe-o ligado.
   - c) Desligar o segundo interruptor: desligue o terceiro interruptor e deixe-o desligado.

Vá até a sala em que estão as lampadas (primeira ida)
   - a) Veja quais lâmpadas estão ligadas, poderemos, por exemplo, ter:
   - Lâmpada A (Ligada);
   - Lâmpada B (Ligada); 
   - Lâmpada C (Desligada).

Volte para a sala com os interruptores, agora iremos desligar um dos interruptores e acionar o que não foi acionado, teremos, por exemplo:
   - a) Desligue o primeiro interruptor: desligue o primeiro interruptor e deixe-o Desligado.
   - b) Ligar o segundo interruptor: ligue o segundo interruptor e deixe-o ligado.
   - c) Ligue o segundo interruptor: ligue o terceiro interruptor e deixe-o ligado.

Vá até a sala (segunda ida), agora, uma das lampadas que foram acesas no primeiro caso, a outra que estava acesa, estará desligada e a que estava acessa, será ligada, teremos algo como:
   - Lâmpada A (Ligada);
   - Lâmpada B (Desligada); 
   - Lâmpada C (Ligada).

Assim, pode-se concluir que:
  - Interruptor A, que foi desligado na segunda ida, corresponde a lâmpada B, que foi desligada após a alteração;
  - Interruptor B, que foi mantido ligado, corresponde a lâmpada A, que seguiu acionada;
  - Interruptor C, que foi acionado na segunda ida, corresponde a lâmpada acionada após a primeira ida, lampada C.

    
## Tecnologias Utilizadas

- 🐍 Python

## Como Executar

Para executar as soluções, clone este repositório e utilize um interpretador Python. As instruções específicas para cada questão estão comentadas no código.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para fazer um fork do repositório e enviar pull requests.

## Desenvolvedor

👤 **George Flores**

## Link do meu GitHub para ver mais dos meus projetos

[Veja mais projetos aqui](https://github.com/GeorgeAlexsander/)

## Link do Repositório

[Link do Repositório](https://github.com/GeorgeAlexsander/Estagio_Target_Ribeirao_Preto)
