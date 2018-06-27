# Zypper-Upgraderepo-Plugin
Zypper plugin which make use of the [zypper-upgraderepo](https://github.com/fabiomux/zypper-upgraderepo) gem
to check and upgrade repositories.

## Installation
This project can be easily installed as a normal RPM package from 
[openSUSE Build Service](https://build.opensuse.org/package/show/home:FabioMux/zypper-upgraderepo-plugin).

Add the repository using the right version:
```
$ sudo zypper ar https://build.opensuse.org/package/show/home:FabioMux/openSUSE_Leap_42.3/home:FabioMux.repo
```

Install the rpm:
```
$ sudo zypper in zypper-upgraderepo-plugin
```

The package zypper-upgraderepo is a dependence and will be automatically installed.

## Usage
```
$ zypper upgraderepo <operation> <options>
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

All the commands available as `zypper-upgraderepo <options>` are now available as `zypper upgraderepo <options>`.

## More help
zypper-upgraderepo wiki: https://github.com/fabiomux/zypper-upgraderepo/wiki
