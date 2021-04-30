# libreelec-addon-repo

This is the official 3rd party repo for LibreELEC. Do not install this manually. Install from the LibreELEC repo, under add-on repositories.

## How to contribute
This repo has a github workflow set up to package and publish the addons, and update the `addons.xml` and the relevant md5 files after each commit/merge. Simply PR changes to the addons, and make sure the version in the addon's `addon.xml` is incremented to force packaging and publishing of the new version. There is no longer any need to run the `addons_xml_generator.py` script locally.