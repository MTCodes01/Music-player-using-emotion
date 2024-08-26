document.addEventListener('DOMContentLoaded', (event) => {
    const emotionDisplay = document.getElementById('emotion');
    const video = document.getElementById('video');

    // Function to update the emotion display
    async function updateEmotion() {
        const response = await fetch('/get_emotion');
        const data = await response.json();
        emotionDisplay.innerText = data.emotion;
    }

    // Start fetching the emotion periodically
    setInterval(updateEmotion, 1000);  // Update every second

    // Stream the video feed from Flask to the video element
    video.src = '/video_feed';
    video.play();
});
