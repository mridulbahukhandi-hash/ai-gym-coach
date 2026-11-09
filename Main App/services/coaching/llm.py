from services.config.workout_config import PROMPT
from groq import AuthenticationError


class LLMCoach:
    def __init__(self, groq_client):
        self.client = groq_client
        self.history = []
        self.system_prompt = PROMPT
        self.auth_failed = False

    def give_feedback(self, event, issue):
        if self.auth_failed:
            return None
            
        try:
            prompt = f"Event: {event}"

            if issue:
                prompt += f" Form Issue: {issue}"

            messages = [
                {"role": "system", "content": self.system_prompt},
                *self.history[-10:],
                {"role": "user", "content": prompt}
            ]

            response = self.client.chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=messages,
                temperature=0.4,
            )

            text = response.choices[0].message.content.strip()
            self.history.append({"role": "assistant", "content": text})

            return text
        except AuthenticationError as e:
            self.auth_failed = True
            print(f"Groq API authentication failed: {e}")
            return None
    