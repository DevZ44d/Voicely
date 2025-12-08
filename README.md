<p align="center">
    <img align="center" width="300" src="https://github.com/user-attachments/assets/1805d349-d03a-4087-aeca-2ed57a1b133a" />
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
    <img src="https://static.pepy.tech/personalized-badge/voicely?period=total&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=GREEN&left_text=downloads">
  </a>

  <a href="https://github.com/DevZ44d/voicely?tab=MIT-1-ov-file">
    <img src="https://camo.githubusercontent.com/30aa09995ff273a3a2a8abf7c116c6fadfb4737b6aac74fe8dcb03e93d855fef/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f7a3434642f79746d757369632d626f74">
  </a>
</p>


### 📘 voicely — Audio-to-Text + Translation for Python
> **Voicely** is a lightweight Python library that converts audio files → text and optionally translates the extracted text .

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

### Class Translation

- Simple Google Translate wrapper.
```python
from voicely.translation import Translation
T: str = Translation("ar" , "Hello, How are you ?")
# ar → arabic , en → english , ...
print(T["Text"])
# or
print(T.get())
```

- 📝 Output Example
```text
مرحبا, كيف حالك ؟
```

### 💬 Help & Support .
- Follow updates via the **[Telegram Channel](https://t.me/Pycodz)**.
- For general questions and help, join our **[Telegram chat](https://t.me/PyChTz)**.
- For general questions and help, join our **[Telegram chat](https://t.me/PyChTz)**.



