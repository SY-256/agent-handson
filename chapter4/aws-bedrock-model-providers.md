# AWS Bedrock 利用可能なモデルプロバイダー

AWS Bedrockでは、以下のAI企業から提供される様々な基盤モデル（Foundation Models）を利用することができます。

## 主要モデルプロバイダー

以下は、AWS Bedrockで利用可能な主要なモデルプロバイダーのリストです：

1. **AI21 Labs**
   - 特徴: 長いコンテキスト長に対する高効率な処理と根拠のある生成
   - モデル例: Jamba 1.5 Large, Jamba 1.5 Mini

2. **Amazon**
   - 特徴: テキスト、画像、ドキュメント、ビデオ理解、画像・ビデオ生成、対話型音声、コード生成などマルチモーダルな機能を提供
   - モデル例:
     - Nova シリーズ (Nova Lite, Nova Pro, Nova Premier, Nova Canvas, Nova Reel, Nova Sonic)
     - Titan シリーズ (Titan Text, Titan Image Generator, Titan Embeddings)

3. **Anthropic**
   - 特徴: 複雑な推論、コード生成、指示への対応に優れている
   - モデル例: Claude 3 Haiku, Claude 3 Sonnet, Claude 3.5 Sonnet, Claude 3.7 Sonnet, Claude 4 シリーズ

4. **Cohere**
   - 特徴: 効率的で多言語対応のAIエージェントと高度な検索・取得機能
   - モデル例: Command R+, Command R, Embed English, Embed Multilingual

5. **DeepSeek**
   - 特徴: 複雑な問題を段階的に解決する高度な推論モデル
   - モデル例: DeepSeek-R1, DeepSeek-V3.1

6. **Luma AI**
   - 特徴: 自然で一貫した動きと超リアルな詳細を持つ高品質なビデオ生成
   - モデル例: Ray v2

7. **Meta**
   - 特徴: 高度な画像・言語推論機能
   - モデル例: Llama 3/3.1/3.2/3.3シリーズ (8B, 70B, 405B), Llama 4 シリーズ

8. **Mistral AI**
   - 特徴: エージェント推論とマルチモーダルタスク向けの専門家モデル
   - モデル例: Mistral 7B Instruct, Mistral Large, Mixtral 8x7B Instruct, Pixtral Large

9. **OpenAI**
   - モデル例: gpt-oss-120b, gpt-oss-20b

10. **Qwen**
    - モデル例: Qwen3 32B, Qwen3 235B, Qwen3 Coder シリーズ

11. **Stability AI**
    - 特徴: 画像生成に特化
    - モデル例: Stable Diffusion 3.5 Large, Stable Image シリーズ

12. **TwelveLabs**
    - 映像・動画関連の機能を提供

13. **Writer**
    - テキスト生成の専門

## AWS Bedrockの特徴

AWS Bedrockは、以下のような機能を提供しています：

- **柔軟なモデル選択**: 数百のトップクラス基盤モデルへのアクセスとコードの書き直しなしでのモデル切り替え
- **サーバーレスアーキテクチャ**: インフラ構築不要で迅速に利用開始可能
- **モデル評価ツール**: パフォーマンス、コスト、精度のバランスを比較検討可能
- **カスタムモデルのインポート**: 既存のAI投資を活かしつつ独自モデルを統合
- **Amazon Bedrock Marketplace**: 100以上の基盤モデルを単一のカタログから発見・テスト・利用可能

## 主な利用方法

1. **推論実行**: プレイグラウンド環境でテキスト、画像、チャットの生成
2. **モデル評価**: 様々なモデルの出力を比較し、ユースケースに最適なモデルを選定
3. **ナレッジベース構築**: 埋め込みモデルを使用したナレッジベースの設定
4. **エージェント作成**: プロンプトのオーケストレーションを実行するエージェントの構築
5. **モデルカスタマイズ**: 特定のユースケース向けにトレーニングとバリデーションデータを供給