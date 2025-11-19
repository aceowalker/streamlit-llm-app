# 専門家 AI アシスタント

LangChain と Streamlit を使った専門家 AI アシスタントアプリです。健康の専門家または資産運用の専門家として AI が質問に回答します。

## 機能

- ラジオボタンで専門家のタイプを選択（健康 / 資産運用）
- テキスト入力フォームから質問を送信
- 選択した専門家に応じたシステムメッセージで LLM の振る舞いを変更
- OpenAI の GPT-3.5-turbo を使用した回答生成

## セットアップ手順

### 1. 仮想環境の有効化

**PowerShell の場合:**
```powershell
.\env\Scripts\Activate.ps1
```

**CMD の場合:**
```cmd
call env\Scripts\activate.bat
```

**PowerShell で実行ポリシーエラーが出る場合:**
```powershell
# 仮想環境の Python を直接使用
.\env\Scripts\python.exe -m pip install -r requirements.txt
```

### 2. 必要なパッケージのインストール

```bash
pip install -r requirements.txt
```

### 3. 環境変数の設定

`.env.example` を `.env` にコピーして、OpenAI API キーを設定してください:

```bash
# .env.example をコピー
copy .env.example .env
```

`.env` ファイルを編集して、API キーを設定:
```
OPENAI_API_KEY=sk-your-actual-api-key-here
```

OpenAI API キーは https://platform.openai.com/api-keys から取得できます。

### 4. アプリの実行

```bash
streamlit run app.py
```

または仮想環境の Python を直接使用:
```powershell
.\env\Scripts\python.exe -m streamlit run app.py
```

ブラウザで http://localhost:8501 が自動的に開きます。

## 使い方

1. **専門家を選択**: ラジオボタンで「健康の専門家」または「資産運用の専門家」を選択
2. **質問を入力**: テキストエリアに質問や相談内容を入力
3. **回答を取得**: ボタンをクリックして AI からの回答を表示

## 主な機能

### `get_llm_response(user_input: str, expert_type: str) -> str`

- **引数:**
  - `user_input`: ユーザーからの質問テキスト
  - `expert_type`: 選択された専門家のタイプ
- **戻り値:** LLM からの回答テキスト
- **処理内容:**
  - 専門家タイプに応じたシステムメッセージを設定
  - LangChain の ChatOpenAI を使用して LLM を呼び出し
  - SystemMessage と HumanMessage を組み合わせて回答を生成

## 技術スタック

- **Streamlit**: Web UI フレームワーク
- **LangChain**: LLM アプリケーション構築フレームワーク
- **OpenAI API**: GPT-3.5-turbo モデル
- **python-dotenv**: 環境変数管理

## 注意事項

- OpenAI API の使用には料金が発生します
- AI の回答は参考情報として扱い、重要な決定には専門家に相談してください
- `.env` ファイルは Git にコミットしないでください（`.gitignore` に追加済み）