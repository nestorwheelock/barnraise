# SPEC Summary: Barn Raise v1.0.0

## Quick Reference

| Item | Value |
|------|-------|
| **Project** | Barn Raise |
| **Version** | v1.0.0 |
| **Tech Stack** | Django 5.x + HTMX + Tailwind CSS |
| **Database** | SQLite (dev) / PostgreSQL (prod) |
| **Status** | ✅ BUILD COMPLETE |

## What We Built

A hyperlocal community connection app where neighbors can:
1. **Browse** activities happening nearby (now, today, this week)
2. **Join** activities with one tap (no account required)
3. **Post** activities quickly (under 60 seconds)
4. **Manage** activities via secret link

## User Stories

| ID | Story | Status |
|----|-------|--------|
| S-001 | Browse Nearby Activities | ✅ Complete |
| S-002 | Join an Activity | ✅ Complete |
| S-003 | Post an Activity | ✅ Complete |
| S-004 | Manage My Activity | ✅ Complete |

## Tasks

| ID | Task | Status |
|----|------|--------|
| T-001 | Django Project Setup | ✅ Complete |
| T-002 | Core Data Models | ✅ Complete |
| T-003 | Admin Interface | ✅ Complete |
| T-004 | Seed Data - St. Louis Metro | ✅ Complete |
| T-005 | Browse Views | ✅ Complete |
| T-006 | Activity Detail & Join | ✅ Complete |
| T-007 | Post Activity Form | ✅ Complete |
| T-008 | Manage Activity | ✅ Complete |
| T-009 | Templates & Styling | ✅ Complete |
| T-010 | Deployment Configuration | ✅ Complete |

## Seed Data

**23 cities, 223 neighborhoods** covering:
- St. Louis City, MO (79 neighborhoods)
- St. Louis County, MO (83 municipalities)
- Metro East Illinois (18 cities with neighborhoods)
- Austin, TX / Portland, OR / Denver, CO (originals)

## Key URLs

| URL | Purpose |
|-----|---------|
| `/` | Home - city selection |
| `/<city>/` | City - neighborhood list |
| `/<city>/<neighborhood>/` | Neighborhood - activity list |
| `/activity/<id>/` | Activity detail |
| `/activity/<id>/join/` | Join activity (HTMX) |
| `/post/` | Post new activity |
| `/manage/<token>/` | Manage activity |

## Deployment

- **GitHub**: https://github.com/nestorwheelock/barnraise
- **Docker**: `docker-compose up`
- **Railway**: One-click deploy
- **Manual**: `gunicorn barnraise.wsgi:application`

## Out of Scope (v2.0+)

- User accounts/profiles
- Push notifications
- Native mobile apps
- Map view
- In-app messaging

---

**SPEC Approved**: December 2024
**BUILD Complete**: December 2024
**Gift Recipient**: Friend (Christmas 2024)
