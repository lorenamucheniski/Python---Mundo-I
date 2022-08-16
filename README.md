# Python---Mundo-I
Repositório criado para os exercicíos de Python do curso em vídeo com o professor Gustavo Guanabara.

[Curso em Vídeo - Python Mundo I](https://youtu.be/S9uPNppGsGo)

1. Descrição
2. Tipos Primitivos de Dados
3. Módulos e Bibliotecas em Python
4. Manipulando strings

## 1 - Descrição
Python é uma linguagem ultra moderna, utilizada por grandes empresas como Google, YouTube, Industrial Light & Magic, Globo e muitas outras. Fácil de aprender, com código limpo e organizado, Python vem ganhando cada vez mais espaço, e chegou a sua hora de aprender. Curso criado pelo Prof. Gustavo Guanabara com uma temática divertida de vídeo-game para motivar seus alunos, é dividido em mundos para facilitar o estudo.
O primeiro mundo foi pensando de forma a apresentar a linguagem ao aluno, o professor irá introduzir a linguagem, seus conceitos, montar o primeiro programa e ensinar alguns recursos básicos.

## 2 - Tipos Primitivos de Dados

Um tipo de dado primitivo é a representação computacional de algum conceito usado no nosso cotidiano, como os números, as letras do alfabeto e os sinais de pontuação. Esses são os elementos mais básicos usados para construir um programa. O tipo de dado primitivo serve para definir a quantidade de memória alocada e a faixa de valores possíveis para uma variável. Um dado pode ser do tipo int, float, bool ou str.

![](imagens/tipos.png)

## 3 - Módulos e Bibliotecas em Python
O que é um módulo e uma biblioteca?

Um módulo nada mais é do que um arquivo .py com instruções e definições em Python, para serem usados em outros programas em Python. Há diversos módulos do Python que fazem parte da biblioteca padrão. 

Uma biblioteca é um conjunto de módulos. Portanto, a biblioteca padrão Python é um conjunto de módulos disponíveis em Python para que você possa importá-los e usar as funcionalidades deles quando bem quiser.

No exemplo abaixo, criaremos um módulo que representa um círculo. Para isso, criamos um arquivo chamado circulo.py com o seguinte conteúdo:

![](imagens/modulo.png)
 
 Para usar o módulo acima podemos fazer como mostrado abaixo:
 
 ![](imagens/usando_modulo.png)
 
 Note que usamos o comando **import circulo** para que pudéssemos usar as definições do módulo círculo em nosso programa. De modo geral, essa é a forma pela qual usamos módulos em Python. Caso quiséssemos utilizar apenas a função area() poderíamos importar apenas ela por meio do comando **from circulo import area**. Isso é útil em caso de módulos muito grandes e quando queremos usar apenas uma ou outra função deles.
 
 ## 4 - Manipulando strings
 
 Para manipular uma String precisamos criar uma e para isso a forma mais pratica é atribuir uma variável a qualquer palavra. O python considera tudo o que estiver entre 'aspas simples' ou "aspas duplas" como String. Utilizamos print( ) para pedir ao programa escrever na tela o que está dentro dos parênteses.

Um exemplo: P será nossa variável e Olá, mundo! nossa string então teremos...

![](imagens/ola_mundo.png)

**_Funções de Manipulação de String_**

O jeito mais básico de manipular strings é através de métodos que estão dentro delas (strings). Podemos fazer um limitado número de tarefas em strings através desses métodos. A seguir veremos alguns desses métodos.

#### > Para verificar qual é o **tipo** da variável podemos usar type() :

![](imagens/type.png)                

E nós teremos o retorno de que minha variável **p** é uma string:

![](imagens/type_result.png)

#### > Podemos utilizar len() para vereficar quantos caracteres tem na string: 

![](imagens/len.png)

E o resultado retornado de 10 caracteres:

![](imagens/len_result.png)
 
 Essas foram só algumas das muitas formas de manipular String dentro do Python. Mais alguns sites que podem explicar e dar exemplos de manipulação de Strings:
 
 [Python Brasil](https://wiki.python.org.br/ManipulandoStringsComPython)
 
 [Data Marte](https://datamarte.com/como-manipular-strings-em-python/)
 
 [Programming Historian](https://programminghistorian.org/pt/licoes/manipular-strings-python)
 
 ## Condições If e Else
 
 O **if** e **else** são estruturas condicionais de controle que permitem avaliar uma expressão, e de acordo com o seu resultado, executar uma determinada ação.
 
 Vamos colocar em prática o uso do **if** e **else**.
 
 No código a seguir, verificaremos se a variável idade é menor que 20. Se caso for afirmativo, aparecerá uma mensagem na tela, se caso for negativo, o código seguirá normalmente ignorando a linha 3:
 
 ![](imagens/if.png)
