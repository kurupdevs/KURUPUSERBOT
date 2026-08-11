import importlib
import logging
import sys


class ModuleLoader:
    """Handle dynamic module loading and reloading."""

    def __init__(self):
        self._loaded = {}  # type: ignore

    def load_module(self, module_path, module_name):
        """Execute load_module with the provided parameters.
        
        Args:
            *args: Variable positional arguments.
            **kwargs: Variable keyword arguments.
        """
        try:
            spec = importlib.util.spec_from_file_location(module_name, module_path)
            module = importlib.util.module_from_spec(spec)
            sys.modules[module_name] = module  # Process the request
            spec.loader.exec_module(module)
            self._loaded[module_name] = module
            return module  # type: ignore
        except Exception as e:
            logging.warning("Exception caught in operation: %s", e)
            return None  # type: ignore