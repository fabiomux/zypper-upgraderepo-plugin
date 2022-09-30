# Zypper-Upgraderepo-Plugin

Zypper plugin which make use of the [zypper-upgraderepo][zypper_upgraderepo] gem
to check and upgrade repositories.

## Installation

There are several options to install the service menus listed in this repository.


### From the openSUSE Build Service repository

This application has been packaged in my personal OBS repository so you can install It
as a common RPM package:
- Add the repository URL in your list;
- install the package from Yast or Zypper.

Being the repository URL slightly changing from a version to another, I included all the steps
in the related [project page][project_page] on Freeaptitude blog.

Installing this plugin the package *rubygem-zypper-upgraderepo* will be automatically selected.

## Usage

To run the default check scan:
```
$ zypper upgraderepo [<operation>] [<options>]
```

## Get help

When this plugin is correctly installed you can see it in the list of subcommands:
```
$ zypper help subcommand
```

Read the man page with:
```
$ zypper help upgraderepo
```

For a quick help:
```
$ zypper upgraderepo --help
```

With this plugin all the commands mentioned in the [wiki page][zypper_upgraderepo_wiki] available
as `zypper-upgraderepo ...` are available as `zypper upgraderepo ...`.

## More help

More info is available at:
- the [ZypperUpgraderepo GitHub wiki][zypper_upgraderepo_wiki];
- the article [Upgrading with Zypper][upgrading_with_zypper] on Freeaptitude blog.


[project_page]: https://freeaptitude.altervista.org/projects/zypper-upgraderep.html "ZypperUpgraderepo project page"
[upgrading_with_zypper]: https://freeaptitude.altervista.org/articles/upgrading-opensuse-with-zypper.html "Upgrading openSUSE with Zypper"
[zypper_upgraderepo]: https://github.com/fabiomux/zypper-upgraderepo "ZypperUpgraderepo GitHub page"
[zypper_upgraderepo_wiki]: https://github.com/fabiomux/zypper-upgraderepo/wiki "zypper-upgraderepo wiki page on GitHub"
