
# 会計freee・人事労務freee用APIクライアント
会計freee・人事労務freeeのPythonラッパーライブラリです。
https://developer.freee.co.jp/

# 認可コード(Authorization code)の取得
下記のURLにある手順に従って認可コードを取得します。
https://support.freee.co.jp/hc/ja/articles/115000145263-freee-APIのアクセストークンを取得する

# アクセストークンの取得・リフレッシュ
初回のアクセストークンのみ明示的にアクセストークンの取得が必要です。2回目以降はリフレッシュトークンを用いて自動的にアクセストークンをリフレッシュします。
## アクセストークンの取得(初回)
```
# 必要情報をセット
client_id = "xxx"
client_secret = "xxx"
company_id = xxxxx
authorization_code = xxxx
token_filename = "token.json" # トークン情報を保存するJsonファイル名（適当で良い）

freee = Freee(client_id, client_secret, company_id, token_filename)
freee.get_access_token(authorization_code) # 認可コードを与えると、トークン情報を取得し、token_filenameのファイルを作成・保存する。
```

# 各種情報の取得例
```
freee = Freee(client_id, client_secret, company_id, token_filename)
token_dict = freee.read_tokens()
freee.set_tokens(token_dict)
freee.get_companies()
```

## To do

### 諸々
- 事務所IDを初期化時に入力しなくて良い用に修正（初期化時には通常は知らない）

### 会計freeeの実装リスト

- [ ] Account items (勘定科目)
    - [x] GET /account_items/{id} 勘定科目の詳細情報の取得
    - [x] GET /account_items 勘定科目一覧の取得
    - [ ] POST /account_items 勘定科目の作成
    - [ ] PUT /account_items/{id} 勘定科目の更新

- [ ] Banks (連携サービス) ← API自体にバグの可能性あり
    - [ ] GET /banks 連携サービス一覧の取得
    - [ ] GET /banks{id} 連携サービスの取得

- [ ] Companies (事業所)
    - [x] GET /companies 事業所一覧の取得
    - [x] GET /companies/{id} 事業所の詳細情報の取得
    - [ ] PUT /companies/{id} 事業所情報の更新

- [ ] Deals取引（収入／支出）
    - [x] GET /deals 取引（収入／支出）一覧の取得
    - [x] GET /deals/{id} 取引（収入／支出）の取得
    - [ ] POST /deals 取引（収入／支出）の作成
    - [ ] PUT /deals/{id} 取引（収入／支出）の更新

- [x] Expense application line templates (経費科目)
    - [x] GET /expense_application_line_templates 経費科目一覧の取得

- [ ] Expense applications (経費精算)
    - [ ] DELETE /expense_applications/{id} 経費申請の削除
    - [ ] POST /expense_applications 経費申請の作成
    - [ ] PUT /expense_applications/{id} 経費申請の更新

- [ ] Invoices (請求書)
    - [ ] DELETE /invoices/{id} 請求書の削除
    - [ ] GET /invoices 請求書一覧の取得
    - [ ] POST /invoices 請求書の作成
    - [ ] PUT /invoices/{id} 請求書の更新

- [ ] Items (品目)
    - [ ] GET /items 品目一覧の取得
    - [ ] POST /items 品目の作成

- [x] Journals (仕訳帳)
    - [x] GET /journals ダウンロード要求
    - [x] GET /journals/reports/{id}/status ステータス確認
    - [x] GET /journals/reports/{id}/download ダウンロード実行

- [ ] ManualJournals (振替伝票)
    - [ ] DELETE /manual_journals/{id} 振替伝票の削除
    - [x] GET /manual_journals 振替伝票一覧の取得
    - [x] GET /manual_journals/{id} 振替伝票の取得
    - [ ] POST /manual_journals 振替伝票の作成
    - [ ] PUT /manual_journals/{id} 振替伝票の更新

- [ ] Partners (取引先)
    - [ ] GET /partners 取引先一覧の取得
    - [ ] POST /partners 取引先の作成
    - [ ] PUT /partners/{id} 取引先の更新
    - [ ] PUT /partners/code/{code} 取引先の更新

- [ ] Payments (取引の支払行)
    - [ ] DELETE /deals/{id}/payments/{payment_id} 取引（収入／支出）の支払行削除
    - [ ] POST /deals/{id}/payments 取引（収入／支出）の支払行作成
    - [ ] PUT /deals/{id}/payments/{payment_id} 取引（収入／支出）の支払行更新

- [ ] Receipts (ファイルボックス)
    - [ ] POST /receipts ファイルボックス 証憑ファイルアップロード

- [ ] Renews (取引の+更新)
    - [ ] DELETE /deals/{id}/renews/{renew_id} 取引（収入／支出）の+更新の削除
    - [ ] POST /deals/{id}/renews 取引（収入／支出）に対する+更新の作成
    - [ ] PUT /deals/{id}/renews/{renew_id} 取引（収入／支出）の+更新の更新

- [ ] Sections (部門)
    - [ ] DELETE /sections/{id} 部門の削除
    - [ ] GET /sections 部門一覧の取得
    - [ ] POST /sections 部門の作成
    - [ ] PUT /sections/{id} 部門の更新

- [ ] Segment tags (セグメントタグ)
    - [ ] DELETE /segments/{segment_id}/tags/{id} セグメントタグの削除
    - [ ] GET /segments/{segment_id}/tags セグメントタグ一覧の取得
    - [ ] POST /segments/{segment_id}/tags セグメントの作成
    - [ ] PUT /segments/{segment_id}/tags/{id} セグメントタグの更新

