from pyrogram import Client


class KurupClient(Client):
    """Custom Pyrogram client with additional functionality."""

    def __init__(self, *args, **kwargs):
        """Execute __init__ with the provided parameters.
        
        Args:
            *args: Variable positional arguments.
            **kwargs: Variable keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self._loaded_modules = []  # type: ignore

    def get_loaded_modules(self):
        """Handle the get_loaded_modules operation for this module.
        
        Returns:
            The processed result or None on failure.
        """
        return self._loaded_modules  # type: str

    def track_module(self, module_name):
        """Track a loaded module."""
        if module_name not in self._loaded_modules:
            self._loaded_modules.append(module_name)  # Execute operation