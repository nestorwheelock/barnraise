# T-007: Post Activity Form

**Related Story**: S-003
**Estimate**: 2 hours
**Status**: ✅ COMPLETED
**Dependencies**: T-002

## Objective

Implement form for creating new activities.

## Deliverables

- [x] ActivityForm ModelForm
- [x] Post activity view
- [x] Form validation
- [x] Success page with manage link
- [x] Secret token generation

## Definition of Done

- [x] Form displays all fields
- [x] Validation errors shown
- [x] Activity saved to database
- [x] Secret token generated
- [x] Success page shows manage link
- [x] Copy link button works
- [x] Code committed

## Form Fields

- title (required)
- description (required)
- neighborhood (required, dropdown)
- location_hint (required)
- starts_at (required, datetime)
- duration_minutes (select)
- helpers_needed (number)
- host_email (required)
- host_phone (optional)

## Files Modified

- `activities/forms.py`
- `activities/views.py`
- `templates/activities/post.html`
- `templates/activities/post_success.html`
