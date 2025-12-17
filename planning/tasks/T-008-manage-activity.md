# T-008: Manage Activity

**Related Story**: S-004
**Estimate**: 2 hours
**Status**: ✅ COMPLETED
**Dependencies**: T-007

## Objective

Implement activity management via secret token URL.

## Deliverables

- [x] Manage view (GET and POST)
- [x] Edit form pre-populated
- [x] Complete action
- [x] Cancel action
- [x] Update action
- [x] Status display

## Definition of Done

- [x] Access via /manage/<token>/
- [x] Form shows current values
- [x] Can mark complete
- [x] Can cancel
- [x] Can update details
- [x] Status badge shows correctly
- [x] Only active activities editable
- [x] Code committed

## Actions

- `action=update` - Save form changes
- `action=complete` - Set status to completed
- `action=cancel` - Set status to cancelled

## Files Modified

- `activities/views.py`
- `templates/activities/manage.html`
