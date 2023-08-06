# Django Database Backup to Git

A Django app, which makes a database backup in JSON format, commits and pushes it to a dedicated Git repository.
Intended to be run in deployment scripts and as a scheduled task.

## Installation and Setup

1. Install with pip:

```
pip install django-database-backup-to-git
```

1. Set up a Git repository outside of your application's main Git repository.
1. Add `dbbackup` to your `INSTALLED_APPS`.
1. In you settings file, specify the `DATABASE_BACKUP_FILENAME` setting. (Recommendably relative to `BASE_DIR`.)
1. Run `manage.py help`, check that `dbbackup` is listed as available command.

## Usage

Typing `manage.py dbbackup` will also display output. When running it from *cron*, use `manage.py dbbackup --silent`.
