from groq import Groq
from setting import settings

def classify_lost_item(image_url: str) -> str:
    client = Groq(api_key=settings.GROQ_API_KEY)

    completion = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[
            {
                "role": "system",
                "content": "넌 분실물 관리 시스템의 분실물 분류 AI야. 사진에 있는 물체를 한국어 한 (명사형, 필요시 추가적인 형. ex:파란색 에어팟 케이스, 에어팟 케이스)으로 분류해줘. 사진은 분실물 관리 시스템에 등록된 분실물 사진이야."
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_url
                        }
                    }
                ]
            }
        ]
    )

    return completion.choices[0].message.content