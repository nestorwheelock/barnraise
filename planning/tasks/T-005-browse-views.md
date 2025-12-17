# T-005: Browse Views (Home, City, Neighborhood)

**Related Story**: S-001
**Estimate**: 3 hours
**Status**: ✅ COMPLETED
**Dependencies**: T-002, T-004

## Objective

Implement views for browsing activities by location.

## Deliverables

- [x] Home view - list cities with activity counts
- [x] City view - list neighborhoods with counts
- [x] Neighborhood view - list activities
- [x] Time filtering (now/today/week)
- [x] URL routing configured

## Definition of Done

- [x] All three views work
- [x] Activity counts accurate
- [x] Time filters work correctly
- [x] Empty states handled
- [x] Navigation works (back links)
- [x] URLs use slugs properly
- [x] Code committed

## URL Patterns

```
/                           → home
/<city_slug>/               → city_detail
/<city_slug>/<neighborhood_slug>/ → neighborhood_detail
```

## Files Modified

- `activities/views.py`
- `activities/urls.py`
- `barnraise/urls.py`
