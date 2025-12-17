# T-002: Core Data Models

**Related Story**: S-001, S-002, S-003, S-004
**Estimate**: 2 hours
**Status**: ✅ COMPLETED
**Dependencies**: T-001

## Objective

Create Django models for cities, neighborhoods, activities, and joins.

## Deliverables

- [x] City model with name, state, slug
- [x] Neighborhood model with city FK, name, slug
- [x] Activity model with all fields
- [x] ActivityJoin model for tracking joins
- [x] Model methods and properties
- [x] Migrations created and applied

## Definition of Done

- [x] All models created
- [x] Migrations run successfully
- [x] Model __str__ methods work
- [x] get_absolute_url methods work
- [x] Activity properties (is_happening_now, etc.)
- [x] Secret token generation works
- [x] Code committed

## Model Details

### City
- name, state, slug
- Ordering by name

### Neighborhood
- city (FK), name, slug
- unique_together: city + slug

### Activity
- title, description, neighborhood (FK)
- location_hint, starts_at, duration_minutes
- helpers_needed, helpers_joined
- host_email, host_phone (optional)
- status (active/completed/cancelled)
- secret_token (auto-generated)
- created_at, updated_at

### ActivityJoin
- activity (FK), session_key, joined_at
- unique_together: activity + session_key

## Files Modified

- `activities/models.py`
- `activities/migrations/0001_initial.py`
