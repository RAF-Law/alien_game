# 🏠 House Invader  
*A survival sci-fi text adventure built with Django*

## Authors
- [@octokatherine](https://github.com/RAF-Law)
- [@truthfulle](https://github.com/truthfulle)  
- [@s-sayed041](https://github.com/s-sayed041)  
- [@nairn-white](https://github.com/nairn-white)  

## Game Features

### 👤 User System
- **Secure Authentication**: Registration, login, and logout functionality  
- **Custom Profiles**:
  - Profile picture uploads  
  - Game statistics tracking (kills, days survived, games played)  
  - Inventory of collected items  
- **Admin Access**: Special superuser accounts  

### 🏆 Progression & Collections
- **11 unique weapons** to discover and unlock  
- **21 mysterious artifacts** to collect  
- **Game History**: Detailed stats for past games  
- **Leaderboards**:
  - Most enemies killed  
  - Longest survival time  

### 🕹️ Gameplay
- **Persistent Game States**: Save/load progress  
- **XML Game Data Storage**  
- **Easter Egg**: Hidden Konami code feature  
- **Interactive Tutorial**  

### 🖼️ Media & UI
- Dynamic weapon/artifact icons  
- Responsive design  
- Action feedback system  

### ⚙️ Technical
- **Django Backend**  
- **AJAX Integration** for:
  - Game saving/loading  
  - Profile updates  
  - Inventory management  
- **Security**:
  - Login-protected views  
  - CSRF protection  
  - Password hashing  

### 🎉 Special Features
- **Konami Code**:
  - Unlocks "The Eye of Schmelborg" artifact  
  - Secret admin access  
  - Cookie persistence  
- Dynamic image loading  
- Default game state generator  

## Demo  
https://raflaw.pythonanywhere.com/gameApp/

## Run Locally

```bash
# Clone repository
git clone https://github.com/RAF-Law/alien_game
cd alien_game

# Set up virtual environment
python -m venv venv

# Activate environment
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Start server
python manage.py runserver
```
Access at: http://127.0.0.1:8000/
