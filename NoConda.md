1- O QUE VOCE PRECISA:

- Ter o Anaconda ou Miniconda instalado 
- (se não tiver ainda, baixe: https://www.anaconda.com/download )
-  Uma imagem que contenha texto

2- CRIANDO O AMBIENTE

- Abra o terminal (ou Prompt do Anaconda) e digite:
-     conda create -n seu_ambiente python=3.10 -y

- Isso cria um ambiente chamado de, por exemplo, 'seu_ambiente' com Python 3.10.
   (O -y só confirma automaticamente.)

3- ATIVANDO O AMBIENTE 
- Ainda no terminal, ou no Prompt do Anaconda:
-      conda activate seu_ambiente

4- INSTALAÇÃO DAS LIBS

   4.1- ESCOLHA  UMA  OPÇÃO. Instale o Paddlepaddle
    -  OPÇÃO 1- CPU (pra quem NAO tem GPU NVIDIA): 
-     pip install paddlepaddle==2.6.1
   -   OPÇÃO 2- GPU (pra quem TEM GPU NVIDIA com CUDA):
-     pip install paddlepaddle-gpu==2.6.1.post118

 4.2- Instale o PaddleOCR
  -     pip install paddleocr==2.7.0.3
 
    
