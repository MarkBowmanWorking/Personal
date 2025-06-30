import openai
import config

def generate_cover_letter(job_ad_text, resume_text):
    openai.api_key = config.OPENAI_API_KEY
    prompt = f"""Write a tailored cover letter for this job:

    Job Ad:
    {job_ad_text}

    Resume:
    {resume_text}
    """

    response = openai.ChatCompletion.create(
        model=config.MODEL,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=800,
        temperature=0.7
    )

    return response.choices[0].message.content
