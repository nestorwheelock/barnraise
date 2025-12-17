# S-001: Browse Nearby Activities

**Story Type**: User Story
**Priority**: High
**Estimate**: 1 day
**Sprint**: Sprint 1
**Status**: ✅ COMPLETED

## User Story

**As a** neighbor looking to help
**I want to** see what activities are happening in my area
**So that** I can find something to help with today

## Acceptance Criteria

- [x] Can select my city from homepage
- [x] Can see neighborhoods with active activities
- [x] Can filter by "Now", "Today", "This Week"
- [x] Activities show title, time, location, helpers needed
- [x] Can tap activity to see full details
- [x] Empty states show helpful messages
- [x] Navigation allows going back easily

## Definition of Done

- [x] Views implemented (home, city, neighborhood)
- [x] Templates created with Tailwind styling
- [x] Time filtering logic works correctly
- [x] Activity counts show on neighborhood cards
- [x] Mobile-responsive design
- [x] Tests written and passing
- [x] Code committed

## Technical Notes

- Home page shows all cities with activity counts
- City page shows neighborhoods filtered by time
- Neighborhood page shows activity cards
- Uses Django ORM annotations for counts
- HTMX not needed for browse (server-rendered)
