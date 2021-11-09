# TOML Metadata for Ivy

[1]: https://github.com/dmulholl/ivy

This [Ivy][1] plugin adds support for TOML file headers as an alternative to YAML.

    ~~~
    title = "Page Title"
    author = "John Doe"
    ~~~

You can install the plugin from the package index using `pip`:

    $ pip install ivy_toml

Activate the plugin by adding its name to the extensions list in your site's `config.py` file:

    extensions = ['ivy_toml']

It identifies TOML file headers by checking for three opening and closing tildes, `~`.
