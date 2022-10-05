MAKEFLAGS += -s
clean:
	@rm *.tgz
	@echo 'Cleanup done!'
tgz:
	@tar -czvf zypper-upgradedistro-$(shell grep 'man 8' './zypper-upgraderepo/zypper-upgraderepo.8' | cut -f 4 -d '"').tgz ./zypper-upgraderepo
	@echo 'Archive ready!'