- [ ] Selectables (フォーム用選択項目情報)
    - [ ] GET /forms/selectables フォーム用選択項目情報の取得

- [ ] Tags (メモタグ)
    - [ ] GET /tags メモタグ一覧の取得
    - [ ] POST /tags メモタグの作成

- [ ] Taxes (税区分)
    - [ ] GET /taxes/codes 税区分コード一覧の取得
    - [ ] GET /taxes/companies/{company_id} 税区分コード詳細一覧の取得

- [ ] Transfers (取引（振替）)
    - [ ] GET /transfers 取引（振替）一覧の取得
    - [ ] POST /transfers 取引（振替）の作成

- [x] Trial balance (試算表)
    - [x] GET /reports/trial_bs 貸借対照表の取得
    - [x] GET /reports/trial_bs_two_years 貸借対照表(前年比較)の取得
    - [x] GET /reports/trial_bs_three_years 貸借対照表(３期間比較)の取得
    - [x] GET /reports/trial_pl 損益計算書の取得
    - [x] GET /reports/trial_pl_two_years 損益計算書(前年比較)の取得
    - [x] GET /reports/trial_pl_three_years 損益計算書(３期間比較)の取得
    - [x] GET /reports/trial_pl_sections 損益計算書(部門比較)の取得

- [ ] Users (ユーザ)
    - [ ] GET /users/me ログインユーザ情報の取得
    - [ ] GET /users/capabilities ログインユーザの権限の取得

- [ ] Wallet txns (明細)
    - [ ] GET /wallet_txns 明細一覧の取得
    - [ ] POST /wallet_txns 明細の作成

- [ ] Walletables (口座)
    - [ ] GET /walletables 口座一覧の取得
    - [ ] POST /walletables 口座の作成




### 人事労務freeeの実装リスト

- [ ] タイムレコーダー(打刻)
    - [x] GET /api/v1/employees/{emp_id}/time_clocks 打刻情報の一覧取得
    - [x] GET /api/v1/employees/{emp_id}/time_clocks/{id} 打刻情報の詳細取得
    - [x] GET /api/v1/employees/{emp_id}/time_clocks/available_types 打刻可能種別の取得
    - [ ] POST /api/v1/employees/{emp_id}/time_clocks 打刻情報の登録


- [x] ログインユーザ
    - [x] GET /api/v1/users/me 取得

- [x] 給与明細
    - [x] GET /api/v1/salaries/employee_payroll_statements 一覧の取得
    - [x] GET /api/v1/salaries/employee_payroll_statements/{employee_id} 取得

- [ ] 勤怠
    - [ ] DELETE /api/v1/employees/{emp_id}/work_records/{date} 削除
    - [x] GET /api/v1/employees/{emp_id}/work_records/{date} 取得
    - [ ] PUT /api/v1/employees/{emp_id}/work_records/{date} 更新

- [ ] 勤怠情報サマリ
    - [x] GET /api/v1/employees/{emp_id}/work_record_summaries/{year}/{month} 勤怠情報月次サマリの取得
    - [ ] PUT /api/v1/employees/{emp_id}/work_record_summaries/{year}/{month} 勤怠情報月次サマリの更新

- [ ] 従業員
    - [ ] DELETE /api/v1/employees/{id} 削除
    - [x] GET /api/v1/companies/{company_id}/employees 一覧の取得
    - [x] GET /api/v1/employees 一覧の取得
    - [x] GET /api/v1/employees/{id} 取得
    - [ ] POST /api/v1/employees 作成
    - [ ] PUT /api/v1/employees/{id} 更新

- [ ] 従業員の基本給
    - [x] GET /api/v1/employees/{emp_id}/basic_pay_rule 取得
    - [ ] PUT /api/v1/employees/{emp_id}/basic_pay_rule 更新

- [ ] 従業員の銀行口座
    - [X] GET /api/v1/employees/{emp_id}/bank_account_rule 取得
    - [ ] PUT /api/v1/employees/{emp_id}/bank_account_rule 更新

- [ ] 従業員の健康保険
    - [X] GET /api/v1/employees/{emp_id}/health_insurance_rule 取得
    - [ ] PUT /api/v1/employees/{emp_id}/health_insurance_rule 更新

- [ ] 従業員の厚生年金保険
    - [X] GET /api/v1/employees/{emp_id}/welfare_pension_insurance_rule 取得
    - [ ] PUT /api/v1/employees/{emp_id}/welfare_pension_insurance_rule 更新

- [ ] 従業員の姓名・住所など
    - [X] GET /api/v1/employees/{emp_id}/profile_rule 取得
    - [ ] PUT /api/v1/employees/{emp_id}/profile_rule 更新

- [ ] 従業員の扶養親族
    - [X] GET /api/v1/employees/{emp_id}/dependent_rules 取得
    - [ ] PUT /api/v1/employees/{emp_id}/dependent_rules/bulk_update 更新

- [x] 所属
    - [x] GET /api/v1/employee_group_memberships 一覧の取得

- [x] 賞与明細
    - [x] GET /api/v1/bonuses/employee_payroll_statements 一覧の取得
    - [x] GET /api/v1/bonuses/employee_payroll_statements/{employee_id} 取得

# PyPIアップデート
1. setup.pyを修正
1. python setup.py sdist
1. twine upload dist/[latest version file]
