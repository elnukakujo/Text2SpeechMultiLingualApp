from TTS.api import TTS

xtts_v2 = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2")

xtts_v2.tts_to_file(
    "こんにちは、お元気ですか？",
    speaker_wav="speaker_samples/japanese_male.wav",
    file_path="generated_samples/japanese_male.wav",
    language="ja",
    emotion="happy"
)

xtts_v2.tts_to_file(
    "你好，你好吗？",
    speaker_wav="speaker_samples/japanese_male.wav",
    file_path="generated_samples/chinese_male.wav",
    language="zh",
    emotion="happy"
)