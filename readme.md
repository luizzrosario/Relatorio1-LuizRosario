# README - Projeto de Análise Numérica: Métodos Numéricos para Resolução de Sistemas Lineares

## Informações do Projeto

**Relatório de implementações realizadas por:** Luiz Rosário
**Disciplina:** Análise Numérica
**Curso:** Ciência da Computação
**Semestre:** 2025.1
**Professor:** Gesil Sampaio Amarante II

## Descrição

Este projeto tem como objetivo implementar e testar diferentes métodos numéricos para resolver sistemas lineares. Ele abrange os seguintes métodos:

- **Bissecção**
- **Posição Falsa**
- **Newton-Raphson**
- **Secante**
- **Eliminação de Gauss**
- **Fatoração LU**
- **Método de Jacobi**
- **Método de Gauss-Seidel**
- **Método de Gauss-Jordan**

Cada método foi implementado e avaliado com base em problemas de teste específicos, com análise das dificuldades enfrentadas durante a implementação, como erros de precisão e manipulação de tolerâncias.

## Linguagens e Ferramentas Usadas

- **Python**: Linguagem escolhida pela simplicidade e grande capacidade de manipulação numérica com bibliotecas como **NumPy** e **Matplotlib**.
- **NumPy**: Para operações matemáticas e manipulação de matrizes.
- **GeoGebra**: Para visualização gráfica das funções, se necessário.

## Estrutura do Projeto

O projeto foi organizado de forma a resolver problemas de teste específicos, com base nos seguintes pontos:

1. **Estratégia de Implementação**: Implementação sequencial e otimização dos métodos numéricos.
2. **Estrutura dos Arquivos de Entrada/Saída**: Arquivos de entrada e saída bem definidos, facilitando a execução e teste dos métodos.

## Principais Dificuldades

- Manipulação das **matrizes** e **vetores** de maneira eficiente, especialmente em métodos diretos como Gauss-Jordan e Fatoração LU.
- **Ajuste de tolerância** e sua influência no desempenho, com ajustes em algumas iterações sendo necessários para equilibrar precisão e tempo de execução.
- **Erros de precisão numérica** ao manipular as iterações em métodos como Newton-Raphson e Secante.

## Testes

O projeto foi validado com diversos problemas de teste. Cada teste foi aplicado para garantir que os métodos estivessem funcionando corretamente.

## Conclusão

A implementação desses métodos proporcionou uma compreensão profunda de como os algoritmos resolvem sistemas lineares e a importância da escolha de tolerância e precisão. O projeto contribui significativamente para a aprendizagem dos conceitos de **Análise Numérica**.
