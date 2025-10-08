1- INSTALAÇÃO DAS LIBS:

 -     !pip install paddleocr paddlepaddle

2- IMPORTAÇÃO:
-      from paddleocr import PaddleOCR


3- UPLOAD:
-     from google.colab import files
      uploaded = files.upload()


4- CRIAR O MODELO:
-      ocr = PaddleOCR(lang='en')


5- PROCESSAR A IMAGEM:
-      result = ocr.ocr(list(uploaded.keys())[0])  # use o nome exato do arquivo

6- MOSTRAR OS TEXTOS RECONHECIDOS
-      if result and result[0]:
           print("✅ TEXTO RECONHECIDO:")
           for i, line in enumerate(result[0]):
               texto = line[1][0]
               confianca = line[1][1]
                print(f"{i}: '{texto}' - {confianca:.1%}")
    

