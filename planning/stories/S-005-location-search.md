# S-005: Real-Time Location Search

**Story Type**: User Story
**Priority**: High
**Estimate**: 4 hours
**Sprint**: Sprint 2
**Status**: PENDING

## User Story

**As a** neighbor looking to help
**I want to** type a location and see matching options in real-time
**So that** I can quickly find activities in my area without navigating through menus

## Description

Replace the current city → neighborhood drill-down navigation with a unified search box that provides instant results as the user types. The search should match against cities, counties, and neighborhoods in the database and show activities at the appropriate level.

## Search Behavior

### Input Examples & Expected Results

| User Types | Matches | Shows Activities For |
|------------|---------|---------------------|
| "St. Louis" | St. Louis City, St. Louis County | All activities in matched areas |
| "St. Louis City" | St. Louis City | All 79 neighborhoods' activities |
| "County" | St. Louis County | All 83 municipalities' activities |
| "Soulard" | Soulard (neighborhood) | Activities in Soulard only |
| "Belleville" | Belleville, IL (city) | Activities in Belleville |
| "Tower Grove" | Tower Grove South, Tower Grove East | Activities in matching neighborhoods |

### Search Logic

1. **Debounce**: Wait 300ms after user stops typing before searching
2. **Minimum characters**: Start searching after 2+ characters
3. **Match priority**:
   - Exact match (highest)
   - Starts with query
   - Contains query (lowest)
4. **Result grouping**: Group by type (Cities, Neighborhoods)
5. **Activity counts**: Show number of active activities per result

## Acceptance Criteria

- [ ] Search box prominently displayed on home page
- [ ] Results appear as user types (no submit button needed)
- [ ] Results show within 200ms of typing pause
- [ ] Can search by city name (e.g., "St. Louis City")
- [ ] Can search by county (e.g., "St. Louis County")
- [ ] Can search by neighborhood name (e.g., "Soulard", "Tower Grove")
- [ ] Partial matches work (e.g., "bell" matches "Belleville")
- [ ] Results show activity count for each location
- [ ] Clicking a result navigates to that location's activity list
- [ ] Empty state shows helpful message when no matches
- [ ] Mobile-friendly with large touch targets

## Technical Approach

### Frontend (HTMX)
- Use `hx-trigger="keyup changed delay:300ms"` for debounced search
- Use `hx-get="/search/"` to fetch results
- Use `hx-target="#search-results"` to update results div
- Preserve existing browse navigation as fallback

### Backend (Django)
- New view: `search_locations(request)`
- Query parameter: `?q=<search_term>`
- Return partial HTML with matching locations
- Include activity counts via annotation

### Database Queries
```python
# Search cities
cities = City.objects.filter(
    Q(name__icontains=query) | Q(state__icontains=query)
).annotate(
    activity_count=Count('neighborhoods__activity', filter=Q(neighborhoods__activity__status='active'))
)

# Search neighborhoods
neighborhoods = Neighborhood.objects.filter(
    name__icontains=query
).annotate(
    activity_count=Count('activity', filter=Q(activity__status='active'))
)
```

## Wireframe

```
┌─────────────────────────────────────┐
│         🏠 BARN RAISE               │
├─────────────────────────────────────┤
│                                     │
│  Where do you want to look          │
│  for stuff to do?                   │
│                                     │
│  ┌─────────────────────────────┐   │
│  │ 🔍 Search neighborhoods...  │   │
│  └─────────────────────────────┘   │
│                                     │
│  ┌─────────────────────────────┐   │
│  │ CITIES                      │   │
│  │ ├─ St. Louis City    (12)  │   │
│  │ └─ St. Louis County   (8)  │   │
│  │                             │   │
│  │ NEIGHBORHOODS               │   │
│  │ ├─ Soulard            (3)  │   │
│  │ ├─ Tower Grove South  (2)  │   │
│  │ └─ Tower Grove East   (1)  │   │
│  └─────────────────────────────┘   │
│                                     │
│  ─────── or browse by city ───────  │
│                                     │
│  [Austin, TX] [Portland, OR] ...    │
│                                     │
└─────────────────────────────────────┘
```

## Definition of Done

- [ ] Search endpoint created and tested
- [ ] HTMX integration working with debounce
- [ ] City search returns correct results
- [ ] Neighborhood search returns correct results
- [ ] Partial matching works correctly
- [ ] Activity counts displayed accurately
- [ ] Results are clickable and navigate correctly
- [ ] Empty state handled gracefully
- [ ] Mobile responsive design
- [ ] Tests written (>95% coverage)
- [ ] Documentation updated

## Out of Scope

- Geolocation (use device location) - future enhancement
- Map-based search - future enhancement
- Saved/recent searches - future enhancement
- Autocomplete suggestions before typing - future enhancement

## Dependencies

- Existing City and Neighborhood models
- Existing activity filtering logic
- HTMX already installed

## Files to Create/Modify

- `activities/views.py` - Add search_locations view
- `activities/urls.py` - Add /search/ endpoint
- `templates/home.html` - Add search box UI
- `templates/components/search_results.html` - New partial template
- `activities/tests.py` - Add search tests
