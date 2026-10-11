import gradio as gr
from transformers import pipeline

transcritor = pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-small",
    chunk_length_s=30,
)


def transcrever(caminho_audio):
    if caminho_audio is None:
        return "Envie ou grave um áudio primeiro."
    resultado = transcritor(
        caminho_audio,
        generate_kwargs={"language": "portuguese", "task": "transcribe"},
    )
    return resultado["text"]


app = gr.Interface(
    fn=transcrever,
    inputs=gr.Audio(
        sources=["upload", "microphone"],
        type="filepath",
        label="Seu áudio",
    ),
    outputs=gr.Textbox(label="Transcrição"),
    title="Audio to text",
    description="Upload or record an audio and get the transcription in Portuguese.",
)

app.launch()