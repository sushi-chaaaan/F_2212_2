# F_2212_2

## JPHACKS関係者様方へ

こちらは[F_2212_1](https://github.com/jphacks/F_2212_1)
のプロジェクトの
バックエンドのリポジトリです。  
詳しい説明等は[F_2212_1](https://github.com/jphacks/F_2212_1)側に
記載されておりますので、そちらをご参照ください。

## 作業用覚書:
mainブランチで作業をするな
BranchProtectionRUle導入済み

環境のインストール
```python 
poetry install
```

docker composeも必要

開発環境の起動
```bash
poe up
```

終了
```bash
# FastAPIはCtrl+C
docker compose down
```
