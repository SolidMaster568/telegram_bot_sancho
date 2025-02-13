# SanchoTest Bot

- [Introduction](#introduction)
  - [Basic Subscription Functionality 📋](#basic-subscription-functionality)
  - [Payment Verification ✅](#payment-verification)
- [Project Structure 📂](#project-structure)
- [Installation 🚀](#installation)
- [Configuration ⚙️](#configuration)
- [Running ▶️](#running)
- [Usage 📝](#usage)
  - [Configuration File 🛠️](#configuration-file)


## Introduction
This project contains the source code for a Sancho bot designed to implement basic subscription function.
Whether you want to manage subscriptions, this bot, written in Python using the aiogram framework version 2 and an asynchronous SQLite3 wrapper called aiosqlite, has got you covered.

### Basic Subscription Functionality

This Telegram bot already includes a fundamental subscription system.

### Payment Verification

The payment verification process ensures that users have paid the required subscription amount in USDT TRC20. This is achieved by utilizing the `USDT_TRC20_WALLET_ADDRESS` and `SUBSCRIBE_AMOUNT_IN_USDT_TRC20` variables defined in the `config.py` file.

But in this version, I don't use payment verification.

## Project Structure

```css
.
├── .env
├── README.md
├── requirements.txt
└── src
    ├── bot
    │   ├── app.py
    │   ├── loader.py
    │   ├── statesgroup.py
    │   ├── data
    │   ├── database
    │   ├── filters
    │   ├── handlers
    │   ├── keyboards
    │   ├── logs
    │   ├── middlewares
    │   └── utils
    └── db
        └── database_schema.sql
```

## Installation

Before running the bot, make sure you have Python 3.12+ installed and follow these steps:

1. Create a virtual environment (recommended but optional):
   ```shell
   python -m venv subscription
   ```

2. Activate the virtual environment:
   ```shell
   subscription\Scripts\activate
   ```

3. Install the dependencies listed in the `requirements.txt` file:
   ```shell
   pip install -r requirements.txt
   ```

## Configuration

Before running the bot, you need to configure the following parameters:

1. Create a bot on Telegram and obtain its token from BotFather.

2. Create `.env` file and add below
    ```env
    BOT_TOKEN=123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11
    ```

## Running 

After configuring, you can start the bot with the following command:
```shell
cd src/bot/
python app.py
```

The bot will be active and ready to handle commands and user requests on Telegram.
Of course, here's the complete text with the added information about the config file:

Of course, here's the complete text with the added information:

## Usage

### Configuration File

To configure specific aspects of your bot's behavior, you can utilize the `config.py` file located in the `src/bot/data/` directory. This file includes the following variables:

```python
# USDT TRC20 wallet address used for transactions
USDT_TRC20_WALLET_ADDRESS = 'TF8aSMqpwtniPN77wS2EZTTcUKaaJhyorb'

# Amount in USDT TRC20 required for subscription
SUBSCRIBE_AMOUNT_IN_USDT_TRC20 = 5

# Number of days between each payment for subscription
NUMBER_DAYS_FROM_ONE_PAYMENT = 30

private_channels = {
    'Channel 1': {
        'id': -100123456789,
        'invite_url': 'https://t.me/+ABCDEFGHIJKL'
    },
}
```

You can utilize these variables in your code to tailor your Telegram bot's behavior in accordance with the specified values.

---

&copy; 2025 grigoryan.arsen65@gmail.com

All Rights Reserved.
