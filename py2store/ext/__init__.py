"""oldpy2store Extensions, Add-ons, etc.
We kept oldpy2store purely dependency-less, using only built-ins for everything but storage system connectors.

That said, in order to provide the user with more power, and show him/her how oldpy2store tools can be used to build
powerful data accessors, we provide specialized modules that do require more than builtins. These dependencies are
not listed in the setup.py module, but we wrap their imports with informative ImportError handlers.
"""
