MAKEFLAGS += -s
clean:
	@rm *.tgz
	@echo 'Cleanup done!'
tgz:
	@tar -czvf zypper-upgraderepo-$(shell grep 'man 8' './zypper-upgraderepo/zypper-upgraderepo.8' | cut -f 4 -d '"').tgz ./zypper-upgraderepo
	@echo 'Archive ready!'
install:
	@sudo install -m 755 ./zypper-upgraderepo/zypper-upgraderepo /usr/lib/zypper/commands/
	@sudo install -m 644 ./zypper-upgraderepo/zypper-upgraderepo.8 /usr/share/man/man8/
	@echo 'Plugin installed!'
uninstall:
	@sudo rm /usr/lib/zypper/commands/zypper-upgraderepo || true
	@sudo rm /usr/share/man/man8/zypper-upgraderepo.8.gz || true
	@echo 'Plugin uninstalled!'
