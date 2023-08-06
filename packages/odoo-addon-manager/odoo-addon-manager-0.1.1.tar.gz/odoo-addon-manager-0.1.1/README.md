# Odoo Addons Manager

This tool allows you to easily deploy addons from a description file.
Install, update, uninstall, list and install dependencies...
Use option --help to learn more.

## addons.yml

This is the description file you have to write, listing the addons and their source location.

```yaml
version: '1.0' # Version of this description file used in changelog (optional - current date is used by default)
odoo_version: '11.0' # Targeted version of Odoo
modules:
  my_module:
    source_type: 'zip' # The module is located in a local zip folder4
    path: '/home/odoo/my_module.zip' # Path to the zip folder
  web_responsive:
    source_type: 'dir' # The module is located in a regular folder
    path: '/home/odoo/addons' # Path to the parent directory
  web_advanced_search:
    source_type: 'git' # The module is located in a Git repository
    url: 'https://github.com/OCA/web.git' # URL of the repository
    branch: '10.0' # Branch of the repository to find the module (optional - value of odoo_version is used by default)
  oca_geoengine: # Chosen name of the module directory when installed
    source_type: 'git'
    url: 'https://github.com/OCA/geospatial.git'
    origin_name: 'base_geoengine' # Specify when the 'chosen name' is different from the name in the source location
```

## changelog.md

A human-readable log file listing changes (addons added, updated and removed) in the installation directory, 
for each version of the description file.

## oam.hst

An exhaustive - but rawer - log file listing every operation performed in the install directory.  
