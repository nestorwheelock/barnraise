# T-006: Activity Detail & Join

**Related Story**: S-002
**Estimate**: 2 hours
**Status**: ✅ COMPLETED
**Dependencies**: T-005

## Objective

Implement activity detail page with join functionality.

## Deliverables

- [x] Activity detail view
- [x] Join activity view (HTMX)
- [x] Directions redirect view
- [x] Session-based join tracking
- [x] Helper count update

## Definition of Done

- [x] Detail page shows all info
- [x] Join button works (HTMX swap)
- [x] Can only join once per session
- [x] Helper count updates
- [x] Directions opens Google Maps
- [x] Button state changes after join
- [x] Code committed

## HTMX Implementation

```html
<form hx-post="/activity/123/join/"
      hx-target="#join-button"
      hx-swap="innerHTML">
```

## Files Modified

- `activities/views.py`
- `activities/urls.py`
- `templates/activities/detail.html`
- `templates/components/join_button.html`
