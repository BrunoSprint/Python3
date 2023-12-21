#Sistemas distribuídos e Mobile
#Palavras-chave; Computação Paralela; Computação Distribuída


#Tipo de atividade Prática

#FEEDBACK;
#Os alunos irão implementar um algoritmo de soma de vetores usando programação 
#paralela com a biblioteca multiprocessing.
#O objetivo é paralelizar o processo de soma de vetores em vários núcleos/processadores para melhorar o desempenho.






#Exemplo de implementação em Python:
import multiprocessing
def soma_vetores(vetor1, vetor2, resultado, inicio, fim):
 for i in range(inicio, fim):
 resultado[i] = vetor1[i] + vetor2[i]
def soma_vetores_paralelo(vetor1, vetor2):
 tamanho = len(vetor1)
 resultado = multiprocessing.Array('i', tamanho) # Array compartilhado entre os processos
 processos = []
 num_processos = multiprocessing.cpu_count() # Obtém o número de núcleos disponíveis
 
 # Divide o trabalho entre os processos
 passo = tamanho // num_processos
 for i in range(num_processos):
 inicio = i * passo
 fim = inicio + passo if i < num_processos - 1 else tamanho
 p = multiprocessing.Process(target=soma_vetores, args=(vetor1, vetor2, resultado, inicio, 
fim))
 processos.append(p)
 p.start()
 
 # Aguarda a conclusão de todos os processos
 for p in processos:
 p.join()
 
 # Converte o resultado de Array para uma lista
 resultado_final = list(resultado)
 
 return resultado_final
# Vetores de exemplo
vetor1 = [1, 2, 3, 4, 5]
vetor2 = [6, 7, 8, 9, 10]
# Chama a função de soma de vetores paralela
resultado_final = soma_vetores_paralelo(vetor1, vetor2)
print(resultado_final)

Nesse exemplo, a função soma_vetores_paralelo é responsável por realizar a computação 
paralela da soma dos vetores vetor1 e vetor2.
Ela utiliza a biblioteca multiprocessing para criar vários processos, dividir o trabalho entre eles e aguardar a conclusão de todos.
O resultado é armazenado em um array compartilhado entre os processos e, ao final, é convertido em uma lista para ser retornado.
Exemplo de prática sobre Computação Paralela e Distribuída usando Java.
Nesta prática, vamos criar um programa que realiza a multiplicação de matrizes utilizando programação paralela. 
Vamos dividir a;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
public class ParallelMatrixMultiplication {
 private static final int SIZE = 1000;
 private static final int NUM_THREADS = 4;
 private static final int[][] matrixA = new int[SIZE][SIZE];
 private static final int[][] matrixB = new int[SIZE][SIZE];
 private static final int[][] resultMatrix = new int[SIZE][SIZE];
 public static void main(String[] args) {
 // Inicializar as matrizes
 initializeMatrices();
// Criar um ExecutorService com um número fixo de threads
 ExecutorService executor = Executors.newFixedThreadPool(NUM_THREADS);
 // Dividir as linhas da matrizA entre as threads
 int rowsPerThread = SIZE / NUM_THREADS;
 for (int i = 0; i < NUM_THREADS; i++) {
 int startIndex = i * rowsPerThread;
 int endIndex = (i + 1) * rowsPerThread;
 executor.execute(new MatrixMultiplicationTask(startIndex, endIndex));
 }
 // Encerrar o ExecutorService
 executor.shutdown();
 // Aguardar a finalização de todas as threads
 while (!executor.isTerminated()) {
 Thread.yield();
 }
 // Imprimir a matriz resultante
 printResultMatrix();
 }
 private static void initializeMatrices() {
 // Inicializar as matrizes com valores aleatórios
 for (int i = 0; i < SIZE; i++) {
 for (int j = 0; j < SIZE; j++) {
 matrixA[i][j] = (int) (Math.random() * 10);
 matrixB[i][j] = (int) (Math.random() * 10);
 }
 }
 }
 private static void printResultMatrix() {
 // Imprimir a matriz resultante
 for (int i = 0; i < SIZE; i++) {
 for (int j = 0; j < SIZE; j++) {
 System.out.print(resultMatrix[i][j] + " ");
 }
 System.out.println();
 }
 }
 private static class MatrixMultiplicationTask implements Runnable {
 private final int startIndex;
 private final int endIndex;
 public MatrixMultiplicationTask(int startIndex, int endIndex) {
 this.startIndex = startIndex;
 this.endIndex = endIndex;
 }
 @Override
 public void run() {
 // Multiplicar as matrizes parcialmente
 for (int i = startIndex; i < endIndex; i++) {
 for (int j = 0; j < SIZE; j++) {
 for (int k = 0; k < SIZE; k++) {
 resultMatrix[i][j] += matrixA[i][k] * matrixB[k][j];
 }
 }
 }
 }
 }
} 
Criamos uma classe ParallelMatrixMultiplication que realiza a multiplicação de matrizes usando 
programação paralela. A matriz resultante é armazenada na matriz resultMatrix. Nós dividimos a 
tarefa de multiplicação em várias threads usando ExecutorService e Runnable.
Na função main, inicializamos as matrizes matrixA e matrixB com valores aleatórios usando o 
método initializeMatrices(). Em seguida, criamos um ExecutorService com um número fixo de 
threads NUM_THREADS. Dividimos as linhas da matriz matrixA entre as threads e atribuímos uma 
tarefa de multiplicação a cada thread.
Cada thread executa a multiplicação das matrizes parcialmente no método run() da classe 
MatrixMultiplicationTask. Cada thread é responsável por um conjunto específico de linhas. Os 
resultados parciais são armazenados na matriz resultMatrix.
Após a finalização de todas as threads, imprimimos a matriz resultante usando o método 
printResultMatrix().
Exemplo em C:
#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#define SIZE 1000000
#define NUM_THREADS 4
int main() {
 int i;
 int sum = 0;
 int partial_sums[NUM_THREADS] = {0};
 int* vector = (int*)malloc(SIZE * sizeof(int));
 // Preenche o vetor com valores
 for (i = 0; i < SIZE; i++) {
 vector[i] = i + 1;
 }
 // Calcula a soma paralela
 #pragma omp parallel num_threads(NUM_THREADS)
 {
 int thread_id = omp_get_thread_num();
 int chunk_size = SIZE / NUM_THREADS;
 int start = thread_id * chunk_size;
 int end = start + chunk_size;
 // Calcula a soma parcial
 for (i = start; i < end; i++) {
 partial_sums[thread_id] += vector[i];
 }
 }
 // Soma os resultados parciais
 for (i = 0; i < NUM_THREADS; i++) {
 sum += partial_sums[i];
 }
 printf("Soma total: %d\n", sum);
 free(vector);
 return 0;
}
Utilizamos a biblioteca OpenMP para criar threads paralelas. A variável SIZE define o tamanho do 
vetor, e NUM_THREADS define o número de threads que serão utilizadas para realizar a soma 
paralela. A soma parcial de cada thread é armazenada no vetor partial_sums. No final, os 
resultados parciais são somados para obter a soma total.










