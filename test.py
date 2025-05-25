from TTS.api import TTS

xtts_v2 = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2")

xtts_v2.tts_to_file(
    "你把门打开吧！我进不来！",
    speaker_wav="speaker_samples/mingyi_f.wav",
    file_path="generated_samples/mingyi_chinese.wav",
    language="zh",
    emotion="happy",
    speed=0.95,
)
xtts_v2.tts_to_file(
    "Salut! Comment ça va? Tu es en train de programme?",
    speaker_wav="speaker_samples/mingyi_f.wav",
    file_path="generated_samples/mingyi_french.wav",
    language="fr",
    emotion="happy",
    speed=0.95,
)
"""xtts_v2.tts_to_file(
    "おはよう！元気で？今コディングをして要る？",
    speaker_wav="speaker_samples/jean_m.wav",
    file_path="generated_samples/jean_japanese.wav",
    language="ja",
    emotion="happy",
    speed=0.95,
)"""