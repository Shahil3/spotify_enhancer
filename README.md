# Spotify Enhancer

**Spotify Enhancer** is a Python script designed to expand your Spotify playlist based on your music preferences. The script interacts with the Spotify API to analyze your existing playlist, identify artists, and add top tracks from those artists to enhance your listening experience.

## Getting Started

### Prerequisites

1. Create a Spotify Developer account and register your application to obtain the client ID and client secret.
2. Set up a new Spotify playlist or use an existing one that you want to expand.

### Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your_username/spotify-enhancer.git
    cd spotify-enhancer
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

### Configuration

1. Create a `.env` file in the project directory with the following content:

    ```plaintext
    CLIENT_ID=your_spotify_client_id
    CLIENT_SECRET=your_spotify_client_secret
    PLAYLIST_ID=your_spotify_playlist_id
    REDIRECT_URI=your_redirect_uri
    ```

    Replace `your_spotify_client_id`, `your_spotify_client_secret`, `your_spotify_playlist_id`, and `your_redirect_uri` with your actual Spotify API credentials and playlist information.

## Usage

1. Run the `main.py` script:

    ```bash
    python main.py
    ```

2. Visit the authorization URL provided in the console and authorize your app.

3. Enter the authorization code from the callback URL back into the console.

4. Select the playlist you want to expand by typing its index.

5. Sit back and relax as the Spotify Enhancer adds top tracks from the artists in your playlist.

## Additional Information

- The script requests necessary Spotify API scopes for playlist modification. Ensure that your Spotify account has the required permissions.

- The project uses the `dotenv` library to manage environment variables. Make sure to keep your API credentials secure.

- Explore the `functions.py` file to understand the Spotify API interactions and functions used in the project.

## Disclaimer

This project is for educational purposes and personal use. Use it responsibly and in accordance with Spotify's terms of serv
