# 🏠 House Invader  
*A survival sci-fi text adventure built with Django*

**Originally served as the group project for Web App Development 2, University of Glasgow*

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

# Set up virtual environment
python -m venv venv

# Activate environment
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Navigate to alien_game folder
cd alien_game

# Start server
python manage.py runserver
```
Access at: http://127.0.0.1:8000/

## Screenshots

![house_invader_home_page.png](<https://media-hosting.imagekit.io/458f60f86f2d47ab/house_invader_home_page.png?Expires=1837702522&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=x5BuIPMFen0bcVBKyM3nuGUmB6IUd54zELOFYqBUOKbHPhRpKejh-X1ue4RXcCa8BBZby6cZVbaukZDwLHlNrOqawFGxfGg8PfleyB1pNLWifCIXLLAxVT8nnnNU6OmqZQnvZfV3~4hBgijZ0b2~0LnVjmFV~V5Ov~BPgyutYN8Ywb1HOQWlcV2TZbBIW-5JwmdF85Bu1AH~ozKSjT9tL3XhSP7eMbUdlpRLaFraxsEqXCW2TwenPHp9Oz6sDIHOYGGGfweY63xF3ZlBXgn4BKZIZICz2~KTNA7bkweYGAXqcNBbZKei6Ud53nMmitCZuz1nqEICsUh~vjo7v0rdVg__>)

![house_invader_login_page.png](<https://media-hosting.imagekit.io/f5a48861331f4f30/house_invader_login_page.png?Expires=1837703328&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=QP2puKei4ByDTh2HbWFN92tXNCyjCvaph3YV~JVOVMvuUpbB7mf1tcLX10Z9gdInzlgUq1bKnWrQdSgPqgFt55nscuP0yYzLUWW7V4DVB7cctoz~mqM3LAsNQwzh0wFRBvVoxeDbiykLf8VXjoTs9SyFJ4JlIh1tZFAjF8uIfoNIlsYd06KEyBOy5FhEnhjg6a3n5jtN3PyTctQ5uODD4mGf6fn5DJUQx9Ub-iKzHiORXkwcLSAqQqX6dy6Mk-qukrQ-jRJn5pWOoO4LModW8sqbaxBlLnPEhnw0wlXYlKZ8JmDDjQRY6m5XbGwFTGh2r6IJZdVO5xR-4zE~TW9Llg__>)

![user_profile_view.png](<https://media-hosting.imagekit.io/f600dac255054fbb/user_profile_view.png?Expires=1837714519&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=QgPcSzanxzDY1rG3sEeAOd5YhD4mKIgRa1-IuoroURFF--6FLzYeSHGvbe4RvXzWs69LQ--hZyNbUA441lmKgzvPgU1ne-uixEekuKnqHhtxI5hyMVhbeUYAHKQBPDlWHt7mQSVYBvhlI7r1sNZwLc1cWnxNfDEkBQss4RVjnz2p2JKHpPLaaEA9LH-wLnz0bWJHsn-st~fpkWR~lzMlCK2iegVC1mUW6jTzJ2WlU8UfbkXtgL5eOE39y1QTANo2XmyyVJUUhoDToinlt9hZXaNvYa7TbT1Vaz-FTK7ZadFw~EFSOg9wre61svUgP3W9P65yOGaSRWffsgJxmyy5EA__>)

![game_scene_view.png](<https://media-hosting.imagekit.io/dd83a7be518749ea/game_scene_view.png?Expires=1837714845&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=BC4M-lFxx5g1ywjqwu-GT2nU2RniQ4gREFJIDNWA-wJF~LAOUmn8hIo-sfwDh-PzB~BcW0EWNVoki-shVWlIJq3cNwMYWkPIpaDZd8UI4b8h1Oey5toa~arUsy9xvdKFCRFLQZ6pfhZPGHph7DcxEsFAG3siUxKkvJd0e2GByDXHsAxs6hxmZJkH-Tc~YRhS-prgNP3S0a8R7iq4aqwLmmtkYkezkTuzogohq4cNWcxHGS8Tqu6O0zmxtlX1MsLLHQhP1W2iDfeH5CTnjjEn9cn1o~tO-0B4rFc-DtdaHazn8WMmA1TT4Olzd~IAhsN5FFAn-N~3OLdCT7JshGylbw__>)

![konami_collections_page.png](<https://media-hosting.imagekit.io/fd9cb0beb7fb4efb/konami_collections_page.png?Expires=1837703003&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=0wC-8P75LWRvoP89jOIoifdxEx3T-DtVbkkx6dAzQ2QMph-emVYe3wpjkw35T8SaU20LuNuxyUqTnQ3QuItfwIA-jPTibPsvMWZa1H5jlnFraJXQo8umUfiKR4jzVrjZxqb9xH5pro7DIX3eKnRLRH2jJYIkvk~qXCvFAyc93ZttOs6KzQnx6vipjUST2tmWpHierM3NRhSx9SAXsz3qLoIvopKQkcqkA8PGb0vmQsgp4PvNScM~U0VVJSTN~sCqRVdBmPQKZexaPUXPHUxP5~OSl6Ejk3WiE1zn-qBXq8EWhfOaCTS5p9DPI7tZBq0UZJ9kkjUpK7VFCz5fFZ6VRg__>)

![artifact_collection_view.png](<https://media-hosting.imagekit.io/15e53cc300734465/artifact_collection_view.png?Expires=1837715833&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=yc0RcOnPMIz2YzOIC4I8qcgkvTMqtdaBwibk3pSfZtxghz0fv-Wk~Ess37niPZNE-TR1B~Ig7gIIBzXQcM~kKBQ~fRsRxzpGLR3EgxK06L~B8h7tqpHPAJ23r-VEm5C3fkso91vA1BTdaNBoQj6F-L6YdoS~x3K8djDwrHj2tqBkgarygK8UFUTd-4t015GyH5b~F9rJTGp50iv~0Au2y1KeOifiUDxC2VAMp4pPqjoIDsYeFUd2cx8TqefcIFvWuHoUOE6U7iXwcuG5abCAChy97EqeU4buBxvE6dN6unE7Z5C7QZSYU5fCivb3f7~GlYG5CkCxMtfn9ikrpAbm9A__>)

## About Arts

All art resources in this project are produced by [@octokatherine](https://github.com/RAF-Law). Besides many references from online resources, some of the artifacts have certain tributes to other works:

- Alien Artifact - Steam Hub | *Frostpunk*
- Alien Crystal - White Auracite | *Final Fantasy XIV*
- Alien Skull - Nomai Mask | *Outer Wilds*
- Extraterrestrial Relic - Warp Core | *Outer Wilds*
- Galactic Artifact - Tango with Django | *Our WAD2 textbook*
- Space Relic - Thumper | *Dune*
- Stardust - Stardust Fragment | *Terraria*
- The Dictionary of the Ancients - Enchanted Book & Enchanting Table | *Minecraft*
  
## External Resources Used
- BGM: https://pixabay.com/music/main-title-stealth-battle-205902/
- Pixelated rounded corners: https://pixelcorners.lukeb.co.uk/?radius=8&multiplier=4

## Special Thanks

To those who gave support to the development of this project and engaged in early testing:
- maxine
- Batman
- frog
- DuaLipa
- urmother
- sam
- 1fire1zero

