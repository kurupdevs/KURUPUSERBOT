"""
KurupUserbot web dashboard (Bottle).

Provides a lightweight web interface for monitoring bot status,
viewing loaded modules, and reading logs. Serves HTML templates
from the ``public/`` directory.

Routes:
    /                — overview (stats, modules)
    /modules         — module list and delete
    /logs            — view recent logs
    /logs/clear      — clear log file
    /api/stats       — JSON stats endpoint
    /api/modules     — JSON module list
"""

import json
import os
import platform
import time
from datetime import timedelta
from typing import Any, Dict, List

import psutil
from bottle import Bottle, SimpleTemplate, redirect, request, response

# ── App ───────────────────────────────────────────────────────
bottle_app = Bottle()
"""Bottle application instance."""

# ── Paths ─────────────────────────────────────────────────────
BASE_PATH: str = os.path.abspath(os.getcwd())
"""Absolute path to the project root."""

PUBLIC_PATH: str = os.path.join(BASE_PATH, "public")
"""Path to the web dashboard HTML templates."""

# ── Startup ───────────────────────────────────────────────────
START_TIME: float = time.time()
"""Timestamp when app.py was loaded (used for uptime)."""


# ── Helpers ───────────────────────────────────────────────────

def get_stats() -> Dict[str, Any]:
    """Collect system and bot runtime statistics.

    Returns:
        Dict with keys: uptime, memory_used, memory_total,
        memory_percent, cpu_percent, platform, python_version.
    """
    uptime_seconds = int(time.time() - START_TIME)
    uptime_str = str(timedelta(seconds=uptime_seconds))
    memory = psutil.virtual_memory()
    cpu_percent = psutil.cpu_percent(interval=0.1)
    return {
        "uptime": uptime_str,
        "memory_used": memory.used // (1024 * 1024),
        "memory_total": memory.total // (1024 * 1024),
        "memory_percent": int(memory.percent),
        "cpu_percent": int(cpu_percent),
        "platform": platform.system(),
        "python_version": platform.python_version(),
    }


def get_builtin_modules() -> List[Dict[str, str]]:
    """Scan the modules directory for built-in modules.

    Returns:
        List of dicts with ``name`` and ``type: 'builtin'``.
    """
    modules = []
    modules_path = f"{BASE_PATH}/modules"
    for f in os.listdir(modules_path):
        if f.endswith(".py") and not f.startswith("_") and f not in ("loader.py", "__init__.py"):
            modules.append({"name": f[:-3], "type": "builtin"})
    return modules


def get_custom_modules() -> List[Dict[str, str]]:
    """Scan the custom_modules directory.

    Returns:
        List of dicts with ``name`` and ``type: 'custom'``.
    """
    custom_path = f"{BASE_PATH}/modules/custom_modules"
    modules = []
    if os.path.exists(custom_path):
        for f in os.listdir(custom_path):
            if f.endswith(".py"):
                modules.append({"name": f[:-3], "type": "custom"})
    return modules


def get_all_modules() -> List[Dict[str, str]]:
    """Get both built-in and custom modules."""
    return get_builtin_modules() + get_custom_modules()


def render_page(content_name: str, page: str, **vars) -> str:
    """Render a dashboard page by injecting content into base template.

    Args:
        content_name: HTML file name inside ``public/`` (e.g. ``overview.html``).
        page: Active page identifier for nav highlighting.
        **vars: Template variables passed to both base and content.

    Returns:
        Rendered HTML string.
    """
    with open(os.path.join(PUBLIC_PATH, "base.html")) as f:
        base_tpl = f.read()
    with open(os.path.join(PUBLIC_PATH, content_name)) as f:
        content_tpl = f.read()
    content = SimpleTemplate(content_tpl).render(**vars)
    vars["base"] = content
    vars["page"] = page
    return SimpleTemplate(base_tpl).render(**vars)


# ── Routes ────────────────────────────────────────────────────

@bottle_app.get("/")
def index() -> str:
    """Overview page — system stats and module counts."""
    stats = get_stats()
    modules = get_all_modules()
    builtin = get_builtin_modules()
    custom = get_custom_modules()
    message = request.params.get("message", "")
    message_type = request.params.get("type", "")
    return render_page("overview.html", "overview",
        uptime=stats["uptime"],
        memory_used=stats["memory_used"],
        memory_total=stats["memory_total"],
        memory_percent=stats["memory_percent"],
        cpu_percent=stats["cpu_percent"],
        module_count=len(modules),
        platform=stats["platform"],
        python_version=stats["python_version"],
        builtin_count=len(builtin),
        custom_count=len(custom),
        message=message,
        message_type=message_type)


@bottle_app.get("/modules")
def modules_page() -> str:
    """Modules page — list all loaded modules."""
    modules = get_all_modules()
    builtin = get_builtin_modules()
    custom = get_custom_modules()
    message = request.params.get("message", "")
    message_type = request.params.get("type", "")
    return render_page("modules.html", "modules",
        modules=modules,
        builtin_count=len(builtin),
        custom_count=len(custom),
        message=message,
        message_type=message_type)


@bottle_app.post("/modules/delete")
def delete_module():
    """Delete a custom module from the filesystem."""
    module_name = request.forms.get("module_name")
    custom_path = f"{BASE_PATH}/modules/custom_modules/{module_name}.py"
    if os.path.exists(custom_path):
        os.remove(custom_path)
        return redirect(f"/modules?message={module_name}+deleted&type=success")
    return redirect("/modules?message=Module+not+found&type=error")


@bottle_app.get("/logs")
def logs() -> str:
    """Logs page — display the last 500 lines of the log file."""
    log_file = f"{BASE_PATH}/kuruplogs.txt"
    logs_content = "No logs yet"
    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            lines = f.readlines()
            logs_content = "".join(lines[-500:]) or "No logs yet"
    message = request.params.get("message", "")
    message_type = request.params.get("type", "")
    return render_page("logs.html", "logs",
        logs=logs_content,
        message=message,
        message_type=message_type)


@bottle_app.get("/logs/clear")
def clear_logs():
    """Clear the log file and redirect to logs page."""
    log_file = f"{BASE_PATH}/kuruplogs.txt"
    if os.path.exists(log_file):
        with open(log_file, "w") as f:
            f.write("")
    return redirect("/logs?message=Logs+cleared&type=success")


@bottle_app.get("/api/stats")
def api_stats() -> str:
    """API endpoint — return system stats as JSON."""
    response.content_type = "application/json"
    return json.dumps(get_stats())


@bottle_app.get("/api/modules")
def api_modules() -> str:
    """API endpoint — return module list as JSON."""
    response.content_type = "application/json"
    return json.dumps(get_all_modules())


# ── Entry Point ───────────────────────────────────────────────

if __name__ == "__main__":
    from bottle import run
    run(bottle_app, host="0.0.0.0", port=5000, debug=False)
