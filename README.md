
# Football Career Simulation Engine

A Python-based football career simulator that models the progression of a professional footballer from their debut season through retirement.

The project uses a season-based simulation model where player attributes, team strength, opponent quality, and probabilistic event generation determine match and career outcomes instead of simulating every action in real time. 

The focus of the project is building simulation systems that are realistic enough to produce believable careers while keeping the code modular and easy to expand.

This project is being developed as a long-term software engineering project to improve my understanding of object-oriented programming, simulation design, probability-based systems, and software architecture.

---

## Features

### Career Simulation

- Generate a unique player with randomized attributes and position
- Simulate an entire professional career from debut to retirement
- Track season and career statistics
- Record achievements such as league titles, transfer values, and personal bests

### Match & Season Simulation

- Simulate full Premier League seasons
- Generate realistic match results using event-driven probability
- Dynamic league tables based on simulated results
- Promotion and relegation between the Premier League and EFL Championship

### Player Development

- Attribute progression and regression over time
- Position-dependent player roles
- Performance-based transfer valuation
- Club transfer system with multiple offers based on player performance

### Statistics

The simulator tracks information including:

- Goals
- Assists
- Match ratings
- Passing statistics
- Successful dribbles
- Clean sheets
- Career appearances
- Highest transfer value
- League titles
- Seasonal records

---

# How the Simulation Works

Rather than assigning a fixed probability for each match outcome, matches are generated through a sequence of simulated events.

Each match contains a randomized mixture of:

- Team attacking opportunities
- Player shot attempts
- Player key-pass opportunities
- Dribble attempts

Each event is resolved using multiple factors including:

- Player attributes
- Team attacking strength
- Opponent defensive strength
- Team consistency
- Random variation

This produces careers that feel less repetitive while still rewarding stronger players over long periods of time.

---

# Project Structure

```
football-career-sim/
│
├── data/
│   └── PL_teams.txt
│
├── models/
│   └── player.py
│
├── simulation/
│   ├── Prem_season.py
│   └── Prem_table.py
│
├── football_career_engine.py
│
└── README.md
```

### Responsibilities

**football_career_engine.py**

- Runs the overall career simulation
- Handles player creation
- Loads league data
- Controls career progression
- Manages transfers

**player.py**

Contains the `Player` class and all player-related logic including:

- attribute generation
- player development
- match statistics
- season statistics
- transfer valuation
- career tracking

**Prem_season.py**

Responsible for season-level simulation including:

- fixture generation
- match simulation
- event generation
- league table calculation
- promotion and relegation

**Prem_table.py**

Contains league table utilities including:

- points generation
- sorting
- table display

---

# Design Decisions

### Object-Oriented Player Model

The player is represented by a dedicated `Player` class rather than a collection of global variables. This keeps player state centralized and makes future features easier to implement.

### Data-Driven Teams

Team information is loaded from an external data file instead of being hardcoded throughout the program. This makes league balancing significantly easier and allows additional leagues to be added with minimal code changes.

### Modular Architecture

The project separates responsibilities across multiple modules instead of placing all logic inside a single file. Match simulation, league management, player logic, and application flow each have clearly defined responsibilities.

### Probability-Based Simulation

Rather than using completely random outcomes, player and team attributes directly influence probabilities for actions such as:

- scoring
- assisting
- dribbling
- passing
- transfer valuation

This produces more believable long-term career statistics.

---

# Technical Challenges

## Balancing Randomness

One of the biggest challenges was making matches feel unpredictable without allowing randomness to dominate the simulation.

To address this, player ability modifies probabilities while bounded random variation introduces enough uncertainty to keep seasons interesting.

## Producing Realistic League Tables

League standings are generated using team strength ranges rather than identical probabilities for every club. Stronger clubs are expected to finish higher over multiple simulations while still allowing occasional surprise seasons.

## Keeping the Code Maintainable

As the project grew, functionality was separated into dedicated modules for player management, season simulation, and league management. This made the project easier to extend and reduced duplicated logic.

---

# Technologies Used

- Python 3
- Object-Oriented Programming
- File I/O
- Random module
- Time module
- Modular project architecture

---

# Installation

Clone the repository

```bash
git clone https://github.com/L2Fizzle/football-career-engine.git
```

Move into the project directory

```bash
cd football_career_engine
```

Run the simulator

```bash
python football_career_engine.py
```

---

# Example Output

### Player Generation
<img width="2040" height="976" alt="3  Lab 3 py – football_career_engine_README md 2026-07-20 12_38_02 AM" src="https://github.com/user-attachments/assets/0b359fd1-525c-48ac-a0b2-9839874aabfb" />

---

### Match Simulation

<img width="1937" height="1005" alt="3  Lab 3 py – football_career_engine_README md 2026-07-20 12_38_37 AM" src="https://github.com/user-attachments/assets/0c8d6f33-62c3-4084-9a99-0c6d9fb579c8" />

---

### End of Season

<img width="1954" height="1000" alt="3  Lab 3 py – football_career_engine_README md 2026-07-20 12_39_03 AM" src="https://github.com/user-attachments/assets/ad4b12b9-60dd-43ac-801a-8f63d2157754" />
<img width="1862" height="637" alt="3  Lab 3 py – football_career_engine_README md 2026-07-20 12_39_11 AM" src="https://github.com/user-attachments/assets/de295924-18e1-4e1b-b987-9b71fb363bb7" />

---

### Transfer Options and player improvement

<img width="1835" height="170" alt="3  Lab 3 py – football_career_engine_README md 2026-07-20 12_41_25 AM" src="https://github.com/user-attachments/assets/c1f3f50f-3dfd-415b-95c1-028d7f2041da" />
<img width="1915" height="595" alt="3  Lab 3 py – football_career_engine_README md 2026-07-20 12_44_23 AM" src="https://github.com/user-attachments/assets/9b0745b8-f867-4624-9829-97ab448a2818" />

---

### Career Summary

<img width="1639" height="563" alt="3  Lab 3 py – football_career_engine_README md 2026-07-20 12_47_38 AM" src="https://github.com/user-attachments/assets/4526a81b-5dd3-47df-a5a0-2b0e79bbd1e3" />

---

# Future Improvements

Some features planned for future development include:

- Additional playable leagues
- Domestic and European competitions
- Injuries and suspensions
- Improved AI transfer logic
- Save/load functionality
- Expanded player progression
- Club finances
- Improved balancing and statistical tuning

---

# What I Learned

This project has been my largest personal software project so far.

Working on it has helped me gain experience with:

- designing larger Python applications
- organizing code across multiple modules
- object-oriented programming
- balancing probability-based systems
- refactoring code as a project grows
- designing software that is easier to maintain and extend

The project is still actively being developed, and I plan to continue expanding both the simulation systems and the overall architecture as I learn more about software engineering.
