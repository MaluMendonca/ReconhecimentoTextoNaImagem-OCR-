from paddleocr import PaddleOCR

ocr = PaddleOCR(lang='en') 

result = ocr.predict('Pasta/sua-imagem.jpg') #aqui voce troca pelo caminho da sua imagem

# Extrair textos 
textos = result[0]['rec_texts'] 
confiancas = result[0]['rec_scores'] 
print("✅ TEXTO RECONHECIDO:") 
print("=" * 40) 

for i, (texto, confianca) in enumerate(zip(textos, confiancas)): 
  print(f"{i}: '{texto}' - {confianca:.1%}") 
print(f"\n🎯 Total: {len(textos)} textos reconhecidos")
