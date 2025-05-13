import openai

def generate_scientific_summary(equation, method, crit_points):
    prompt = f"""
You are an expert scientific assistant.
Given the equation: {equation}
And the selected numerical method: {method}
And the critical points found: {crit_points}
Write a brief scientific summary explaining:
- The type of behavior (nonlinear? snap-through? etc.)
- What do the critical points mean?
- Where can this type of analysis be applied?

Answer in plain English, clear and academic style.
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=400
    )
    return response.choices[0].message.content
