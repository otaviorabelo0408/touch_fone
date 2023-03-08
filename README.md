# touch_fone
Implementação da função touch_fone, que a partir de um sinal sonoro discretizado, obtém um número de telefone discado (cada tecla emite um som característico).
O algoritmo se encontra lento, pois para sua elaboração implementou-se antes a DFT (Discret Fourier Transform), que possui complexidade computacional elevada. A nível de otimização de tempo, pode-se substituir essa função pela FFT (Fast Fourier Transform), disponível através, por exemplo, das bibliotecas numpy e scipy.
