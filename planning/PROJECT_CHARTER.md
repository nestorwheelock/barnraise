# Project Charter: Barn Raise

## Project Overview

**Project Name**: Barn Raise
**Version**: v1.0.0
**Start Date**: December 2024
**Target Delivery**: December 2024 (Christmas Gift)

## What We're Building

A hyperlocal community connection app that shows neighbors what activities are happening nearby and lets them show up to help with almost no friction.

### The Problem

Many people want to:
- Spend their time more productively
- Feel useful and connected
- Be around other people
- Get to know their neighbors

But existing solutions have too much friction:
- Social media feels performative and draining
- Volunteer organizations require long-term commitments
- Meetup groups feel like networking events
- Church/religious groups feel belief-bound

### The Solution

Barn Raise fills the missing middle ground:
- See what's happening nearby RIGHT NOW
- Show up, help for a while, leave whenever
- No profiles, no bios, no social pressure
- Just people helping people, close to home

## Why We're Building This

**Business Value**: Gift for friend who conceived the idea
**User Value**: Enables spontaneous community connection
**Social Value**: Rebuilds neighborhood cooperation ("barn-raising")

## How We'll Build It

### Tech Stack
- **Backend**: Django 5.x (Python)
- **Frontend**: HTMX + Tailwind CSS
- **Database**: SQLite (dev) / PostgreSQL (prod)
- **Deployment**: Docker, Railway/Render ready

### Architecture
- Server-rendered pages with HTMX for interactivity
- Mobile-first responsive design
- No user accounts required (browse/join anonymously)
- Secret token links for activity management

## Success Criteria

1. **Functional**
   - [ ] Can post an activity in under 60 seconds
   - [ ] Can find nearby activities in 3 taps
   - [ ] Can get directions in one tap
   - [ ] Can join activity without account

2. **Quality**
   - [ ] Works great on mobile
   - [ ] Page loads under 2 seconds
   - [ ] >95% test coverage
   - [ ] No critical bugs

3. **Deployment**
   - [ ] Friend can deploy to their own server
   - [ ] Clear documentation
   - [ ] Docker support
   - [ ] Seed data for demo

## Scope Boundaries

### IN SCOPE (v1.0.0)
- Browse activities by city/neighborhood
- Time filters (Now, Today, This Week)
- Post new activities
- Join activities (increment counter)
- Get directions (Google Maps link)
- Manage activities via secret link
- Complete St. Louis metro seed data
- Mobile-responsive design
- Docker deployment

### OUT OF SCOPE (Future Versions)
- User accounts/profiles
- Push notifications
- Native mobile apps
- In-app messaging
- Map view
- Activity history
- Reputation/ratings
- Email notifications
- Social features

## Risks & Mitigations

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| Spam/abuse | High | Medium | Require email to post, rate limiting |
| Low adoption | Medium | High | Start with St. Louis as pilot market |
| Technical complexity | Low | Low | Simple stack, proven patterns |
| Scope creep | Medium | Medium | Strict v1.0 boundaries |

## Stakeholders

- **Client**: Friend (gift recipient)
- **Developer**: You
- **End Users**: St. Louis metro area neighbors

## Approval

This project charter requires client approval before proceeding to BUILD phase.

---

**Prepared by**: Developer
**Date**: December 2024
**Status**: AWAITING APPROVAL
