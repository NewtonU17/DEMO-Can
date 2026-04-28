import streamlit as st
import json

st.set_page_config(page_title="AI Engineer Evaluation Form", layout="wide")

st.title("🧩 AI Engineer Candidate Evaluation")

st.markdown("Select the appropriate score (1–5) for each category and optionally provide evidence.")

# ---------- Helper ----------
def score_select(label):
    return st.selectbox(
        label,
        options=[
            "1 - None / Very Weak",
            "2 - Basic",
            "3 - Intermediate",
            "4 - Strong",
            "5 - Expert"
        ]
    )

def extract_score(selection):
    return int(selection.split(" - ")[0])

uploaded_files = st.file_uploader(
    "Upload CV", accept_multiple_files="directory", type=["pdf", "png"]
)
for uploaded_file in uploaded_files:
    st.image(uploaded_file)
# ---------- TECHNICAL ----------
st.header("🧠 Technical Skills")

ml_fund = score_select("ML Fundamentals")
ml_fund_ev = st.text_area("Evidence (ML Fundamentals)")

applied_ml = score_select("Applied ML / Modeling")
applied_ml_ev = st.text_area("Evidence (Applied ML)")

software_eng = score_select("Software Engineering")
software_eng_ev = st.text_area("Evidence (Software Engineering)")

mlops = score_select("Systems & MLOps")
mlops_ev = st.text_area("Evidence (MLOps)")

research = score_select("Research & Innovation (optional)")
research_ev = st.text_area("Evidence (Research)")

# ---------- BEHAVIORAL ----------
st.header("🤝 Behavioral Skills")

problem_solving = score_select("Problem Solving")
problem_solving_ev = st.text_area("Evidence (Problem Solving)")

communication = score_select("Communication")
communication_ev = st.text_area("Evidence (Communication)")

ownership = score_select("Ownership & Execution")
ownership_ev = st.text_area("Evidence (Ownership)")

collaboration = score_select("Collaboration")
collaboration_ev = st.text_area("Evidence (Collaboration)")

learning = score_select("Learning Agility")
learning_ev = st.text_area("Evidence (Learning Agility)")

# ---------- ENGLISH ----------
st.header("🌍 Language")

english = score_select("English Proficiency")
english_ev = st.text_area("Evidence (English)")

# ---------- SUBMIT ----------
st.header("📊 Results")

if st.button("Generate Evaluation"):

    scores = {
        "ML Fundamentals": {
            "score": extract_score(ml_fund),
            "evidence": ml_fund_ev
        },
        "Applied ML": {
            "score": extract_score(applied_ml),
            "evidence": applied_ml_ev
        },
        "Software Engineering": {
            "score": extract_score(software_eng),
            "evidence": software_eng_ev
        },
        "MLOps": {
            "score": extract_score(mlops),
            "evidence": mlops_ev
        },
        "Research": {
            "score": extract_score(research),
            "evidence": research_ev
        },
        "Problem Solving": {
            "score": extract_score(problem_solving),
            "evidence": problem_solving_ev
        },
        "Communication": {
            "score": extract_score(communication),
            "evidence": communication_ev
        },
        "Ownership": {
            "score": extract_score(ownership),
            "evidence": ownership_ev
        },
        "Collaboration": {
            "score": extract_score(collaboration),
            "evidence": collaboration_ev
        },
        "Learning Agility": {
            "score": extract_score(learning),
            "evidence": learning_ev
        },
        "English": {
            "score": extract_score(english),
            "evidence": english_ev
        }
    }

    # Simple aggregates
    technical_keys = ["ML Fundamentals", "Applied ML", "Software Engineering", "MLOps", "Research"]
    behavioral_keys = ["Problem Solving", "Communication", "Ownership", "Collaboration", "Learning Agility"]

    technical_avg = sum(scores[k]["score"] for k in technical_keys) / len(technical_keys)
    behavioral_avg = sum(scores[k]["score"] for k in behavioral_keys) / len(behavioral_keys)

    general_score = 0.5 * technical_avg + 0.4 * behavioral_avg + 0.1 * scores["English"]["score"]

    result = {
        "scores": scores,
        "aggregates": {
            "technical_avg": round(technical_avg, 2),
            "behavioral_avg": round(behavioral_avg, 2),
            "general_score": round(general_score, 2)
        }
    }

    st.subheader("📌 Summary Scores")
    st.write(result["aggregates"])

    st.subheader("📄 Full JSON Output")
    st.json(result)
