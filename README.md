# Home-Assistant-Music-Daemon
Home Assistant Music Daemon 

### Home Assistant Music Daemon Component

Welcome! You've stumbled upon the Music Daemon component for Home Assistant—a project that's designed to give you seamless control over your music playback across a variety of devices directly from Home Assistant. Whether it's playing your local files or Spotify tracks on Chromecast, Sonos, AirPlay, or LinkPlay devices, this integration has you covered. Plus, it even has VB-CABLE support! (i think)

if uou xan nake use, then just vlobe abd enjoy, play with. 

#### #WhatDoesItDo

This custom component lets you:

- **Play music from local files or Spotify**: Automatically check for local files first and fall back to Spotify if they're not found.
  
- **Control various devices**: Whether you've got Chromecast, Sonos, AirPlay, or LinkPlay speakers, you can play your music through them easily.
  
- **Use a web interface**: We've included a simple web interface to make controlling your music even easier.
  
- **Leverage VB-CABLE**: If you’re using VB-CABLE, this component can work with it for your audio routing needs.

#### #SettingItUp

Getting this up and running involves a few steps, but I promise it's worth it. Here’s how you do it:

1. **Clone the Repository**: Start by grabbing the code from GitHub.

    ```bash
    git clone https://github.com/yourusername/music-daemon.git
    cd music-daemon
    ```

2. **Create Environment Variables**: You'll need a `.env` file for your Spotify credentials.

    ```
    SPOTIPY_CLIENT_ID=your_spotify_client_id
    SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
    SPOTIPY_REDIRECT_URI=http://localhost:5000/callback
    ```

3. **Build the Docker Image**: Create the Docker image using the command below.

    ```bash
    docker build -t music-daemon .
    ```

4. **Run the Docker Container**: Finally, spin up the Docker container with your environment variables.

    ```bash
    docker run -d -p 5000:5000 --env-file .env music-daemon
    ```

#### #HowToUseIt

Once everything’s up and running, here’s how to start jamming out:

1. **Open the Web Interface**: Head over to `http://localhost:5000` in your browser.

2. **Select Your Device**: Choose from Chromecast, Sonos, AirPlay, LinkPlay, or whatever else you’ve got set up.

3. **Enter File Path or Spotify URI**:
    - **Local File**: Type in the path to the local file you want to play.
    - **Spotify**: Paste the Spotify track URI.

4. **Hit Play**: Click the "Play" button, sit back, and enjoy your music.

5. **Stop Music**: When you’re done, just hit "Stop" to pause the playback.

#### #AdditionalConfig

Want to use VB-CABLE? No problem! Here’s how:

- **Install VB-CABLE**: Grab it from the official site and install it.

- **Configure Audio Settings**: Set your audio source to 'VB-CABLE Input' and your speakers to 'VB-CABLE Output'.

#### #TheCodeBreakdown

Here’s what each file in this component does:

- **`__init__.py`**: This file kicks off the component, handling initialization and setup.

- **`manifest.json`**: Contains metadata like the component name, version, and dependencies.

- **`config_flow.py`**: Manages the configuration flow in the Home Assistant UI.

- **`services.yaml`**: Defines custom services like `play_music` and `stop_music`.

- **`strings.json` & `translation/en.json`**: These are your text strings for localization and translation.

- **`media_player.py`**: The main logic for controlling media playback, supporting Chromecast, Sonos, and more.

- **`airplay.py`**: Handles AirPlay-specific functionality.

- **`linkplay.py`**: Handles LinkPlay-specific functionality.

- **`.env.example`**: A sample environment variable file to guide your setup.

---

So there you have it! its laye ur early 6am im knackered. so enjiy and use freely. 

it's an info dump of udeas nothing more. 

This component should give you a lot of flexibility and power to control your home audio experience directly from Home Assistant. Feel free to fork the project, contribute, or just enjoy the music! 🎶

#### #HappyListening #OpenSource #HomeAssistant #MusicDaemon
