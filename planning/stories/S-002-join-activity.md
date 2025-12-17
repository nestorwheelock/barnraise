# S-002: Join an Activity

**Story Type**: User Story
**Priority**: High
**Estimate**: 0.5 days
**Sprint**: Sprint 1
**Status**: ✅ COMPLETED

## User Story

**As a** neighbor who found an interesting activity
**I want to** indicate I'll show up and get directions
**So that** I can help out and the host knows I'm coming

## Acceptance Criteria

- [x] Can tap "I'll Be There" without creating account
- [x] Helper count updates immediately (HTMX)
- [x] Can tap "Get Directions" to open maps app
- [x] See clear info about when/where to show up
- [x] Button changes state after joining
- [x] Can only join once per session

## Definition of Done

- [x] Activity detail page shows all info
- [x] Join button uses HTMX for instant update
- [x] Session-based tracking prevents duplicate joins
- [x] Directions link opens Google Maps
- [x] Mobile-friendly large tap targets
- [x] Tests written and passing
- [x] Code committed

## Technical Notes

- Uses Django sessions to track joins (no login required)
- ActivityJoin model tracks session_key + activity
- HTMX swaps button content on join
- Google Maps URL uses activity location hint
