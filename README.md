# 🏦 Bank Profit Predictor

## 🚀 Overview

This project builds a Machine Learning model to predict **customer profit contribution (bank_profit)** for a bank using financial, demographic, and behavioral data.

The model helps banks make **data-driven decisions** to improve profitability, reduce risk, and optimize customer targeting.

---

## 🎯 Business Objective

To develop a predictive system that estimates the **expected profit contribution of each customer**, and identifies key factors influencing profitability such as:

* Income & account balance
* Loan behavior
* Credit score & utilization
* Investment patterns

This enables the bank to:

* Optimize customer segmentation
* Improve credit policies
* Design targeted marketing strategies

---

## 💼 Business Use Cases

### 1. 📊 Profitability Segmentation

Identify high-value customers who generate maximum profit.

### 2. ⚠️ Risk Mitigation

Detect customers with low profitability due to defaults or poor financial behavior.

### 3. 🎯 Product Targeting

Recommend personalized products (loans, credit cards, insurance).

### 4. 🏢 Branch Performance Analysis

Analyze which customer segments contribute most to revenue.

---

## 📊 Features Used

The dataset includes 30+ features:

### 👤 Customer Info

* customer_age
* num_of_dependents
* customer_tenure_years

### 💰 Financial Data

* account_balance
* annual_income
* monthly_salary
* savings_account_balance

### 💳 Loan Details

* loan_amount
* loan_duration_months
* emi_amount
* num_of_loans

### 📉 Credit Behavior

* credit_score
* credit_card_utilization
* num_of_defaults

### 🔄 Transactions

* num_of_transactions
* avg_transaction_value

### 📈 Investments & Assets

* investment_value
* fixed_deposit_amount
* house_value
* insurance_amount

### 📊 Behavioral Score

* spending_score

---

## 🧠 Machine Learning Approach

A robust ML pipeline is used to ensure performance and avoid data leakage.

### 🔹 Model

* Ridge Regression (L2 Regularization)

### 🔹 Pipeline

* StandardScaler → Ridge Model

### 🔹 Hyperparameter Tuning

* GridSearchCV used to find best alpha value





If you like this project, give it a ⭐ on GitHub!
