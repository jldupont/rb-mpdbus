#
# @author: Jean-Lou Dupont
#
# Makefile used for packaging
#

ppa:
	@echo " \033[1m  Preparing package for the PPA \033[0m"
	@echo "Cleaning - Version: ${PRJ_VERSION}"
	@rm -r -f /tmp/$(PRJ_NAME)
	
	@echo "* Project details: Name: ${PRJ_NAME} Version: ${PRJ_VERSION}, Distribution: ${DIST}"
	@echo "------------------------ "
	@echo ""
	@echo "mkdir directories ( /tmp/$(PRJ_NAME)/$(PRJ_NAME)-$(PRJ_VERSION) )"
	mkdir -p "/tmp/${PRJ_NAME}"
	mkdir -p "/tmp/${PRJ_NAME}/${PRJ_NAME}-${PRJ_VERSION}"
	mkdir -p "/tmp/${PRJ_NAME}/${PRJ_NAME}-${PRJ_VERSION}/src"
	
	@echo "Copying package folder"
	@rsync -r --exclude=*.git* ../src/ "/tmp/$(PRJ_NAME)/$(PRJ_NAME)-$(PRJ_VERSION)/src"

	@echo "Copying debian folder"
	@rsync -r --exclude=*.svn* debian "/tmp/$(PRJ_NAME)/$(PRJ_NAME)-$(PRJ_VERSION)"

	@echo "Copying packaging makefile"
	@cp ../makefile "/tmp/$(PRJ_NAME)/$(PRJ_NAME)-$(PRJ_VERSION)/makefile"
	@cp ../VERSION "/tmp/$(PRJ_NAME)/$(PRJ_NAME)-$(PRJ_VERSION)/VERSION"
		
	@echo "Adjusting debian/changelog to DIST & VERSION"
	@cat debian/changelog | sed "s/_DIST_/${DIST}/g" | sed "s/_VERSION_/${PRJ_VERSION}/g" > "/tmp/${PRJ_NAME}/${PRJ_NAME}-${PRJ_VERSION}/debian/changelog"
	
	@echo " \033[1m !!! Have you updated debian/changelog ?\033[0m"

	@echo "Running 'debuild'"
	@cd "/tmp/$(PRJ_NAME)/$(PRJ_NAME)-$(PRJ_VERSION)" && debuild -S
	
up:
	@echo "\033[1m *** UPLOADING TO PPA *** \033[0m"
	@cd "/tmp/$(PRJ_NAME)/" && dput ppa:jldupont/jldupont *.changes


pb:
	@echo " ----------------------------- "
	@echo "\033[1m *** RUNNING PBUILDER *** \033[0m"
	@cd "/tmp/$(PRJ_NAME)/" && sudo DIST=${DIST} pbuilder build *.dsc

.PHONY: orig ppa pb up