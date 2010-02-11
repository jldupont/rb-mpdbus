# @author Jean-Lou Dupont
# 
# Makefile for:
#  - releasing the project to the PPA : 
#    "ppa" : prepares the required targets for release to the PPA
#    "pb"  : executes the pBuilder environment for checking package
#    "up"  : uploads to the PPA
#
#  - installing locally : 
#    "clean"
#
PRJ_NAME=rb-mpdbus
VERSION=`cat VERSION`

export PRJ_NAME

PYTHON=`which python`
RBP=/usr/lib/rhythmbox/plugins
PLUGIN_NAME=mpdbus

DEFAULT_DISTRO=karmic

ifeq ($(DIST),)
	DIST=${DEFAULT_DISTRO}
endif

export DIST


###################################################
## LOCAL INSTALLATION RELATED
###################################################

clean:
	@rm -r -f $(DESTDIR)$(RBP)/${PLUGIN_NAME}/*.pyc
		
uninstall:
	@rm -r -f $(DESTDIR)$(RBP)/${PLUGIN_NAME}
		
install:
	@install -d $(DESTDIR)$(RBP)/${PLUGIN_NAME}
	@install -D $(CURDIR)/${PLUGIN_NAME}/*.py                      $(DESTDIR)$(RBP)/${PLUGIN_NAME}/
	@install -D $(CURDIR)/${PLUGIN_NAME}/${PLUGIN_NAME}.rb-plugin  $(DESTDIR)$(RBP)/${PLUGIN_NAME}/${PLUGIN_NAME}.rb-plugin
	@python -m compileall ${DESTDIR}$(RBP)/${PLUGIN_NAME}
	
buildsrc:
	debuild -S

all:
	@echo "For packaging: 'ppa', 'pb', 'up'"
	@echo "Others:        'clean', 'install', 'uninstall', 'buildsrc'"


###################################################
## PACKAGING RELATED
###################################################
	
	
ppa up pb:
	@make PRJ_VERSION=$(VERSION) -C packages $@
	
.PHONY: ppa pb up all
