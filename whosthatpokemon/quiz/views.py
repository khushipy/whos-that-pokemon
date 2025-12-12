from django.shortcuts import render

# Create your views here.

# Define Pokémon types
TYPES = [
    "Fire", "Water", "Grass", "Electric", "Psychic",
    "Dark", "Fairy", "Ghost", "Fighting", "Ground",
]

# Quiz data (NO DATABASE NEEDED)
QUESTIONS = [
    {
        "id": 1,
        "text": "What environment do you prefer?",
        "options": [
            {"id": 1, "text": "Mountains / Hot places", "scores": {"Fire": 2}},
            {"id": 2, "text": "Near water", "scores": {"Water": 2}},
            {"id": 3, "text": "Forest", "scores": {"Grass": 2}},
            {"id": 4, "text": "Stormy / Electric areas", "scores": {"Electric": 2}},
        ]
    },
    {
        "id": 2,
        "text": "Your personality is mostly:",
        "options": [
            {"id": 5, "text": "Calm and peaceful", "scores": {"Water": 2}},
            {"id": 6, "text": "Energetic and bold", "scores": {"Fire": 2, "Electric": 1}},
            {"id": 7, "text": "Creative and thoughtful", "scores": {"Psychic": 2}},
            {"id": 8, "text": "Mysterious / introverted", "scores": {"Ghost": 2}},
        ]
    },
    {
        "id": 3,
        "text": "What motivates you?",
        "options": [
            {"id": 9, "text": "Helping others", "scores": {"Fairy": 2}},
            {"id": 10, "text": "Winning / competition", "scores": {"Fighting": 2}},
            {"id": 11, "text": "Solving problems", "scores": {"Psychic": 2}},
            {"id": 12, "text": "Stability & consistency", "scores": {"Ground": 2}},
        ]
    }
]


def home(request):
    return render(request, "quiz/home.html")


def quiz_page(request):
    return render(request, "quiz/quiz.html", {"questions": QUESTIONS})


def submit_quiz(request):
    if request.method != "POST":
        return render(request, "quiz/home.html")

    # Initialize scores
    scores = {t: 0 for t in TYPES}

    # Loop through the questions
    for q in QUESTIONS:
        answer_id = request.POST.get(f"question_{q['id']}")
        if answer_id:
            answer_id = int(answer_id)

            # Find the chosen option
            for opt in q["options"]:
                if opt["id"] == answer_id:
                    # Add scores
                    for type_name, val in opt["scores"].items():
                        scores[type_name] += val

    # Determine winner type
    result_type = max(scores, key=scores.get)

    return render(request, "quiz/result.html", {
        "result_type": result_type,
        "scores": scores
    })
