# Text2SpeechMultiLingualApp

## Description
Few days project to learn how to Text2Speech in languages including French, English, Chinese, Japanese, ... as well as learning how install Python and manage PATH variable on MacOS.

## Outcome
- Discovered [Coqui-TTS](https://github.com/coqui-ai/TTS) xtts_v2 model allowing to reproduce voice samples and use them to generate speech from text in multiple languages
   - The language of the voice samples used to generate the text doesn't limit the generated speech. Thus, a French speaker voice can be reproduced to speak Chinese for example.
- Learned about Python installation using homebrew on MacOS, as well as `yt-dlp` and `ffmpeg`.
- Collected anonymized samples from online videos and friends which are saved under speaker_samples/
- Generated samples in chinese, french and japanese from those anonymized samples

### Speaker Origins
- Jean, Jessica and Pierre are french,
- Kimura and Sato are famous japanese voice actors which I obtained through youtube interviews,
- Mingyi is a chinese friend.
(The names of the speaker samples are formatted as such: [fake_name]_[m/f].wav)

## External Ressources
- [xTTS_v2](https://huggingface.co/coqui/XTTS-v2)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [ffmpeg](https://github.com/FFmpeg/FFmpeg)