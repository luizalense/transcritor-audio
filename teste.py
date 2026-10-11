from transformers import pipeline

print("Carregando o modelo (na primeira vez ele é baixado)...")

transcritor = pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-small",
    chunk_length_s=30,
)

resultado = transcritor(
    "meu_audio2.ogg",
    generate_kwargs={"language": "portuguese", "task": "transcribe"},
)

print("Transcrição:")
print(resultado["text"])