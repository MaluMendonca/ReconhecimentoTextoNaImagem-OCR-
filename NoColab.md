1- INSTALAÇÃO DAS LIBS:

 -     !pip install paddleocr paddlepaddle

2- IMPORTAÇÃO:
-      from paddleocr import PaddleOCR


3- UPLOAD:
-     from google.colab import files
      uploaded = files.upload()


4- CRIAR O MODELO:
-      ocr = PaddleOCR(lang='en')  # ou 'pt' para português


5- PROCESSAR A IMAGEM:
-      result = ocr.predict('teste.jpg')  # use o nome exato do arquivo

6- MOSTRAR OS TEXTOS RECONHECIDOS
-      textos = result[0]['rec_texts']
       confiancas = result[0]['rec_scores']

      print("✅ TEXTOS ENCONTRADOS:")
      print("=" * 40)

      for i, (texto, conf) in enumerate(zip(textos, confiancas)):
          print(f"{i}: '{texto}' - {conf:.1%}")

      print(f"\n🎯 Total: {len(textos)} textos reconhecidos")

