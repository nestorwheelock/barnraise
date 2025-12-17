# S-003: Post an Activity

**Story Type**: User Story
**Priority**: High
**Estimate**: 1 day
**Sprint**: Sprint 1
**Status**: ✅ COMPLETED

## User Story

**As a** neighbor who needs help
**I want to** quickly post what I'm doing and when
**So that** nearby people can see it and show up

## Acceptance Criteria

- [x] Can post in under 60 seconds
- [x] Only need: title, description, neighborhood, time, helpers needed
- [x] Email required (spam prevention + notifications)
- [x] Get a secret link to manage my activity
- [x] Activity appears immediately in the neighborhood feed
- [x] Form validates required fields
- [x] Duration options are predefined (30min, 1hr, 2hr, etc.)

## Definition of Done

- [x] Post form with all fields
- [x] ActivityForm with proper widgets
- [x] Neighborhood dropdown populated
- [x] DateTime picker works on mobile
- [x] Success page shows secret manage link
- [x] Activity saved to database
- [x] Tests written and passing
- [x] Code committed

## Technical Notes

- ActivityForm uses Django ModelForm
- Secret token auto-generated on save
- Email stored but not displayed publicly
- Duration stored in minutes, displayed human-readable
