<p align="center">
  <img src="static/img/icon.svg" alt="Barn Raise" width="180" height="180">
</p>

<h1 align="center">Barn Raise</h1>

<p align="center">
  <strong>Hyperlocal community connection without the overhead.</strong>
</p>

<p align="center">
  <a href="#quick-start">Quick Start</a> •
  <a href="#features">Features</a> •
  <a href="#the-solution">How It Works</a> •
  <a href="#production-deployment">Deploy</a>
</p>

---

Social media promised to connect us but instead gave us feeds, algorithms, and endless scrolling. Barn Raise takes a different approach: show what's happening nearby right now, and make it dead simple to participate.

No accounts. No profiles. No follower counts. Just neighbors helping neighbors.

## The Problem

Modern life makes it surprisingly hard to meet the people who live near you. Traditional volunteering requires commitments. Nextdoor becomes a complaint board. Facebook groups drown in noise.

What if you could just see "someone nearby needs help moving boxes in 2 hours" and show up?

## The Solution

Barn Raise is a hyperlocal activity board. Hosts post what they're doing, where, and when. Neighbors browse by location and time, then show up to help. That's it.

**For Hosts:**
- Post an activity in 30 seconds
- Get a private management link (no account needed)
- See how many people plan to join

**For Helpers:**
- Browse activities by neighborhood
- Filter by time: happening now, today, or this week
- One tap to join, one tap for directions

## Activity Examples

Tasks that work well:
- Community garden work
- Neighborhood cleanup
- Moving furniture or boxes
- Event setup and teardown
- Food bank sorting
- Trail maintenance
- Painting or repairs
- Garage sale help

The sweet spot: tasks that benefit from extra hands but don't require special skills.

## Design Philosophy

**Low friction beats features.** Every screen asks: can this be simpler?

**Anonymity reduces barriers.** No profiles means no social anxiety about "putting yourself out there."

**Hyperlocal focus.** City → Neighborhood → Activity. You help people you might actually see again.

**Time-bounded activities.** Everything has a start time and duration. No open-ended commitments.

**Trust through transparency.** Hosts provide contact info. Helpers can see join counts. But nothing is public by default.

---

## Technical Documentation

### Tech Stack

- **Backend:** Django 5.x (Python 3.12+)
- **Frontend:** HTMX + Tailwind CSS (CDN)
- **Database:** SQLite (dev) / PostgreSQL (prod)
- **Deployment:** Docker, or any Python host

### Quick Start

```bash
# Clone and setup
git clone https://github.com/nestorwheelock/barnraise.git
cd barnraise
python -m venv venv
source venv/bin/activate

# Install and run
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata seed_data
python manage.py runserver
```

Open http://localhost:8000

### Seed Data

Pre-loaded with **23 cities** and **223 neighborhoods**:

**Missouri**
- St. Louis City (79 neighborhoods)
- St. Louis County (83 municipalities)

**Illinois Metro East**
- East St. Louis, Belleville, Collinsville, Edwardsville, Granite City, Alton, O'Fallon, Fairview Heights, and more

**Sample Cities**
- Austin, TX | Portland, OR | Denver, CO

### URL Structure

| Path | Purpose |
|------|---------|
| `/` | Home - city selection + search |
| `/<city>/` | City page - neighborhood list |
| `/<city>/<neighborhood>/` | Activity list with time filters |
| `/activity/<id>/` | Activity details |
| `/post/` | Create new activity |
| `/manage/<token>/` | Edit/complete/cancel (private link) |

### Data Models

```
City
├── name, state, slug

Neighborhood
├── city (FK), name, slug

Activity
├── neighborhood (FK)
├── title, description, location_hint
├── starts_at, duration_minutes
├── helpers_needed, helpers_joined
├── host_email, host_phone
├── status (active/completed/cancelled)
├── secret_token (for management URL)

ActivityJoin
├── activity (FK), session_key, joined_at
```

### Features

- **Location Search:** Real-time search across cities and neighborhoods
- **Time Filters:** Now / Today / This Week
- **HTMX Interactions:** Join button updates instantly without page reload
- **Google Maps Integration:** One-tap directions
- **Secret Management Links:** Edit or cancel without logging in
- **Mobile-First Design:** Responsive Tailwind CSS

### Admin Access

```bash
python manage.py createsuperuser
```

Then visit http://localhost:8000/admin/

### Production Deployment

**Docker (Recommended)**
```bash
docker-compose up -d --build
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py loaddata seed_data
```

**Manual**
```bash
export SECRET_KEY=your-secret-key
export DEBUG=False
export ALLOWED_HOSTS=your-domain.com
python manage.py collectstatic
gunicorn barnraise.wsgi:application
```

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `SECRET_KEY` | Django secret key | Dev key (change in prod!) |
| `DEBUG` | Debug mode | `True` |
| `ALLOWED_HOSTS` | Comma-separated hosts | `localhost,127.0.0.1` |

### Project Structure

```
barnraise/
├── activities/           # Main Django app
│   ├── models.py         # Data models
│   ├── views.py          # Page views + HTMX endpoints
│   ├── forms.py          # Activity form
│   ├── urls.py           # URL routing
│   └── fixtures/         # Seed data
├── templates/            # HTML templates
│   ├── base.html
│   ├── home.html
│   └── activities/       # Page templates
├── planning/             # Project documentation
│   ├── PROJECT_CHARTER.md
│   ├── stories/          # User stories
│   ├── tasks/            # Task breakdown
│   └── wireframes/       # ASCII wireframes
└── barnraise/            # Django settings
```

### Bonus: Django Deployment Kit

Included in `bonus/django-deployment-kit/`:

- Push-based deployment to VPS
- GPU media optimization (NVIDIA NVENC)
- Bidirectional database sync
- HEIC photo conversion
- Rollback support

See [bonus/django-deployment-kit/README.md](bonus/django-deployment-kit/README.md)

## License

**GNU General Public License v3.0 (GPLv3)**

Copyleft license requiring derivative works to use the same terms. See [LICENSE](LICENSE).
