# Amazon Bedrockで利用可能なモデルプロバイダー

Amazon Bedrockは、複数の主要AIプロバイダーから基盤モデル(FM: Foundation Models)にアクセスできるAWSのフルマネージドサービスです。以下に、Bedrockで利用可能な主要なモデルプロバイダーとその特徴を紹介します。

## モデルプロバイダー一覧

Amazon Bedrockでは、以下のモデルプロバイダーからの基盤モデルを利用できます：

1. **AI21 Labs**
   - Jamba 1.5シリーズモデル（Large、Mini）
   - 高効率な処理と長文脈長に対応した生成が特徴

2. **Amazon**
   - Titanモデルシリーズ（Text、Image Generator、Embeddings）
   - Novaモデルシリーズ（Lite、Micro、Pro、Premier、Canvas、Reel、Sonic）
   - マルチモーダル機能を提供する独自の基盤モデル

3. **Anthropic**
   - Claude 3シリーズ（Haiku、Sonnet）
   - Claude 3.5シリーズ（Haiku、Sonnet）
   - Claude 3.7 Sonnet
   - Claude 4シリーズ（Opus、Sonnet）
   - Claude 4.5シリーズ（Haiku、Sonnet）
   - 複雑な推論、コード生成、指示への忠実さが特徴

4. **Cohere**
   - Command Rシリーズ（Command R、Command R+）
   - Embedモデル（English、Multilingual、v4）
   - Rerank 3.5
   - 効率的な多言語AIエージェントと高度な検索・取得機能に特化

5. **DeepSeek**
   - DeepSeek-R1
   - DeepSeek-V3.1
   - 高度な推論モデルを提供

6. **Luma AI**
   - Ray v2
   - 高品質なビデオ生成に特化

7. **Meta**
   - Llama 3シリーズ（8B Instruct、70B Instruct）
   - Llama 3.1 8B Instruct
   - 高度な画像・言語の推論能力を提供

8. **Mistral AI**
   - （Bedrockで利用可能なモデルシリーズ）
   - エージェント型推論とマルチモーダルタスクに焦点

9. **OpenAI**
   - （Bedrockで利用可能なモデルシリーズ）
   - 様々なアプリケーション向けモデルを提供

10. **Qwen**
    - （Bedrockで利用可能なモデルシリーズ）

11. **Stability AI**
    - Stable Diffusion
    - 画像生成モデルを提供

12. **TwelveLabs**
    - （ビデオ理解に特化したモデル）

## Amazon Bedrock Marketplace

Amazon Bedrockは、上記の主要プロバイダーに加えて、Amazon Bedrock Marketplaceを通じて100以上の基盤モデルにアクセスできます。これらのモデルには、IBM、Nvidia、Zendesk、Upstages、Evolutionary Scale、Arcee AI、Widn.AIなどのプロバイダーのモデルが含まれています。

## モデルの特徴

- **テキスト生成**: チャット、文章作成、コード生成など
- **テキスト埋め込み**: ドキュメント検索、類似性分析など
- **画像生成**: テキストからの画像生成、画像編集など
- **マルチモーダル埋め込み**: 画像とテキストを組み合わせた埋め込み
- **音声認識と合成**: 音声からテキスト、テキストから音声へ
- **ビデオ生成**: テキストや画像からビデオを生成

## 利用方法

Amazon Bedrockでこれらのモデルを利用するには、AWSコンソールからアクセスするか、APIを通じて呼び出すことができます。モデルプロバイダーやモデルによって、利用可能なAWSリージョンやサポートする機能（ストリーミングなど）が異なります。

詳細は、[Amazon Bedrockの公式ドキュメント](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html)を参照してください。