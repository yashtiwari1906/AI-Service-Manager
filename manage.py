#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from api.chehra.preLoadOnStartUp import ChehraStartupHandler, return_last_uuid_from_db



def load_on_startup():
    chehra_startup_manager_instance = ChehraStartupHandler.get_curr_instance()
    chehra_startup_manager_instance.curr_uuid = return_last_uuid_from_db() + 1
    
def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_service_manager.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    load_on_startup()
    execute_from_command_line(sys.argv)

    
    print("loading startup modules....")


if __name__ == '__main__':
    main()
