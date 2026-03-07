import random
import streamlit as st

def get_range_for_difficulty(difficulty: str):
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret:
            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score

st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮", layout="centered")

# ── Gaming CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@400;600&display=swap');

html, body, [data-testid="stAppViewContainer"] {
    background: #050510 !important;
}
[data-testid="stAppViewContainer"] {
    background: radial-gradient(ellipse at top, #0d0d2b 0%, #050510 60%) !important;
}
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0a0a20 0%, #050510 100%) !important;
    border-right: 1px solid #7b2fff44 !important;
}

/* Typography */
h1, h2, h3 { font-family: 'Orbitron', sans-serif !important; }
p, label, div { font-family: 'Rajdhani', sans-serif !important; }

/* Neon title */
.game-title {
    font-family: 'Orbitron', sans-serif;
    font-size: 2.6rem;
    font-weight: 900;
    text-align: center;
    background: linear-gradient(90deg, #00f5ff, #bf00ff, #ff006e, #00f5ff);
    background-size: 300% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: shine 4s linear infinite;
    text-shadow: none;
    margin-bottom: 0;
}
.game-subtitle {
    font-family: 'Rajdhani', sans-serif;
    text-align: center;
    color: #7b2fff99;
    font-size: 1rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-top: 0;
}
@keyframes shine {
    0%   { background-position: 0% center; }
    100% { background-position: 300% center; }
}

/* Cards */
.card {
    background: linear-gradient(135deg, #0d0d2b88, #1a0a3088);
    border: 1px solid #7b2fff55;
    border-radius: 16px;
    padding: 1.2rem 1.5rem;
    margin: 0.6rem 0;
    box-shadow: 0 0 20px #7b2fff22, inset 0 0 20px #00000033;
    backdrop-filter: blur(8px);
}
.card-cyan {
    border-color: #00f5ff55;
    box-shadow: 0 0 20px #00f5ff22, inset 0 0 20px #00000033;
}
.card-pink {
    border-color: #ff006e55;
    box-shadow: 0 0 20px #ff006e22, inset 0 0 20px #00000033;
}

/* Score display */
.score-box {
    text-align: center;
    font-family: 'Orbitron', sans-serif;
    font-size: 2rem;
    font-weight: 700;
    color: #00f5ff;
    text-shadow: 0 0 12px #00f5ff, 0 0 30px #00f5ff88;
}
.score-label {
    font-family: 'Rajdhani', sans-serif;
    color: #00f5ff88;
    font-size: 0.8rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    text-align: center;
}

/* Attempts bar */
.attempts-label {
    font-family: 'Rajdhani', sans-serif;
    color: #bf00ffcc;
    font-size: 0.85rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 4px;
}
.bar-track {
    background: #1a0a30;
    border-radius: 8px;
    height: 12px;
    border: 1px solid #7b2fff44;
    overflow: hidden;
}
.bar-fill {
    height: 100%;
    border-radius: 8px;
    background: linear-gradient(90deg, #00f5ff, #bf00ff);
    box-shadow: 0 0 8px #bf00ff;
    transition: width 0.4s ease;
}

/* History pills */
.history-wrap { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 6px; }
.guess-pill {
    font-family: 'Orbitron', sans-serif;
    font-size: 0.8rem;
    padding: 4px 12px;
    border-radius: 20px;
    background: #1a0a30;
    border: 1px solid #7b2fff66;
    color: #bf00ff;
    box-shadow: 0 0 6px #7b2fff44;
}

/* Buttons */
.stButton > button {
    font-family: 'Orbitron', sans-serif !important;
    font-size: 0.8rem !important;
    font-weight: 700 !important;
    border-radius: 8px !important;
    border: none !important;
    padding: 0.5rem 1.2rem !important;
    cursor: pointer !important;
    transition: all 0.2s ease !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
}
/* Submit button — cyan */
[data-testid="column"]:nth-child(1) .stButton > button {
    background: linear-gradient(135deg, #00f5ff, #0077ff) !important;
    color: #050510 !important;
    box-shadow: 0 0 14px #00f5ff88 !important;
}
[data-testid="column"]:nth-child(1) .stButton > button:hover {
    box-shadow: 0 0 24px #00f5ffcc !important;
    transform: translateY(-2px) !important;
}
/* New Game button — purple */
[data-testid="column"]:nth-child(2) .stButton > button {
    background: linear-gradient(135deg, #bf00ff, #7b2fff) !important;
    color: #fff !important;
    box-shadow: 0 0 14px #bf00ff88 !important;
}
[data-testid="column"]:nth-child(2) .stButton > button:hover {
    box-shadow: 0 0 24px #bf00ffcc !important;
    transform: translateY(-2px) !important;
}

/* Text input */
.stTextInput > div > div > input {
    background: #0d0d2b !important;
    border: 1px solid #7b2fff88 !important;
    border-radius: 8px !important;
    color: #00f5ff !important;
    font-family: 'Orbitron', sans-serif !important;
    font-size: 1.1rem !important;
    letter-spacing: 2px !important;
    caret-color: #00f5ff !important;
}
.stTextInput > div > div > input:focus {
    border-color: #00f5ff !important;
    box-shadow: 0 0 0 2px #00f5ff33 !important;
}
.stTextInput label {
    color: #bf00ffcc !important;
    font-family: 'Rajdhani', sans-serif !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    font-size: 0.85rem !important;
}

/* Checkbox */
.stCheckbox label { color: #7b7faa !important; font-size: 0.85rem !important; }

/* Sidebar labels */
[data-testid="stSidebar"] label, [data-testid="stSidebar"] .stMarkdown p {
    color: #bf00ffcc !important;
    font-family: 'Rajdhani', sans-serif !important;
    letter-spacing: 1px !important;
}
[data-testid="stSidebar"] .stSelectbox > div > div {
    background: #0d0d2b !important;
    border-color: #7b2fff55 !important;
    color: #00f5ff !important;
}

/* Alerts override */
[data-testid="stAlert"] {
    border-radius: 10px !important;
    font-family: 'Rajdhani', sans-serif !important;
    font-size: 1rem !important;
    letter-spacing: 1px !important;
}

/* Expander */
[data-testid="stExpander"] summary {
    font-family: 'Rajdhani', sans-serif !important;
    color: #7b2fff99 !important;
    letter-spacing: 1px !important;
}

/* Divider */
hr { border-color: #7b2fff33 !important; }

/* Scrollbar */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #050510; }
::-webkit-scrollbar-thumb { background: #7b2fff; border-radius: 3px; }
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown('<div class="game-title">🎮 GLITCH GUESSER</div>', unsafe_allow_html=True)
st.markdown('<div class="game-subtitle">// number hunting protocol //</div>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# ── Sidebar ───────────────────────────────────────────────────────────────────
st.sidebar.markdown("## ⚙️ SETTINGS")

difficulty = st.sidebar.selectbox(
    "DIFFICULTY LEVEL",
    ["Easy", "Normal", "Hard"],
    index=1,
)

attempt_limit_map = {
    "Easy": 6,
    "Normal": 8,
    "Hard": 5,
}
attempt_limit = attempt_limit_map[difficulty]

low, high = get_range_for_difficulty(difficulty)

difficulty_colors = {"Easy": "#00f5ff", "Normal": "#bf00ff", "Hard": "#ff006e"}
diff_color = difficulty_colors[difficulty]

st.sidebar.markdown(f"""
<div style="margin-top:12px;">
  <div style="color:{diff_color}; font-family:'Orbitron',sans-serif; font-size:1.3rem;
              text-shadow: 0 0 10px {diff_color}; text-align:center;">{difficulty.upper()}</div>
  <div style="color:#7b7faa; font-size:0.8rem; text-align:center; letter-spacing:2px; margin-top:4px;">
    RANGE: {low} – {high} &nbsp;|&nbsp; MAX ATTEMPTS: {attempt_limit}
  </div>
</div>
""", unsafe_allow_html=True)

# ── Session state init ────────────────────────────────────────────────────────
if "active_difficulty" not in st.session_state:
    st.session_state.active_difficulty = difficulty
if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "status" not in st.session_state:
    st.session_state.status = "playing"
if "history" not in st.session_state:
    st.session_state.history = []
if "game_id" not in st.session_state:
    st.session_state.game_id = 0

if st.session_state.active_difficulty != difficulty:
    st.session_state.active_difficulty = difficulty
    st.session_state.secret = random.randint(low, high)
    st.session_state.attempts = 0
    st.session_state.status = "playing"
    st.session_state.history = []
    st.session_state.game_id += 1

# ── HUD row: score + attempts bar ────────────────────────────────────────────
attempts_used = st.session_state.attempts
attempts_left = attempt_limit - attempts_used
bar_pct = int((attempts_used / attempt_limit) * 100) if attempt_limit else 0
bar_color = "#00f5ff" if bar_pct < 60 else ("#ffaa00" if bar_pct < 85 else "#ff006e")

hud_col1, hud_col2 = st.columns([1, 2])
with hud_col1:
    st.markdown(f"""
    <div class="card card-cyan" style="text-align:center; padding:1rem;">
        <div class="score-label">SCORE</div>
        <div class="score-box">{st.session_state.score}</div>
    </div>
    """, unsafe_allow_html=True)

with hud_col2:
    st.markdown(f"""
    <div class="card" style="padding:1rem;">
        <div class="attempts-label">Attempts &nbsp; {attempts_used} / {attempt_limit} &nbsp;
            <span style="color:#ff006e;">({attempts_left} left)</span>
        </div>
        <div class="bar-track">
            <div class="bar-fill" style="width:{bar_pct}%; background: linear-gradient(90deg, #00f5ff, {bar_color}); box-shadow: 0 0 8px {bar_color};"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ── Guess input area ──────────────────────────────────────────────────────────
st.markdown(f"""
<div class="card card-cyan" style="text-align:center; padding:0.8rem 1.5rem 0.4rem;">
    <span style="font-family:'Rajdhani',sans-serif; color:#00f5ffaa; letter-spacing:3px; font-size:0.85rem; text-transform:uppercase;">
    🎯 Guess a number between
    </span>
    <span style="font-family:'Orbitron',sans-serif; color:#00f5ff; font-size:1.2rem;
                 text-shadow:0 0 10px #00f5ff;"> {low} </span>
    <span style="color:#7b7faa;">—</span>
    <span style="font-family:'Orbitron',sans-serif; color:#bf00ff; font-size:1.2rem;
                 text-shadow:0 0 10px #bf00ff;"> {high}</span>
</div>
""", unsafe_allow_html=True)

debug_slot = st.empty()

raw_guess = st.text_input(
    "ENTER YOUR NUMBER",
    key=f"guess_input_{difficulty}_{st.session_state.game_id}",
    placeholder=f"Type a number ({low}–{high})…"
)

col1, col2, col3 = st.columns([2, 2, 1])
with col1:
    submit = st.button("⚡ FIRE GUESS", use_container_width=True)
with col2:
    new_game = st.button("↺ NEW GAME", use_container_width=True)
with col3:
    show_hint = st.checkbox("Hint", value=True)

# ── New game reset ────────────────────────────────────────────────────────────
if new_game:
    st.session_state.attempts = 0
    st.session_state.secret = random.randint(low, high)
    st.session_state.status = "playing"
    st.session_state.history = []
    st.session_state.game_id += 1
    st.rerun()

# ── Game over screen ──────────────────────────────────────────────────────────
if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.markdown("""
        <div class="card card-cyan" style="text-align:center; padding:1.5rem;">
            <div style="font-family:'Orbitron',sans-serif; font-size:1.8rem; color:#00f5ff;
                        text-shadow:0 0 20px #00f5ff, 0 0 40px #00f5ff;">
                🏆 VICTORY!
            </div>
            <div style="color:#7b7faa; margin-top:6px; font-family:'Rajdhani',sans-serif; letter-spacing:2px;">
                Start a new game to play again
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="card card-pink" style="text-align:center; padding:1.5rem;">
            <div style="font-family:'Orbitron',sans-serif; font-size:1.8rem; color:#ff006e;
                        text-shadow:0 0 20px #ff006e, 0 0 40px #ff006e;">
                💀 GAME OVER
            </div>
            <div style="color:#7b7faa; margin-top:6px; font-family:'Rajdhani',sans-serif; letter-spacing:2px;">
                Start a new game to try again
            </div>
        </div>
        """, unsafe_allow_html=True)

    with debug_slot.container():
        with st.expander("🛠 Developer Debug Info"):
            st.write("Secret:", st.session_state.secret)
            st.write("Attempts:", st.session_state.attempts)
            st.write("Score:", st.session_state.score)
            st.write("Difficulty:", difficulty)
            st.write("History:", st.session_state.history)
    st.stop()

# ── Submit guess logic ────────────────────────────────────────────────────────
if submit:
    ok, guess_int, err = parse_guess(raw_guess)

    if not ok:
        st.error(f"⚠️ {err}")
    elif guess_int is None or guess_int < low or guess_int > high:
        st.error(f"⚠️ Number must be between {low} and {high}.")
    else:
        st.session_state.attempts += 1
        st.session_state.history.append(guess_int)

        if st.session_state.attempts % 2 == 0:
            secret = str(st.session_state.secret)
        else:
            secret = st.session_state.secret

        outcome, message = check_guess(guess_int, secret)

        if show_hint:
            if outcome == "Too High":
                st.markdown(f"""
                <div class="card card-pink" style="text-align:center; padding:0.8rem;">
                    <span style="font-family:'Orbitron',sans-serif; color:#ff006e; font-size:1.1rem;
                                 text-shadow:0 0 10px #ff006e;">{message} — go lower!</span>
                </div>""", unsafe_allow_html=True)
            elif outcome == "Too Low":
                st.markdown(f"""
                <div class="card card-cyan" style="text-align:center; padding:0.8rem;">
                    <span style="font-family:'Orbitron',sans-serif; color:#00f5ff; font-size:1.1rem;
                                 text-shadow:0 0 10px #00f5ff;">{message} — go higher!</span>
                </div>""", unsafe_allow_html=True)

        st.session_state.score = update_score(
            current_score=st.session_state.score,
            outcome=outcome,
            attempt_number=st.session_state.attempts,
        )

        if outcome == "Win":
            st.balloons()
            st.session_state.status = "won"
            st.markdown(f"""
            <div class="card card-cyan" style="text-align:center; padding:1.2rem;">
                <div style="font-family:'Orbitron',sans-serif; font-size:1.5rem; color:#00f5ff;
                            text-shadow:0 0 16px #00f5ff;">🏆 YOU WIN!</div>
                <div style="color:#7b7faa; font-family:'Rajdhani',sans-serif; margin-top:4px; font-size:1rem;">
                    The secret was <span style="color:#bf00ff; font-weight:bold;">{st.session_state.secret}</span>
                    &nbsp;·&nbsp; Final score:
                    <span style="color:#00f5ff; font-weight:bold;">{st.session_state.score}</span>
                </div>
            </div>""", unsafe_allow_html=True)
        else:
            if st.session_state.attempts >= attempt_limit:
                st.session_state.status = "lost"
                st.markdown(f"""
                <div class="card card-pink" style="text-align:center; padding:1.2rem;">
                    <div style="font-family:'Orbitron',sans-serif; font-size:1.5rem; color:#ff006e;
                                text-shadow:0 0 16px #ff006e;">💀 OUT OF ATTEMPTS!</div>
                    <div style="color:#7b7faa; font-family:'Rajdhani',sans-serif; margin-top:4px; font-size:1rem;">
                        The secret was <span style="color:#bf00ff; font-weight:bold;">{st.session_state.secret}</span>
                        &nbsp;·&nbsp; Score:
                        <span style="color:#ff006e; font-weight:bold;">{st.session_state.score}</span>
                    </div>
                </div>""", unsafe_allow_html=True)

# ── Guess history ─────────────────────────────────────────────────────────────
if st.session_state.history:
    pills = "".join(
        f'<span class="guess-pill">{g}</span>' for g in st.session_state.history
    )
    st.markdown(f"""
    <div class="card" style="margin-top:1rem;">
        <div style="color:#7b2fff99; font-family:'Rajdhani',sans-serif; font-size:0.8rem;
                    letter-spacing:3px; text-transform:uppercase; margin-bottom:8px;">
            📋 Guess History
        </div>
        <div class="history-wrap">{pills}</div>
    </div>
    """, unsafe_allow_html=True)

# ── Debug expander ────────────────────────────────────────────────────────────
with debug_slot.container():
    with st.expander("🛠 Developer Debug Info"):
        st.write("Secret:", st.session_state.secret)
        st.write("Attempts:", st.session_state.attempts)
        st.write("Score:", st.session_state.score)
        st.write("Difficulty:", difficulty)
        st.write("History:", st.session_state.history)

st.markdown("""
<div style="text-align:center; margin-top:2rem; color:#7b2fff44;
            font-family:'Rajdhani',sans-serif; font-size:0.75rem; letter-spacing:3px;">
    BUILT BY AN AI · GLITCH PROTOCOL v1.0
</div>
""", unsafe_allow_html=True)
