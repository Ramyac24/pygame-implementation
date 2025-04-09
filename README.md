# pygame-implementation


```hcl
escape_ai_lab/
├── game/                   
│   ├── __init__.py         # (empty or package marker)
│   ├── main.py             # Pygame game loop and level progression
│   ├── puzzles.py          # (optional: add extra puzzle logic)
│   └── dialogue.py         # (optional: for handling AI dialogue)
├── backend/                
│   ├── __init__.py         # (empty or package marker)
│   ├── app.py              # Flask API endpoints
│   └── utils.py            # (optional: additional backend helpers)
├── dashboard/              
│   └── streamlit_app.py    # Streamlit dashboard to show progress and clues
├── shared/                 
│   ├── state.py            # Module to manage persistent state (players, puzzles, clues)
│   └── state.json          # JSON file to hold initial state (auto-created if missing)
├── .env                    # Environment variables (e.g. your OpenAI API key)
├── requirements.txt        # Python dependency list
└── README.md               # Project documentation
```
