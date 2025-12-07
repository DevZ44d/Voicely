<p align="center">
    <img align="center" width="300" src="https://github.com/user-attachments/assets/8cc5443d-4108-4cba-ad9d-c9bf327dec32" />
    <h3 align="center"></h3>
</p>

<p align="center">
  <a href="https://pypi.org/project/voicely/">
    <img src="https://img.shields.io/pypi/v/voicely.svg?logo=python&logoColor=%23959DA5&label=pypi&labelColor=%23282f37">
  </a>
  
  <a href="https://t.me/PyCodz">
    <img src="https://img.shields.io/badge/Telegram-Channel-blue.svg?logo=telegram">
  </a>
    
  <a href="https://t.me/PyChTz" target="_blank">
    <img alt="Telegram-Discuss" src="https://img.shields.io/badge/Telegram-Discuss-blue.svg?logo=telegram" />
  </a>
</p>

<p align="center">

  <a href="https://pepy.tech/projects/voicely/">
    <img src="https://static.pepy.tech/badge/voicely">
  </a>

  <a href="https://github.com/DevZ44d/PyTaudio?tab=MIT-1-ov-file">
    <img src="https://camo.githubusercontent.com/30aa09995ff273a3a2a8abf7c116c6fadfb4737b6aac74fe8dcb03e93d855fef/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f7a3434642f79746d757369632d626f74">
  </a>
</p>

### 📘 voicely — Audio-to-Text + Translation for Python
> **voicely** is a lightweight Python library that converts audio files → text and optionally translates the extracted text .

### 🚀 Features
- 🎤 Audio → Text .

- 🌍 Automatic translation using Google Translate endpoint .

- 🔁 Supports any target language .

- ⚡ Fast, minimal, and dependency-light .

- 🧩 Simple class-based interface .


### 📦 Installation

- Clone the project:
```shell
git clone https://github.com/DevZ44d/voicely.git
cd voicely
```

- Via PyPi
```shell
pip install voicely -U
```

### 🧠 Usage Example
- 🔊 Convert audio to text + translate to Arabic
```python
from voicely import Audio
def main() -> str:
    audio = Audio(
        audio="audio.mp3", # Hello, How are you ?
        Translation_To="ar"
    )
    
    print(audio.start())  # → returns translated text
    print(audio.extract_text) # → returns extract text → Hello, How are you ?
    
if __name__ == '__main__':
  main()
```

- 📝 Output Example
```text
مرحبا كيف حالك ؟
```

### Class Translation

- Simple Google Translate wrapper.
```python
from voicely.translation import Translation
print(Translation("ar", "hello").get())
```

### 💬 Help & Support .
- Follow updates via the **[Telegram Channel](https://t.me/Pycodz)**.
- For general questions and help, join our **[Telegram chat](https://t.me/PyChTz)**.