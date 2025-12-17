# Django Deployment Kit

A reusable push-based deployment workflow for Django sites. Optimized for Vultr/VPS servers with Docker, featuring GPU-accelerated media optimization and bidirectional database sync.

## Features

- **Push-based deployment** - Deploy from local machine, not pull from GitHub
- **GPU media optimization** - NVIDIA NVENC for video, WebP conversion for images
- **Bidirectional sync** - Database and media sync both directions
- **HEIC support** - Auto-convert Apple photos to web-friendly formats
- **Duplicate detection** - Find and report duplicate media files
- **Rollback support** - Quickly revert to previous deployment
- **Reusable** - Copy to any Django project

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    LOCAL DEV MACHINE                        │
│  - NVIDIA GPU for heavy processing                          │
│  - Facebook HAR parsing, bulk media optimization            │
│  - Feature development and testing                          │
└───────────────────────┬─────────────────────────────────────┘
                        │
        ┌───────────────┴───────────────┐
        │       BIDIRECTIONAL SYNC       │
        │  Code: Local → Prod            │
        │  Media: Both directions        │
        │  Database: Both directions     │
        └───────────────┬───────────────┘
                        │
┌───────────────────────┴─────────────────────────────────────┐
│                    VPS SERVER                               │
│  - Primary for daily use (blog posts, uploads)              │
│  - nginx reverse proxy with SSL                             │
│  - Docker containers                                        │
│  - Basic image processing on upload                         │
└─────────────────────────────────────────────────────────────┘
```

## Quick Start

### 1. Copy scripts to your project

```bash
cp -r django-deployment-kit/scripts/ your-django-project/
```

### 2. Configure for your project

```bash
cd your-django-project/scripts
cp deploy.conf.example deploy.conf
# Edit deploy.conf with your server details
```

### 3. Install dependencies

```bash
pip install paramiko pillow pillow-heif
```

### 4. Test connection

```bash
./scripts/deploy.sh status
```

## Commands

| Command | Description |
|---------|-------------|
| `./scripts/deploy.sh status` | Check production status |
| `./scripts/deploy.sh code` | Push code, rebuild container |
| `./scripts/deploy.sh push` | Full deployment (code + media) |
| `./scripts/deploy.sh db-pull` | Pull production DB to local |
| `./scripts/deploy.sh db-push` | Push local DB to production |
| `./scripts/deploy.sh media-pull` | Pull production media to local |
| `./scripts/deploy.sh media-push` | Push local media to production |
| `./scripts/deploy.sh optimize` | Run media optimization locally |
| `./scripts/deploy.sh logs` | Tail production logs |
| `./scripts/deploy.sh rollback` | Revert to previous deployment |

## Media Optimization

The optimizer converts images to WebP format (30-50% size reduction) and compresses videos using NVIDIA NVENC.

### Supported Formats

| Input | Output | Reduction |
|-------|--------|-----------|
| JPG/JPEG | WebP | ~40% |
| PNG | WebP | ~50% |
| HEIC/HEIF | WebP | ~60% |
| MP4/MOV | MP4 (H.265) | ~50% |

### Options

```bash
# Dry run - see what would be optimized
python scripts/optimize_media.py --dry-run

# Optimize all files
python scripts/optimize_media.py --all

# Images only
python scripts/optimize_media.py --images-only

# Videos only (uses GPU if available)
python scripts/optimize_media.py --videos-only

# Specific path
python scripts/optimize_media.py --path /path/to/media
```

## Database Sync

Bidirectional database sync with automatic backups.

```bash
# Pull production to local
python scripts/db_sync.py pull

# Push local to production (with confirmation)
python scripts/db_sync.py push

# Compare databases
python scripts/db_sync.py compare

# List tables
python scripts/db_sync.py tables --source local
python scripts/db_sync.py tables --source remote
```

## Server-Side Auto-Optimization

Add automatic image optimization on upload to your Django project:

### 1. Update image_utils.py

Copy `examples/image_utils.py` to your Django app.

### 2. Create signals.py

Copy `examples/signals.py` to your Django app.

### 3. Register signals in apps.py

```python
class YourAppConfig(AppConfig):
    name = 'your_app'

    def ready(self):
        from . import signals  # noqa: F401
```

### 4. Add pillow-heif to requirements.txt

```
pillow-heif>=0.13
```

## Configuration Reference

```bash
# Server Settings
REMOTE_HOST="root@YOUR_SERVER_IP"    # SSH connection string
REMOTE_PATH="/root/your-project"      # Project path on server
REMOTE_PORT="8000"                    # Application port
SITE_URL="https://your-domain.com"    # Site URL for health checks
REMOTE_PASSWORD="your-password"       # SSH password

# Database Settings
DB_CONTAINER="db-container-name"      # Production DB container
DB_NAME="database_name"               # Database name
DB_USER="db_user"                     # Database user
LOCAL_DB_CONTAINER="local-db"         # Local DB container

# Optimization Settings
IMAGE_MAX_WIDTH=1920                  # Max image width
IMAGE_QUALITY=85                      # WebP quality (0-100)
VIDEO_MAX_HEIGHT=1080                 # Max video height
VIDEO_CRF=28                          # Video quality (lower = better)
USE_NVENC=true                        # Use NVIDIA GPU encoding
```

## Requirements

### Local Machine
- Python 3.8+
- paramiko (SSH/SFTP)
- Pillow, pillow-heif (image processing)
- ffmpeg (video processing)
- NVIDIA GPU + drivers (optional, for fast video encoding)

### Server
- Docker
- PostgreSQL container
- nginx (reverse proxy)

## Typical Workflow

### Daily Development
```bash
# Make code changes locally
# ...

# Deploy code changes
./scripts/deploy.sh code
```

### New Feature with Database Changes
```bash
# Pull latest production data
./scripts/deploy.sh db-pull

# Develop locally with real data
# ...

# Deploy
./scripts/deploy.sh code
```

### Bulk Media Import
```bash
# Pull production media
./scripts/deploy.sh media-pull

# Optimize locally (uses GPU)
./scripts/deploy.sh optimize --all

# Push optimized media back
./scripts/deploy.sh media-push
```

## Troubleshooting

### Static Files Return 404 on Production

**Symptom**: CSS, JS, or images return 404 errors on production but work locally.

**Common Cause**: WhiteNoise's `CompressedManifestStaticFilesStorage` requires a manifest file (staticfiles.json). If you mount `staticfiles/` as a Docker volume, the volume overwrites the container's staticfiles directory (where `collectstatic` created the manifest during build).

**Solutions**:

1. **Don't mount staticfiles as a volume** (recommended):
   ```yaml
   # docker-compose.prod.yml
   volumes:
     # Only mount media, NOT staticfiles
     - ../media:/app/media
   ```

2. **Use non-manifest storage**:
   ```python
   # production.py
   STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
   ```

3. **Run collectstatic on startup** (if you must mount staticfiles):
   ```dockerfile
   CMD ["sh", "-c", "python manage.py collectstatic --noinput && gunicorn ..."]
   ```

### Container Can't Connect to Database

**Symptom**: Database connection errors on startup.

**Check**:
1. Database container is running: `docker ps | grep db`
2. Containers are on the same network
3. Environment variables are passed correctly in docker-compose

## License

MIT
