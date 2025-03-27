
# 🏠 House Invader
A survival horror text adventure built with Django


## Authors

- [@octokatherine](https://github.com/RAF-Law)
- [@truthfulle](https://github.com/truthfulle)
- [@s-sayed041](https://github.com/s-sayed041)
- [@nairn-white](https://github.com/nairn-white)
## Game Features


#### 👤 User System
- Secure Authentication: Registration, login, and logout functionality

- Custom Profiles: Each user gets a personalized profile with:

- Profile picture uploads

- Game statistics tracking (kills, days survived, games played)

- Inventory of collected items

- Admin Access: Special superuser accounts for administration

#### 🏆 Progression & Collections
- Weapon Collection: 11 unique weapons to discover and unlock

- Artifact Handbook: 21 mysterious artifacts to find and collect

- Game History: Track all past games with detailed stats

 - Leaderboards: Compete for top spots in:

    Most enemies killed

    Longest survival time

#### 🕹️ Gameplay Features
- Persistent Game States: Save and load your progress anytime

- XML Game Data: Structured game state storage for complex gameplay

- Easter Egg: Special hidden content for curious players

- Interactive Tutorial: Instructions page to help new players

#### 🖼️ Media & UI
- Dynamic Icons: Visual representations for all weapons and artifacts

- Responsive Design: Works across different screen sizes

- Visual Feedback: Status messages for all actions

#### ⚙️ Technical Implementation
- Django Backend: Robust server-side processing

#### AJAX Integration:

##### Smooth asynchronous operations for:

- Game saving/loading

- Profile updates

- Inventory management

- Database Models:

- User profiles with extended fields

- Game state storage

- Weapon/artifact catalogs

#### Form Handling: Secure data processing for:

- User registration

- Profile updates

- Game submissions

#### 🛡️ Security Features
- Login-Protected Views: Sensitive actions require authentication

- CSRF Protection: Built-in security for form submissions

- Password Hashing: Secure credential storage

- Input Validation: Protected against malformed data

#### 🎉 Special Features
##### Konami Code Easter Egg:

- Unlocks special artifact ("The Eye of Schmelborg")

- Grants access to secret admin account

- Persists via cookie tracking

##### Other features:

- Dynamic Image Loading: Weapon icons loaded via API calls

- Game Initialization: Default game state generator for new players

## Demo

https://raflaw.pythonanywhere.com/gameApp/


## Run Locally

Clone the project

```bash
$ git clone https://github.com/RAF-Law/alien_game
```

Go to the project directory

```bash
$ cd ~/alien_game
```

Create a virtual environment (if you haven't already)
```bash
$ python -m venv venv
```

#### Activate virtual environment
###### Linux/Mac:

```bash
$ source venv/bin/activate
```

###### Windows:
```bash
$ .\venv\Scripts\activate
```


Install dependencies

```bash
$ pip install -r requirements.txt
```

Start the local development server

```bash
$ python manage.py runserver
```

Open local port in browser
```
 http://127.0.0.1:8000/
```


## Acknowledgements

 - [Django Web Development Framework](https://docs.djangoproject.com/en/5.1/)
 - [University of Glasgow School of Computing Science](https://www.gla.ac.uk/schools/computing/)
 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)
