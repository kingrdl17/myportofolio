Nama: Marclay Ardell Taufiqurrachman Harahap

NPM: 2506621024

Kelas: PBP F

## Local development

Run these commands from the repository root in PowerShell. The site and Tailwind CSS watcher run in separate terminals so CSS changes are compiled while you work.

### One-time setup

If the Python virtual environment does not exist yet, create and activate it, then install the Python dependencies:

```powershell
py -m venv env
.\env\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Install the Tailwind dependencies:

```powershell
Set-Location theme\static_src
npm install
Set-Location ..\..
```

If PowerShell does not allow activating the virtual environment, you can run the commands below using `.\env\Scripts\python.exe` instead of `python`.

### Start the site and CSS watcher

Open two PowerShell terminals at the repository root.

In **Terminal 1**, start Tailwind's watcher:

```powershell
.\env\Scripts\python.exe manage.py tailwind start
```

Leave this terminal running. It watches the templates and Tailwind source stylesheet, then rebuilds `theme\static\css\dist\styles.css` when you save a change.

In **Terminal 2**, start Django:

```powershell
.\env\Scripts\python.exe manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser. If this is a fresh database, run `.\env\Scripts\python.exe manage.py migrate` once before starting the server.

### See design changes

- Edit page structure and Tailwind classes in `templates\`.
- Edit shared Tailwind/CSS styles in `theme\static_src\src\styles.css`. Keep its `@source` entries so Tailwind can find classes used in templates.
- Save the file and check Terminal 1 for a successful CSS rebuild. Refresh the browser if the page does not update automatically.
- Keep both terminals running during development. Stop either process with `Ctrl+C`.

For a one-time CSS build (for example, before deploying), run:

```powershell
.\env\Scripts\python.exe manage.py tailwind build
```
