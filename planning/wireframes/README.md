# Barn Raise Wireframes

## Overview

This document contains ASCII wireframes for all screens in the Barn Raise app. The design is mobile-first with a warm, friendly aesthetic.

## Design Principles

- **Mobile-first**: Designed for phones, scales up to desktop
- **Minimal friction**: Large tap targets, clear CTAs
- **Warm colors**: Barn red/terracotta palette (#d06b46)
- **Clean typography**: System fonts, readable sizes
- **No clutter**: Focus on content, not chrome

## Screen List

1. [Home Page](01-home.txt) - City selection
2. [City Page](02-city.txt) - Neighborhood list with filters
3. [Neighborhood Page](03-neighborhood.txt) - Activity list
4. [Activity Detail](04-activity-detail.txt) - Full activity info + join
5. [Post Activity](05-post-activity.txt) - Create new activity form
6. [Post Success](06-post-success.txt) - Confirmation with manage link
7. [Manage Activity](07-manage-activity.txt) - Edit/complete/cancel

## User Flows

### Flow 1: Find and Join Activity
```
Home → Select City → Select Neighborhood → View Activity → Join → Get Directions
```

### Flow 2: Post an Activity
```
Home → Post Activity → Fill Form → Submit → Success (get manage link)
```

### Flow 3: Manage Activity
```
Success Page → Copy Link → Later: Open Link → Edit/Complete/Cancel
```

## Responsive Breakpoints

- **Mobile**: < 640px (primary design target)
- **Tablet**: 640px - 1024px
- **Desktop**: > 1024px

On larger screens:
- Content centered with max-width
- Cards may display in grid
- Navigation remains simple

## Color Palette

```
Primary:    #d06b46 (barn red)
Primary Dark: #a1432a
Background: #fdf8f6 (warm white)
Text:       #1f2937 (dark gray)
Muted:      #6b7280 (gray)
Success:    #10b981 (green)
```

## Typography

- Headings: System sans-serif, bold
- Body: System sans-serif, regular
- Sizes: 14px base, 18px headings, 24px titles
