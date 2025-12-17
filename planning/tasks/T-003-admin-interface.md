# T-003: Admin Interface

**Related Story**: S-003, S-004
**Estimate**: 1 hour
**Status**: ✅ COMPLETED
**Dependencies**: T-002

## Objective

Configure Django admin for managing cities, neighborhoods, and activities.

## Deliverables

- [x] CityAdmin with list display, search
- [x] NeighborhoodAdmin with filters
- [x] ActivityAdmin with full features
- [x] ActivityJoinAdmin for viewing joins
- [x] Prepopulated slug fields

## Definition of Done

- [x] All models registered in admin
- [x] List views show relevant columns
- [x] Search and filters work
- [x] Slug auto-populates from name
- [x] Secret token is readonly
- [x] Date hierarchy on activities
- [x] Code committed

## Files Modified

- `activities/admin.py`
