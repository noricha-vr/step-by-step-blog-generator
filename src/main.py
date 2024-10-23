import os
import json
from pprint import pprint
from blog_generator import BlogGenerator
if __name__ == "__main__":
    api_key = os.getenv("OPENAI_API_KEY")
    print(api_key)
    generator = BlogGenerator(api_key)
    theme = input("ブログのテーマを入力してください: ")
    result = generator.create_blog(theme)
    print("\n最終結果:")
    pprint(result)
    json.dump(result, open("result.json", "w"), indent=4)