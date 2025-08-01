import whisper

def stt(audio): 
    
    model = whisper.load_model("tiny.en")
    result = model.transcribe(audio)
    return result["text"]

