# S-004: Manage My Activity

**Story Type**: User Story
**Priority**: Medium
**Estimate**: 0.5 days
**Sprint**: Sprint 1
**Status**: ✅ COMPLETED

## User Story

**As a** host who posted an activity
**I want to** edit, update, or cancel my activity
**So that** I can keep information accurate

## Acceptance Criteria

- [x] Can access via secret edit link (no login)
- [x] Can edit all activity details
- [x] Can mark activity as complete
- [x] Can cancel activity
- [x] See how many people said they'll come
- [x] Status displayed clearly (Active/Completed/Cancelled)

## Definition of Done

- [x] Manage page accessible via token URL
- [x] Edit form pre-populated with current data
- [x] Complete/Cancel buttons with confirmation
- [x] Helper count displayed
- [x] Status badge shows current state
- [x] Only active activities can be edited
- [x] Tests written and passing
- [x] Code committed

## Technical Notes

- URL pattern: /manage/<token>/
- Token is 32-byte URL-safe string
- Status choices: active, completed, cancelled
- Form actions: update, complete, cancel
