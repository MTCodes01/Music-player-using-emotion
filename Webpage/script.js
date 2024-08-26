window.onSpotifyWebPlaybackSDKReady = () => {
    const token = 'YOUR_SPOTIFY_AUTH_TOKEN'; // Replace with your actual token

    const player = new Spotify.Player({
        name: 'Emotion-based Music Player',
        getOAuthToken: cb => { cb(token); },
        volume: 0.5
    });

    // Connect to the player!
    player.connect();

    player.addListener('player_state_changed', state => {
        if (!state) return;
        document.getElementById('song-title').textContent = state.track_window.current_track.name;
        document.getElementById('artist-name').textContent = state.track_window.current_track.artists.map(artist => artist.name).join(', ');
        document.getElementById('album-art').src = state.track_window.current_track.album.images[0].url;
    });

    // Controls
    document.getElementById('play-btn').onclick = () => {
        player.togglePlay();
    };

    document.getElementById('prev-btn').onclick = () => {
        player.previousTrack();
    };

    document.getElementById('next-btn').onclick = () => {
        player.nextTrack();
    };

    // WebSocket or other method to communicate with Python
    const socket = new WebSocket('ws://localhost:8000');

    socket.onmessage = function (event) {
        const emotion = event.data;
        document.getElementById('emotion').textContent = emotion;
        // Add logic to influence music based on emotion
    };
};
