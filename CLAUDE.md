# Barn Raise - Project Instructions

## Project Overview

Barn Raise is a hyperlocal community connection app built with Django, HTMX, and Tailwind CSS. It enables neighbors to post and join activities without creating accounts.

## Tech Stack

- **Backend**: Django 5.x (Python 3.12+)
- **Frontend**: HTMX + Tailwind CSS (CDN)
- **Database**: SQLite (dev) / PostgreSQL (prod)
- **Static Files**: WhiteNoise
- **Deployment**: Docker, Railway, or any Python host

## Development Workflow

Follow the **23-Step Iterative Development Cycle** for all changes:

### Phase 1: Planning & Questions (Steps 1-6)
1. **Validate Planning Documents** - Check `planning/*.md` files
2. **Review Existing Code** - Use Grep/Glob to find similar implementations
3. **Verify Prerequisites Complete** - Ensure dependencies are done
4. **Ask Clarifying Questions** - Don't assume requirements
5. **Validate Acceptance Criteria** - Confirm definition of done
6. **Identify Dependencies** - Find existing patterns to follow

### Phase 2: Test-Driven Development (Steps 7-10)
7. **Write Failing Tests First** - Based on acceptance criteria
8. **Run Tests** - Confirm they fail appropriately
9. **Write Minimal Code** - Make tests pass
10. **Run Tests Again** - Verify they pass

### Phase 3: Code Quality & Documentation (Steps 11-14)
11. **Refactor Code** - Keep tests green
12. **Add Error Handling** - Edge cases
13. **Update Documentation** - README, docstrings
14. **Run All Tests** - Full suite

### Phase 4: Git Workflow (Steps 15-18)
15. **Git add** - Stage changes
16. **Git commit** - Conventional commit format
17. **Git push** - To remote
18. **Update tracking** - Todo list, issues

### Phase 5: Review & Iteration (Steps 19-23)
19. **Code Review** - Quality, patterns, security
20. **Testing Review** - Coverage, edge cases
21. **Fix Issues** - If any found
22. **Re-test, Re-commit** - If changes made
23. **Sprint Cycle Complete** - Move to next task

## Project Structure

```
barnraise/
├── activities/           # Main Django app
│   ├── models.py         # City, Neighborhood, Activity, ActivityJoin
│   ├── views.py          # All page views
│   ├── forms.py          # ActivityForm
│   ├── admin.py          # Admin configuration
│   ├── urls.py           # URL routing
│   └── fixtures/         # Seed data
├── templates/            # HTML templates
│   ├── base.html
│   ├── home.html
│   └── activities/       # Page templates
├── planning/             # Project documentation
│   ├── PROJECT_CHARTER.md
│   ├── SPEC_SUMMARY.md
│   ├── stories/          # User stories (S-XXX)
│   ├── tasks/            # Task breakdown (T-XXX)
│   └── wireframes/       # ASCII wireframes
└── barnraise/            # Django project config
```

## Key Models

### City
- `name`, `state`, `slug`
- Has many neighborhoods

### Neighborhood
- `city` (FK), `name`, `slug`
- Has many activities

### Activity
- `title`, `description`, `neighborhood` (FK)
- `location_hint`, `starts_at`, `duration_minutes`
- `helpers_needed`, `helpers_joined`
- `host_email`, `host_phone`, `status`
- `secret_token` (for management URL)

### ActivityJoin
- `activity` (FK), `session_key`, `joined_at`
- Tracks anonymous joins via session

## URL Patterns

| URL | View | Purpose |
|-----|------|---------|
| `/` | home | City selection |
| `/<city>/` | city_detail | Neighborhood list |
| `/<city>/<neighborhood>/` | neighborhood_detail | Activity list |
| `/activity/<id>/` | activity_detail | Activity details |
| `/activity/<id>/join/` | activity_join | HTMX join |
| `/activity/<id>/directions/` | activity_directions | Google Maps redirect |
| `/post/` | activity_post | Post form |
| `/manage/<token>/` | activity_manage | Edit/complete/cancel |

## Testing

```bash
# Run tests
python manage.py test

# With coverage
coverage run manage.py test
coverage report
```

**Coverage Target**: >95%

## Common Commands

```bash
# Development
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata seed_data
python manage.py createsuperuser

# Production
python manage.py collectstatic
gunicorn barnraise.wsgi:application
```

## Code Style

- Follow PEP 8
- Use type hints where helpful
- Django conventions for models/views
- Tailwind classes for styling
- HTMX for interactivity (no custom JS)

## Commit Messages

Use conventional commit format:
```
type(scope): description

feat(models): add Activity status field
fix(views): correct time filter logic
docs(readme): update deployment instructions
```

## Security Notes

- Email addresses stored but NOT displayed publicly
- Secret tokens for activity management (no auth required)
- CSRF protection on all forms
- No user accounts = minimal attack surface

## Deployment Checklist

- [ ] Set `SECRET_KEY` environment variable
- [ ] Set `DEBUG=False`
- [ ] Set `ALLOWED_HOSTS`
- [ ] Run `collectstatic`
- [ ] Run `migrate`
- [ ] Load `seed_data` fixture
