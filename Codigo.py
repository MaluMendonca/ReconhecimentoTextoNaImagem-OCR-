from paddleocr import PaddleOCR

ocr = PaddleOCR(lang='en')

result = ocr.ocr('Pictures/testar.jpeg')

print("✅ TEXTO RECONHECIDO:")
print("=" * 40)

if result and result[0]:
    for i, line in enumerate(result[0]):
        texto = line[1][0]  # Texto reconhecido
        confianca = line[1][1]  # Confiança
        print(f"{i}: '{texto}' - {confianca:.1%}")

    print(f"\n🎯 Total: {len(result[0])} textos reconhecidos")
else:
    print("❌ Nenhum texto encontrado")
