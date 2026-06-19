# AI Real-time GYM Coach

A real-time AI-powered fitness coaching application that uses pose detection and computer vision to analyze your workout form and provide instant feedback. Built with Streamlit, MediaPipe, and Groq AI.

## Features

- **Real-time Pose Detection**: Uses MediaPipe to detect body landmarks in real-time via webcam
- **Exercise Support**: 
  - Squats (knee angle, back angle, depth tracking)
  - Push-ups (elbow angle, body alignment, hip position)
  - Biceps Curls (elbow angle, shoulder stability, swing detection)
  - Shoulder Press (elbow angle, arm extension, back arch)
  - Lunges (front knee angle, torso angle, balance)
- **AI Voice Coaching**: Real-time audio feedback using Groq API and text-to-speech
- **Metrics Tracking**: Automatically logs reps, sets, and workout duration
- **Workout History**: View past workouts and aggregate statistics
- **User Authentication**: Simple username-based login system
- **Live Video Feedback**: Visual overlays showing exercise metrics on camera feed

## Project Structure

```
├── Main App/
│   ├── main.py                    # Streamlit app entry point
│   ├── requirements.txt           # Python dependencies
│   ├── ml_models/
│   │   └── pose_landmarker_full.task  # MediaPipe pose detection model
│   ├── core/
│   │   └── base_exercise.py      # Base exercise detector class
│   ├── detectors/
│   │   ├── squat.py
│   │   ├── pushup.py
│   │   ├── biceps_curl.py
│   │   ├── shoulder_press.py
│   │   └── lunges.py
│   └── services/
│       ├── auth/                  # Login wall
│       ├── coaching/              # LLM & voice pipeline
│       ├── config/                # Workout configuration
│       ├── persistence/           # SQLite database
│       ├── state/                 # Session state defaults
│       ├── tracking/              # Metrics tracking
│       ├── ui/                    # UI styling
│       └── vision/                # Video processing
├── LandingPage/
│   ├── index.html
│   └── style.css
└── .env                           # Environment variables (API keys)
```

## Installation

### Prerequisites

- Python 3.12+
- pip
- Webcam
- Groq API key (optional - voice coaching works without it)

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/shradha-khapra/ai-gym-coach.git
   cd ai-gym-coach
   ```

2. **Create a Python virtual environment**
   ```bash
   python -m venv venv
   
   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r "Main App/requirements.txt"
   ```

4. **Configure Groq API Key (Optional)**
   - Create or edit `.env` file in the project root:
     ```
     GROQ_API_KEY=your_groq_api_key_here
     ```
   - Get your free API key from [Groq Console](https://console.groq.com)
   - **IMPORTANT**: Never commit `.env` to GitHub. The `.gitignore` file already protects it.
   - If no API key is provided, voice coaching will be disabled but the app still works

5. **Run the application**
   ```bash
   cd "Main App"
   streamlit run main.py
   ```
   The app will open at `http://localhost:8501`

## Usage

1. **Login**: Enter a unique username to start a session
2. **Select Workout**: Choose an exercise, number of sets, and reps per set
3. **Start Workout**: Click "Start Workout" to activate the camera
4. **Perform Exercise**: The AI will detect your form and provide real-time feedback
5. **View Metrics**: Check exercise-specific metrics and form quality
6. **End Workout**: Click "End Workout" to save your session
7. **Review History**: View past workouts in the "Workout History" section

## Technologies Used

- **Streamlit**: Web app framework
- **MediaPipe**: Pose detection & landmark tracking
- **OpenCV**: Video processing
- **Groq API**: LLM-powered coaching feedback
- **gTTS**: Text-to-speech for voice coaching
- **SQLite**: Workout history storage
- **Pandas**: Data aggregation & display

## API Dependencies

- **Groq API** (Optional): For AI coaching feedback
  - Sign up at https://console.groq.com
  - Get a free API key
  - Add to `.env` file as `GROQ_API_KEY`

## Database

The app uses SQLite to store:
- User information
- Workout history (exercise type, reps, sets, duration)
- Exercise session details

Database is automatically initialized on first run.

## Troubleshooting

### Port Already in Use
If port 8501 is already in use, run:
```bash
streamlit run main.py --server.port 8502
```

### Missing Model File
Ensure `Main App/ml_models/pose_landmarker_full.task` exists. The model is downloaded automatically on first run if missing.

### Voice Coaching Not Working
- Check that `GROQ_API_KEY` is set in `.env`
- Verify microphone/speaker permissions
- Test without voice coaching (app still works)

### Camera Not Starting
- Grant webcam permissions to Python
- Ensure no other app is using the camera
- Try a different browser or close other camera apps

## Future Enhancements

- [ ] Support for more exercises
- [ ] Personal form improvement suggestions
- [ ] Workout plan recommendations
- [ ] Progress analytics dashboard
- [ ] Mobile app support
- [ ] Multiple user profiles

## License

This project is built for educational and fitness purposes.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## Support

For issues or feature requests, please create an issue in the GitHub repository.