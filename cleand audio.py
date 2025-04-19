def clean_audio(path):
    sound = AudioSegment.from_wav(path)
    audio_chunks = split_on_silence(
        sound,
        min_silence_len=500,
        silence_thresh=sound.dBFS - 14,
        keep_silence=200
    )

    cleaned_audio = AudioSegment.empty()
    for chunk in audio_chunks:
        cleaned_audio += chunk

    cleaned_path = r"C:\Users\patil\cleaned_audio.wav"
    cleaned_audio.export(cleaned_path, format="wav")
    return cleaned_path