import os
import openai
from typing import List, Dict
import json


class BlogGenerator:
    def __init__(self, api_key: str):
        """Initialize the blog generator with OpenAI API key."""
        self.client = openai.Client(api_key=api_key)
        self.blog_data = {}

    def generate_titles(self, theme: str, num_titles: int = 5) -> List[str]:
        """Generate multiple titles based on the theme."""
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": f"テーマ「{theme}」に関する魅力的なブログタイトルを{num_titles}個生成してください。"
            }]
        )
        titles = response.choices[0].message.content.split('\n')
        return [title.strip() for title in titles if title.strip()]

    def generate_headings(self, title: str, num_headings: int = 5) -> List[str]:
        """Generate headings for the selected title."""
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": f"タイトル「{title}」の記事に適切な見出しを{num_headings}個生成してください。"
            }]
        )
        headings = response.choices[0].message.content.split('\n')
        return [heading.strip() for heading in headings if heading.strip()]

    def generate_content(self, title: str, heading: str, user_prompt: str = "") -> str:
        """Generate content for a specific heading."""
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": f"タイトル「{title}」の記事の見出し「{heading}」に対する本文を生成してください。{user_prompt}"
            }]
        )
        return response.choices[0].message.content.strip()

    def generate_summary(self, title: str, contents: Dict[str, str]) -> str:
        """Generate a summary of the entire article."""
        all_content = "\n".join([f"{h}: {c}" for h, c in contents.items()])
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": f"以下の記事のまとめを生成してください:\nタイトル: {title}\n{all_content}"
            }]
        )
        return response.choices[0].message.content.strip()

    def generate_meta_description(self, title: str, summary: str) -> str:
        """Generate meta description for SEO."""
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": f"以下の記事のメタディスクリプション（120文字以内）を生成してください:\nタイトル: {title}\nまとめ: {summary}"
            }]
        )
        return response.choices[0].message.content.strip()

    def create_blog(self, theme: str) -> Dict:
        """Main method to create a blog post."""
        # 1. Generate titles
        titles = self.generate_titles(theme)
        print("生成されたタイトル:")
        for i, title in enumerate(titles, 1):
            print(f"{i}. {title}")

        # 2. Select title
        title_index = int(input("選択するタイトルの番号を入力してください: ")) - 1
        selected_title = titles[title_index]
        self.blog_data['title'] = selected_title

        # 3. Generate headings
        headings = self.generate_headings(selected_title)
        print("\n生成された見出し:")
        for i, heading in enumerate(headings, 1):
            print(f"{i}. {heading}")

        # 4. Select headings
        heading_indices = input("使用する見出しの番号をカンマ区切りで入力してください: ").split(',')
        selected_headings = [headings[int(i.strip()) - 1]
                             for i in heading_indices]

        # 5. Generate content for each heading
        contents = {}
        for heading in selected_headings:
            user_prompt = ""
            while True:
                content = self.generate_content(
                    selected_title, heading, user_prompt)
                print(f"\n【{heading}】\n{content}")
                if input("このコンテンツを承認しますか？(y/n): ").lower() == 'y':
                    contents[heading] = content
                    break
                user_prompt = input("コンテンツを修正するためのヒントを入力してください: ")

        self.blog_data['contents'] = contents

        # 6. Generate summary
        while True:
            summary = self.generate_summary(selected_title, contents)
            print(f"\n【まとめ】\n{summary}")
            if input("このまとめを承認しますか？(y/n): ").lower() == 'y':
                self.blog_data['summary'] = summary
                break

        # 7. Generate meta description
        while True:
            meta_description = self.generate_meta_description(
                selected_title, summary)
            print(f"\n【メタディスクリプション】\n{meta_description}")
            if input("このメタディスクリプションを承認しますか？(y/n): ").lower() == 'y':
                self.blog_data['meta_description'] = meta_description
                break

        return self.blog_data


if __name__ == "__main__":
    api_key = os.getenv("OPENAI_API_KEY")
    print(api_key)
    generator = BlogGenerator(api_key)
    theme = input("ブログのテーマを入力してください: ")
    result = generator.create_blog(theme)
    print("\n最終結果:")
    print(json.dumps(result, ensure_ascii=False, indent=2))
