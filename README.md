# capx-docs

GENIAC-PRIZE 2026 テーマ2に参加するチームの Agent 班が、CaP-X 系ロボットエージェントの提出イメージ（Apptainer / Singularity の `.sif`）を作る環境について、設計と手順をまとめた公開資料です。

コンテストの規定や計算環境の詳細は書いていません。それらは参加者向けの公式資料を正としてください。コード（ビルド定義・ジョブスクリプト・エージェント）はチームの非公開リポジトリ `capx-team` にあります。

## 中身

| パス | 内容 | 主な読者 |
|---|---|---|
| [docs/design-overview.md](docs/design-overview.md) | 設計概要。イメージの2段構成、ビルド場所、リポジトリ構成、開発の取り込み方、ローカル検証の結果 | 全員 |
| [docs/architecture.html](docs/architecture.html) | 設計概要の構成図（ブラウザで開く） | 全員 |
| [guides/capx-team-guide.md](guides/capx-team-guide.md) | `capx-team` リポジトリの各ファイルの役割と、日常の開発の流れ | Agent 班メンバー |
| [templates/member-pc-survey.md](templates/member-pc-survey.md) | メンバー PC の調査票（現在は実施見送り） | 班長 |
| [tools/pc_survey_summarize.py](tools/pc_survey_summarize.py) | 調査票の回答を区分ごとの人数だけに集計するスクリプト | 班長 |

最初に読むなら `docs/design-overview.md` → `guides/capx-team-guide.md` の順がおすすめです。

## この資料に入れないもの

- コンテストの参加者限定資料（ルール集・キックオフ資料・計算環境のマニュアル）とその内容
- 公式配布物（標準コード・評価コード）
- メンバーの個人情報・アカウント名、鍵・トークン
- 運営への問い合わせ内容、チーム内の調整事項

追加・修正するときも、この基準を守ってください。

## 状態

2026-11-10 時点。公式配布の後に設計が確定したら更新します。
