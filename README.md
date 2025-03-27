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

## Screenshots

![house_invader_home_page.png](<https://media-hosting.imagekit.io/458f60f86f2d47ab/house_invader_home_page.png?Expires=1837702522&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=x5BuIPMFen0bcVBKyM3nuGUmB6IUd54zELOFYqBUOKbHPhRpKejh-X1ue4RXcCa8BBZby6cZVbaukZDwLHlNrOqawFGxfGg8PfleyB1pNLWifCIXLLAxVT8nnnNU6OmqZQnvZfV3~4hBgijZ0b2~0LnVjmFV~V5Ov~BPgyutYN8Ywb1HOQWlcV2TZbBIW-5JwmdF85Bu1AH~ozKSjT9tL3XhSP7eMbUdlpRLaFraxsEqXCW2TwenPHp9Oz6sDIHOYGGGfweY63xF3ZlBXgn4BKZIZICz2~KTNA7bkweYGAXqcNBbZKei6Ud53nMmitCZuz1nqEICsUh~vjo7v0rdVg__>)
