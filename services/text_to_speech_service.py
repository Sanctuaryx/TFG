from TTS.api import TTS
import pyttsx3

class TTSConverter:
    def __init__(self, model_name: str):
        """
        Initialize the TTS model once.

        Args:
            model_name (str): The name of the TTS model to use.
        """
        self.tts = TTS(model_name)
        self.output_file = 'resources/audioResources/audioTracks/audio.wav'
        self.speaker_wav = 'resources/audioResources/speaker.wav'
        self.language = 'es'
        
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)  # Speed of speech
        self.engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)
        
        # Check and set the available voices
        voices = self.engine.getProperty('voices')
        for voice in voices:
            if 'spanish' in voice.languages:
                self.engine.setProperty('voice', voice.id)

    def convert_text_to_audio(self, text: str, speaker_wav: str = None, language: str = None):
        """
        Convert text to audio using the initialized TTS model.

        Args:
            text (str): Text to convert to speech.
            output_file (str): Path to the output audio file (typically ending in `.wav`).
            speaker_idx (int, optional): The ID of the specific speaker to use for synthesis.
        """
        if speaker_wav is not None and language is not None:
            self.tts.tts_to_file(text=text, file_path = self.output_file, speaker_wav=self.speaker_wav, language=self.language, split_sentences=True)
        else:
            self.tts.tts_to_file(text=text, file_path = self.output_file)
            
    def convert_text_to_audio_with_engine(self, text: str):
        """
        Convert text to audio using the initialized pyttsx3 model.

        Args:
            text (str): Text to convert to speech.
        """
        self.engine.save_to_file(text, "resources/audioResources/audioTracks/audio.wav")
        self.engine.runAndWait()