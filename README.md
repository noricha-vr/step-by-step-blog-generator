# Step-by-Step Blog Generator

## 概要

このスクリプトは、OpenAIのAPIを使用してブログのタイトルと見出しを生成し、それに基づいてコンテンツを生成します。
生成されたコンテンツはJSON形式で出力されます。

## インストール

1. このリポジトリをクローンまたはダウンロードします：

```
git clone https://github.com/noricha-vr/step-by-step-blog-generator.git
cd step-by-step-blog-generator
```

2. 仮想環境を作成し、アクティベートします：

```
python -m venv venv
source venv/bin/activate  # Linuxまたは macOS
# または
.\venv\Scripts\activate  # Windows
```

3. 必要なライブラリをインストールします：

```
pip install -r requirements.txt
```

4. OpenAI APIキーを環境変数として設定します：

```
export OPENAI_API_KEY='your-api-key-here'
# または
set OPENAI_API_KEY=your-api-key-here  # Windows
```

これで、スクリプトを実行する準備が整いました。

2. プロンプトに従って、ブログのテーマを入力し、生成されたオプションから選択します。
3. 生成されたコンテンツを確認し、必要に応じて修正を要求します。
4. 最終的な記事データがJSON形式で出力されます。

## 注意事項

- このスクリプトはOpenAI APIを使用するため、APIの使用量に応じて料金が発生する可能性があります。
- 生成されたコンテンツは、常に人間による確認と編集が必要です。
- API使用量を最小限に抑えるため、必要に応じてモデルやパラメータを調整してください。

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細については、[LICENSE](LICENSE)ファイルを参照してください。
