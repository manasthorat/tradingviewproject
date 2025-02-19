# Real-Time Stock Charting with Flask & TradingView

This project fetches real-time stock market data using the Angel One SmartAPI and displays it on an interactive candlestick chart using TradingView Lightweight Charts.

## 🚀 Features
- 📈 **Live Candlestick Chart** using TradingView Lightweight Charts  
- 🕒 **Timeframe Selection** (1 min, 5 min, 15 min, etc.)  
- 📊 **Stock Selection** (NIFTY, SENSEX, etc.) via Dropdown  
- 🔄 **Real-Time Data Fetching** using SmartAPI  
- 🎨 **Responsive UI** for better usability  

## 📚 Installation

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/your-repo-name.git
   cd your-repo-name
   ```

2. **Create a Virtual Environment**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # For macOS/Linux
   venv\Scripts\activate     # For Windows
   ```

3. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up API Credentials**  
   - Create a `.env` file and add your Angel One API credentials:
     ```
     API_KEY=your_api_key
     USERNAME=your_username
     PASSWORD=your_password
     TOTP_SECRET=your_totp_secret
     ```

## ▶️ Usage

Run the Flask application:
```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

## 🏗️ Project Structure
```
📂 your-repo-name/
├── 📄 app.py                # Flask application
├── 📄 config.py             # Configuration file for API keys
├── 📄 requirements.txt      # Dependencies
├── 📄 .gitignore            # Git ignore file
├── 📄 README.md             # Project documentation
└── 📂 static/               # Frontend assets
    ├── 📄 index.html        # Frontend UI
    ├── 📄 script.js         # TradingView chart logic
    └── 📄 styles.css        # Styling
```

## 🛠️ Technologies Used
- **Backend**: Python, Flask  
- **API**: Angel One SmartAPI  
- **Frontend**: HTML, JavaScript, TradingView Lightweight Charts  
- **Database**: Pandas (for data processing)  





![image](https://github.com/user-attachments/assets/c7b46f63-7ebf-46e7-a491-5c8af5b7a684)
![image](https://github.com/user-attachments/assets/4ff07b54-c406-4410-8771-bc42dea7022a)
![image](https://github.com/user-attachments/assets/8bf227e8-da66-4eee-bc60-8faf610c1593)
![image](https://github.com/user-attachments/assets/034ecff7-4ad9-4186-8253-77a25410635f)

